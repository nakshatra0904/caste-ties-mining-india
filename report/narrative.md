# Research question and what this report establishes

I developed a dissertation research programme on caste relationships and enterprise growth in India's mining economy, and completed the empirical analyses supported by the public data I acquired. The central finding is a substantial descriptive difference in the employment scale of proprietary mining establishments across owners' broad social groups. The central identification finding is equally important: the available tabulations do not observe business relationships or repeated outcomes for the same firm. They therefore cannot identify the causal effect of caste ties on growth. The completed regressions describe geographic associations; the fieldwork and causal designs specify how to answer the original question credibly.

I used three source documents for my original establishment analysis: the government-authored All India Report of the Sixth Economic Census, Maharashtra's Sixth Economic Census report, and the Census of India 2011 Primary Census Abstract spreadsheet. I obtained the national report from an Ecensus mirror after official download attempts failed, and the Maharashtra report from NITI for States. I retained source files, acquisition routes, hashes, table locations, extracted data, transformations, statistical outputs and figures in my research package. These are historical data, principally 2011 and 2013-14, not a description of the mining economy in 2026. [S02] [S07] [S09]

There are 85,176 mining and quarrying establishments and 557,474 workers in the extracted national tables. The proprietary subset contains 73,170 establishments and 319,425 workers. Among that subset, workers per establishment are 2.63 for SC owners, 3.68 for ST owners, 3.77 for OBC owners and 5.62 for the residual Others category. These are ratios of employment totals to establishment totals, not medians of individual firms. The SC ratio is about 46.9 percent of the Others ratio. That difference motivates research on resources, market access and exclusion, but does not by itself establish any one mechanism.

I fitted nine regional OLS specifications. The national demographic merge contains 35 historical state/UT regions after pooling residual Andhra Pradesh and Telangana to match the 2011 undivided Andhra Pradesh geography. Log-size models have 33 observations because Delhi and Lakshadweep have no mining establishments in the extracted table. The Maharashtra replication contains 35 historical districts. Adjusted log-size associations with regional SC and ST population shares are imprecise. One SC coefficient in the state density model has an unadjusted p-value of 0.036, but the Benjamini-Hochberg adjusted value is 0.651 for the specified family of 18 social-composition coefficients. No causal conclusion follows from it.

I propose building a consent-based owner and business-relationship panel, linked where authorized to mine, lease, company and procurement identifiers. Fieldwork should cover operators and contractors separately, include both registered and less visible businesses, and follow surviving firms, exits and new entrants. A randomized introduction or procurement-brokerage intervention is the most defensible prospective route to a causal estimate of access to business relationships. Observational policy designs remain useful, but must establish a credible comparison group and cannot simply label a policy coefficient a caste-network effect.

I extended the analysis with official Census B18, B18SC and B18ST counts, two Coal India employee snapshots, selected recruitment disclosures and published Rajasthan worker evidence. The worker baseline contains 2,105,736 people in NIC divisions 05-09. Four fitted aggregate duration models show how SC/ST differences change with sex, rural/urban residence, state and mining division controls. The expanded inventory has 65 entries, the report includes nineteen graphs, and the questionnaire now has 86 draft measures including 30 worker/job-entry items. The worker chapter specifies source-specific denominators and limitations. [S56] [S57] [S58] [S59] [S60] [S61] [S62]

## Evidence status

I completed source discovery and classification; downloading the three actual inputs; extracting national state tables and 23 industry by four social-group cells; constructing state and district demographic joins; checking arithmetic; producing descriptive statistics, correlations, nine OLS models, HC3 intervals, influence diagnostics, leave-one-out ranges, multiple-testing corrections, aggregate industry fixed-effect contrasts, twelve establishment graphs and illustrative trial-power calculations; the worker extension adds seven graphs and four employment-weighted controlled comparisons.

I did not conduct interviews, invent respondents or access a proprietary firm panel. No actual caste-tie variable, firm sales-growth series, individual-firm survival history, randomized assignment, policy treatment panel, instrumental-variable first stage or valid regression-discontinuity running variable was acquired. Consequently, I have not estimated a causal effect of caste ties or regressed observed mining firm growth on observed caste ties. I developed a detailed research specification for those analyses once the required data exist.

I assembled an expanded source inventory containing 65 entries, including documents, databases, administrative systems and source families. It is deliberately broad, but cannot certify that every possible Indian record has been located. Entries distinguish downloaded inputs, verified public documentation, conditional or commercial access, candidate source families and primary data still to be collected. A portal's existence is not treated as proof that its transaction-level data are publicly downloadable.

# Conceptual framework

## Caste identity and caste ties are different objects

An owner's broad category is an attribute. A caste tie is a relationship with another person or organization that may transmit information, trust, credit, labour, referrals, political access or obligations. A person can share a broad category with another entrepreneur without sharing a jati or any actual relationship. Conversely, a business tie can cross jati, category, religion or locality. Administrative SC, ST, OBC and residual classifications must not be treated as four internally uniform social networks.

I propose distinguishing at least four measurements in my future fieldwork. First, record self-reported broad social category and optional self-described jati. Second, observe named or coded business contacts and the respondent's own account of whether a relationship is connected to shared community identity. Third, record what each contact actually did, when it occurred and whether money or business information changed hands. Fourth, measure the eligible opportunity set: nearby businesses, procurement buyers, lenders, labour brokers and associations with which contact could plausibly have occurred.

Scheduled Tribe identity also deserves a distinct analytical treatment. Adivasi social organization, community claims, land access, displacement and the institutional circumstances of mining are not adequately represented by assuming they are identical to caste-based entrepreneur networks. SC and ST results should be presented separately before any pooled disadvantaged-group analysis. The EC residual Others category is a coding residual; it is not a validated indicator of upper-caste identity or dominance. [S01] [S13]

I will not infer individuals' caste from surnames, photographs, geography, directors' names or association labels. Identity and relationship information should come from voluntary self-report or an explicitly authorized administrative classification, with a separate unknown or declined-response code. This preserves construct validity and avoids turning uncertain social classification into a hidden measurement error.

## Mechanisms and competing hypotheses

H1 is an information mechanism: community contacts reduce the cost of learning about leases, tenders, buyers, equipment and credit. H2 is an enforcement mechanism: repeated social interaction permits trade credit and informal insurance where legal collection is costly. H3 concerns labour recruitment and monitoring: referrals can ease hiring, but may also segment jobs and exclude outsiders. H4 concerns access to gatekeepers: connected firms may navigate administrative requirements or secure introductions more quickly. These hypotheses require process measures, not merely a coefficient on owner category.

H5 is a constraint mechanism. Dense within-community networks can lock firms into a narrow buyer pool, impose transfers or obligations, and discourage relationships outside a familiar market. H6 is an exclusion mechanism: established networks may screen out entrepreneurs from historically disadvantaged groups even when those entrepreneurs have comparable productive capabilities. The effect of ties can therefore vary by type of contact, social location, mineral, scale and institutional setting. A single positive or negative average coefficient would conceal that heterogeneity.

Resources and selection produce competing explanations. Wealthier households may both enter capital-intensive mining and sustain influential contacts. Larger firms may attract buyers and lenders, creating ties as a consequence of success. Migration may alter both network composition and business opportunities. Technology, concession size, mineral quality, inherited land, local demand and formal-company organization can generate size differences even if relationships have no causal effect. The report treats these alternatives as hypotheses to discriminate, not as explanations already demonstrated.

The literature offers motivation rather than a transferable mining estimate. Iyer, Khanna and Varshney's work establishes the usefulness of Economic Census ownership information for studying entrepreneurship and social hierarchy. Munshi and Rosenzweig examine how traditional networks can influence choices and mobility in a different setting. Neither study licenses extrapolating a causal coefficient to Indian mining firms. The research contribution here would be direct relationship measurement in a sector with strong licensing, geology and buyer concentration, followed by longitudinal or experimental identification.

## Outcomes and estimands

The preferred primary outcome is employment growth over a pre-specified interval, with real sales growth and survival as separate outcome families. A secondary outcome is production growth in mineral-specific physical units. Employment should separate owner work, unpaid family work, directly hired labour and contract labour. Sales should separate production sales, trading revenue and inter-company transactions. A firm with several mines requires both establishment-level and legal-entity-level accounts.

For continuing businesses with positive employment at both dates, annualized log employment growth is defined as follows. It should be supplemented by levels and by a symmetric growth measure that handles entry and exit, since conditioning only on survivors selects on an outcome affected by relationships.

```math
g_i^{E}=\frac{\log E_{i,t_1}-\log E_{i,t_0}}{t_1-t_0},\qquad
g_i^{DHS}=\frac{2(E_{i,t_1}-E_{i,t_0})}{E_{i,t_1}+E_{i,t_0}}.
```

For a prospectively randomized brokerage offer, the primary estimand is the intention-to-treat effect of being offered the programme among eligible baseline firms. A treatment-on-the-treated interpretation for actual relationship formation needs additional assumptions. It is inappropriate to describe the effect of an offer containing training, information and introductions as the pure effect of caste ties. Those components must be measured and, where feasible, separated by design.

```math
\operatorname{ITT}=\mathbb{E}[Y_i(1)-Y_i(0)],\qquad
Y_i(z)=\text{outcome under assignment }z.
```

For the observational panel, the target must be stated as an association unless a defensible identification argument is supplied. A one-standard-deviation increase in a pre-specified relationship index, a new buyer introduction and a change in within-jati tie share are different exposures and estimands. The dissertation should not switch among them after inspecting which specification is significant.

# Mining sector scope and the empirical population

## Operators and the mining supply chain

The core operator universe uses the relevant mining and quarrying classification. NIC 2008 Section B covers divisions 05 through 09, including coal and lignite, petroleum and natural gas, metal ores, other mining and quarrying, and support activities. The Sixth EC broad activity code 05 is a broad mining category; it is not NIC division 05, which specifically denotes coal and lignite. Confusing those two code systems would create a serious sample error. [S01] [S02]

Mining-dependent suppliers can belong to transport, machinery repair, construction, trading, professional services or other classifications. A supplier should be included on the basis of a documented mining revenue share or verified mining contracts, not on its industry code alone. A practical threshold is to pre-specify a mining sales-exposure measure and retain the continuous share for robustness. Operator estimates and supplier estimates should be reported separately even when both populations are sampled in the same district.

Major-mineral mines, small stone quarries, sand operations, coal enterprises and hydrocarbon operators face different reporting and concession regimes. The all-India public-data analysis is broad; the prospective fieldwork should concentrate on populations in which owner relationships can be measured reliably and enough independent businesses exist. Large public enterprises can serve as buyers and institutional context, but their own output cannot be attributed to an entrepreneur's caste network.

## Geographic priorities

An initial core could combine Rajasthan's stone and quarrying businesses, Odisha's mineral and contractor ecosystem, and Maharashtra's quarrying and contractor population. The inclusion of Maharashtra is supported by an actually acquired district dataset, which permits frame checks and a transparent replication. Odisha has a verified public lessee register and an administrative system with stable codes. Rajasthan offers a potentially useful small-operator setting, but its current frame needs to be acquired and checked before district selection. [S07] [S33] [S34] [S35]

The final cluster list should be chosen after a short listing pilot rather than by declaring well-known mining districts representative. Stratify within states by mineral, formal operator versus contractor, approximate scale, rurality and lease or contract status. Include commercially active locations and areas with small or intermittent operations. Oversample groups with small entrepreneur counts, while retaining probabilities and survey weights so the target population remains explicit.

Geography must be historical when historical data are used. The national merge pools EC residual Andhra Pradesh and Telangana into the 2011 state of Andhra Pradesh. The Maharashtra merge uses 35 districts in their historical configuration, including Thane before Palghar's later separation and the older names in the source. Present-day district maps should not be applied to these counts without a documented crosswalk. There is no spatial regression or geocoded mine map in the completed analysis.

# Data discovery and acquisition strategy

## Four layers of evidence

Layer 1 is the establishment frame: Economic Censuses, state directories, lease registers, Udyam and a new area listing. Layer 2 is outcomes: authorized mine returns, company accounts, production and dispatch records, procurement contracts and repeated field measurements. Layer 3 is relationships: a consented owner and alter module, association participation and dated introductions. Layer 4 is context: geology, mineral prices, transport access, population composition and institutional events.

No single identified source provides all four layers. Economic Census data are particularly useful for broad coverage and owner category but weak for direct relationships and firm-level growth. Company panels provide financial trajectories but exclude many small businesses and do not supply validated owner caste. Administrative mining records may provide physical outcomes and concession events but require access verification and still need a relationship module. IHDS offers household social-capital questions and longitudinal household information, with mining sample size and business attribution still to be checked. [S01] [S12] [S20] [S37] [S39]

ASUSE and the related unincorporated manufacturing, trade and service sources need a coverage check before use. The checked official coverage excludes mining Section B. They may be valuable for eligible ancillary enterprises, but treating them as a mining-operator dataset would misstate the population. ASI likewise requires an explicit factory and industry eligibility check; mineral processing and manufacturing are not automatically the same population as mine operators. [S15] [S16]

## Acquiring usable records

First request original EC5 and EC6 microdata through the official registered access route, schedules, record layouts and code lists. Obtain social group by mining by district tabulations if direct unit access is delayed. Retrieve the official distribution when possible to verify the mirrored national report byte-for-byte or reconcile content differences. Do not mix provisional and final census totals. The official FAQ checked during this work describes seventh-census finalization; an unverified final seventh-census file is not included. [S03] [S05]

Second request a deidentified mine-month or mine-year panel from IBM and the selected state departments, including mine code, lease holder, mineral, physical output, employment, dispatch, operational status, filing status and revisions. Ask for unsuccessful and non-operating records as well as operating mines. A returns system can omit precisely the businesses most likely to exit or remain informal. Administrative non-filing must not be silently recoded as zero production. [S20] [S21] [S34]

Third seek the university's Prowess licence or authorized MCA research access. Define entity identifiers and preserve standalone and consolidated financial statements. Add procurement bidder and award records for a clearly scoped set of buyers and services. Losing bidders and eligibility failures are particularly valuable: a winners-only dataset cannot estimate the probability of obtaining a contract. Obtain the relevant portal terms before downloading or redistributing restricted extracts. [S38] [S39] [S45]

Fourth undertake field listing and an owner panel. Record permission for each linkage, maintain contact information outside the analytical files, and use a stable pseudonymous firm identifier. Mine codes, legal firms and operating establishments form a many-to-many system. The linkage table must preserve ownership transfers, separate subsidiaries and multiple mines, rather than collapsing them into a deceptively simple one-row-per-company file.

## Access status and search limits

The archive includes an acquisition log with successful and failed attempts. The official national-report landing and some older MoSPI download routes did not yield a usable report during my acquisition attempts, while a government-authored mirror did. EC microdata metadata were discoverable, but the requested downloadable unit records were not acquired. Original microdata have not been replaced with invented establishment observations or surname-derived owner labels.

The 65-entry appendix records source-specific access and analytical roles. Families such as GST, payroll, bank credit, GeM, state-board consents, other state mining departments, exporter records and association lists remain conditional research leads. Their presence in the appendix is not a claim of access or an assessment of every file's schema. I have not sent institutional data requests or opened accounts to obtain restricted research records.

# Construction of the completed analytical data

## Extraction and source traceability

The national report contributes Table 2.5 on mining establishments at PDF page 145, printed page 135, and Table 4.5 on mining employment at PDF page 169, printed page 159. Table 12 at PDF page 195, printed page 185, and Table 15 at PDF page 198, printed page 188, provide industry by owner-group establishment and employment totals. The Maharashtra report contributes Table 2.5 at PDF page 123, printed page 117, and Table 4.5 at PDF page 147, printed page 141. Page references are one-based.

I extracted the trailing numerical columns for each geography and checked every row against own-account plus hired-establishment totals, rural plus urban totals and combined counts. The extracted national totals reconcile to 85,176 establishments and 557,474 workers. The Maharashtra totals reconcile to 6,229 establishments and 29,527 workers and match the national Maharashtra row. The four mining owner-group counts reconcile to 73,170 proprietary establishments and 319,425 workers.

The numerical columns labelled employment in establishments with at least one hired worker include all persons working in those establishments. They are not counts of hired workers alone. Similarly, an own-account establishment has no hired worker under the census definition but may involve several household members. Misreading these columns would distort both employment shares and average size.

There are 92 aggregate industry-group observations, consisting of 23 broad industries crossed with four owner groups. These are not 92 sampled firms and are certainly not 52 million independent microdata rows. I therefore computed the industry contrasts as ratios of published counts and reported descriptive point estimates without manufacturing firm-level standard errors.

## Demographic joins and transformations

The PCA input supplies total population, SC population, ST population, urban population and literate population at state and district levels. I joined state codes to historical geographic units after correcting Andhra Pradesh, and checked Maharashtra district names against both the source names and the historical district codes. The completed merge retains all 35 state/UT regions and all 35 Maharashtra districts; no unmatched geography is silently dropped.

```math
\overline E_r=\frac{W_r}{N_r},\qquad
d_r=100000\frac{N_r}{P_r},\qquad
h_r=100\frac{N_r^{H}}{N_r}.
```

Here W is workers, N is establishments, P is the 2011 population and NH is the count of establishments with at least one hired worker. The population reference date differs from the establishment enumeration period. Density is a contextual historical measure with that timing limitation. SC and ST shares equal their population counts divided by total population, multiplied by 100. Literacy equals the literate population divided by population aged seven and above, not total population.

Size and hired shares are undefined when establishments are zero. They remain missing for Delhi and Lakshadweep; they are not filled with zero. Density includes the zeros. The density regression uses log of one plus establishments per 100,000 residents, making that dependent variable explicitly different from log density. The 50-establishment restriction is a sensitivity analysis intended to reduce instability in small district denominators, not a rule for deleting genuine large mines.

## Quality and measurement limitations

Arithmetic reconciliation validates extraction, not census completeness. Under-enumeration, industry miscoding, intermittent activity and ownership classification can remain. The EC does not supply a verified longitudinal business identity in these tabulations. The national ownership categories are reported for proprietary establishments; incorporated operators, partnerships and public enterprises do not inherit a caste label from a table about proprietors.

The mineral composition of a region is not observed in the completed regressions. Major metal mines, smaller stone units and support activities can have very different labour intensity. This missing composition is a plausible explanation of geographic variation. Local demographics and infrastructure may also influence selection into mining. The report does not claim that basic literacy and urbanization controls remove these confounders.

The package preserves raw numerical counts and full-precision transformations. Rounded published percentages are retained for checking, while reported shares are recomputed from counts. The distinction matters because rounded percentages may sum to 100.1 or 99.9 without any extraction error. Unknown categories, non-applicable ownership and true zero establishments should be kept conceptually separate.

# Descriptive findings

## Ownership and scale

The national average is 6.54 workers per mining establishment when employment and establishments are summed before division. About 73.74 percent of establishments are rural. About 52.03 percent have at least one hired worker, and those establishments account for 88.84 percent of workers in the mining table. Proprietary businesses comprise 85.90 percent of establishments but 57.30 percent of mining employment. This indicates that the establishment frame is dominated numerically by proprietors while employment is more concentrated in larger and other organizational forms.

Within proprietary mining, SC owners account for 12.03 percent of establishments but 7.25 percent of workers. ST owners account for 8.87 percent and 7.47 percent respectively; OBC owners account for 38.93 percent and 33.60 percent. Others account for 40.18 percent of establishments and 51.68 percent of workers. Employment in a social-group row is employment at establishments owned by that group. It is not employment of workers from that group.

The SC mean is about 53.1 percent lower than the Others mean. The ST and OBC means are about 34.5 and 32.9 percent lower respectively. This is meaningful for describing business scale in this historical proprietary population. It cannot establish whether differences arise at entry, through subsequent expansion, through survival, through mineral specialization or through access to finance and contracts. Those explanations require different data and empirical tests.

Comparing owner shares with the whole population can provide a rough context, but it is not a properly adjusted entrepreneurship participation rate. The eligible-owner denominator depends on age, location, labour-market attachment, household resources and business opportunity. A national OBC participation ratio cannot be calculated from the acquired PCA because that source has no comparable general OBC population denominator. Broad Others categories also differ across datasets.

## Geography and heterogeneity

After combining Andhra Pradesh and Telangana, the five largest state/UT regions account for 49.41 percent of establishments and 51.25 percent of workers. The establishment Herfindahl index is 0.0722 and the employment index is 0.0768 across those historical regions. These indices describe geographic concentration, not firm market concentration or buyer competition. They are affected by region size and aggregation.

The unweighted mean of the 33 non-empty regional size ratios is 9.18 workers, while their median is 6.48. These differ from the national 6.54 because the national ratio weights each regional mean by its establishment count. An average of regional ratios answers a different question from the ratio of national totals. The discrepancy is particularly large when small regions contain a few large operations.

Maharashtra has 6,229 mining establishments and 29,527 workers, for a pooled mean of 4.74 workers. Across districts the unweighted mean is 5.73 and the median is 3.15. Chandrapur's ratio is 58.5 workers per establishment, reflecting 5,148 workers across 88 establishments in the table. This is not a reason to classify the observation as an error: it is a reason to inspect sector composition and influence. The 23-district restriction with at least 50 establishments yields another explicit target population.

The report provides raw regional counts, denominator-based indicators, distribution summaries, rank figures, social-group shares, cross-industry ratios and the state correlation matrix. Histograms describe distributions of regional mean sizes. They do not describe the individual-firm employment distribution. Individual medians, firm-size percentiles, inequality within owner groups, and the fraction of SC mining firms above a given size cannot be recovered from the acquired aggregates.

## Cross-industry contrasts

An aggregate descriptive model relates log of the group-specific industry mean size to industry indicators and group indicators. With equal weight per industry-group cell, the fitted SC contrast is -0.261 log points, approximately 23.0 percent smaller than Others. The OBC and ST contrasts are approximately 16.6 and 15.3 percent smaller. With establishment-count weights, the SC contrast is about 17.5 percent smaller and the OBC and ST contrasts about 13.5 and 13.4 percent smaller.

These results are summaries of published cell means across industries. Changing the weights changes the target summary, so the two estimates are not robustness proofs for a causal parameter. The particularly large raw mining SC contrast is useful for prioritizing a sector-specific investigation. It cannot show that a mining mechanism is statistically different from an individual-firm mechanism in other industries. No sampling p-values are presented for the cell models.

# Regression methods and completed results

## Specifications

The completed regional models use a baseline specification with SC and ST population shares, and an adjusted specification adding urban population share and literacy. All shares are scaled so a unit increase means ten percentage points. The source observations are regions, not individual owners. The dependent variables are log mean employment size, log of one plus establishment density, and the share of establishments with at least one hired worker. Each outcome has its own units.

```math
\log \overline E_r=\alpha+\beta_{SC}\frac{s_{SC,r}}{10}
+\beta_{ST}\frac{s_{ST,r}}{10}
+\gamma_U\frac{u_r}{10}+\gamma_L\frac{\ell_r}{10}+\varepsilon_r.
```

S1 is the state log-size baseline. S2 adds the two controls. S3 repeats the adjusted size model among the 28 historical states excluding 2011 UTs. S4 uses transformed establishment density across all 35 regions, including zero-count regions. S5 uses the hired-establishment share in 33 non-empty regions. D1, D2 and D3 repeat adjusted size, density and hired-share models in the 35 Maharashtra districts. D4 restricts adjusted district size to the 23 districts with at least 50 establishments.

I used HC3 heteroskedasticity corrections and t-based intervals for the regional OLS models. The HC3 adjustment gives greater weight to the uncertainty introduced by high-leverage observations. These are model-based uncertainty summaries across a hypothetical population of comparable regions; the published census counts are not a random sample of these particular regions. Spatial dependence remains unaddressed because verified coordinates or a contemporaneous boundary adjacency file were not acquired. HC3 is not a correction for all spatial correlation.

## Main coefficients and interpretation

In S2, the SC coefficient is 0.0306 with a 95 percent interval from -0.4932 to 0.5544; the ST coefficient is 0.0084 with an interval from -0.1421 to 0.1589. These associations are small at their point estimates but extremely imprecise. For example, the SC interval permits a substantial negative or positive relationship of local population composition with regional mean mining size. It does not permit a confident finding of no relationship.

In D1, the SC coefficient is -0.0406 with an interval from -0.6760 to 0.5948. The ST coefficient is 0.1273 with an interval from -0.2685 to 0.5230. The district data similarly do not identify a stable adjusted association. The ecological regressions should therefore be used as a description of context and a check against overconfident geographic narratives, not as an owner-level caste-effect analysis.

S4 yields an SC coefficient of -0.5284 on log of one plus establishment density, with an unadjusted p-value of 0.0362. A ten-percentage-point difference in SC population share corresponds to a fitted factor exp(-0.5284), about 0.59, for one plus density, conditional on the included controls. This cannot simply be reported as a 41 percent reduction in density itself, particularly near zero. The association may reflect geology, mineral composition, administrative coverage, region size or other omitted factors.

I defined an exploratory testing family of eighteen SC/ST coefficients across the nine regional models and calculated Holm and Benjamini-Hochberg adjustments, which I retained in the CSV. The S4 SC adjusted value is approximately 0.651; no coefficient meets a 5 percent threshold after the corrections. The models and sample restrictions were selected for feasibility and sensitivity analysis rather than chosen after screening for significance. This remains exploratory work, not a preregistered confirmatory study.

## Influence and robustness

Cook's distances and leverage are retained for every observation in every OLS model. Leave-one-out coefficient ranges show how a fitted relationship changes when each region is removed in turn. The report also contrasts inclusion and exclusion of UTs and removes very small district denominators in D4. Such checks can reveal instability, but they do not cure omitted geology or replace direct network measurement.

When a large mine creates a high district average, deleting it would change the question from all mining establishments to a selected small-scale segment. The appropriate response is to collect mineral, organizational form and operating-scale information, then stratify or model those features. Winsorization should be a pre-specified sensitivity exercise, not a method of forcing a convenient coefficient. I did not winsorize the completed model data.

The raw regression table includes all intercepts and control coefficients, sample sizes, R-squared values, HC3 standard errors, raw p-values and confidence intervals. The source package also contains the influence file, the correlation matrix and full descriptive output. I emphasize social-composition coefficients in my main discussion because they address the research question, and I retain the other fitted terms in the complete results.

# Why the completed results cannot identify caste ties and growth

## Missing treatment and missing longitudinal outcomes

Identification requires an observed exposure and an outcome related to the desired causal contrast. The acquired caste tables observe owner category and total employment at a single enumeration. Regional tables observe population composition and aggregate mining scale. None observes the tie intensity Ti, the baseline firm size Ei0 and the subsequent outcome Ei1 jointly for a business. Repeated aggregate censuses would help describe net changes but would still mix entry, exit and incumbent expansion.

Many different business histories can produce the same aggregate table. One world could have no effect of community relationships and strong inherited-resource differences. Another could have powerful network advantages offset by other disadvantages. Both could reproduce the observed owner-group counts and employment totals. Because those worlds imply different causal effects while yielding the same acquired data, the desired effect is not identified by these tabulations.

This is not a problem resolved by adding more regression commands. Fixed effects, matching, propensity scores, a complex machine-learning model or an instrumental-variable label cannot reconstruct an unobserved treatment. Data construction and the assignment mechanism must lead the econometric choice. The observed disparity is an important fact about scale; it is not an estimate of discrimination or the economic return to same-caste contacts.

## Causal pathways and adjustment

The conceptual graph has baseline household resources, geology, inherited land and business ability affecting both relationships and outcomes. Baseline social identity can affect treatment opportunities and resources. Relationships can affect finance, buyer access and hiring, which can affect growth. Previous firm success can also create relationships. Local institutions and commodity demand influence several pathways simultaneously.

If the goal is the total effect of relationships, controlling for credit or contract wins measured after the relationship was formed may block mechanisms the study is trying to estimate. If the goal is a direct effect holding finance constant, stronger assumptions are required and the estimand changes. Baseline predictors, mediators and outcome consequences need separate variable tags in the data dictionary.

A district fixed effect can compare firms facing a shared local environment, but does not remove owner-specific wealth or ability. A firm fixed effect can remove time-invariant characteristics, but not a new buyer relationship formed in anticipation of expansion. Lagging contacts improves temporal ordering but cannot guarantee exogeneity. Fixed effects do not randomize owner identity.

# Prospective causal inference designs

## A randomized business introduction design

The most credible prospective intervention is a randomized offer of structured business introductions or brokerage among eligible firms. Randomize clusters of connected business environments when introductions can spill over. Stratify assignment by state, mineral, baseline scale and the sampled owner categories. Pre-specify an equal-probability treatment assignment and retain a control group receiving any ordinary public information required by the study's ethical commitments.

Measure whether the offer creates additional business relationships, whether those relationships cross existing community boundaries, and whether new contacts yield actual loans, quotations, contracts or orders. Primary outcomes can be real sales, employment and survival at 12 and 24 months. Programme delivery must not discriminate against participants based on caste. Subgroup analyses should examine heterogeneity in access and gains while presenting the overall programme effect first.

```math
Y_{ic,1}=\alpha+\tau Z_c+\rho Y_{ic,0}
+\lambda_{\text{randomization stratum}}+X_{ic,0}'\theta+e_{ic}.
```

Estimate intention-to-treat by assignment with inference at the randomization unit. Report take-up and a first stage for relationship formation. Instrumenting actual ties with assignment could target a local effect only if the exclusion, monotonicity and relevance conditions are credible. A package that independently teaches procurement rules or improves applications violates a pure relationship exclusion restriction unless those channels are isolated. The principal claim should remain the causal effect of the offered programme.

Networks create interference. A contact made by a treated business can become available to controls; contracts can also be displaced from controls to treated firms. Record contact sharing and define exposure to treated neighbours before analysis. A saturation or two-stage randomized design can estimate direct and spillover effects, but it requires enough clusters and a defensible interference map. Arbitrary post hoc network definitions would undermine the estimand. Aronow and Samii provide a formal framework for exposure-based inference; the specific exposure definitions here remain a proposed study decision.

## Policy and auction difference in differences

A plausible observational programme would examine a verified change in auctions, procurement support, registration, portal access or licensing that varies across eligible units and time. Collect several outcome waves before the event and enough after it, including unaffected or not-yet-affected comparable units. Define exposure using eligibility and actual legal implementation, rather than whether a firm benefited or won a contract.

If treatment timing is staggered, estimate cohort-time effects using a method appropriate for heterogeneous treatment effects and state the comparison groups explicitly. Callaway and Sant'Anna offer one such framework. Avoid interpreting a conventional two-way fixed-effects coefficient mechanically when already-treated firms become controls. Show event-study estimates with simultaneous uncertainty, composition checks and robustness to comparison-group choice. A failure to reject pre-trends is not proof of parallel trends.

```math
\operatorname{ATT}(g,t)=
\mathbb{E}[Y_t(1)-Y_t(0)\mid G=g],\quad t\geq g.
```

An interaction with baseline self-reported network strength can test effect heterogeneity, but it identifies a policy effect differing by baseline connections, not necessarily the causal effect of those connections. Policy adoption can reflect local mining conditions, administrative capacity or political demand. The nationwide 2015 change is not automatically a staggered experiment. A dissertation must show the actual exposure variation and legal timing relevant to the selected population. [S24] [S25]

## Regression discontinuity and close auctions

A verified support-programme cutoff could permit a discontinuity design if eligibility is determined by a predetermined score that firms cannot precisely manipulate, outcomes are smooth in the score absent treatment, and observations exist on both sides. Collect the complete running variable, the operational threshold, exceptions, application outcomes and programme take-up. Inspect bunching, balance and the local support. None of those inputs was acquired for this report.

A close-auction design needs the exact bidding mechanism, all bids, tie rules, eligibility conditions and reasons bids were rejected. Merely comparing winners with losers close in an endogenous bid does not create random assignment. Even a credible local allocation effect concerns acquiring a concession or contract. A caste-network interpretation additionally requires observed relationships and an argument separating allocation from other channels.

## Instruments that should not be assumed valid

Historical caste concentration, distance to co-community settlements, geology, mineral prices, local political ties and family business ownership are tempting instruments. Each plausibly affects growth directly or proxies persistent resources and demand. Their exclusion restrictions are therefore weak without unusually strong evidence. Historical instruments can add a veneer of causality while magnifying measurement error and geographic confounding.

If a valid instrument emerges, report the institutional argument first, then relevance, weak-instrument diagnostics, reduced-form outcomes and the scope of the local effect. Use uncertainty methods that remain valid when the first stage is weak. Overidentification tests cannot establish that all excluded instruments are valid. The present report does not estimate an IV model because no defensible observed instrument-treatment-outcome dataset exists.

## Observational matching and doubly robust estimation

Once the firm panel exists, matching or inverse-probability approaches can improve comparisons on observed baseline characteristics. They require conditional exchangeability, positivity, consistent treatment definition and adequate measurement. Diagnose common support and effective sample size; trim according to pre-specified rules and report the resulting population. Outcome and treatment nuisance models can be estimated with cross-fitting in sufficiently large samples.

These methods remain vulnerable to unobserved inherited resources, ability and anticipated growth. Report estimates as conditional associations unless the exchangeability argument is credible. A sensitivity analysis should ask how much omitted confounding would overturn the substantive conclusion, not merely whether the adjusted p-value is below a threshold. Network spillovers and endogenous tie formation are additional complications beyond ordinary binary treatment selection.

# Fieldwork design and questionnaire

## Sampling and recruitment

Start with a frame merge of leases, registrations, firms, directory entries, buyer vendors and a new area listing. Deduplicate establishments while retaining multiple sites under one legal firm. List inactive concessions, intermittently operating units and known closed businesses. Do not rely exclusively on referrals from influential association members: such recruitment can build the treatment into the sample selection mechanism.

A proposed baseline target is 1,200 businesses across 80 clusters, with roughly 15 businesses per cluster. This is a design assumption, not an observed sample. Allocate separate operator and contractor strata and ensure multiple clusters within each selected state and mineral. A trial would need an explicit cluster assignment unit; a descriptive panel could use different sampling clusters. Final allocation should follow pilot response rates, subgroup incidence, costs and measured outcome variability.

Use probability sampling within completed listings, with documented oversampling for smaller entrepreneur groups. If a hard-to-reach segment requires a supplemental referral sample, label it separately and do not claim that inverse-probability weights solve unknown inclusion probabilities. Weights for population estimation should reflect listing and within-cluster selection; regression estimands should clarify whether they target the sampled firms or the frame population.

## Owner and business module

Collect legal and operating names, pseudonymous business ID, organizational form, mines and sites, operating start, mineral, support activity, licence and registration status, and the respondent's role. Record all active owners and ownership shares where feasible. Ask who exercises effective control, separately from the legal proprietor. Do not automatically assign a multi-owner business the caste of the interviewer’s main respondent.

The identity module asks voluntary self-reported broad category, optional jati name, state of category recognition, religion where relevant to the conceptual question, and whether the respondent wishes to decline. Retain original text in a protected coding environment and use a documented harmonized classification in the analytical file. Record ambiguity rather than forcing a category. Interview owners in a setting where colleagues or gatekeepers cannot overhear sensitive answers.

The baseline resource module covers education, earlier experience, inherited business or concession, initial capital source, household assets in broad bands, previous employment, land access, equipment and initial workforce. Sensitive wealth and revenue questions should offer ranges and a declined-response option. Distinguish inherited capability, family financing and commercial relationships in both questions and analysis.

## Relationship name generators

Ask the respondent to identify coded contacts who helped obtain the most recent major buyer, loan, equipment, licence-related information, large contract or recruitment batch. For each contact record role, relationship origin, date first known, date of assistance, geographic location, frequency of interaction and whether the contact has business authority. Separate family relationships from explicitly reported community relationships and from ordinary commercial referrals.

Ask whether the respondent considers each contact part of the same jati or community, whether that fact mattered to the introduction, and whether the contact's identity is directly known. Do not force respondents to classify an alter they do not know. Relationship coding should include unknown and declined responses, as well as cross-community contacts. Contacts need not be named publicly: local identifiers and a protected linkage key can support panel tracking.

For each assistance event ask what changed: a buyer introduction, a quotation, a guarantee, a loan amount or range, deferred payment, information about a tender, a hiring recommendation, or no observable result. Record the sequence of dates. A contact merely known to the owner is different from a contact activated for business, and the latter is different from a completed transaction.

## Financial and growth module

Collect monthly or quarterly employment and production where records exist, plus the preceding fiscal year's sales, costs, inventories, equipment purchases, borrowing and receivables. Retain evidence flags: audited statement, ledger, payslip or payroll, dispatch record, respondent recall, or bounded estimate. Align recall windows to the fiscal year or operating season and record downtime. Separate quantity, grade and price to distinguish production growth from commodity-price changes.

Measure buyer and supplier concentration, top-customer revenue share, payment delays, contract values, bidding participation, wins, reasons for nonparticipation and geographic market reach. Record credit applications and rejections as well as loans received. Ask about formal and informal finance separately. Contract workers require establishment and employer identifiers to avoid counting the same labour both at the contractor and mine operator.

Panel follow-ups at 12 and 24 months should verify operating status and collect growth outcomes. A closed business remains in the panel. Ask the owner or a permitted substitute about closure timing and reasons, and distinguish temporary suspension from exit. Track ownership transfers and mergers. New entrants can form a supplementary entry sample, but they should not be mixed with the original experimental cohort without explicit definitions.

## Qualitative work

Conduct a nested qualitative sample selected for analytical contrasts: different minerals, owner categories, business scales, strong versus weak networks, successful versus unsuccessful applications and surviving versus exiting firms. A provisional target of 60 to 90 interviews is a planning range, not a saturation claim. Include lenders, buyer procurement officers, association representatives and workers where the research question requires them.

Interview guides should reconstruct events rather than solicit only general views about caste. Compare accounts of the same transaction when permission permits, triangulate documents, and record disagreement. Analyse negative cases in which relationships failed to help or cross-community ties became commercially important. Qualitative evidence can sharpen mechanisms and reveal mismeasurement; it does not substitute for the assignment assumptions of a causal estimate.

# Network measurement and analysis plan

## Core indicators

Define the activated business-contact set before estimating relationships with growth. A within-jati share is the fraction of classified activated contacts the respondent reports as sharing jati. Record its denominator and the fraction whose identity is unknown. A categorical broad-group homophily index is a different measure and should not replace the jati-specific index without explanation.

```math
H_i=\frac{\sum_j A_{ij}1\{J_i=J_j\}}{\sum_j A_{ij}},\qquad
C_i=\frac{\text{activated contacts with classification}}{\text{all activated contacts}}.
```

H should be missing when no eligible classified contacts exist, while Ci records classification completeness. Report the number of contacts, within-community share, cross-community bridging ties, functional diversity, geographic reach and dependence on the strongest contact separately. A high share with only one contact is different from a high share across ten contacts. Fix the maximum number of elicited alters or record truncation so interview caps do not masquerade as network limits.

Adjust homophily for the plausible opportunity set where that set is measured. For example, local co-jati prevalence among listed eligible suppliers can benchmark observed contact shares. General village SC share is not a substitute for the prevalence of the owner's jati among eligible mining buyers. Availability-adjusted homophily is especially important when an apparent same-community preference is mechanically generated by who is nearby.

An ego-network survey does not identify complete network centrality, global betweenness or the entire mining industry's network structure. Such measures require a sufficiently complete bounded network and accurate alter linkage. Use degree and brokerage measures appropriate to the observed design, preserve anonymous unlinked alters, and test sensitivity to missing links. Any reported network visualization should avoid making protected identities reidentifiable.

## Firm panel specifications

The descriptive baseline panel can regress later growth on baseline tie measures, owner identity and baseline resources, with location by mineral effects. Separate a total-association model from models including potentially mediating credit and buyer access. Interactions with SC, ST and OBC identity should be pre-specified and interpreted within their support. Report group-specific sample sizes and tie distributions.

```math
g_{i,t+1}=\alpha_{d\times m}+\beta T_{i,t}
+\sum_c\delta_c1\{C_i=c\}
+\sum_c\phi_cT_{i,t}1\{C_i=c\}+X_{i,0}'\theta+u_{i,t+1}.
```

Repeated employment levels can support firm fixed effects and mineral-by-time controls. Dynamic specifications need enough waves and careful treatment of endogenous lagged outcomes. A two-wave observational panel cannot justify an elaborate dynamic GMM procedure merely because such software exists. With small samples, simple transparent specifications and credible assignment are preferable to a long list of fragile estimators.

Analyze employment, real sales and production in separate outcome families. Use appropriate deflators and price exposure. Report survival separately and present a growth measure that includes exits. Conditional-survivor sales growth answers a selected question; it should not be the sole headline result if the programme changes survival. Quantile or distributional analysis needs adequate firm-level data and cluster-aware inference.

# Power, inference and pre-analysis commitments

## Power assumptions

The supplied power table is illustrative. It assumes equal treatment assignment, 15 baseline businesses per cluster, 20 percent attrition, 80 percent power, a two-sided 5 percent test, and intracluster correlations of 0.02, 0.05 and 0.10. Calculations use a cluster-based t critical value plus the normal 80-percent power quantile and a design effect evaluated at the retained average cluster size. They do not incorporate any verified pilot residual variance or covariate gain.

```math
\operatorname{DEFF}=1+(m_{\rm retained}-1)\rho,\qquad
\operatorname{MDE}_{SD}\approx
(t_{0.975,G-2}+z_{0.80})\sqrt{\frac{4\operatorname{DEFF}}{n_{\rm retained}}}.
```

The 1,200-business, 80-cluster proposal with ICC 0.05 yields an MDE of roughly 0.23 outcome standard deviations under these assumptions. If the residual standard deviation of log growth were 0.5, that corresponds to roughly 0.114 log points. That standard deviation is assumed, not estimated from this study. Unequal clusters, rare group incidence, noncompliance, spillovers and multiple outcomes may require more clusters or larger samples.

Heterogeneous effects by owner group require their own power calculations. A design adequately powered for the overall programme effect can be badly underpowered for an SC-versus-ST interaction. Do not promise precise subgroup estimates without pilot incidence and cluster allocation. Compute detectable first-stage changes in relationships as well as detectable outcome changes before funding the intervention.

## Pre-analysis plan

Register the primary estimand, primary outcome window, assignment unit, strata, sample exclusions and treatment coding before outcomes are observed. Fix rules for permanent exit, temporary shutdown, multiple sites, ownership transfer and missing accounts. Pre-specify baseline adjustment and the distinction between total programme effects, mechanisms and exploratory heterogeneity.

Declare outcome families and multiplicity corrections. For an experimental study, use randomization inference when appropriate and cluster inference at the assignment level. For few clusters, use methods suited to that design rather than relying only on asymptotic robust standard errors. Report confidence intervals and substantively meaningful magnitudes; absence of statistical significance does not establish absence of an economically meaningful effect.

Track missingness by treatment assignment, owner category, mineral and baseline size. Report attrition rates and reasons. Weighting under a missing-at-random assumption should be accompanied by sensitivity analysis. Bound outcomes under transparent scenarios when missingness is plausibly nonignorable; monotonicity-based bounds require a defended direction of selection. No attrition adjustment was needed in the completed census-table analysis because it is not a respondent panel.

## Placebos and robustness

For the observational policy design, inspect pre-treatment outcomes, alternative unaffected minerals or service categories, eligibility placebo definitions, policy anticipation and concurrent changes. A convincing placebo test cannot rescue an implausible assignment mechanism, but contradictory placebo evidence can undermine it. Collect the same information for treated and comparison groups to prevent differential outcome measurement.

For the firm panel, vary credible baseline resource controls, geographic and mineral strata, outcome definitions and treatment measures. Show sensitivity to network classification completeness, ties that predate business establishment, self-reported versus documentary outcomes, and the presence of family firms. Use a principled limited set of checks; do not search every transformation and report the subset with favourable signs.

# Ethics, governance and field implementation

## Consent and disclosure control

The relationship module concerns potentially sensitive social identity and commercial arrangements. Explain the research purpose, voluntary participation, right to skip questions, intended use and linkage options in the respondent's preferred language. Seek the applicable institutional ethics review before fieldwork. Separate permission to be interviewed from permission to link records, contact alters or conduct follow-ups. Participation should not affect licensing or procurement opportunities.

Store names, phone numbers, exact locations and linkage keys separately from analytical data. Limit access to the minimum research team, encrypt retained identifiers and define a deletion schedule. Public releases should suppress small cells and remove reidentifiable relationship diagrams. A public GitHub repository should contain code and properly licensed aggregates; it should not contain raw owner identities, classified alter identities or unauthorized commercial histories.

Sensitive statements about influence, exclusion or administrative contact should be recorded without assuming illegality. Qualitative claims need corroboration and appropriate anonymization. Enumerators must not pressure respondents to name officials or discuss actions they consider risky. This study is designed to measure business relationships and economic outcomes, not to classify people from external clues or make unsupported allegations.

## Enumerator and data quality protocol

Pilot the identity and relationship questions in the selected local languages. Use neutral examples, separate the question about knowing a contact from the question about receiving assistance, and test whether respondents distinguish caste, family and business association. Rotate or standardize module order to reduce priming. Capture interview duration, skipped modules and reasons for ambiguous classifications.

Use checks that flag inconsistent units, duplicated sites, improbable employment jumps and mismatched fiscal years. Confirm a subset of nonsensitive numerical responses and document enumerator corrections. Back-checking should not disclose one respondent's caste or commercial relationships to another. Record provenance for each correction rather than overwriting the original response invisibly.

## Proposed timetable

Months 1-3 should cover original-data access, administrative negotiations, instrument translation and ethics review. Months 4-5 should conduct listing and a small pilot, finalize power and cluster selection, and freeze the pre-analysis plan. Months 6-9 should complete baseline fieldwork and any randomized rollout. Short verification contacts can monitor operating status, while outcome follow-ups occur at 12 and 24 months after baseline. Analysis and dissertation writing follow validated data freezes rather than an arbitrary promise of immediate causal results.

A formal budget should be built from local quotes for listing, enumerators, travel, translation, data management, follow-up and record acquisition. No fabricated rupee budget is presented. The scope can be scaled by reducing minerals or states while preserving enough independent clusters; expanding geographic coverage without sufficient cluster depth can weaken the actual identification design.

# Interpretation and dissertation contribution

The acquired data demonstrate historical inequality in the scale of proprietary mining businesses across broad owner categories. The strongest current result is the gap in ratios of employment to establishments, supported by exact published counts and reproducible arithmetic. The findings do not identify the effects of caste ties, discrimination, ability or inherited resources. The regional regressions reinforce that caution: local population shares are weak and imprecise proxies for the actual relationships the question concerns.

The relevance is practical. A fieldwork project can use the Economic Census as a coverage benchmark, administrative mine and lease systems as a current operator frame, financial or production records as growth outcomes, and a new relationship panel as the essential treatment measurement. A study that combines those sources can ask whether community relationships facilitate entry and expansion, constrain diversification, or mediate exclusion, with distinct evidence for each mechanism.

A credible dissertation contribution would be threefold: direct measurement of functional business relationships in a differentiated mining population; longitudinal separation of entry, survival and incumbent growth; and an identified intervention or policy comparison showing how access to relationships changes economic outcomes. I assembled the source map, historical statistical baseline and research architecture needed to pursue that contribution. It should be cited as a preliminary public-data analysis and research design, not as a completed causal dissertation.

Policy implications remain conditional. The observed size gap supports investigating whether entrepreneurs face unequal financing, buyer access, equipment or licensing constraints. It does not yet establish that a particular caste-based programme will improve growth. A brokerage trial could test whether opening business access helps and whom it helps; complementary resource and discrimination measures are needed before attributing any observed advantage to networks alone.

# Reproducibility and reading the research package

The package contains the self-contained LaTeX report, source inventory, raw acquired reports and spreadsheet, extracted text, derived CSV files, full statistical results, all nineteen PNG figures, scripts, requirements and a README. Hashes identify the downloaded files. The national mirror and official producer are both recorded. Download failures and unavailable unit records are documented rather than hidden.

The analysis script reproduces the source extraction, joins, ratios, regressions, diagnostics, descriptive cell contrasts and power assumptions. An additional plotting script produces the extended figure set. Code does not require a commercial licence or a hidden respondent dataset. The raw-source hashes and totals provide meaningful integrity checks; exact coefficient reproduction also depends on numerical-library versions, which are specified.

The standalone LaTeX document embeds plotting coordinates and tables, so it is designed to compile without external figure assets. The PNG versions are supplied for reuse in slides or papers and correspond to the information reproduced in the report; panel arrangement may differ. The source is opened in the built-in editor. The archive records the actual compilation outcome and any environment limitations. I prepared a public GitHub research deposit containing the compiled report, editable source, public inputs, analysis outputs and reproducible scripts. The deposit does not contain confidential respondent records.

Historical tables can be reused for context, but a current dissertation should update the frame and validate the original releases before making current-policy claims. New microdata, administrative panels or fieldwork responses should be added as separately versioned inputs, with their own terms and access log. Re-running the public-data scripts will not magically add the unobserved relationships or growth outcomes.

# Selected methodological and substantive references

Iyer, Lakshmi, Tarun Khanna and Ashutosh Varshney. Caste and Entrepreneurship in India. Harvard Business School working paper 12-028, 2011; related article in Economic and Political Weekly 48(6), 2013. Primary working paper: https://www.hbs.edu/ris/Publication%20Files/12-028_0e6e69ba-da4d-4abc-b66a-9611dc07c53b.pdf . Used to motivate ownership and enterprise research, not to supply a mining causal estimate.

Munshi, Kaivan and Mark Rosenzweig. Traditional Institutions Meet the Modern World Caste Gender and Schooling Choice in a Globalizing Economy. American Economic Review 96(4), 2006. https://pubs.aeaweb.org/doi/abs/10.1257/aer.96.4.1225 . Used for conceptual motivation about networks and mobility in a different population.

Callaway, Brantly and Pedro H C Sant'Anna. Difference in Differences with Multiple Time Periods. Journal of Econometrics 225(2), 2021. Author manuscript: https://psantanna.com/files/Callaway_SantAnna_2020.pdf . Used to specify a potential staggered-policy design; no such design was estimated with the acquired cross-section.

Aronow, Peter M and Cyrus Samii. Estimating Average Causal Effects under General Interference with Application to a Social Network Experiment. Annals of Applied Statistics, 2017. https://arxiv.org/abs/1305.6156 . Used for a proposed exposure and spillover framework; no observed network experiment is available here.

Central Statistics Office. All India Report of Sixth Economic Census. Ministry of Statistics and Programme Implementation, 2016. Official landing: https://www.mospi.gov.in/all-india-report-sixth-economic-census . Acquired mirror and exact empirical tables are documented in source S02.

Directorate of Economics and Statistics Government of Maharashtra. Sixth Economic Census 2013 Maharashtra. Acquired official repository copy: https://www.nitiforstates.gov.in/public-assets/Policy/policy-repo/urbanization/RSS71M000226.pdf . The exact mining district tables are documented in source S07.

Office of the Registrar General and Census Commissioner India. Primary Census Abstract India and States State and District Level 2011. https://censusindia.gov.in/nada/index.php/catalog/6191 . The downloaded workbook supplies the demographic denominators and controls.
