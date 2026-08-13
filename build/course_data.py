"""Single source of truth for TGS-2026061581 courseware."""

TITLE = "Strategic Mergers and Acquisitions - Valuation, Risk, and Integration"
SHORT_TITLE = "Strategic Mergers and Acquisitions"
COURSE_CODE = "TGS-2026061581"
TSC_CODE = "WST-CFI-5003-1.1-1"
TSC_TITLE = "Mergers and Acquisition"
VERSION = "v2.0"
VERSION_DATE = "13 August 2026"
DOC_VERSION = "2.0"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Dr. Alfred Ang"
DAYS = 2
GITHUB_URL = "https://github.com/tertiarycourses/TGS-2026061581-Strategic-Mergers-and-Acquisitions-Valuation-Risk-and-Integration"
LMS_URL = "https://lms-tms.tertiaryinfotech.com/"

LEARNING_OUTCOMES = [
    "LO1: Apply financial instruments and valuation methods to structure mergers and acquisitions that optimise organisational benefit and shareholder value.",
    "LO2: Evaluate the business, financial and tax impact of potential M&A deals using industry data and forecasting techniques.",
    "LO3: Identify, assess and manage M&A risks across the full transaction lifecycle from target selection to post-deal integration.",
    "LO4: Collaborate with stakeholders to develop and implement M&A plans while ensuring governance, synergy realisation and strategic alignment.",
]

KNOWLEDGE = [
    "K1: Financial instruments to shape the structure of a deal for the benefit of the organisation",
    "K2: Business impact forecast of potential M&A deals",
    "K3: Business valuation concepts",
    "K4: Industry knowledge of potential M&A targets, including patents, pricing pressures and tax considerations",
    "K5: Financial and tax implications of a deal on the organisation's financial position",
]

ABILITIES = [
    "A1: Support opportunities that improve tax efficiency, organisational valuation and internal economies of scale",
    "A2: Function as checks and balances throughout the M&A process",
    "A3: Facilitate implementation plans with internal stakeholders to integrate the acquired company",
    "A4: Risk-manage the process from target identification through diligence, execution and integration",
    "A5: Leverage business intelligence and data analysis to facilitate deal structuring",
    "A6: Identify and evaluate M&A opportunities that create shareholder value",
]

# Each lesson descriptor is rendered with a visual component; detailed procedures stay in the LG.
TOPICS = [
    dict(num=1, code="01", title="Deal Structuring and Valuation Principles",
         subtitle="Financial instruments · valuation · shareholder value · economies of scale",
         criteria="K1 · K3 · A1", concepts=[
             ("Deal thesis", "A transaction starts with a testable strategic rationale, not a price."),
             ("Structure", "Consideration, financing, control and risk allocation work together."),
             ("Value", "Triangulate methods; reconcile enterprise value to equity value."),
             ("Discipline", "Normalise earnings, challenge synergies and preserve downside protection."),
         ], lessons=[
             ("cards", "Merger, acquisition or another route?", [
                 ("Merger", "Businesses combine under shared control; governance must be redesigned."),
                 ("Acquisition", "A buyer obtains control through shares, assets or a negotiated business transfer."),
                 ("Alternatives", "Joint venture, alliance, licensing or organic build may deliver the objective with less integration risk."),
             ]),
             ("flow", "The M&A value chain", ["Strategy and target thesis", "Screen and approach", "Value and structure", "Diligence and negotiate", "Close and integrate"]),
             ("tile", "Why organisations pursue M&A", [
                 ("Scale", "Lower unit costs through procurement, systems and shared services."),
                 ("Scope", "Add capabilities, products, client segments or geographies."),
                 ("Speed", "Buy proven talent, technology, licences or distribution rather than build."),
                 ("Resilience", "Diversify revenue, reduce concentration or reinforce a strategic position."),
             ]),
             ("tile", "Consideration instruments", [
                 ("Cash", "Price certainty for the seller; liquidity and leverage pressure for the buyer."),
                 ("Shares", "Shares risk and upside; introduces dilution, valuation and governance questions."),
                 ("Earn-out", "Defers value until agreed performance is achieved; definitions must be precise."),
                 ("Rollover equity", "Keeps sellers invested in NewCo and aligns them with future value creation."),
             ]),
             ("tile", "Financing and risk-allocation instruments", [
                 ("Senior debt", "Lower cost and tax-deductible interest, but covenants constrain flexibility."),
                 ("Seller note", "Bridges a funding or valuation gap; seller retains credit exposure."),
                 ("Preferred / convertible", "Blends downside protection with participation in upside."),
                 ("Escrow / holdback", "Secures claims for warranties, indemnities or post-close adjustments."),
             ]),
             ("two", "Share purchase versus asset purchase", [
                 "Buyer acquires the legal entity and its contracts, assets and liabilities.",
                 "Continuity may be simpler, but unknown liabilities can follow the entity.",
                 "Diligence, warranties and indemnities are critical."
             ], [
                 "Buyer selects assets and assumed liabilities subject to transfer rules.",
                 "May permit tax basis step-up, but consents and novation can be complex.",
                 "Employee, licence and indirect-tax effects need local advice."
             ]),
             ("big", "Price is what is paid; value is what the buyer can defend.", "A valuation range must show assumptions, uncertainty and the bridge to the negotiated consideration."),
             ("flow", "Valuation triangulation", ["Normalise earnings", "Build standalone forecast", "Value with DCF", "Benchmark comps and precedents", "Reconcile to a range"]),
             ("tile", "Enterprise value and equity value", [
                 ("Enterprise value", "Value of operations available to debt and equity capital providers."),
                 ("Equity bridge", "EV minus debt-like items plus cash and agreed adjustments."),
                 ("Working capital", "Completion accounts or a locked-box protects the normal operating level."),
                 ("Per-share value", "Equity value divided by diluted shares, after options and other claims."),
             ]),
             ("two", "Income approach: DCF", [
                 "Forecast unlevered free cash flow from operating drivers.",
                 "Discount with a rate consistent with risk and cash-flow definition.",
                 "Estimate terminal value without letting it dominate unexplained."
             ], [
                 "DCF exposes value drivers and integration assumptions.",
                 "It is sensitive to WACC, terminal growth, margins and reinvestment.",
                 "Use scenarios and sensitivities; avoid false precision."
             ]),
             ("two", "Market approaches", [
                 "Trading comparables apply peer valuation multiples to the target's metric.",
                 "They reflect current market expectations but require genuinely comparable peers.",
                 "Adjust for scale, growth, margins, geography and business mix."
             ], [
                 "Precedent transactions reflect control premiums and deal-market conditions.",
                 "They may include strategic synergies not available to every buyer.",
                 "Date, cycle, structure and accounting consistency matter."
             ]),
             ("tile", "Normalising EBITDA and cash flow", [
                 ("Owner items", "Replace related-party or owner compensation with market levels."),
                 ("One-offs", "Remove genuinely non-recurring items, with evidence."),
                 ("Run-rate", "Reflect contracted or implemented changes without double counting."),
                 ("Cash conversion", "Test capex, working capital and tax; EBITDA is not cash flow."),
             ]),
             ("tile", "Valuation risk controls", [
                 ("Sensitivity", "Show value over a rational WACC and terminal assumption range."),
                 ("Scenario", "Build base, upside and downside operating cases."),
                 ("Cross-check", "Compare implied multiples and free-cash-flow yield."),
                 ("Independent challenge", "Separate deal advocacy from valuation review and approval."),
             ]),
             ("tile", "Value-creation levers", [
                 ("Revenue", "Cross-sell, price, retention, channel and new capability."),
                 ("Cost", "Procurement, property, technology and shared services."),
                 ("Capital", "Working capital, capex, tax and portfolio optimisation."),
                 ("Multiple", "Improve recurring revenue, resilience, governance and growth quality."),
             ]),
             ("cards", "Internal economies of scale", [
                 ("Commercial", "Shared brand, channels, CRM and client coverage."),
                 ("Operating", "Central procurement, platforms, training and administration."),
                 ("Financial", "Funding access, cash pooling and professionalised controls."),
             ]),
         ]),
    dict(num=2, code="02", title="Forecasting, Financial and Tax Implications",
         subtitle="Business impact · synergies · pro forma statements · tax",
         criteria="K2 · K5 · A1 · A2", concepts=[
             ("Standalone first", "Forecast the target before adding buyer-specific synergies."),
             ("Timing matters", "Separate run-rate benefit, ramp-up and one-off cost to achieve."),
             ("Three statements", "Trace assumptions through profit, cash flow and the balance sheet."),
             ("Tax is contextual", "Structure effects require jurisdiction-specific professional advice."),
         ], lessons=[
             ("flow", "Build a defensible deal forecast", ["Historical quality", "Standalone drivers", "Synergy cases", "Integration costs", "Cash and returns"]),
             ("tile", "Standalone forecast drivers", [
                 ("Volume", "Clients, units, capacity, utilisation or transactions."),
                 ("Price and mix", "Rate cards, discounts, segment mix and churn."),
                 ("Margin", "Labour productivity, procurement, delivery model and overhead."),
                 ("Investment", "Capex, working capital, technology and compliance."),
             ]),
             ("tile", "Synergy taxonomy", [
                 ("Revenue", "Cross-sell, pricing, retention and new routes to market."),
                 ("Cost", "Duplicate roles, vendors, facilities and systems."),
                 ("Capital", "Working capital, capex avoidance and financing efficiency."),
                 ("Dis-synergy", "Client loss, talent exits, service disruption or cannibalisation."),
             ]),
             ("two", "Run-rate benefit versus cash realisation", [
                 "Run-rate is the annualised benefit once fully implemented.",
                 "A phased ramp recognises hiring cycles, contracts and operational dependencies.",
                 "Owners and dates turn ambition into an integration commitment."
             ], [
                 "Cash realisation nets cost-to-achieve, tax and working-capital effects.",
                 "Track both recurring benefit and one-off spend.",
                 "Avoid recognising a synergy before the underlying action is complete."
             ]),
             ("tile", "Integration costs", [
                 ("People", "Retention, severance, relocation and training."),
                 ("Technology", "Migration, licences, cybersecurity and data remediation."),
                 ("Operations", "Rebranding, facilities, process redesign and advisers."),
                 ("Contingency", "A transparent risk allowance linked to specific uncertainty."),
             ]),
             ("flow", "Scenario design", ["Base case", "Downside drivers", "Severe but plausible", "Management actions", "Liquidity and covenant check"]),
             ("tile", "Deal return measures", [
                 ("NPV", "Present value of incremental cash flows less investment."),
                 ("IRR", "Discount rate at which deal cash flows have zero NPV."),
                 ("ROIC", "Post-tax operating profit relative to invested capital."),
                 ("Payback", "Time until cumulative cash inflow recovers the investment."),
             ]),
             ("two", "Accretion/dilution is not intrinsic value", [
                 "EPS accretion asks whether pro forma EPS rises after financing and accounting effects.",
                 "It can be influenced by relative P/E multiples, funding mix and buyback alternatives.",
                 "A deal can be EPS-accretive yet destroy economic value."
             ], [
                 "Value creation asks whether return exceeds the risk-adjusted cost of capital.",
                 "Use NPV/ROIC, strategic option value and downside resilience.",
                 "Report both views to decision-makers."
             ]),
             ("tile", "Financial statement effects", [
                 ("Profit and loss", "New revenue/cost base, financing, amortisation and integration charges."),
                 ("Balance sheet", "Consideration, debt, goodwill, intangibles and deferred tax."),
                 ("Cash flow", "Purchase consideration, transaction costs, integration spend and working capital."),
                 ("Ratios", "Leverage, liquidity, interest cover, margins and covenant headroom."),
             ]),
             ("flow", "Purchase price allocation", ["Identify consideration", "Fair-value assets/liabilities", "Recognise intangibles", "Record deferred tax", "Residual goodwill"]),
             ("tile", "Tax diligence questions", [
                 ("Compliance", "Returns, audits, uncertain positions and indirect taxes."),
                 ("Attributes", "Losses, credits and incentives, including limits after ownership change."),
                 ("Structure", "Share/asset route, financing, withholding and stamp duties."),
                 ("Integration", "Transfer pricing, systems, tax governance and reporting readiness."),
             ]),
             ("two", "Effective tax rate: opportunity and guardrail", [
                 "Interest may create a tax shield subject to deductibility limits.",
                 "Tax attributes can have value only if legally usable and supported by future profits.",
                 "Asset basis and intangible deductions vary by jurisdiction."
             ], [
                 "Do not optimise the model without legal substance and business purpose.",
                 "Model cash tax separately from accounting tax expense.",
                 "Escalate cross-border, anti-avoidance and transfer-pricing questions to advisers."
             ]),
             ("tile", "Checks and balances before approval", [
                 ("Data owner", "Every key assumption has a named source and as-of date."),
                 ("Independent case", "Finance challenges sponsor assumptions and double counting."),
                 ("Risk gate", "Legal, tax, compliance, cyber and people leads sign off."),
                 ("Board view", "Decision paper shows range, downside, mitigations and walk-away conditions."),
             ]),
             ("big", "A synergy is not value until an action, owner, date and cash impact are traceable.", "Forecasting connects the investment case to integration execution."),
         ]),
    dict(num=3, code="03", title="Target Identification, Risk and Intelligence",
         subtitle="Industry intelligence · screening · diligence · risk · BI",
         criteria="K4 · A4 · A5 · A6", concepts=[
             ("Thesis-led search", "Define the capability gap and target archetype before scanning names."),
             ("Evidence hierarchy", "Triangulate management data with external, operational and customer evidence."),
             ("Holistic risk", "Financial, operational, strategic, regulatory, cultural and external risks interact."),
             ("Decision intelligence", "Dashboards support judgement; they do not replace accountable approval."),
         ], lessons=[
             ("flow", "Target-screening funnel", ["Market map", "Long list", "Screening score", "Short list", "Approach and diligence"]),
             ("tile", "Industry intelligence", [
                 ("Market", "Growth, concentration, customer demand and disruption."),
                 ("Competition", "Differentiation, entry barriers, pricing pressure and substitutes."),
                 ("Capability", "Talent, patents, licences, data, technology and delivery model."),
                 ("Context", "Tax, regulation, geopolitics, ESG and funding conditions."),
             ]),
             ("tile", "Screening criteria", [
                 ("Strategic fit", "Does the target directly advance the deal thesis?"),
                 ("Financial quality", "Growth, margin, cash conversion and recurring revenue."),
                 ("Synergy fit", "Specific buyer advantages without double counting."),
                 ("Executability", "Valuation, owner intent, approvals and integration capacity."),
             ]),
             ("two", "Patents and intellectual property", [
                 "Confirm ownership, registrations, licences and freedom to operate.",
                 "Identify open-source, contractor and employee-created IP exposure.",
                 "Assess remaining life, enforceability and revenue dependence."
             ], [
                 "Map IP to products, customers and the deal thesis.",
                 "Evaluate obsolescence and substitute technologies.",
                 "Reflect remediation, protection cost and uncertainty in price or terms."
             ]),
             ("flow", "Due diligence workstreams", ["Commercial and strategic", "Financial and tax", "Legal and regulatory", "Operations and technology", "People, culture and ESG"]),
             ("tile", "Quality of earnings", [
                 ("Revenue", "Recognition, cut-off, concentration, backlog and churn."),
                 ("Costs", "Run-rate staffing, related parties, capitalisation and one-offs."),
                 ("Working capital", "Seasonality, ageing, provisions and normal level."),
                 ("Cash", "Conversion, capex, debt-like items and off-balance-sheet obligations."),
             ]),
             ("tile", "MDPI review: four connected risk themes", [
                 ("Information asymmetry", "Unequal or opaque information can distort price and decisions."),
                 ("Performance and reputation", "Operating outcomes and stakeholder trust influence each other."),
                 ("Litigation and investor protection", "Rights, enforcement and governance affect downside."),
                 ("Geopolitical factors", "Policy, sanctions and uncertainty can change feasibility and value."),
             ]),
             ("tile", "Enterprise M&A risk classes", [
                 ("Financial", "Overpayment, leverage, liquidity and forecast error."),
                 ("Operational", "Process, systems, service continuity and supply chain."),
                 ("Strategic", "Weak rationale, competition, customer response and disruption."),
                 ("Regulatory and cultural", "Approvals, compliance, leadership, talent and behaviour."),
             ]),
             ("two", "Risk identification and prioritisation", [
                 "Fishbone analysis prompts causes across people, process, technology, data, market and governance.",
                 "Diligence findings should describe cause, event and consequence.",
                 "Link every material risk to valuation or integration."
             ], [
                 "Score likelihood and impact with defined scales.",
                 "Use weighted multi-criteria methods only when assumptions are transparent.",
                 "Prioritise by exposure, velocity, detectability and control strength."
             ]),
             ("flow", "Risk response", ["Avoid", "Reduce", "Transfer or allocate", "Accept with appetite", "Monitor and escalate"]),
             ("tile", "Diligence red flags", [
                 ("Earnings", "Late adjustments, unexplained margins or unsupported add-backs."),
                 ("Concentration", "Dependence on a client, partner, employee, licence or platform."),
                 ("Control", "Weak approvals, data lineage, cybersecurity or regulatory evidence."),
                 ("Culture", "Leadership gaps, regretted attrition, grievance patterns or conflicting incentives."),
             ]),
             ("tile", "Business intelligence for deal analysis", [
                 ("Market view", "Peer multiples, pricing, market share and customer sentiment."),
                 ("Target view", "Cohorts, margin bridges, pipeline, churn and productivity."),
                 ("Risk view", "Exceptions, incidents, litigation, cyber and compliance indicators."),
                 ("Integration view", "Synergy, milestones, talent, clients and Day One readiness."),
             ]),
             ("flow", "Decision gates", ["Thesis gate", "Indicative value gate", "Diligence gate", "Signing gate", "Close and Day One gate"]),
             ("big", "Uncertainty should change price, terms, protection or the decision—not disappear in a footnote.", "A strong deal team makes uncertainty visible early enough to act."),
         ]),
    dict(num=4, code="04", title="Stakeholder Alignment and Post-Merger Integration",
         subtitle="Governance · checks and balances · IMO · culture · change",
         criteria="A2 · A3 · K2", concepts=[
             ("Integration starts before close", "Diligence findings and the deal thesis must transfer into the plan."),
             ("Governance enables pace", "Decision rights, escalation and cadence prevent cross-functional drift."),
             ("Protect value", "Client continuity, talent and culture are economic value drivers."),
             ("Measure outcomes", "Track commitments, not activity volume."),
         ], lessons=[
             ("tile", "Stakeholder map", [
                 ("Governance", "Board, SteerCo, deal executive and regulators."),
                 ("Delivery", "IMO, workstream leads, integration teams and business owners."),
                 ("People", "Leaders, employees, talent groups and representatives."),
                 ("External", "Clients, suppliers, lenders, partners and communities."),
             ]),
             ("two", "RACI and decision rights", [
                 "Responsible performs the work; Accountable owns the outcome.",
                 "Consulted contributes before a decision; Informed receives the result.",
                 "One accountable owner avoids committee ambiguity."
             ], [
                 "Define reserved decisions, thresholds and escalation routes.",
                 "Separate deal sponsorship from independent control challenge.",
                 "Record decisions, assumptions, owners and due dates."
             ]),
             ("flow", "EY: nine integration steps", ["Value drivers and principles", "Legal interaction rules", "Stand up IMO", "Day One charters", "Operating model", "Functional plans", "Execute", "Capture value", "Manage stakeholders"]),
             ("cards", "Three-tier integration governance", [
                 ("SteerCo", "Sets direction and resolves the highest-significance issues."),
                 ("IMO", "Coordinates workstreams, risks, dependencies, decisions and value."),
                 ("Functional teams", "Deliver milestones and resolve day-to-day issues."),
             ]),
             ("tile", "Pre-close guardrails", [
                 ("Clean team", "Restrict competitively sensitive data to authorised reviewers."),
                 ("Gun-jumping", "Do not control the target before legal close."),
                 ("Confidentiality", "Define channels, access, retention and permitted use."),
                 ("Readiness", "Plan Day One without prematurely implementing control."),
             ]),
             ("tile", "Day One must-haves", [
                 ("People", "Leadership, employment continuity, access and emergency contacts."),
                 ("Clients", "Service continuity, relationship owners and approved messages."),
                 ("Controls", "Authority limits, cash, compliance, cyber and incident escalation."),
                 ("Operations", "Systems access, critical vendors, sites and business continuity."),
             ]),
             ("flow", "First 100 days", ["Stabilise", "Confirm baseline", "Mobilise initiatives", "Track outcomes", "Adjust and embed"]),
             ("tile", "Integration strategy choices", [
                 ("Absorption", "Fully integrate when standardisation and scale are central to value."),
                 ("Preservation", "Protect autonomy when brand, culture or specialist capability drives value."),
                 ("Symbiosis", "Share selected capabilities while allowing mutual adaptation."),
                 ("Holding", "Maintain a portfolio relationship with limited operational integration."),
             ]),
             ("tile", "Synergy governance", [
                 ("Baseline", "Freeze the standalone reference point and avoid moving targets."),
                 ("Initiative", "Name the action, owner, milestone, dependency and cost-to-achieve."),
                 ("Finance validation", "Confirm recurring P&L and cash impact; remove double counting."),
                 ("Reporting", "Separate forecast, achieved, at-risk and lost value."),
             ]),
             ("two", "Culture integration", [
                 "Profile decision style, client model, risk appetite, incentives and leadership behaviours.",
                 "Identify where differences are complementary and where they threaten the thesis.",
                 "Design the future culture through observable behaviours, not slogans."
             ], [
                 "Listen through interviews, surveys, data and leader observation.",
                 "Protect critical identity where specialist trust creates value.",
                 "Track regretted attrition, engagement, client continuity and conduct indicators."
             ]),
             ("tile", "Professional services integration", [
                 ("Talent", "Retention combines economics, career opportunity, identity and clarity."),
                 ("Clients", "Relationship continuity and conflict checks protect revenue."),
                 ("Governance", "Partner autonomy must align with board, risk and reporting discipline."),
                 ("Technology", "Data, workflow and platforms should scale without weakening quality."),
             ]),
             ("tile", "Change and communication plan", [
                 ("Audience", "Map what each stakeholder needs to know, feel and do."),
                 ("Message", "Explain the rationale, impact, timing and unresolved questions honestly."),
                 ("Channel", "Use leader cascades, client outreach, town halls and two-way forums."),
                 ("Feedback", "Track sentiment, rumours, adoption barriers and response actions."),
             ]),
             ("tile", "Integration scorecard", [
                 ("Value", "Revenue, cost, capital and cost-to-achieve."),
                 ("Customers", "Retention, pipeline, complaints and service levels."),
                 ("People", "Critical talent retention, engagement and role fill."),
                 ("Execution and risk", "Milestones, dependencies, incidents and controls."),
             ]),
             ("big", "Closing completes the transaction; integration must still earn the value.", "The deal thesis becomes an operating commitment on Day One."),
         ]),
]

DAY_THEMES = {1: "Structure, Valuation, Forecasting and Tax", 2: "Risk, Intelligence, Integration and Assessment"}

SCHEDULE = {
    1: [
        ("9:00", "9:30", 30, "admin", "Welcome, attendance, outcomes and assessment briefing"),
        ("9:30", "12:15", 165, "topic", "Topic 1 — Deal Structuring and Valuation Principles; Activities 1–2"),
        ("12:15", "13:15", 60, "lunch", "Lunch break"),
        ("13:15", "15:30", 135, "topic", "Topic 2 — Forecasting, Financial and Tax Implications; Activity 3"),
        ("15:30", "15:40", 10, "break", "Afternoon break"),
        ("15:40", "17:45", 125, "topic", "Topic 2 continued; Activity 4 and Day 1 deal-team review"),
        ("17:45", "18:00", 15, "recap", "Day 1 recap and reflection"),
    ],
    2: [
        ("9:00", "11:45", 165, "topic", "Topic 3 — Target Identification, Risk and Intelligence; Activities 5–6"),
        ("11:45", "11:55", 10, "break", "Morning break"),
        ("11:55", "12:40", 45, "topic", "Topic 3 decision gates and risk review"),
        ("12:40", "13:40", 60, "lunch", "Lunch break"),
        ("13:40", "15:45", 125, "topic", "Topic 4 — Stakeholder Alignment and Integration; Activities 7–8"),
        ("15:45", "16:00", 15, "recap", "Course synthesis and assessment preparation"),
        ("16:00", "17:00", 60, "assess", "Written Assessment (WA-SAQ)"),
        ("17:00", "18:00", 60, "assess", "Case Study Assessment (CS)"),
    ],
}

ASSESSMENT = dict(
    written="Written Assessment (WA-SAQ) — 4 open-ended questions, 1 hour, open book.",
    practical="Case Study Assessment (CS) — 3 integrated tasks, 1 hour, open book.",
    note="Competency requires satisfactory evidence across K1–K5 and A1–A6, plus at least 75% attendance.",
)

SOURCES = [
    ("Course page", "https://www.tertiarycourses.com.sg/wsq-strategic-mergers-and-acquisitions-valuation-risk-and-integration.html"),
    ("Bonadio–TGA transaction report", "https://www.cpapracticeadvisor.com/2026/08/06/credit-risk-management-firm-joins-the-bonadio-group/188098/"),
    ("M&A risk review", "https://www.mdpi.com/2227-9091/12/9/143"),
    ("Professional services M&A briefing", "https://www.financierworldwide.com/briefing-room-ma-in-the-professional-services-sector"),
    ("EY integration program", "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/insights/mergers-acquisitions/documents/ey-nine-key-steps-to-setting-up-merger-acquisition-integration-program.pdf"),
    ("Enterprise M&A risk management review", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5106493"),
]
