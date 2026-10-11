# Units, variables and transformations

I documented the units, transformations and controls used in my completed aggregate analysis below.

`mining_states_raw_2013.csv` has 36 Economic Census regions. The matched state table has 35 Census-2011 regions after pooling residual Andhra Pradesh and Telangana. The Maharashtra table has 35 historical districts. All three use EC establishment and employment counts, not company observations.

- `code`: published EC regional code; Maharashtra codes 01–35 are mapped to Census district codes 497–531.
- `geo_code`, `Name`: matching Census 2011 geographic code and name.
- `est_*`: number of establishments. `emp_*`: number of workers at those establishments.
- `rural`, `urban`, `total`: geographic subdivision and combined total.
- `oae`: own-account establishment; `hired`: establishment with hired workers. `emp_*_hired` counts **all workers at that class of establishment**, not only hired workers.
- `population`: Census 2011 total residents.
- `sc_pct`, `st_pct`: 100 times the respective Census population divided by total residents. These do not measure entrepreneurs' caste or tie intensity.
- `urban_pct`: 100 times Census urban residents divided by total residents.
- `literacy_pct`: 100 times literate residents divided by total population minus age 0–6 population.
- `mean_size`: EC workers / EC establishments; missing when the denominator is zero.
- `hired_est_pct`: 100 times establishments with hired workers / all establishments; missing when total is zero.
- `mining_rural_pct`: 100 times rural mining establishments / total mining establishments.
- `est_per_100k`, `emp_per_100k`: 100,000 times EC count / Census 2011 population.
- `log_size`: natural log of workers per establishment; missing for empty regions.
- `log_density`: natural log of one plus establishments per 100,000 residents.
- `*_10pp`: population percentage divided by ten. A one-unit increase is ten percentage points.
- `is_ut_2011`: historical Union Territory indicator. Jammu and Kashmir is a state at this vintage.

`industry_social_group_cells_2013.csv` has 23 broad industries × four owner groups = 92 aggregate cells. `establishments` and `employment` concern proprietary establishments classified by owner group. `mean_size` is a ratio of totals. `est_share_pct` and `emp_share_pct` are recomputed within industry. Published percentages are retained separately. `size_relative_others` divides group mean size by the same industry's Others mean size.

Regression fields are `model`, `outcome`, `term`, `beta`, `se_hc3`, `p_hc3_t`, `ci_low`, `ci_high`, `n` and `r2`. `p_holm_18`/`q_bh_18` adjust only the specified 18 SC/ST composition coefficients across nine models. They are blank for intercepts and other controls. HC3 intervals use model residual degrees of freedom. Geographic dependence is not eliminated by HC3.

Influence rows contain Cook's distance, leverage and residual. Rows beginning `LEAVE_ONE_OUT_` contain the minimum and maximum focal coefficient after separately removing every region. These are sensitivity summaries, not confidence intervals.

Descriptive statistics distinguish the unweighted mean across regions from the pooled national workers/establishment ratio. Percentiles describe regional means, not individual-firm distributions. Industry fixed-effect outputs are descriptive cell summaries, without reported microdata p-values.

Power fields are **assumptions/calculations**: baseline clusters and firms, retained firms under 20% attrition, ICC, design effect, MDE in SD and assumed log-growth units. No trial data were used.


## Worker extension

`worker_cells_census2011.csv` retains published workbook rows, historical state codes, NIC division, own social group, sex, residence, main and marginal counts. Only zero/absent division rows are padded against the all-worker grid; all-state sums reconcile to India. `Remaining` is derived All−SC−ST, including OBC. Do not add Persons to Male/Female, Total residence to Rural/Urban, or India to states. Main/marginal is six-month duration, not contract formality.

`worker_regression_cells2011.csv` contains only 1,275 nonempty disjoint state×division×sex×area×group cells. `marginal_pct` is 100×marginal/total; `total` is the denominator weight. W1–W4 use weighted least squares. W3 has additive sex/area/state/division controls; W4 has joint contextual strata. `beta_pp` is a percentage-point contrast; state-cluster SE/intervals are model-based. Population weights are not independent microdata sample counts. All coefficient values, reference categories, specifications and data are archived.

Coal counts use disclosed corporate employee stocks, not all workers or applicants. Remaining = Total−SC−ST−OBC, including EWS in 2026. `secl_vacancy_filling2024_25.csv` uses vacancy categories; UR is not worker caste. Fill percentage = 100×filled/advertised.

Stone study files retain published margins and source PDF pages. Rounded ILO group percentages sum to 99 and are not normalized. Budhpura's composition denominator is unresolved between instrument scopes. Makrana recruitment has N=50; the referral count 40 derives from the stated 80%. No joint caste×route records exist. Count-based and percentage-only indicators are distinguished; the conflicting Makrana 36%/38% advance reports are documented. PPE use does not establish adequate protection.
