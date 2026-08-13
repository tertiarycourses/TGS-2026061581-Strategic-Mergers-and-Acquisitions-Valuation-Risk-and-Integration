"""Topic 1 activities — one progressive real transaction case."""
CASE_FACTS = (
    "On 6 August 2026, CPA Practice Advisor reported that The Bonadio Group would add "
    "T. Gschwender & Associates (TGA), a Syracuse provider of credit-risk management "
    "services to financial institutions. The transaction was expected to close on "
    "16 August 2026; financial terms were not disclosed. TGA was to join Bonadio's "
    "internal audit business unit within Advisory & Consulting."
)
SOURCE = "https://www.cpapracticeadvisor.com/2026/08/06/credit-risk-management-firm-joins-the-bonadio-group/188098/"

DOMAIN1 = [
 dict(num=1, topic=1, title="Bonadio–TGA Deal Thesis and Structure Lab",
      objective="Apply financial instruments to shape a deal structure (K1, A1, A6)",
      desc="Use the announced Bonadio–TGA professional-services transaction to build a defensible strategic thesis and term-sheet architecture.",
      build="A one-page deal thesis, strategic-fit scorecard and proposed consideration/risk-allocation package",
      services="Public transaction evidence · deal-thesis canvas · structure decision matrix",
      criteria="K1 · A1 · A6", source=SOURCE, fact_basis=CASE_FACTS,
      assumptions=[
          "No purchase price, revenue, EBITDA or ownership terms were reported; do not infer them.",
          "For comparison only, assume the seller values continuity, client service and continued management participation.",
          "Treat every proposed instrument as a learner recommendation, not an account of the actual transaction."
      ],
      scenario="You are on Bonadio's deal team before the expected closing. Leadership wants a concise view of why TGA fits, which capabilities create value, and how a structure could protect client continuity and specialist talent when the actual terms are unknown.",
      questions=[
          "Which facts support strategic fit, and which important facts remain unknown?",
          "Would cash, rollover equity, an earn-out, a seller note or a holdback best allocate risk? Why?",
          "What value could scale create without weakening TGA's specialist edge?",
          "What conditions would make the team pause or walk away?"
      ],
      steps=[
          ("Read the source and separate verified facts from interpretation", "Create two columns: Reported fact | Deal-team inference. Record the publication and expected-close dates."),
          ("Write a one-sentence deal thesis", "Complete: Bonadio should pursue TGA because [capability/client/geography], creating value through [specific mechanism], provided [critical risk] is controlled."),
          ("Score strategic fit", "Rate capability fit, client adjacency, specialist differentiation, cultural fit, execution complexity and integration capacity from 1–5; justify every score."),
          ("Map value creation", "Identify revenue, cost, capital and resilience levers. Reject any lever that lacks an owner or evidence path."),
          ("Design the consideration mix", "Compare cash, rollover equity, earn-out, seller note and escrow/holdback against certainty, retention, financing, tax and dispute risk."),
          ("Draft risk allocation", "Propose at least three protections such as working-capital adjustment, warranties, indemnity, escrow, retention condition or client-revenue earn-out."),
          ("Run the challenge meeting", "Assign Deal Sponsor, Finance, Legal/Risk and Integration roles. Each role states one objection and one required condition."),
          ("Finalise the decision page", "State recommendation, preferred structure, top three risks, mitigations and walk-away triggers. Label all assumptions.")
      ],
      output="Deal Thesis and Structure Decision Page (PDF or DOCX)",
      test="The page distinguishes facts from assumptions, proposes at least two instruments, links each term to a risk or value driver, and includes an explicit go/conditional/no-go recommendation."),
 dict(num=2, topic=1, title="Bonadio–TGA Valuation Triangulation Lab",
      objective="Apply business valuation concepts and reconcile a valuation range (K3, A1)",
      desc="Build a screening valuation for the real announced transaction using clearly labelled training assumptions because the deal's financial terms were not disclosed.",
      build="A transparent valuation workbook with DCF, trading-comparable and precedent-transaction cross-checks",
      services="Enterprise-value bridge · DCF · comparable multiples · sensitivity analysis",
      criteria="K3 · A1", source=SOURCE, fact_basis=CASE_FACTS,
      assumptions=[
          "Training case only: FY2026 revenue US$8.0m; normalised EBITDA US$2.0m; cash tax 24%; capex US$0.20m; change in NWC US$0.10m.",
          "Five-year revenue growth: 8%, 7%, 6%, 5%, 4%; EBITDA margin gradually rises from 25% to 27%.",
          "DCF base: WACC 12%; terminal growth 3%; net debt US$0.50m.",
          "Market cross-check range: 7.0x–9.0x normalised EBITDA. These are course assumptions, not reported facts."
      ],
      scenario="The deal sponsor asks for an indicative range before committing more resources. Your model must make uncertainty visible and must not present simulated inputs as Bonadio or TGA disclosures.",
      questions=[
          "What adjustments are needed to move reported EBITDA to normalised EBITDA?",
          "What value range emerges from DCF and the 7.0x–9.0x multiple cross-check?",
          "How does enterprise value bridge to equity value?",
          "Which two assumptions drive the widest value change?"
      ],
      steps=[
          ("Create an Assumptions block", "Enter every training input in a dedicated blue-font input cell with units, source type and an explicit 'Training assumption' flag."),
          ("Normalise EBITDA", "Start from US$2.0m and add separate rows for owner/related-party, one-off and run-rate adjustments. Keep the base case at US$2.0m unless you can justify a change."),
          ("Forecast operating performance", "Build revenue, EBITDA, cash tax, capex and change-in-NWC rows for five years; calculate unlevered free cash flow."),
          ("Calculate DCF value", "Discount each year's FCF at 12%; calculate Gordon-growth terminal value at 3%; discount terminal value to present."),
          ("Build the equity bridge", "Start with enterprise value, subtract debt-like items, add cash if assumed and state resulting equity value."),
          ("Add market cross-checks", "Apply 7.0x, 8.0x and 9.0x to normalised EBITDA; explain why scale, growth, recurring revenue and key-person dependence affect positioning."),
          ("Create a two-way sensitivity", "Vary WACC from 10%–14% and terminal growth from 2%–4%. Each cell must recalculate the DCF."),
          ("Reconcile to a range", "Explain differences across methods; present low/base/high, implied EBITDA multiple and FCF yield."),
          ("Perform model checks", "Confirm FCF components tie, terminal value is discounted, EV-to-equity bridge works and no output is hard-coded.")
      ],
      output="Valuation Workbook and one-page Valuation Range Memo",
      test="The model is formula-driven, shows sources/assumptions, has a working sensitivity table and reconciles DCF with the multiple range without claiming undisclosed deal facts.")
]
