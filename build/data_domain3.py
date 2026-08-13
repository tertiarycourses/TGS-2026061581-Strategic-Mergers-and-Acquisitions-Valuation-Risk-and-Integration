"""Topic 3 activities."""
from data_domain1 import CASE_FACTS, SOURCE

MDPI = "https://www.mdpi.com/2227-9091/12/9/143"
SSRN = "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5106493"

DOMAIN3 = [
 dict(num=5, topic=3, title="Bonadio–TGA Target Screening and Diligence Activity",
      objective="Use industry intelligence to screen a target and plan risk-based diligence (K4, A4, A6)",
      desc="Convert the public transaction rationale into a target-screening scorecard and a diligence plan that tests specialist capability, client trust and regulatory quality.",
      build="A target-screening scorecard, evidence request list and diligence workplan",
      services="Market map · screening criteria · evidence hierarchy · QoE · commercial/legal/tech/people diligence",
      criteria="K4 · A4 · A6", source=SOURCE, fact_basis=CASE_FACTS,
      assumptions=[
          "Verified facts include TGA's reported service areas, founding year, target client type and planned Bonadio business-unit placement.",
          "Client concentration, financial performance, staff roster, contracts, cyber posture and regulatory findings are unknown and must be requested.",
          "The exercise tests whether the announced rationale is supported; it does not assert undisclosed findings."
      ],
      scenario="The deal team must prepare a red-flag diligence sprint before expected close. Because the target advises regulated financial institutions, independence, data security, professional quality and client continuity are central.",
      questions=[
          "Which screening criteria best test the announced capability-expansion thesis?",
          "What evidence would confirm service quality and sticky client relationships?",
          "Which diligence items can change value, structure or the decision?",
          "What must be handed from diligence to the integration team?"
      ],
      steps=[
          ("Create the target archetype", "Define required services, clients, talent, geography, quality, technology, economics and cultural characteristics before scoring TGA."),
          ("Build weighted screening criteria", "Assign transparent weights totalling 100%; score strategic fit, financial quality, capability, risk, culture and executability."),
          ("Separate evidence levels", "Tag each score as public evidence, management claim, data-room evidence, third-party evidence or unresolved."),
          ("Design commercial diligence", "Request client cohorts, concentration, retention, pipeline, pricing, win/loss, market and competitor evidence."),
          ("Design financial and tax diligence", "Request QoE, working capital, cash conversion, debt-like items, commitments, returns, audits and uncertain positions."),
          ("Design regulatory and legal diligence", "Review licences, independence, professional standards, complaints, litigation, contracts, privacy and regulatory interactions."),
          ("Design operations, technology and cyber diligence", "Review delivery workflows, quality controls, systems, data access, resilience, vendors, incidents and remediation."),
          ("Design people and culture diligence", "Map leaders, critical talent, incentives, succession, attrition, engagement, decision style and client ownership."),
          ("Prioritise red flags", "Classify each request as confirmatory, value-changing, term-changing or deal-breaking; name an owner and deadline."),
          ("Create the integration handoff", "Convert material findings into Day One controls, retention actions, synergy constraints and post-close monitoring.")
      ],
      output="Target Screening and Diligence Workplan",
      test="Weights total 100%, scores cite evidence status, every high-risk item has an owner and decision impact, and diligence findings flow into integration actions."),
 dict(num=6, topic=3, title="Bonadio–TGA M&A Risk Intelligence Activity",
      objective="Use BI to assess and manage M&A risk across the lifecycle (A2, A4, A5, A6)",
      desc="Apply the MDPI risk themes and the SSRN enterprise-risk framework to the real announced deal, then create a decision dashboard and escalation memo.",
      build="A risk taxonomy, heat map, bow-tie controls, BI dashboard and go/conditional/no-go memo",
      services="MDPI risk themes · Fishbone · risk scoring · controls · leading indicators · decision gates",
      criteria="A2 · A4 · A5 · A6", source=MDPI, fact_basis=CASE_FACTS,
      assumptions=[
          "The MDPI review identifies four connected themes: information asymmetry; performance/reputation; litigation/investor protection; geopolitical factors.",
          "The SSRN review discusses financial, operational, strategic, regulatory and cultural risk and structured identification/quantification methods.",
          "Risks used in this case are hypotheses for diligence, not allegations about either firm."
      ],
      scenario="An independent Risk Committee must challenge the deal before signing. It needs a concise view of what could prevent value creation, how exposure will be reduced and what information would trigger escalation.",
      questions=[
          "How do information asymmetry and reputation risk interact in a regulated advisory business?",
          "Which causes sit behind client loss, specialist-talent loss and regulatory-quality failure?",
          "What controls reduce likelihood and what recovery actions reduce impact?",
          "Which metrics and thresholds should trigger escalation?"
      ],
      steps=[
          ("Define the risk taxonomy", "Map financial, operational, strategic, regulatory/legal, cultural, information, reputation and external risks to M&A phases."),
          ("Run Fishbone analysis", "For three top events, identify causes across people, process, technology, data, market and governance."),
          ("Write cause-event-consequence statements", "Avoid vague labels. Example format: Because [cause], [event] may occur, leading to [consequence]."),
          ("Score inherent exposure", "Use defined 1–5 likelihood and impact scales; add velocity and detectability when useful."),
          ("Design controls and deal protections", "Map diligence tests, conditions precedent, warranties, indemnities, escrow, retention and integration controls."),
          ("Score residual exposure", "Re-score only after a named control owner and evidence of design/operation are specified."),
          ("Build bow-tie views", "For the top risks show preventive controls before the event and recovery controls after the event."),
          ("Design the BI dashboard", "Include client concentration/retention, critical-talent status, quality findings, data incidents, synergy milestones and unresolved diligence."),
          ("Set thresholds and escalation", "Define green/amber/red limits, decision owner, meeting cadence and required action for each indicator."),
          ("Write the independent memo", "Recommend go, conditional go or no-go; state residual risks, conditions and monitoring.")
      ],
      output="Risk Intelligence Dashboard and Independent Risk Committee Memo",
      test="Risk statements are specific, scoring scales are defined, controls have owners, dashboard thresholds are actionable and the recommendation follows the evidence.")
]
