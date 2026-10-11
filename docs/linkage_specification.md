# Prospective linkage specification

I designed this prospective linkage specification for an anonymous worker-firm panel. The administrative and fieldwork linkage described below has not been carried out.

Create distinct entities for firm/enterprise, establishment/site, mine, lease, corporate legal entity, respondent, business contact and contract. A firm can operate several sites or leases, change its legal owner and appear in several administrative systems. Do not collapse these automatically.

Maintain a source-specific ID crosswalk with source vintage, original and normalized name, geography, mineral, confidence, matching method, reviewer and validity dates. Prefer verified CIN/LLPIN, mine code, lease ID and official procurement identifiers. Survey-generated IDs remain the primary panel key. Exact ID matches come before deterministic name/address matches and reviewed fuzzy matches. Never infer caste from a name.

Use a separate many-to-many firm-site-lease bridge. Resolve duplicate procurement and company entries before counting outcomes. Distinguish operator changes, renewals and legal restructurings from firm exits. A closed mine does not necessarily mean the company exited, and an awarded lease does not imply operational production.

Store private identity/contact keys separately from analysis files. Linkage permission is source- and respondent-specific. Release only disclosure-controlled aggregates. A failed link is missing with a documented reason, not a zero outcome. Record unmatched rates by owner group, firm size and registration status to diagnose selective linkage.

Current frame priorities are Rajasthan quarrying/stone; Odisha major-mineral operators and contractors; and Maharashtra as a district-method pilot. These are reasoned proposed locations, not fieldwork already conducted. Retain separate strata for mineral, operator versus contractor, registration, baseline size and locality. Use area listing to cover establishments absent from formal lease registers.
