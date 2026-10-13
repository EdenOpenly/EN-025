# EN-025 — Five numbers, five ways of counting

Companion repository for the Eden Openly Evidence Note **EN-025**, *Five numbers, five ways of counting: what the trans suicide figures circulating in the UK actually measure* (version 1.0, DOI [10.5281/zenodo.23327489](https://doi.org/10.5281/zenodo.23327489)).

*Content note: the note discusses suicide, including the deaths of children. Suicide is preventable. If anything here affects you, Samaritans are there day or night on 116 123 (free, UK and Ireland) or at samaritans.org.*

## What the note does

It examines five figures presented as counts of suicides among trans people in the UK (46, 104, 12, 50 and 21), sets out what each one counts, and shows why none of them, on its own, can estimate a suicide rate, show a trend, or show how the rate among trans people compares with the general population. It is a narrative evidence note; it is not a systematic review and it is not peer reviewed.

## What is here

| Path | Contents |
|---|---|
| `sources/sources.csv` | The 13 source documents: issuer, title, date, where to obtain each, and a SHA-256 of the archived text that was read. |
| `data/claims.csv` | 59 claims in the note, each with the source, the location in it, and the exact passage that supports it. |
| `data/arithmetic.csv` | The nine calculations the note relies on. |
| `scripts/verify_claims.py` | Checks every claim and calculation against the sources (below). |
| `docs/DATA-PROCESSING-RECORD.md` | How the data were obtained, read, transformed and checked, and what each check found. |

## What is not here, and why

- **The source documents themselves.** They belong to their publishers, and two are Freedom of Information responses held privately. `sources/sources.csv` says where each published source can be obtained. To run the checks you need your own copies.
- **No personal information** about anyone who died, and no names other than the author's.
- **Links to the Good Law Project and QueerAF articles.** Samaritans' media guidelines advise against linking to earlier stories about suicide, so they are identified by title. This is not a judgement on their work: several of the figures are public because of their investigations.

## Checking the note yourself

Download the deposited PDF of the note from [doi:10.5281/zenodo.23327489](https://doi.org/10.5281/zenodo.23327489). Save each source as plain text named `<source_id>.txt` (IDs as in `sources/sources.csv`) in one directory, then:

```
python3 scripts/verify_claims.py --sources DIR --note EN-025-v1.0.pdf
python3 scripts/verify_claims.py --sources DIR --note EN-025-v1.0.pdf --self-test
```

The first command checks that each claim's wording appears in the note and its supporting passage appears in the source, and recomputes each calculation. The second corrupts one passage and one sum and confirms that both are caught. Text is compared after normalising case, whitespace, quotation marks, dashes and the ligatures that PDF text extraction drops. Your extracted text may differ from ours in layout; a failure means "look here", not necessarily "wrong".

The script needs Python 3 and the `pypdf` package. Run against the deposited PDF and our archived source texts, all 68 checks pass.

## How it was made

The note was prepared with the assistance of a large language model (Claude, Anthropic), used for source retrieval, arithmetic verification, structural editing and adversarial review. The author is responsible for every claim, number and citation. The checks described in `docs/DATA-PROCESSING-RECORD.md` were carried out with AI assistance and have not been independently repeated by a human. Errors found during production are listed in the note's correction record.

## Corrections

If you find an error, please open an issue. Corrections are published as new versions, never made silently; see [edenopenly.com/editorial/corrections](https://edenopenly.com/editorial/corrections/).

## Licence

The data and documentation are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); the scripts under the MIT licence (`LICENSE`). Short quotations from the sources in `data/claims.csv` are included for verification and remain the property of their publishers.

## Citation

Eden. *Five numbers, five ways of counting: what the trans suicide figures circulating in the UK actually measure.* Evidence Note EN-025, version 1.0. Eden Openly; 2026. doi:10.5281/zenodo.23327489
