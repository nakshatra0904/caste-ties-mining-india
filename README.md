# Caste ties and firm growth in India's mining industry

I compiled this research repository with a detailed LaTeX report, 19 graphs, a 65-entry data-source inventory, acquired public inputs, all extracted analytical data, nine regional establishment specifications, four controlled worker-duration models and reproducible Python scripts. I also drafted fieldwork instruments and prospective causal identification designs.

**Evidence status:** I completed a historical public-data analysis and developed a detailed research design. It is not a completed causal study of caste networks. The acquired data do not contain actual caste ties or repeated outcomes for the same mining firm. I did not invent survey respondents, firm observations, growth histories or causal estimates. Evidence vintages are Census 2011, EC6 2013–14, ILO 2021, Arisa/CLRA 2024 and Coal India snapshots 2024/2026. No source is a complete current national mining-worker panel.

## Results and their implications

The extracted national mining and quarrying tables contain **85,176 establishments and 557,474 workers**, averaging **6.54 workers per establishment** across all ownership forms. About 73.74% of establishments are rural. Establishments with hired workers account for 52.03% of establishments and 88.84% of recorded workers. The latter is employment **at** establishments with hired workers; it is not the fraction of workers who themselves are hired.

The proprietary subset contains **73,170 establishments and 319,425 workers**. Aggregate employment scale by the owner's broad social category is:

- **SC:** 8,799 establishments, 23,171 workers; **2.63 workers per establishment**.
- **ST:** 6,489 establishments, 23,853 workers; **3.68 workers per establishment**.
- **OBC:** 28,485 establishments, 107,323 workers; **3.77 workers per establishment**.
- **Others:** 29,397 establishments, 165,078 workers; **5.62 workers per establishment**.

The SC mean-size ratio is **46.9% of the Others ratio**, or about **53.1% smaller**. SC owners account for 12.03% of proprietary establishments but 7.25% of their employment. These are ratios of published employment totals to establishment totals, not medians or estimated conditional firm effects. Others is a residual category and cannot be relabelled upper caste. Owner group does not identify workers' caste.

![Owner-group employment scale](figures/mining_size_by_social_group.png)

The national merge covers **35 historical state/UT regions**, pooling residual Andhra Pradesh and Telangana to match Census 2011 undivided Andhra Pradesh. Size regressions use 33 nonempty regions because Delhi and Lakshadweep have zero establishments. A separate replication covers **35 historical Maharashtra districts**. These boundaries predate current administrative changes.

I fitted nine OLS models describing regional relationships between SC/ST population shares and mining size, density or hired-establishment share. The adjusted models control for regional urbanization and literacy; S1 supplies an unadjusted comparison. They use **HC3 standard errors and t-based 95% intervals**. In the adjusted state log-size model, the SC coefficient per ten percentage points is **0.0306** (95% interval **−0.4932 to 0.5544**), and the ST coefficient is **0.0084** (**−0.1421 to 0.1589**). The Maharashtra adjusted log-size coefficients are **−0.0406** for SC and **0.1273** for ST, also imprecise.

One SC coefficient in the state log(1+density) model has unadjusted **p=0.0362**, but its **BH q=0.6513** across the stated family of 18 SC/ST coefficients. **No social-composition coefficient passes the Holm or BH correction.** Wide intervals are uncertainty, not proof of no relationship. Small regional samples, omitted geology and mineral composition, spatial dependence and measurement mismatch limit interpretation.

![All regional coefficients](figures/all_regression_intervals.png)

Descriptive industry fixed-effect contrasts across 92 industry-by-owner-category cells suggest smaller SC-owned scale relative to Others across sectors: approximately −22.97% under equal cell weighting and −17.51% under establishment weighting. These are aggregate contrasts without firm-level or causal inference. They are supplementary context, not evidence that caste ties cause growth.

**What the results imply:** unequal historical business scale merits direct investigation of financing, buyer access, equipment, licensing, inherited resources and exclusion. The data do not distinguish among those mechanisms. Regional SC/ST population composition is a weak proxy for the relationships the research question concerns. The substantive next step is a consent-based owner and contact panel, linked where authorized to mine/lease/company/procurement identifiers and measured at baseline, 12 and 24 months.

**Research relevance:** mining spans formal operators and less visible quarrying, contracting, transport and services. A sound dissertation should distinguish them, observe actual functional relationships, separate entry and exit from incumbent growth, and identify how improved business access changes outcomes. A proposed cluster-randomized business-introduction intervention is developed in the report, alongside qualified DiD, RD, IV and doubly robust designs. None was estimated as a causal design with the acquired cross-section.

## Worker composition, recruitment and controlled results

The Census worker baseline contains **2,105,736 main-plus-marginal workers** in NIC divisions 05–09: **439,519 SC (20.87%)**, **364,749 ST (17.32%)**, and 1,301,468 remaining workers. Remaining includes OBC and other groups. The EC6 worker totals classify establishments; Census B18 classifies persons. Their differing totals cannot be read as growth or an informal-work residual.

I fitted four employment-weighted regressions using **1,275 observed cells across 35 historical state/UT regions**. The outcome is the share working less than six months in the reference year. W1 is unadjusted; W2 controls sex/residence; W3 adds state and mining-division effects; W4 absorbs their joint strata. SC contrasts versus Remaining fall **3.83 → 2.47 → 1.89 → 1.49 percentage points**; ST contrasts fall **10.99 → 7.58 → 6.23 → 5.08 points**. W4 state-clustered model intervals are **−0.46 to +3.45 (SC)** and **+3.58 to +6.58 (ST)**. Full control coefficients, sample definitions and source rows are archived. Age, education, occupation and employer/referral characteristics are not jointly available and are not invented.

**Interpretation:** geographic, mineral and sex/residence composition explains part of the pooled descriptive difference. The remaining ST duration contrast motivates research on seasonal tasks and access to longer-duration work; it is not a causal discrimination or caste-network estimate. Marginal duration is not a contract/formality measure, and inference describes a regional model, not Census enumeration error.

![Controlled worker contrasts](figures/worker_controlled_duration_contrasts.png)

Local Arisa/CLRA interviews in Makrana report **82% SC workers** and **80% entering through relatives/co-workers**, among 50 interviewees. These are separate margins without a caste-by-route table; no controlled hiring regression can be fitted from them. I retained published education, locality, contract, piece-rate, advance and PPE details, including conflicting advance percentages. ILO's two-cluster sample reports broad worker groups and job-entry/working-condition evidence. Local samples cover the stone supply chain and are not national mining estimates.

Coal India discloses **214,333 employees on 1 January 2026**, including SC 16.49%, ST 12.48% and OBC 18.85%. Corporate employment groups and two-date stocks are distinct from mine-face workers and recruitment flows. The SECL vacancy example records **350 advertised / 345 filled** posts; its ST vacancy-fill rate is not an ST applicant hiring probability.

**Relevance:** these additions make the labour recruitment/retention mechanism measurable and guide a matched worker-firm panel. Thirty new W01–W30 fieldwork measures bring the draft instrument to **86 items**. The report now supplies **19 figures and 35 statistical tables**, with **65 source entries** and roughly 12,050 narrative words before appendices. All controls actually used are documented; further PLFS wage models remain prospective until unit records are acquired.

## Data actually used

1. **MoSPI/CSO, All India Report of Sixth Economic Census.** Government-authored; acquired from an [Ecensus mirror](https://ecensus.in/wp-content/uploads/2022/10/All-India-Report-of-Sixth-Economic-Census.pdf) after official download attempts failed. [Official producer landing](https://www.mospi.gov.in/all-india-report-sixth-economic-census). Mining state establishment/worker tables: Table 2.5, PDF p.145 (printed p.135), and Table 4.5, PDF p.169 (printed p.159). Owner-group proprietary counts: Tables 12 and 15, PDF pp.195 and 198 (printed pp.185 and 188). The mirror is the acquisition route; MoSPI is the statistical producer.
2. **Government of Maharashtra, Sixth Economic Census 2013 report**, acquired from the [NITI for States repository](https://www.nitiforstates.gov.in/public-assets/Policy/policy-repo/urbanization/RSS71M000226.pdf). District mining counts and workers: Tables 2.5 and 4.5, PDF pp.123 and 147 (printed pp.117 and 141).
3. **Census of India 2011 Primary Census Abstract**, [catalogue 6191](https://censusindia.gov.in/nada/index.php/catalog/6191), [exact workbook](https://censusindia.gov.in/nada/index.php/catalog/6191/download/9268/DDW_PCA0000_2011_Indiastatedist.xlsx). Supplies historical populations, SC/ST shares, urban shares and literacy denominators. Literacy uses population age seven and above.


4. **Census 2011 B18 / B18SC / B18ST**, [all workers](https://censusindia.gov.in/nada/index.php/catalog/43234), [SC](https://censusindia.gov.in/nada/index.php/catalog/43270), [ST](https://censusindia.gov.in/nada/index.php/catalog/43302): actual official Excel counts by division, sex, rural/urban residence and main/marginal duration. These supply worker composition and controlled duration results.
5. **Coal Ministry annual reports**, [2023–24 chapter 16](https://www.coal.nic.in/sites/default/files/2024-07/chap16AnnualReport2024en2.pdf) and [2025–26 chapter 16](https://www.coal.nic.in/sites/default/files/2026-02/chap16AnnualReport2026en.pdf): administrative employee snapshots and selected vacancy flows. Transcribed counts reconcile to published totals.
6. **Arisa/CLRA**, [Caste in stone, November 2024](https://arisa.nl/wp-content/uploads/Caste-in-stone_November-2024.pdf): selected aggregate local worker composition, recruitment and conditions; no individual records.
7. **ILO**, [Rajasthan natural stone employment study, 2021](https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_dialogue/%40sector/documents/publication/wcms_781885.pdf): published two-cluster worker composition and working-condition summaries; no matched firm panel. Full ILO and Arisa publications are linked rather than copied into this repository; acquired hashes and selected factual cells are retained.
8. **PLFS 2023–24**, [catalogue 213](https://microdata.gov.in/NADA/index.php/catalog/213): layout and interview instructions acquired to verify potential individual controls; **not a microdata input for fitted regressions**. Labour Bureau mining wage and SC/ST survey sources are identified leads, not acquired individual datasets.

SHA-256 hashes and download/failure logs are in `provenance/`. The underlying EC unit is an establishment. A mine, enterprise, company, lease, owner and household are distinct units. EC broad industry code 05 means Mining and quarrying; it should not be confused with NIC division 05 alone.

[View all nineteen graphs](docs/figure_gallery.md). The report contains **19 figures, 35 statistical tables and the complete 86-item draft questionnaire**, in addition to the narrative and 65-entry source inventory.

## Wider source map

The [source catalogue](data/derived/source_catalogue.csv) classifies **65 entries**, with URLs, access status, unit, social information, growth information and research use. It covers EC4/5/6 and EC7 status; Census/DCHB; PLFS/IHDS; ASUSE/ASI and their coverage limits; IBM yearbooks, monthly statistics, prices, leases and MTS; coal statistics; DGMS/DGH; major/minor mineral auctions; Parivesh/consent systems; state mining registers; MCA/Prowess/company filings; Udyam/NSSH/procurement; finance/tax/labour/trade sources; geology/DMF/spatial data; associations and primary fieldwork.

The three establishment inputs and the worker sources described above supply the executed analysis and published empirical summaries. PLFS documentation is acquired, but PLFS individual records are not. Registered microdata, commercial databases, restricted returns and candidate sources were not silently treated as downloaded data. ASUSE is not a mining-sector replacement; standard ASI coverage does not provide a census of all mine operators. The catalogue is broad but cannot certify that every possible Indian record exists or was located.

## Contents

- `report/caste_ties_and_mining_growth_india.tex`: self-contained LaTeX report, approximately 12,050 narrative words before the full tables, graphs and source appendix. It embeds vector plot coordinates and needs no external images to compile.
- `report/narrative.md`: original detailed research narrative.
- `figures/`: all 19 PNG graphs, including ownership, concentration, geographic scatterplots, all coefficients, correlations, influence and prospective power.
- `data/raw/`: establishment reports/PCA plus official Census worker tables, coal chapters and PLFS documentation. Local research publications are linked with hashes; full ILO/Arisa publications are not redistributed.
- `data/derived/`: counts, demographic joins, descriptive moments/percentiles, correlations, full coefficients, HC3 intervals, multiple-testing adjustments, leave-one-out ranges, influence diagnostics, industry-cell contrasts and power assumptions.
- `docs/`: data dictionary, linkage specification, fieldwork instrument and prospective pre-analysis plan.
- `scripts/`: portable acquisition, extraction, analysis, plotting and LaTeX-building code.
- `provenance/`: source catalogue, download logs, versions, checks, compilation status and integrity manifest.

## Reproduce locally

Create a Python environment, install `requirements.txt`, then run:

```sh
python -m pip install -r requirements.txt
python scripts/reproduce.py
```

The default reproduction is offline and uses the bundled source files and extracted text. To regenerate the layout text, run `python scripts/extract_text.py` before reproduction. To reacquire exact inputs, run `python scripts/download_inputs.py`; the script checks hashes and stops if source bytes change. No API key, paid database or respondent file is required for the observed-data analysis.

The principal substantive checks are exact table totals and arithmetic identities, merge cardinality and geographic reconciliation, raw-file hashes and coefficient reproduction. Regeneration can change image metadata and therefore PNG byte hashes while preserving plotted values. Numerical-library versions are pinned; see `provenance/software_versions.json` for the actual authoring environment.

## LaTeX compilation status

I successfully compiled the current LaTeX source with the local editor compiler on 11 October 2026. Earlier environment failures were resolved, and I corrected a source-formatting error and wrapped long graph labels. Compilation stayed local. The report PDF is available in the existing editor preview; this repository contains the complete, engine-validated source rather than an exported PDF file.

On a working local TeX Live/MiKTeX setup or a user-controlled LaTeX environment, compile this same source with:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=report report/caste_ties_and_mining_growth_india.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=report report/caste_ties_and_mining_growth_india.tex
```

A third pass may be necessary for long-table widths. Dependencies are standard LaTeX packages: geometry, amsmath/amssymb, booktabs, longtable, array, xcolor/colortbl, TikZ/PGFPlots, hyperref and xurl. See `provenance/compilation_record.json`. The current source passed local engine compilation; page layout should still be reviewed before academic submission.

## Repository and source distribution

My repository is [nakshatra0904/caste-ties-mining-india](https://github.com/nakshatra0904/caste-ties-mining-india). The downloadable archive contains the same research files. I chose private visibility for the initial deposit. Each source file is below GitHub's 25 MiB browser-upload limit and its ordinary 100 MiB repository file limit ([GitHub documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)); the package excludes installed environments, credentials and respondent identifiers. Public reports/data retain original authorship and terms; review those terms before redistributing a public repository. `LICENSE-CODE.txt` applies only to original code. Cite the original institutions separately from my research report.

Do not add fieldwork identities, named contact networks, confidential tax/financial records or restricted microdata to a public repository. The proposed fieldwork requires consent, separate linkage keys and disclosure control, as specified in the report.
