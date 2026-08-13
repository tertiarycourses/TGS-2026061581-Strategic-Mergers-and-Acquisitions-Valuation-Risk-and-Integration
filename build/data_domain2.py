"""Topic 2 activities."""
from data_domain1 import CASE_FACTS, SOURCE

DOMAIN2 = [
 dict(num=3, topic=2, title="Bonadio–TGA Three-Year Synergy Forecast Activity",
      objective="Forecast business impact and assess effects on financial performance (K2, A1, A2, A5)",
      desc="Translate the public strategic rationale into a three-year base/downside/upside forecast with a traceable synergy bridge.",
      build="A standalone-to-combined forecast, synergy register, cost-to-achieve schedule and executive dashboard",
      services="Driver model · synergy bridge · scenarios · NPV/ROIC · BI dashboard",
      criteria="K2 · A1 · A2 · A5", source=SOURCE, fact_basis=CASE_FACTS,
      assumptions=[
          "Use Activity 2's course-only financial base; none of the financial inputs are reported transaction facts.",
          "Potential value levers may include cross-selling credit-risk, loan-review and regulatory-advisory services across Bonadio's financial-institution clients.",
          "Model base synergies: revenue US$0.25m/0.60m/1.00m; cost US$0.10m/0.25m/0.35m in Years 1–3.",
          "Model cost-to-achieve: US$0.80m in Year 1 and US$0.30m in Year 2; use 24% cash tax."
      ],
      scenario="Leadership wants to know whether the capability combination can generate value after ramp-up, investment and talent/client risks. Finance must independently validate the sponsor's case.",
      questions=[
          "Which synergy levers are buyer-specific and incremental to standalone performance?",
          "What is the Year 3 run-rate synergy and cumulative cash realisation?",
          "How do downside assumptions affect NPV, ROIC and payback?",
          "Which leading indicators should the IMO monitor before financial benefits appear?"
      ],
      steps=[
          ("Lock the standalone baseline", "Bring in Activity 2 revenue, EBITDA and FCF. Save a versioned baseline that will not move with later underperformance."),
          ("Create the synergy register", "For each revenue and cost lever record formula, owner, milestone, start date, ramp, dependency, risk and cost-to-achieve."),
          ("Model revenue synergies", "Separate cross-sell pipeline, conversion, average revenue and delivery capacity. Do not enter one unsupported lump sum."),
          ("Model cost synergies", "Separate procurement, systems, facilities and shared services; prevent double counting with standalone improvement."),
          ("Model dis-synergies and investment", "Add client attrition, talent retention, duplicated systems and integration-team costs."),
          ("Calculate after-tax cash impact", "Translate benefits and costs into cash by year and calculate cumulative cash, payback, NPV and ROIC."),
          ("Build downside and upside cases", "Downside: 50% revenue synergy, 75% cost synergy, 25% higher cost-to-achieve and one-year delay. Upside must also be evidence-based."),
          ("Design the BI dashboard", "Show baseline, forecast, achieved, at-risk and lost value; include pipeline conversion, retention, milestone and spend KPIs."),
          ("Run Finance challenge", "Identify unsupported assumptions, timing gaps and dependencies; revise the base case and document changes.")
      ],
      output="Three-Year Synergy Model, Synergy Register and Management Dashboard",
      test="Standalone and synergy cases are separate; every synergy has an owner and timing; cash impact includes cost-to-achieve and tax; downside results are visible."),
 dict(num=4, topic=2, title="Bonadio–TGA Pro Forma and Tax Challenge Activity",
      objective="Evaluate financial and tax implications and act as checks and balances (K5, A1, A2)",
      desc="Trace an illustrative acquisition through the income statement, balance sheet and cash flow, then challenge tax and control assumptions.",
      build="A pro forma bridge, purchase-price allocation sketch, tax issue list and board challenge paper",
      services="Pro forma statements · PPA · goodwill · leverage · tax diligence · approval gate",
      criteria="K5 · A1 · A2", source=SOURCE, fact_basis=CASE_FACTS,
      assumptions=[
          "Training case only: purchase enterprise value US$16.0m; consideration 60% cash/debt and 40% buyer equity.",
          "Illustrative identifiable intangible assets: client relationships US$4.0m and trade name US$1.0m; assumed useful lives 8 and 5 years.",
          "Illustrative fair-value adjustment to other net assets: US$1.5m; deferred-tax rate 24%.",
          "Use this as an accounting and governance simulation; obtain jurisdiction-specific accounting, legal and tax advice for a real deal."
      ],
      scenario="Before board approval, the controller, tax lead and independent risk reviewer must explain how the illustrative structure changes profit, cash, leverage and tax—and which issues cannot be resolved from public information.",
      questions=[
          "What drives goodwill under the training PPA?",
          "How do financing, intangible amortisation and integration charges affect earnings and cash differently?",
          "Which tax attributes or exposures need documentary evidence?",
          "What approval conditions should the independent review team impose?"
      ],
      steps=[
          ("Build sources and uses", "Show enterprise value, debt-like/cash adjustments, fees, consideration mix and financing. Confirm sources equal uses."),
          ("Sketch purchase-price allocation", "Allocate consideration to tangible net assets, client relationships, trade name, deferred tax and residual goodwill."),
          ("Build the pro forma income bridge", "Combine standalone results, financing cost, amortisation, synergies and integration charges. Keep recurring and one-off effects separate."),
          ("Build the balance-sheet bridge", "Show new debt/equity, acquired assets and liabilities, intangibles, deferred tax and goodwill."),
          ("Build the cash-flow bridge", "Show consideration, financing, fees, integration spend, tax and operating cash; explain non-cash amortisation."),
          ("Assess ratios and headroom", "Calculate leverage, interest cover, liquidity and covenant headroom for base and downside cases."),
          ("Create the tax diligence list", "Cover filings/audits, nexus, indirect tax, payroll, transfer pricing, losses/credits, financing deductibility and post-close reporting."),
          ("Separate cash tax from accounting tax", "Reconcile statutory rate to effective tax rate and flag items that require local advice."),
          ("Write the board challenge paper", "State key unknowns, downside, sensitivity, required warranties/indemnities and approval conditions.")
      ],
      output="Pro Forma Impact Pack and Board Challenge Paper",
      test="The pack ties across sources/uses and statement bridges, labels training assumptions, distinguishes cash/non-cash and recurring/one-off items, and lists unresolved tax evidence.")
]
