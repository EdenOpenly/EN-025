#!/usr/bin/env python3
"""Verify EN-025's claims against its source documents.

For every row of data/claims.csv this checks that
  (1) the manuscript_text appears in the deposited EN-025 PDF, and
  (2) the source_excerpt appears in the named source document;
and for every row of data/arithmetic.csv that the expression evaluates to the expected value.

The source documents are not distributed with this repository (see README). Obtain them
(sources/sources.csv says where), save each as plain text named <source_id>.txt in one
directory, and run:

    python3 scripts/verify_claims.py --sources DIR --note EN-025-v1.0.pdf

(the PDF deposited under doi:10.5281/zenodo.23327489; requires the pypdf package).

Text is compared after normalisation: case, whitespace, typographic quotes and dashes, and
the ligatures (fi, fl, ff) that PDF text extraction often drops. The PDF's running head and
footer are removed, so a sentence broken across pages is read as one. Where a two-column layout
splits a sentence, the excerpt is given as fragments separated by " | ", each of which must be found. Exit status is non-zero if any
check fails. --self-test corrupts one excerpt and one sum and confirms that both are caught.
"""
import argparse, csv, os, re, sys

def norm(s):
    s = s.lower()
    for a, b in (("ﬁ", "fi"), ("ﬂ", "fl"), ("ﬀ", "ff"), ("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("−", "-")):
        s = s.replace(a, b)
    for lig in ("fi", "fl", "ff"):          # extracted PDF text often loses these entirely
        s = s.replace(lig, "")
    s = s.replace("!", "")                    # some web captures render fi as "!"
    return re.sub(r"[\s\"']+", "", s)

def read_note(path):
    if path.lower().endswith(".pdf"):
        from pypdf import PdfReader
        # Drop the running head and footer printed on each page, so that a sentence
        # broken across a page boundary is read as one.
        furniture = re.compile(r"^(EVIDENCE NOTE · EN-025.*|Identifier: EN-025 · .*|"
                               r"Eden Openly · EN-025 · doi:.*|Page \d+ of \d+)$")
        lines = (l for p in PdfReader(path).pages for l in (p.extract_text() or "").splitlines())
        return "\n".join(l for l in lines if not furniture.match(l.strip()))
    return open(path, encoding="utf-8").read()

def run(sources, note, claims, arith, corrupt=False):
    man = norm(read_note(note))
    cache, fails, n = {}, [], 0
    for r in csv.DictReader(open(claims, encoding="utf-8")):
        n += 1
        sid = r["source_id"]
        if sid not in cache:
            path = os.path.join(sources, sid + ".txt")
            cache[sid] = norm(open(path, encoding="utf-8").read()) if os.path.exists(path) else None
        exc = r["source_excerpt"] + (" CORRUPTED" if corrupt and r["claim_id"] == "C01" else "")
        if norm(r["manuscript_text"]) not in man:
            fails.append(f'{r["claim_id"]}: text not found in the note: {r["manuscript_text"]!r}')
        if cache[sid] is None:
            fails.append(f'{r["claim_id"]}: source file missing: {sid}.txt')
        elif not all(norm(part) in cache[sid] for part in exc.split(" | ")):
            fails.append(f'{r["claim_id"]}: excerpt not found in {sid} ({r["locator"]}): {exc!r}')
    for r in csv.DictReader(open(arith, encoding="utf-8")):
        n += 1
        expr = r["expression"] + ("+1" if corrupt and r["check_id"] == "A02" else "")
        if not re.fullmatch(r"[0-9+\-*/(). ]+", expr):
            fails.append(f'{r["check_id"]}: refused expression {expr!r}'); continue
        got = round(eval(expr), 1)
        if got != float(r["expected"]):
            fails.append(f'{r["check_id"]}: {expr} = {got}, expected {r["expected"]}')
    return n, fails

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", required=True)
    ap.add_argument("--note", required=True, help="the deposited EN-025 PDF")
    ap.add_argument("--claims", default="data/claims.csv")
    ap.add_argument("--arithmetic", default="data/arithmetic.csv")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        _, fails = run(a.sources, a.note, a.claims, a.arithmetic, corrupt=True)
        caught = {f.split(":")[0] for f in fails}
        ok = {"C01", "A02"} <= caught
        print("self-test:", "PASS (both corruptions caught)" if ok else f"FAIL (caught {sorted(caught)})")
        sys.exit(0 if ok else 1)
    n, fails = run(a.sources, a.note, a.claims, a.arithmetic)
    for f in fails: print("FAIL", f)
    print(f"{n} checks, {n - len(fails)} passed, {len(fails)} failed")
    sys.exit(1 if fails else 0)
