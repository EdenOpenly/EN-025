# EN-025 — Data processing record

*Five numbers, five ways of counting: what the trans suicide figures circulating in the UK actually measure*  
Evidence Note EN-025, version 1.0 · DOI (this version) 10.5281/zenodo.23327489 · Eden Openly

This record describes how the figures in EN-025 were obtained, read, transformed, checked and published. It is a companion to the note, not part of it. Where the note and this record differ, the note governs, and the difference is an error to be reported.

---

## 1. Sources

Thirteen source documents were used; all were read in full. The register, with issuer, title, date, where each can be obtained and a SHA-256 of the archived text, is in [`sources/sources.csv`](../sources/sources.csv).

| Source | What EN-025 uses it for |
|---|---|
| National Child Mortality Database, FOI response (Parts 1–3 and methodology notes) | 647, 107 and 46; the umbrella definition of trans; how cases were found; the underestimate and exact-match caveats; "may differ to other NCMD publications" |
| University of Bristol, FOI2526-321 | The yearly series 5, 4, 22, 10, 3, 2; recent years likely underestimated |
| NCISH annual reports 2023, 2024, 2025 and 2026 | 104 and the earlier running totals (37, 53, 84); how deaths and trans status are recorded; figures revised "as further information is received"; 26% of all suicides; the count-versus-rate example |
| DHSC, review of suicides at the Tavistock and Portman | 12; 5 before and 7 after; NHS-year caveat; "likely" longer-term rise; NCMD under-18s note; "generally poor" and "good reasons to believe"; "multiple risks acting in combination" |
| Good Law Project and QueerAF article, 25 April 2026 | 50; the circulated 47, "England and Wales", "seven-year", 16/34/20, "less than 1%" and "7%"; the article's reviewer's statements; two young people referred under 18 |
| QueerAF article, 10 October 2026 | 21 by clinic; three of 13 clinics; at least 618 deaths; Belfast and Wales; why other clinics gave no figure |
| ONS FOI-2025-2822 | No separate gender identity question on the death certificate (England and Wales); possible census linkage |
| ONS census gender identity guidance (26 March 2025) and quality information (8 April 2025) | Census estimates: aged 16 and over; voluntary question; extra uncertainty; "official statistics in development"; "should not be used as precise estimates…" |
| Samaritans, *Media Guidelines for Reporting Suicide* (2026) | The suicide-reporting check; "suicide is preventable"; not linking to earlier stories about suicide |

The Good Law Project and QueerAF articles are identified by title and not linked, for the reason given in the note.

## 2. Extraction

Each document was filed in Eden Openly's source archive and read from the archived copy, not from a summary or a search result. Extraction meant reading: no tables were parsed and no data were scraped.

Three features of the archived text affected reading, and the verification script allows for them:

- **Two-column layouts** (the NCISH reports, the Samaritans guidelines). Extracted text interleaves the columns, so a sentence can be split. Such excerpts are checked as fragments.
- **Dropped or substituted ligatures.** PDF extraction drops "fi", "fl" and "ff" in some documents; one web capture renders "fi" as "!".
- **Page numbers.** The NCISH extracted text has no page breaks. Printed page numbers were inferred from each report's running footers and its own "see details on page N" cross-references, and checked by a separate reader.

## 3. Transformation

The note performs no statistical transformation. The only calculations are simple arithmetic on published figures, listed in [`data/arithmetic.csv`](../data/arithmetic.csv) and recomputed by the script:

| Check | Calculation | Result |
|---|---|---|
| A01 | 46 ÷ 647 | 7.1% ("about 7%") |
| A02–A04 | 53 − 37; 84 − 53; 104 − 84 | 16; 31; 20 |
| A05 | 618 − 21 | 597 |
| A06 | 10 + 6 + 5 | 21 |
| A07 | 2016 to 2023 inclusive | 8 years |
| A08 | 5 + 4 + 22 + 10 + 3 + 2 | 46 |
| A09 | 5 + 7 | 12 |

The subtractions A02–A04 are reported in the note only to show that successive NCISH running totals cannot reliably give yearly counts, because NCISH revises earlier years.

## 4. Disclosure control

No individual-level data were obtained or used. The note reproduces only counts already published by their sources, at the level published (including QueerAF's "between one and five"). No person who died is named or described. The Good Law Project article names and describes individuals; nothing from those passages is used, and the verification excerpts in this repository were chosen to avoid them. No person other than the author is named in the note or in this repository.

## 5. Analysis

The analysis is descriptive. For each figure the note records who is counted, how a death is defined, the period, the area and how deaths were found, and then asks whether the figures can be added up, compared, or turned into a rate. No rate, trend or comparison is estimated. The note does not grade the certainty of any evidence.

## 6. Verification

Every check below was carried out with AI assistance (Claude, Anthropic). Checks marked *separate pass* were made by a pass that had not drafted the text it checked. None is independent human verification.

| # | What was checked | Result |
|--|------------------------------------|------------------------------------------------------|
| 1 | The five figures against their source documents (separate pass) | Found 47 for 46 and "England and Wales" for England; eight years, not seven; the 2022 figure of 34 not in any NCISH report. |
| 2 | Every factual sentence of an early draft for a source (separate pass) | 26 problems; unsourceable statements cut. |
| 3 | Every source re-read from its archived copy | 17 problems fixed. |
| 4 | Every statement of the draft, sentence by sentence (separate pass) | 87 statements: 68 supported, 18 problems fixed. |
| 5 | Re-check of every changed passage (separate pass) | 6 problems fixed, including a logic error about the 597. |
| 6 | First external adversarial review (AI-generated) | Accepted after checking each claim against the source: definitions of "trans" and of the death counted; denominator; outcome definitions; recording changes over time. Suggestions resting on unfiled sources were not used. |
| 7 | Re-check of the revision (separate pass) | 4 problems and 4 minor points fixed. |
| 8 | Suicide-reporting check against the Samaritans guidelines | Requirements met; content note, "suicide is preventable" and fuller signposting added. |
| 9 | Second external adversarial review | 13 points accepted, including the section on suicide rates. |
| 10 | Re-check of that revision (separate pass) | 2 problems and 4 minor points fixed, including a sentence that presupposed the risk is higher. |
| 11 | Third external adversarial review | 8 points applied, including one factual error: the census does include 16- and 17-year-olds. |
| 12 | Re-check of that revision (separate pass) | No errors; one tightening. |
| 13 | Full read of the final text against all 13 sources (separate pass) | About 108 statements: no problems; 4 minor points fixed. |
| 14 | The deposit's front matter and correction record (two separate passes) | 14 problems fixed, including an attribution of the NCISH figures to the investigations that only repeated them. |
| 15 | `scripts/verify_claims.py`, run against the deposited PDF and the archived source texts | 68 checks (59 claims, 9 calculations): 68 passed. Self-test: a corrupted excerpt and a corrupted sum were both caught. |

Substantive errors found during production are listed in the note's correction record.

## 7. Outputs

| Output | SHA-256 |
|---|---|
| EN-025 version 1.0, PDF deposited under 10.5281/zenodo.23327489 | `e0124d8d70c19add10e70994d888b523d55caaacfb2d856f167b18656e7613ec` |

A file cannot contain its own hash, so the PDF's hash is recorded here and on the Zenodo record. The PDF's integrity block gives the SHA-256 of the manuscript it was built from; the manuscript is held by Eden Openly.

The companion repository holds the source register, the claims and calculations, and the verification script.

## Correspondence

The discrepancies the note reports in the Good Law Project and QueerAF articles were reported to QueerAF on 12 October 2026, copying the QueerAF journalist who co-wrote both articles. The journalist acknowledged the report on 13 October 2026 and said a fuller reply would follow. Publication did not wait for it; any reply will be reflected in a later version of the note.
