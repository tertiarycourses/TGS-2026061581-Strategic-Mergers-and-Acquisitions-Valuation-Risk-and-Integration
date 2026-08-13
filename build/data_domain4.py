"""Topic 4 activities."""
from data_domain1 import CASE_FACTS, SOURCE

EY = "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/insights/mergers-acquisitions/documents/ey-nine-key-steps-to-setting-up-merger-acquisition-integration-program.pdf"
FW = "https://www.financierworldwide.com/briefing-room-ma-in-the-professional-services-sector"

DOMAIN4 = [
 dict(num=7, topic=4, title="Bonadio–TGA Integration Program Design Activity",
      objective="Develop an implementation plan with stakeholders and governance (A2, A3, A4)",
      desc="Use EY's nine-step integration framework to turn the Bonadio–TGA deal thesis and diligence findings into a Day One and first-100-days program.",
      build="Integration strategy, governance/RACI, workstream charters, Day One checklist and 100-day roadmap",
      services="SteerCo · IMO · workstreams · legal guardrails · operating model · synergy governance",
      criteria="A2 · A3 · A4", source=EY, fact_basis=CASE_FACTS,
      assumptions=[
          "The exercise occurs before the expected close, so integration planning must respect confidentiality and gun-jumping restrictions.",
          "TGA is expected to join Bonadio's internal audit business unit; detailed operating-model decisions are not publicly reported.",
          "Learner choices are recommendations based on the deal thesis and risk analysis."
      ],
      scenario="The CEO asks you to stand up the integration program. The plan must protect regulatory quality and client service while enabling the reported capability expansion.",
      questions=[
          "Which value drivers and guiding principles should govern integration decisions?",
          "What belongs with SteerCo, IMO and functional workstreams?",
          "What must be ready on Day One, and what should be phased?",
          "How will the team prove that value is captured without weakening quality?"
      ],
      steps=[
          ("Confirm value drivers and principles", "Translate the deal thesis into measurable value drivers and 4–6 decision principles, including client continuity and professional quality."),
          ("Document legal interaction guardrails", "Define clean-team access, confidentiality, allowed planning, prohibited pre-close control and escalation to counsel."),
          ("Design three-tier governance", "Name SteerCo, integration leader, IMO and workstreams; define decisions, thresholds, cadence and escalation."),
          ("Create RACI and decision log", "Assign one accountable owner per major outcome; record assumptions, decisions, dissent, owner and due date."),
          ("Draft workstream charters", "For Client/Commercial, People/Culture, Service/Quality, Technology/Data, Finance/Tax and Legal/Risk, define scope, outcomes, dependencies and resources."),
          ("Define Day One must-haves", "List leadership, employee/client communication, access, authority, controls, cyber, continuity and critical vendor actions."),
          ("Design the target operating model", "State what is absorbed, preserved or shared across people, process, technology and governance."),
          ("Build the first-100-days roadmap", "Sequence stabilise, validate baseline, mobilise synergies, integrate priority capabilities and embed controls."),
          ("Set synergy governance", "Create initiative charters with owner, finance validator, baseline, milestone, benefit, cost-to-achieve, risk and status."),
          ("Create the program dashboard", "Track Day One readiness, milestones, decisions, risks, dependencies, clients, talent, quality and value.")
      ],
      output="Integration Program Blueprint and 100-Day Roadmap",
      test="The blueprint maps all nine EY steps, separates pre-close planning from post-close control, assigns governance and owners, and links integration actions to value and risk."),
 dict(num=8, topic=4, title="Bonadio–TGA Culture, Talent and Client Continuity Activity",
      objective="Align stakeholders and manage culture/change in professional-services integration (K2, A2, A3)",
      desc="Use the professional-services M&A briefing to design a people-and-client integration plan that preserves specialist identity while enabling scaled capabilities.",
      build="Culture risk map, critical-talent plan, client continuity playbook and stakeholder communication pack",
      services="Culture diligence · retention · client ownership · change narrative · pulse dashboard",
      criteria="K2 · A2 · A3", source=FW, fact_basis=CASE_FACTS,
      assumptions=[
          "The briefing emphasises that professional-services value depends heavily on people, client relationships, specialist identity and culture.",
          "No talent, client or culture problems have been reported for the Bonadio–TGA transaction; the risks below are planning hypotheses.",
          "Retention should combine financial alignment, career opportunity, clarity and cultural fit."
      ],
      scenario="The integration team must protect TGA's specialist expertise and trusted client relationships while introducing Bonadio governance, reporting and cross-selling. A rushed absorption could undermine the capability the buyer sought.",
      questions=[
          "Which aspects of TGA's specialist identity should be preserved, and which should standardise?",
          "Who are the critical talent and client relationships, and what would make them leave?",
          "How should leadership explain the transaction to staff and clients?",
          "Which leading indicators show culture or client value is deteriorating?"
      ],
      steps=[
          ("Map stakeholder impact", "For leaders, specialists, wider staff, clients, regulators and partners, record needs, concerns, influence, desired behaviour and owner."),
          ("Profile culture and operating norms", "Compare decision style, risk appetite, client ownership, quality standards, incentives, collaboration and career paths."),
          ("Choose integration posture by capability", "For each area decide absorb, preserve, symbiose or hold; link the choice to the value thesis and risk."),
          ("Identify critical talent", "Map role criticality, client dependence, scarcity, succession, flight risk and retention action without assuming money is sufficient."),
          ("Design retention and progression", "Combine rollover/long-term incentives where relevant, role clarity, career path, leadership access, development and recognition."),
          ("Build the client continuity plan", "Name relationship owners, conflict/independence checks, service assurances, outreach timing, escalation and cross-sell guardrails."),
          ("Write the change narrative", "Explain why the deal, what changes, what stays, when decisions occur, how questions are answered and what cannot yet be disclosed."),
          ("Create the communication cascade", "Sequence leaders, employees, clients, regulators/partners and public messaging; use approved scripts and feedback channels."),
          ("Build the pulse dashboard", "Track regretted attrition, critical roles, engagement, client retention, complaints, service levels, cross-sell quality and conduct."),
          ("Run a 30-day scenario test", "Respond to a key specialist resignation plus a top-client concern; update ownership, mitigation and communication.")
      ],
      output="People, Culture and Client Continuity Playbook",
      test="The playbook distinguishes preservation from standardisation, names owners and indicators, covers critical talent and clients, and includes a tested response to an early warning.")
]
