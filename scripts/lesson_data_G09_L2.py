#!/usr/bin/env python3
"""Complete lesson data for G09L2-L01 through G09L2-L10 (Grade 9 Level 2: Advanced Computational Modeling)"""

L01 = {
    "id": "G09L2-L01",
    "title": "The Antibiotic Resistance Arms Race",
    "subtitle": "How Superbugs Are Winning — And Why We Created Them",
    "ngss": "HS-LS4-2, HS-LS4-3",
    "ngss_desc": "Construct an explanation based on evidence that the process of evolution primarily results from four factors: (1) the potential for a species to increase in number, (2) the heritable genetic variation of individuals in a species due to mutation and sexual reproduction, (3) competition for limited resources, and (4) the proliferation of those organisms that are better able to survive and reproduce in the environment. Apply concepts of statistics and probability to support explanations that organisms with an advantageous heritable trait tend to increase in proportion to organisms lacking this trait.",
    "big_question": "Why are doctors terrified of \"superbugs\" \u2014 and how did WE create them?",
    "objectives": [
        "Model how natural selection drives antibiotic resistance in bacterial populations through reinforcing feedback loops",
        "Explain why incomplete antibiotic courses accelerate resistance evolution",
        "Analyze the reinforcing feedback loop between resistant bacteria proportion and antibiotic effectiveness",
        "Predict how different treatment strategies affect the long-term balance between bacteria and antibiotics",
        "Evaluate public health policies designed to slow the emergence of superbugs"
    ],
    "vocabulary": [
        ("Antibiotic Resistance", "The ability of bacteria to survive and reproduce despite exposure to antibiotics that would normally kill them, arising through random mutations and natural selection"),
        ("Reinforcing Feedback Loop", "A system cycle where the output amplifies the input \u2014 more of A leads to more of B, which leads to even more of A, creating exponential change"),
        ("Selective Pressure", "An environmental factor that gives organisms with certain traits a survival advantage, driving evolution in a particular direction"),
        ("Mutation Rate", "The frequency at which random genetic changes occur in a population, introducing new traits including potential drug resistance"),
        ("Horizontal Gene Transfer", "The process by which bacteria share resistance genes directly with other bacteria, even across species, accelerating resistance spread"),
        ("Minimum Inhibitory Concentration", "The lowest concentration of an antibiotic that prevents visible growth of a bacteria \u2014 the threshold between effective and ineffective treatment")
    ],
    "components": [
        ("Antibiotic Dosage", "The concentration of antibiotic administered to the patient, measured relative to the minimum inhibitory concentration", True),
        ("Treatment Duration", "How long the antibiotic course is maintained \u2014 full course (10-14 days) vs. shortened or incomplete treatment", True),
        ("Bacterial Population", "Total number of bacteria in the infection, including both susceptible and resistant strains", False),
        ("Resistant Bacteria Percentage", "The proportion of the bacterial population carrying resistance genes \u2014 the key variable in the reinforcing feedback loop", False),
        ("Mutation Rate", "The rate at which random genetic mutations occur, some of which may confer antibiotic resistance to individual bacteria", False),
        ("Immune Response", "The strength of the body's natural immune defenses working alongside antibiotics to clear the infection", False)
    ],
    "think_about_it": "When a patient stops taking antibiotics early because they feel better, which bacteria are still alive \u2014 the susceptible ones or the resistant ones? What happens to the resistant bacteria percentage, and how does that change the effectiveness of the same antibiotic next time?",
    "scenarios": [
        ("Full Course Treatment", "Set Antibiotic Dosage to high and Treatment Duration to full course \u2014 observe Bacterial Population and Resistant Bacteria Percentage over time"),
        ("Incomplete Treatment", "Set Antibiotic Dosage to high but reduce Treatment Duration to 50% \u2014 observe the reinforcing feedback loop activating"),
        ("Sub-Therapeutic Dosage", "Set Antibiotic Dosage below the minimum inhibitory concentration and observe what happens to Mutation Rate and Resistant Bacteria Percentage"),
        ("Immune-Compromised Patient", "Set Immune Response to low and run full treatment \u2014 observe how reduced immune support changes outcomes")
    ],
    "sim_scenarios": [
        ("Full Course", "High dosage, full duration, normal immune response", "What do you predict will happen to Resistant Bacteria Percentage when treatment is completed fully? Will it increase, decrease, or stay the same?"),
        ("Incomplete Course", "High dosage, 50% duration, normal immune response", "What do you predict happens to Bacterial Population AFTER the patient stops treatment early? Think about which bacteria survived."),
        ("Sub-Therapeutic Dosage", "Low dosage, full duration, normal immune response", "What do you predict is MORE dangerous \u2014 no antibiotic at all, or a dose that's too low? Why?")
    ],
    "discoveries": [
        "Antibiotics don't create resistant bacteria \u2014 they create the CONDITIONS for resistant bacteria to thrive by killing susceptible competitors",
        "Incomplete antibiotic courses are worse than no treatment at all because they selectively breed resistance",
        "The reinforcing feedback loop means once resistance passes a threshold, the same antibiotic becomes essentially useless",
        "Bacteria can share resistance genes through horizontal gene transfer, meaning one resistant species can arm others",
        "The mutation rate is constant, but selection pressure from antibiotics determines whether those mutations matter",
        "Immune response is a critical partner \u2014 antibiotics alone cannot eliminate infections if the immune system is compromised"
    ],
    "answer": "Doctors are terrified of superbugs because WE created them through the misuse of antibiotics. Every time someone takes an incomplete course or uses antibiotics unnecessarily, they kill susceptible bacteria but leave resistant ones alive. Those resistant bacteria multiply, share their resistance genes, and become a larger proportion of the population. This reinforcing feedback loop \u2014 more resistance leads to less effectiveness leads to more resistance \u2014 has produced bacteria that no existing antibiotic can kill. We are in an arms race with evolution, and right now, the bacteria are winning.",
    "stem_title": "Design a Public Health Antibiotic Stewardship Campaign",
    "stem_mission": "Using data from your simulation model, design an evidence-based public health campaign that communicates WHY antibiotic misuse creates superbugs and recommends specific behavioral changes to slow resistance evolution.",
    "stem_scenario": "The World Health Organization has hired your team to create a campaign targeting teenagers and young adults. You must use your model data to create compelling, scientifically accurate messaging about antibiotic resistance that changes behavior, not just awareness.",
    "stem_questions": [
        "Which simulation scenario produced the most dangerous outcome \u2014 and why would that be the most important to communicate?",
        "How can you explain the reinforcing feedback loop in language that a non-science person would understand?",
        "What specific behavioral changes would have the biggest impact on slowing resistance evolution?"
    ],
    "stem_design_qs": [
        "What data visualizations from your model would be most persuasive in your campaign?",
        "How will you communicate the urgency without causing panic or hopelessness?",
        "What medium (social media, poster, video, app) best reaches your target audience?",
        "How will you measure whether your campaign actually changes behavior, not just awareness?"
    ],
    "career": "Epidemiologists and Antimicrobial Resistance Researchers study how diseases spread and how bacteria evolve resistance. They work at the CDC, WHO, pharmaceutical companies, and universities, earning $75,000\u2013$150,000/year. This field is considered one of the most critical public health challenges of the 21st century.",
    "images": {
        "cover": ("G09L2-L01-cover.png", "A photorealistic, cinematic close-up of a petri dish showing bacterial colonies with a clear antibiotic resistance zone, dramatic lighting with teal and amber tones, a blurred laboratory background with a diverse group of 14-15 year old students in lab coats observing through a microscope"),
        "landscape": ("G09L2-L01-landscape.png", "A photorealistic image of a diverse, multicultural group of 14-15 year old students in a modern biology laboratory examining bacterial cultures on petri dishes, wearing safety goggles and gloves, with digital screens showing bacterial growth data, soft natural lighting"),
        "modeling": ("G09L2-L01-modeling.png", "A photorealistic image of diverse 14-15 year old students working on laptops building computational models with feedback loop diagrams visible on screens, modern classroom with scientific posters about antibiotic resistance on walls, collaborative engaged expressions"),
        "discussion": ("G09L2-L01-discussion.png", "A photorealistic image of a diverse group of 14-15 year old students in an animated class discussion about antibiotic resistance, a teacher facilitating at a smartboard showing a reinforcing feedback loop diagram, students raising hands with engaged expressions"),
        "stem": ("G09L2-L01-stem.png", "A photorealistic image of diverse 14-15 year old students creating public health campaign materials about antibiotic resistance, working with tablets, poster boards, and laptops, collaborative teamwork in a modern science classroom")
    },
    "pre_assessment": [
        "What are antibiotics and what do they do? Have you ever taken them?",
        "Why do you think doctors always say to finish your entire prescription even if you feel better?",
        "What is a 'superbug' and why might it be dangerous?",
        "Draw or describe what you think happens inside your body when you take an antibiotic."
    ],
    "extend_components": [
        ("Horizontal Gene Transfer Rate", "The rate at which bacteria share resistance genes with other bacteria through plasmid transfer, even between different species"),
        ("Antibiotic Diversity", "The number of different antibiotic classes available for treatment \u2014 when resistance develops to one, doctors switch to another"),
        ("Biofilm Formation", "The ability of bacteria to form protective communities on surfaces, which dramatically increases their resistance to antibiotics")
    ],
    "reflections": [
        "Why is the reinforcing feedback loop in antibiotic resistance so dangerous compared to a system with balancing feedback?",
        "Your model shows that incomplete treatment is worse than no treatment. How would you explain this counterintuitive result to a friend?",
        "How does horizontal gene transfer make the resistance problem even worse than your basic model shows?",
        "What role does the immune system play in your model, and why can't we rely on antibiotics alone?",
        "If you were a hospital administrator, what policies would you implement based on your model's predictions?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model with reinforcing feedback loops to explain how natural selection drives antibiotic resistance in bacterial populations under different treatment conditions."),
        ("Disciplinary Core Idea", "LS4.B Natural Selection / LS4.C Adaptation", "Natural selection acts on the variation in bacterial populations, where antibiotic exposure provides selective pressure favoring resistant individuals. Adaptation occurs at the population level as resistant traits become more prevalent."),
        ("Crosscutting Concept", "Cause and Effect: Mechanism and Prediction", "Students trace the causal chain from antibiotic misuse through selective pressure to resistance evolution, using their model to predict outcomes of different treatment strategies.")
    ],
    "cast_items": [
        "Model how natural selection drives antibiotic resistance through reinforcing feedback loops",
        "Explain why incomplete antibiotic treatment accelerates resistance evolution",
        "Predict the outcome of different treatment strategies using computational modeling",
        "Evaluate public health interventions based on model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A patient takes antibiotics for 3 days instead of the prescribed 10 days because they feel better. According to the reinforcing feedback loop model, what is the most likely long-term consequence?"),
        ("Constructed Response:", "Using your computational model, explain the reinforcing feedback loop that drives antibiotic resistance. Include in your explanation why this loop makes resistance an accelerating problem rather than a self-correcting one, and propose an evidence-based intervention to slow the loop.")
    ],
    "background_intro": "This lesson uses a feedback-dominant model to explore one of the most pressing threats to global health: antibiotic resistance. The core dynamic is a reinforcing feedback loop \u2014 as resistant bacteria increase in proportion, antibiotic effectiveness decreases, which allows even more resistant bacteria to survive. Unlike systems with balancing feedback that self-correct, this reinforcing loop drives exponential change, making resistance an accelerating crisis rather than a self-limiting problem. Students will explore how human behavior (dosage and duration choices) interacts with evolutionary mechanisms (mutation and natural selection) to produce outcomes that threaten modern medicine.",
    "background_sections": [
        ("The Evolution of Resistance", "Antibiotic resistance is evolution in real time. When Alexander Fleming discovered penicillin in 1928, he warned that bacteria would evolve resistance if the drug was misused. He was right. Bacteria reproduce every 20-30 minutes, with each generation introducing random mutations. Most mutations are neutral or harmful, but occasionally one confers resistance to an antibiotic. In a normal population, these resistant bacteria have no advantage. But when antibiotics are introduced, they kill susceptible bacteria while resistant ones survive and multiply \u2014 classic natural selection. The key insight is that antibiotics don't CAUSE resistance; they CREATE THE CONDITIONS where pre-existing resistance becomes advantageous."),
        ("The Reinforcing Feedback Loop", "The dangerous dynamic in antibiotic resistance is a reinforcing (positive) feedback loop. As the proportion of resistant bacteria increases, the effective antibiotic concentration decreases (because fewer bacteria are susceptible). Lower effectiveness means more bacteria survive treatment, which further increases the resistant proportion. This loop accelerates over time \u2014 each cycle makes the next cycle worse. In systems thinking, this is called a 'vicious cycle' because it drives the system toward an increasingly undesirable state. The only way to break the loop is to interrupt it early, before resistance becomes dominant."),
        ("Why Incomplete Treatment Is Worse Than None", "This is the counterintuitive insight that makes the model powerful: taking antibiotics for only a few days is MORE dangerous than not taking them at all. With no antibiotics, resistant and susceptible bacteria coexist without selective pressure favoring either group. But a partial course kills most susceptible bacteria while leaving resistant ones alive. The resistant bacteria, now freed from competition, multiply rapidly. The patient 'feels better' because the bacterial load dropped, but the remaining population is now dominated by resistant strains. Next time, the same antibiotic may not work at all."),
        ("The Global Crisis", "The WHO has declared antibiotic resistance a top-10 global public health threat. In the US alone, over 2.8 million antibiotic-resistant infections occur annually, causing over 35,000 deaths. Some bacteria, like MRSA (methicillin-resistant Staphylococcus aureus) and CRE (carbapenem-resistant Enterobacteriaceae), resist nearly all existing antibiotics. The pipeline for new antibiotics is nearly empty because pharmaceutical companies find antibiotics less profitable than drugs for chronic conditions. Without effective antibiotics, routine surgeries, cancer chemotherapy, and organ transplants become life-threatening procedures.")
    ],
    "lever_L": "Students identify six components of the antibiotic resistance system: Antibiotic Dosage and Treatment Duration as external variables (human-controlled), and Bacterial Population, Resistant Bacteria Percentage, Mutation Rate, and Immune Response as internal variables (system-determined). Students must recognize that human choices directly drive the selective pressure that feeds the reinforcing loop.",
    "lever_E": "Students map the reinforcing feedback loop: Antibiotic Dosage kills susceptible bacteria \u2192 Resistant Bacteria Percentage increases \u2192 Antibiotic effectiveness decreases \u2192 more resistant bacteria survive \u2192 Resistant Bacteria Percentage increases further. They also identify the balancing role of Immune Response and the threshold effect of Treatment Duration (completing vs. not completing the course).",
    "lever_V": "Students build a multi-component model showing how Antibiotic Dosage and Treatment Duration interact with Bacterial Population dynamics, the reinforcing feedback loop driving Resistant Bacteria Percentage, the modulating effect of Mutation Rate, and the supporting role of Immune Response.",
    "lever_Ev": "Students run scenarios comparing full course, incomplete course, and sub-therapeutic dosage, evaluating which conditions activate the reinforcing feedback loop most dangerously. They analyze why incomplete treatment produces worse outcomes than no treatment \u2014 a counterintuitive prediction their model must explain.",
    "lever_R": "Students extend the model by adding Horizontal Gene Transfer Rate, Antibiotic Diversity, or Biofilm Formation to explore how real-world complexity accelerates or mitigates resistance evolution beyond the basic reinforcing loop.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic imagery of bacterial colonies and antibiotic resistance zones", "say": "Right now, bacteria are evolving to defeat every drug we have. And the terrifying part? We're helping them do it.", "do": "Show a news headline about a recent superbug outbreak. Ask: 'Has anyone heard the term superbug before? What do you think it means?'", "time": "3 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals, vocabulary terms, and the reinforcing feedback loop diagram", "say": "Today we're modeling one of the most dangerous feedback loops on Earth \u2014 one that's happening inside hospitals and medicine cabinets right now.", "do": "Have students read objectives. Pre-teach 'reinforcing feedback loop' using a simple everyday example (rumor spreading). Introduce vocabulary with emphasis on 'selective pressure' as the driving force.", "time": "4 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why are doctors terrified of superbugs \u2014 and how did WE create them?", "say": "Alexander Fleming, the man who discovered penicillin, warned us this would happen. In his 1945 Nobel Prize speech, he predicted that misuse of antibiotics would create resistant bacteria. He was right.", "do": "Share Fleming's actual Nobel Prize quote. Quick poll: 'Have you ever stopped taking antibiotics early because you felt better?' (Don't shame \u2014 this is about understanding why it matters.)", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with emphasis on the feedback loop analysis", "say": "We're building a model with a reinforcing feedback loop \u2014 a system that amplifies itself. Unlike self-correcting systems, this one spirals out of control.", "do": "Preview LEVER steps. Draw the reinforcing loop on the board: more resistance \u2192 less effectiveness \u2192 more resistance. Ask: 'What makes this loop dangerous compared to a balancing loop that self-corrects?'", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for antibiotic resistance model with external/internal sorting", "say": "We have six components. Two are things WE control \u2014 dosage and duration. Four are things the SYSTEM controls. Which is which, and why does that distinction matter?", "do": "Guide component sorting. Key discussion: Why are Antibiotic Dosage and Treatment Duration external? Because humans decide them. Why is that important? Because the crisis is driven by human CHOICES, not just biology.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship mapping with reinforcing loop highlighted", "say": "Here's where it gets interesting. Trace what happens when you increase antibiotic dosage \u2014 what happens to bacterial population? And then what happens to resistant bacteria percentage? And then what happens to the antibiotic's effectiveness?", "do": "Students map relationships. Explicitly identify the reinforcing loop. Have students trace the loop multiple times, noting how each cycle amplifies the previous one. Discuss: 'How is this different from the balancing feedback loops we've seen before?'", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Scenario comparison graphs showing full course vs. incomplete course vs. sub-therapeutic", "say": "We're running three scenarios. One is proper treatment. One is what most people actually do. One is what happens when the dose is too low. Predict which is the MOST dangerous \u2014 then test your prediction.", "do": "Students predict outcomes BEFORE running simulations. Run all three scenarios. Key revelation: incomplete treatment produces WORSE long-term outcomes than no treatment. Have students explain WHY using the reinforcing feedback loop.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with data from simulations and real-world statistics", "say": "Here's the takeaway that should genuinely scare you: 2.8 million antibiotic-resistant infections happen in the US every year. Over 35,000 people die. And the pipeline for new antibiotics is nearly empty.", "do": "Lead discussion connecting model results to real-world data. Key question: 'If your model shows that incomplete treatment accelerates resistance, what does that mean for the millions of people who stop antibiotics early every year?' Discuss systemic vs. individual responsibility.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Public health campaign design challenge with evaluation criteria", "say": "The WHO says antibiotic resistance is a top-10 global health threat. Your team has been hired to create a campaign that changes behavior \u2014 not just awareness. Your model data is your evidence.", "do": "Groups design evidence-based campaigns using model data. Emphasize that effective campaigns change BEHAVIOR, not just knowledge. Groups present and peer-evaluate campaigns on scientific accuracy, persuasiveness, and actionability.", "time": "12 min"}
    ],
    "sort_reasoning": "Antibiotic Dosage and Treatment Duration are external components because they are controlled by human decisions \u2014 doctors prescribe them and patients choose whether to follow through. The system doesn't determine these values; people do. Bacterial Population, Resistant Bacteria Percentage, Mutation Rate, and Immune Response are internal because they are determined by biological processes within the system. Mutation Rate is internal because while it has a baseline, it is a property of the bacterial population itself, not something externally controlled. The key insight is that the external components (human choices) drive the selective pressure that activates the internal reinforcing feedback loop.",
    "relationships": [
        ("Antibiotic Dosage to Bacterial Population", "NEGATIVE (-)", "Higher antibiotic dosage kills more susceptible bacteria, reducing the total Bacterial Population. However, this effect diminishes as Resistant Bacteria Percentage increases \u2014 a critical non-linearity in the system."),
        ("Treatment Duration to Resistant Bacteria Percentage", "NEGATIVE (-)", "Longer, complete treatment courses reduce Resistant Bacteria Percentage by ensuring that even partially resistant bacteria are eliminated. Incomplete treatment leaves resistant bacteria alive and removes their susceptible competitors."),
        ("Bacterial Population to Resistant Bacteria Percentage", "POSITIVE (+) [Reinforcing Loop]", "As susceptible bacteria are killed by antibiotics, the Resistant Bacteria Percentage increases because resistant bacteria survive and reproduce without competition. This is the entry point to the reinforcing feedback loop."),
        ("Resistant Bacteria Percentage to Bacterial Population", "POSITIVE (+) [Reinforcing Loop]", "As resistance increases, antibiotics become less effective, allowing the total Bacterial Population to rebound \u2014 now dominated by resistant strains."),
        ("Mutation Rate to Resistant Bacteria Percentage", "POSITIVE (+)", "Higher mutation rates increase the probability of resistance genes appearing in the population, feeding the reinforcing loop with new resistant individuals."),
        ("Immune Response to Bacterial Population", "NEGATIVE (-)", "A strong immune response works alongside antibiotics to reduce bacterial population. When immune response is weak, antibiotics must do all the work, increasing the chance of incomplete clearance.")
    ],
    "sim_answers": [
        ("Full Course Scenario", "When Antibiotic Dosage is high and Treatment Duration is complete, the Bacterial Population drops rapidly and stays low. Resistant Bacteria Percentage initially increases as susceptible bacteria are killed first, but with sustained treatment, even partially resistant bacteria are eliminated. The Immune Response has time to clear remaining bacteria. The reinforcing loop is activated briefly but interrupted before it can spiral."),
        ("Incomplete Course Scenario", "When Treatment Duration is cut to 50%, the initial results look similar \u2014 Bacterial Population drops and the patient feels better. However, the remaining bacteria are disproportionately resistant. Without continued antibiotic pressure, these resistant bacteria multiply rapidly. Resistant Bacteria Percentage surges to near 100%. The reinforcing loop fully activates: more resistance \u2192 less effectiveness \u2192 more resistance. If this infection is treated again, the same antibiotic will be far less effective."),
        ("Sub-Therapeutic Dosage Scenario", "Low dosage creates the WORST outcome. The antibiotic is strong enough to create selective pressure (killing some susceptible bacteria) but too weak to kill resistant ones. This is the perfect environment for evolving resistance \u2014 strong enough to select, too weak to eliminate. Resistant Bacteria Percentage climbs steadily while Bacterial Population remains high. The reinforcing loop runs continuously at a moderate rate, breeding resistance over time.")
    ],
    "reflection_exemplars": [
        ("Why is incomplete treatment worse than no treatment?", "Without antibiotics, resistant and susceptible bacteria coexist in their natural proportions \u2014 there's no selective pressure favoring either group. But incomplete treatment kills most susceptible bacteria while leaving resistant ones alive. Now the resistant bacteria have no competition for resources. They multiply and become the dominant population. The next time antibiotics are used, the starting population is already heavily resistant, making the reinforcing feedback loop kick in faster and harder."),
        ("How does the reinforcing feedback loop make this an accelerating crisis?", "In a balancing feedback loop, the system self-corrects \u2014 more of one thing leads to less of it, stabilizing the system. But the antibiotic resistance loop is reinforcing: more resistant bacteria \u2192 less antibiotic effectiveness \u2192 more resistant bacteria survive \u2192 even less effectiveness. Each cycle amplifies the previous one. This means resistance doesn't grow linearly \u2014 it accelerates. Once the resistant proportion passes a critical threshold, the antibiotic becomes effectively useless, and the loop has 'won.'")
    ],
    "stem_intro": "Present the challenge: The WHO has declared antibiotic resistance a top-10 global health threat. Your team has been hired to create a public health campaign that uses your model data to change behavior around antibiotic use. You must communicate the science of reinforcing feedback loops in a way that motivates action, not just understanding.",
    "stem_concepts": [
        ("Reinforcing Feedback Loops", "Unlike balancing loops that stabilize systems, reinforcing loops amplify change. In antibiotic resistance, the loop is: more resistant bacteria \u2192 less antibiotic effectiveness \u2192 more resistance. This means the problem accelerates over time unless the loop is interrupted."),
        ("Selective Pressure and Natural Selection", "Antibiotics create selective pressure by killing susceptible bacteria. Resistant bacteria survive not because antibiotics make them resistant, but because pre-existing mutations give them an advantage. This is natural selection in real time, observable over days rather than millennia."),
        ("Threshold Effects in Treatment", "There is a critical threshold in treatment: if enough bacteria are killed (by completing the full course), the immune system can clear the rest. If not enough are killed (incomplete course), the surviving resistant population rebounds. The threshold is the difference between cure and catastrophe.")
    ],
    "stem_eval": [
        ("Expert (4)", "Campaign uses specific model data to support claims, accurately explains the reinforcing feedback loop in accessible language, proposes evidence-based behavioral changes with measurable outcomes, and addresses both individual and systemic solutions"),
        ("Proficient (3)", "Campaign accurately represents the science of resistance, uses model data, and proposes clear behavioral recommendations"),
        ("Developing (2)", "Campaign shows understanding of resistance but lacks model data support or proposes vague behavioral changes"),
        ("Beginning (1)", "Campaign contains scientific inaccuracies or does not connect to model evidence")
    ],
    "support": [
        "Provide a visual reinforcing feedback loop diagram that students can trace with their finger, labeling each step",
        "Use a physical analogy: red and green M&Ms in a bag \u2014 'antibiotics' remove only green ones, leaving red to dominate",
        "Sentence frames: 'When [treatment variable] changes, the reinforcing loop [activates/is interrupted] because ___'",
        "Scaffolded data table for recording simulation results with columns for each component over time"
    ],
    "extensions": [
        "Research MRSA or CRE and model how horizontal gene transfer accelerates resistance spread across species",
        "Investigate phage therapy as an alternative to antibiotics and add it as a new component in the model",
        "Analyze real-world data from the CDC's Antibiotic Resistance Threats Report and compare to model predictions",
        "Model the economic incentives that discourage pharmaceutical companies from developing new antibiotics"
    ],
    "cross_curr": [
        ("Math", "Calculate exponential growth rates for resistant bacterial populations and determine the 'tipping point' where resistance becomes dominant using your model data"),
        ("ELA", "Write a persuasive op-ed for a school newspaper explaining why antibiotic misuse is everyone's problem, using evidence from your computational model"),
        ("Social Studies", "Research how antibiotic resistance disproportionately affects low-income communities and countries with less regulated pharmaceutical systems")
    ],
    "misconceptions": [
        ("Antibiotics stop working because your body becomes immune to them", "It's not YOUR body that becomes resistant \u2014 it's the BACTERIA. Antibiotic resistance is an evolutionary adaptation of bacterial populations, not a change in human physiology. The bacteria evolve through natural selection: those with resistance genes survive treatment and pass those genes to their offspring.", "Ask: 'If you take the same painkiller many times, does the painkiller stop working, or does your body change?' Then flip it: 'With antibiotics, it's the bacteria that change, not you or the drug.'"),
        ("Antibiotics create resistant bacteria", "Antibiotics don't CREATE resistance \u2014 they CREATE THE CONDITIONS where pre-existing resistance becomes advantageous. Resistance mutations exist randomly in bacterial populations before any antibiotic exposure. Antibiotics just remove the competition, allowing those rare resistant individuals to dominate.", "Analogy: Imagine a classroom where some students have umbrellas and others don't. Rain doesn't CREATE umbrellas \u2014 but rain makes having an umbrella a huge advantage. The umbrellas were already there."),
        ("Taking more antibiotics is always better", "Higher doses and longer courses aren't always better \u2014 the optimal strategy is taking the RIGHT dose for the RIGHT duration as prescribed. Excessive antibiotic use (including in livestock agriculture) creates unnecessary selective pressure that breeds resistance without medical benefit. The goal is to use antibiotics precisely, not maximally.", "Ask: 'If using a hammer is good for driving nails, is using a sledgehammer always better?' Precision matters more than force in both construction and medicine.")
    ]
}

L02 = {
    "id": "G09L2-L02",
    "title": "Climate Tipping Points: The Point of No Return",
    "subtitle": "When Earth's Climate System Crosses a Threshold It Can't Come Back From",
    "ngss": "HS-ESS3-5, HS-ESS2-4",
    "ngss_desc": "Analyze geoscience data and the results from global climate models to make an evidence-based forecast of the current rate of global or regional climate change and associated future impacts to Earth systems. Use a model to describe how variations in the flow of energy into and out of Earth's systems result in changes in climate.",
    "big_question": "Is there a temperature where Earth's climate spirals out of control \u2014 and are we close to it?",
    "objectives": [
        "Model how Earth's climate system contains multiple reinforcing feedback loops that can trigger tipping points",
        "Explain the ice-albedo feedback mechanism and why it accelerates warming once activated",
        "Identify threshold dynamics where small changes in input produce dramatically different system outcomes",
        "Analyze how permafrost methane release creates a reinforcing loop independent of human emissions",
        "Evaluate the scientific basis for climate tipping point warnings using model evidence"
    ],
    "vocabulary": [
        ("Tipping Point", "A critical threshold in a system where a small additional change triggers a dramatic and often irreversible shift in the system's behavior"),
        ("Albedo Effect", "The reflectivity of a surface \u2014 ice reflects 80-90% of solar radiation (high albedo) while ocean absorbs 90% (low albedo), creating a powerful feedback mechanism"),
        ("Reinforcing Feedback", "A system loop where the output amplifies the original change \u2014 warming melts ice, which reduces albedo, which causes more warming"),
        ("Permafrost", "Permanently frozen ground in Arctic regions that contains an estimated 1.5 trillion tons of carbon \u2014 twice what's currently in the atmosphere"),
        ("Threshold Dynamics", "System behavior where outcomes are relatively stable until a critical value is crossed, then change rapidly and may become irreversible"),
        ("Thermal Inertia", "The tendency of oceans and large systems to resist temperature change \u2014 creating a time delay between cause and effect that masks the true trajectory")
    ],
    "components": [
        ("CO2 Emissions", "The rate of carbon dioxide released into the atmosphere from human activity, measured in gigatons per year", True),
        ("Global Temperature", "The average surface temperature of Earth, currently about 1.1\u00b0C above pre-industrial levels and rising", False),
        ("Ice Cover", "The total area of glaciers, ice sheets, and sea ice, which has been declining at accelerating rates since the 1980s", False),
        ("Albedo Effect", "The overall reflectivity of Earth's surface \u2014 decreases as ice melts and is replaced by darker ocean or land", False),
        ("Permafrost Methane Release", "The rate at which thawing permafrost releases trapped methane and CO2 \u2014 a greenhouse gas source independent of human activity", False),
        ("Sea Level", "Global average sea level, which rises from both melting ice and thermal expansion of warming ocean water", False),
        ("Ocean Heat Absorption", "The rate at which oceans absorb atmospheric heat \u2014 oceans have absorbed 90% of excess heat but are approaching saturation", False)
    ],
    "think_about_it": "If melting ice reduces Earth's reflectivity, which causes more warming, which melts more ice \u2014 what kind of feedback loop is this? Now add permafrost: warming thaws permafrost, releasing methane (a greenhouse gas 80x more potent than CO2), which causes more warming. How many reinforcing loops can you find in this system?",
    "scenarios": [
        ("Below Tipping Point", "Set CO2 Emissions to moderate levels and observe system behavior \u2014 does it stabilize or accelerate?"),
        ("At the Tipping Point", "Gradually increase CO2 Emissions until the system behavior changes dramatically \u2014 identify the threshold"),
        ("Past the Tipping Point", "Set CO2 Emissions high enough to trigger the ice-albedo feedback loop and observe cascading effects"),
        ("Emissions Reduction", "After triggering the tipping point, reduce CO2 Emissions to zero \u2014 does the system recover?")
    ],
    "sim_scenarios": [
        ("Below Threshold", "Moderate CO2 emissions, current conditions", "What do you predict happens to Global Temperature and Ice Cover when emissions stay at moderate levels? Does the system find a new equilibrium?"),
        ("Crossing the Threshold", "CO2 emissions increase past the tipping point", "What do you predict happens to Ice Cover and Albedo Effect once Global Temperature crosses the tipping point? Does the change accelerate or slow down?"),
        ("Attempted Recovery", "Emissions drop to zero after tipping point is crossed", "If we reduce CO2 Emissions to zero AFTER the tipping point, do you predict the system will return to its original state? Why or why not?")
    ],
    "discoveries": [
        "The climate system has multiple reinforcing feedback loops that can activate simultaneously, creating cascading tipping points",
        "The ice-albedo feedback loop means that once ice loss passes a threshold, warming accelerates even without additional CO2 emissions",
        "Permafrost thawing creates a second reinforcing loop that is independent of human emissions \u2014 once it starts, we can't stop it by reducing our emissions alone",
        "Thermal inertia means the full effects of today's emissions won't be felt for decades \u2014 the system has a dangerous time delay",
        "Some tipping points are irreversible on human timescales \u2014 even eliminating all emissions may not restore the system",
        "Ocean heat absorption has been masking the true rate of warming, but oceans are approaching their capacity to continue absorbing excess heat"
    ],
    "answer": "Earth's climate system contains multiple reinforcing feedback loops that can trigger tipping points \u2014 thresholds where the system shifts from gradual change to rapid, potentially irreversible transformation. The ice-albedo loop (melting ice reduces reflectivity, causing more warming, causing more melting) and the permafrost methane loop (warming releases methane, causing more warming, releasing more methane) can cascade into each other. Scientists estimate the critical threshold is around 1.5-2.0\u00b0C above pre-industrial levels \u2014 and we're already at 1.1\u00b0C. The terrifying truth is that once crossed, some tipping points cannot be reversed even if we eliminate all emissions.",
    "stem_title": "Design a Climate Tipping Point Data Dashboard",
    "stem_mission": "Create an interactive data dashboard that visualizes the key climate tipping points, shows where we currently stand relative to each threshold, and communicates the urgency and irreversibility of crossing these points.",
    "stem_scenario": "A city government is making decisions about climate policy and needs a clear, visual tool that shows elected officials \u2014 who are not scientists \u2014 exactly what climate tipping points are, how close we are to them, and what happens if we cross them. Your team has been hired to build this dashboard using your model data.",
    "stem_questions": [
        "Which tipping point in your model is we closest to crossing, and what data supports this?",
        "How can you visualize the difference between reversible and irreversible tipping points?",
        "What is the most important single number or threshold that a policymaker needs to understand?"
    ],
    "stem_design_qs": [
        "How will you represent multiple feedback loops visually without overwhelming the viewer?",
        "What color coding or visual language will you use to communicate urgency levels?",
        "How will you show the time delay between emissions and effects (thermal inertia)?",
        "How will your dashboard help a non-scientist understand why 1.5\u00b0C vs. 2.0\u00b0C matters so much?"
    ],
    "career": "Climate Scientists and Earth System Modelers build computational models of global climate systems and study tipping points. They work at NOAA, NASA, IPCC, universities, and think tanks, earning $80,000\u2013$160,000/year. Their work directly informs international climate policy decisions.",
    "images": {
        "cover": ("G09L2-L02-cover.png", "A photorealistic, cinematic split-image showing a pristine Arctic ice sheet on one side and a melting, crumbling glacier on the other, dramatic lighting showing the contrast between before and after a tipping point, deep blues and warm oranges"),
        "landscape": ("G09L2-L02-landscape.png", "A photorealistic image of diverse 14-15 year old students examining a large interactive climate data display in a modern science classroom, with temperature graphs and ice coverage maps visible on screens, engaged expressions of concern and curiosity"),
        "modeling": ("G09L2-L02-modeling.png", "A photorealistic image of diverse 14-15 year old students working on laptops building climate system models with feedback loop diagrams and temperature graphs on screens, modern classroom with climate data posters, collaborative engaged atmosphere"),
        "discussion": ("G09L2-L02-discussion.png", "A photorealistic image of a diverse group of 14-15 year old students in a heated class discussion about climate tipping points, a teacher at a smartboard showing a threshold diagram with before/after scenarios, students actively debating with raised hands"),
        "stem": ("G09L2-L02-stem.png", "A photorealistic image of diverse 14-15 year old students designing data dashboards on tablets and large monitors, working with climate visualizations showing temperature thresholds and ice coverage data, collaborative teamwork in a tech-equipped classroom")
    },
    "pre_assessment": [
        "What do you already know about climate change? What causes it?",
        "What does 'tipping point' mean to you? Can you think of an everyday example where a small change triggers a big, irreversible effect?",
        "Why do you think scientists talk about 1.5\u00b0C as a critical number for global warming?",
        "Draw what you think happens to Earth's systems if average temperatures increase by 2\u00b0C."
    ],
    "extend_components": [
        ("Carbon Sink Capacity", "The ability of forests and oceans to absorb CO2, which decreases as these systems are stressed or destroyed"),
        ("Thermohaline Circulation", "The global ocean current system driven by temperature and salinity differences, which could collapse if freshwater from melting ice disrupts the pattern"),
        ("Cloud Feedback", "Changes in cloud formation patterns that can either amplify or dampen warming, one of the biggest uncertainties in climate models")
    ],
    "reflections": [
        "What makes a tipping point different from a gradual change? How does your model demonstrate this difference?",
        "Why is thermal inertia (time delay) one of the most dangerous features of the climate system?",
        "Your model shows that reducing emissions to zero after crossing the tipping point doesn't restore the system. Why not?",
        "How do the ice-albedo and permafrost methane feedback loops reinforce each other? What does cascading tipping points mean?",
        "If you were advising world leaders, what would you tell them based on your model's predictions?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model with threshold dynamics and multiple reinforcing feedback loops to explain how Earth's climate system can cross tipping points, producing irreversible changes."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate / ESS3.D Global Climate Change", "The foundation for Earth's climate is the flow of energy from the Sun and the cycling of matter through Earth's systems. Human activities are increasing greenhouse gas concentrations and driving global climate change with multiple feedback effects."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how climate systems can appear stable while approaching critical thresholds, and how small perturbations can trigger large-scale irreversible changes when tipping points are crossed.")
    ],
    "cast_items": [
        "Model how reinforcing feedback loops in Earth's climate system create tipping points",
        "Explain why the ice-albedo feedback accelerates warming once a threshold is crossed",
        "Analyze threshold dynamics using computational models to predict system behavior",
        "Evaluate the irreversibility of climate tipping points using model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "In the ice-albedo feedback loop, what happens when a significant amount of Arctic ice melts and is replaced by dark ocean water?"),
        ("Constructed Response:", "Using your computational model, explain why climate scientists describe tipping points as 'points of no return.' In your response, identify at least two reinforcing feedback loops in the climate system and explain how they can cascade into each other to produce irreversible change.")
    ],
    "background_intro": "This lesson uses a threshold model to explore one of the most critical questions in Earth science: can Earth's climate system cross a point of no return? The model features multiple reinforcing feedback loops (ice-albedo and permafrost methane) that interact to create threshold dynamics \u2014 where the system behaves one way below the threshold and dramatically differently above it. Students will discover that some changes are irreversible on human timescales and that time delays (thermal inertia) mask the true trajectory of the system.",
    "background_sections": [
        ("What Is a Tipping Point?", "A tipping point is a critical threshold in a system where a small additional change triggers a dramatic, often irreversible shift. Think of pushing a ball up a hill \u2014 small pushes keep it rolling slowly upward, but once it crests the hill, it rolls down the other side with accelerating speed. In climate systems, tipping points occur when reinforcing feedback loops overwhelm the system's natural stabilizing mechanisms. Below the threshold, the system absorbs perturbations and returns toward equilibrium. Above the threshold, the system enters a self-reinforcing cycle that drives it away from its original state."),
        ("The Ice-Albedo Feedback", "Ice and snow reflect 80-90% of incoming solar radiation back to space (high albedo). Dark ocean water absorbs about 94% of that same radiation (low albedo). As global temperatures rise, ice melts and is replaced by dark water, which absorbs more heat, which causes more warming, which melts more ice. This reinforcing loop means that ice loss accelerates once it begins. Arctic sea ice has declined by about 40% since 1979, and the rate of loss is accelerating. Scientists estimate that an ice-free Arctic summer could occur by the 2040s, which would dramatically amplify warming."),
        ("The Permafrost Carbon Bomb", "Arctic permafrost contains an estimated 1.5 trillion tons of carbon \u2014 roughly twice the amount currently in Earth's entire atmosphere. As global temperatures rise, permafrost thaws and microorganisms begin decomposing this ancient organic material, releasing CO2 and methane. Methane is approximately 80 times more potent as a greenhouse gas than CO2 over a 20-year period. This creates a reinforcing loop independent of human emissions: warming thaws permafrost \u2192 releases greenhouse gases \u2192 causes more warming \u2192 thaws more permafrost. Once this loop activates, reducing human emissions alone cannot stop it."),
        ("Cascading Tipping Points", "The most dangerous scenario is cascading tipping points \u2014 where crossing one threshold triggers another. For example: warming melts Arctic ice (crossing tipping point 1), which accelerates warming enough to thaw massive permafrost regions (crossing tipping point 2), which releases enough methane to destabilize ocean methane hydrates (crossing tipping point 3). Each cascade makes the next one more likely. Scientists have identified at least 15 potential climate tipping points, and several may already be activated. The interactions between these systems make precise prediction difficult but make the precautionary principle urgent."),
        ("Thermal Inertia and Hidden Danger", "Oceans have absorbed approximately 90% of the excess heat trapped by greenhouse gases. This thermal inertia means the atmosphere is warming more slowly than it otherwise would \u2014 but it also means we haven't yet felt the full effect of emissions already released. Even if all emissions stopped today, global temperatures would continue to rise for decades as the oceans release stored heat. This time delay creates a dangerous illusion: the system appears to be changing slowly, but the committed warming is much larger than what we currently observe.")
    ],
    "lever_L": "Students identify seven components: CO2 Emissions as the sole external driver, and six internal components (Global Temperature, Ice Cover, Albedo Effect, Permafrost Methane Release, Sea Level, Ocean Heat Absorption) that interact through feedback loops. Students recognize that having only one external driver means the system's internal dynamics dominate behavior.",
    "lever_E": "Students map multiple feedback loops: the ice-albedo reinforcing loop (warming \u2192 less ice \u2192 lower albedo \u2192 more warming) and the permafrost methane reinforcing loop (warming \u2192 thawing \u2192 methane release \u2192 more warming). They identify the threshold where these loops overpower natural stabilizing mechanisms and the system enters a self-reinforcing cascade.",
    "lever_V": "Students build a model showing how CO2 Emissions drive Global Temperature, which triggers the ice-albedo and permafrost feedback loops once thresholds are crossed, leading to accelerating changes in Sea Level, Ocean Heat Absorption, and the other internal components.",
    "lever_Ev": "Students run below-threshold, at-threshold, and above-threshold scenarios to identify the tipping point. They test whether reducing emissions to zero after crossing the threshold can reverse the changes \u2014 and discover that some tipping points are irreversible on human timescales.",
    "lever_R": "Students extend the model with Carbon Sink Capacity, Thermohaline Circulation, or Cloud Feedback to explore additional tipping points and the cascading interactions between them.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split image: pristine ice sheet vs. collapsing glacier", "say": "There are moments in Earth's history where the climate shifted so fast that entire ecosystems collapsed in decades. Are we approaching one of those moments right now?", "do": "Show a time-lapse of Arctic ice loss from 1979 to present. The visual impact is powerful \u2014 let it speak for itself before discussion.", "time": "3 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals, vocabulary, and a visual of a ball balanced on a hill (tipping point metaphor)", "say": "Today's model is different from anything we've built before. We're looking for the THRESHOLD \u2014 the point where the system's behavior changes fundamentally.", "do": "Introduce the ball-on-a-hill metaphor for tipping points. Pre-teach 'threshold dynamics' and 'reinforcing feedback.' Ask: 'What everyday examples of tipping points can you think of?'", "time": "4 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Is there a temperature where Earth's climate spirals out of control?", "say": "Scientists keep talking about 1.5 degrees Celsius. That sounds tiny. Why would 1.5 degrees matter? Because in a system with tipping points, small numbers can mean everything.", "do": "Quick activity: 'Can you think of other situations where a tiny change triggers a massive effect?' (Examples: one degree between water and ice, one vote in an election.) Build intuition for threshold dynamics.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with emphasis on identifying tipping points", "say": "We're going to build a model, find its tipping point, and then try to reverse the damage. Spoiler alert: the results will change how you think about 'fixing' climate change.", "do": "Preview LEVER steps. Draw two feedback loops on the board (ice-albedo and permafrost methane). Ask: 'What happens when TWO reinforcing loops activate at the same time?'", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards with external/internal sorting activity", "say": "We have seven components but only ONE external driver \u2014 CO2 Emissions. That means the system's own internal dynamics control most of what happens. Why is that significant?", "do": "Guide component sorting. Discuss: With only one external variable, this system is mostly self-driven once activated. That's what makes tipping points so dangerous \u2014 once the internal loops take over, changing the external input may not be enough.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Feedback loop mapping with two reinforcing loops highlighted in different colors", "say": "Map every connection. Then find the loops. How many reinforcing feedback loops can you identify? And here's the key question: what happens when BOTH loops activate simultaneously?", "do": "Students map relationships and identify both reinforcing loops. Use different colored markers for each loop. Key discussion: 'Cascading tipping points happen when one loop's output triggers another loop. Trace how the ice-albedo loop could trigger the permafrost loop.'", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Three scenario graphs showing below, at, and past the tipping point", "say": "Run three scenarios: below the threshold, at the threshold, and past it. Then run a fourth \u2014 the most important one: reduce emissions to ZERO after crossing the tipping point. What happens?", "do": "Students predict before running simulations. The critical moment is Scenario 4: even with zero emissions, the system continues to warm due to activated feedback loops. This is the 'point of no return' concept made tangible. Allow time for students to process this result.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with current data on Arctic ice loss and temperature trends", "say": "We are currently at 1.1\u00b0C above pre-industrial. The threshold in most models is between 1.5\u00b0C and 2.0\u00b0C. That means we may have less than half a degree of safety margin. Your model just showed you what happens when we cross it.", "do": "Connect model results to real-world data. Share current CO2 levels (425+ ppm) and rate of increase. Discuss: 'Your model shows that crossing the tipping point is irreversible. What does that mean for decisions we make THIS decade?'", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Data dashboard design challenge for policymakers", "say": "Policymakers aren't scientists. They need to see the data clearly, understand the thresholds, and know what's at stake. Your dashboard needs to make the invisible visible.", "do": "Groups design data dashboards. Emphasize translating complex system dynamics into visual tools that non-scientists can act on. Groups present and peer-evaluate on clarity, accuracy, and actionability.", "time": "12 min"}
    ],
    "sort_reasoning": "CO2 Emissions is the only external component because it represents human activity \u2014 the one variable we directly control. All other components are internal because they are determined by the system's own dynamics. Global Temperature responds to greenhouse gas concentrations. Ice Cover responds to temperature. Albedo Effect responds to ice cover. Permafrost Methane Release responds to temperature. Sea Level responds to ice melt and thermal expansion. Ocean Heat Absorption responds to temperature differences between atmosphere and ocean. The key insight is that with only one external driver, the system's behavior is dominated by its internal feedback loops once they activate.",
    "relationships": [
        ("CO2 Emissions to Global Temperature", "POSITIVE (+)", "Increasing CO2 Emissions raises greenhouse gas concentrations, trapping more heat and increasing Global Temperature. This is the primary driver that can push the system toward tipping points."),
        ("Global Temperature to Ice Cover", "NEGATIVE (-)", "Higher Global Temperature melts glaciers, ice sheets, and sea ice, reducing total Ice Cover. This relationship accelerates as temperature rises due to the feedback loops it activates."),
        ("Ice Cover to Albedo Effect", "POSITIVE (+)", "Less Ice Cover means lower Albedo Effect (less reflectivity), as dark ocean and land replace reflective ice. This is a proportional relationship \u2014 as one decreases, so does the other."),
        ("Albedo Effect to Global Temperature", "NEGATIVE (-) [Reinforcing Loop]", "Lower Albedo Effect means Earth absorbs more solar radiation, increasing Global Temperature. Combined with the Temperature-to-Ice connection, this completes the ice-albedo reinforcing loop."),
        ("Global Temperature to Permafrost Methane Release", "POSITIVE (+) [Threshold]", "Above a critical temperature threshold, permafrost begins thawing and releasing trapped methane and CO2. Below the threshold, this component is essentially zero. This is a step-function relationship."),
        ("Permafrost Methane Release to Global Temperature", "POSITIVE (+) [Reinforcing Loop]", "Released methane and CO2 increase greenhouse gas concentrations, raising Global Temperature. This completes the second reinforcing feedback loop, independent of human emissions."),
        ("Global Temperature to Sea Level", "POSITIVE (+)", "Higher temperatures cause both ice sheet melting and thermal expansion of ocean water, raising Sea Level."),
        ("Ocean Heat Absorption to Global Temperature", "NEGATIVE (-) [Temporary]", "Ocean heat absorption temporarily slows atmospheric warming by storing heat in deep water. However, this capacity is limited \u2014 as oceans warm, they absorb less heat, and this buffering effect diminishes over time.")
    ],
    "sim_answers": [
        ("Below Threshold Scenario", "With moderate CO2 Emissions, Global Temperature rises slowly. Ice Cover decreases gradually, Albedo Effect drops slightly, but the reinforcing loops don't fully activate. The system is stressed but still within its range of natural variability. Permafrost Methane Release remains near zero. Ocean Heat Absorption buffers some warming. The system finds a new, warmer equilibrium."),
        ("Crossing the Threshold Scenario", "When CO2 Emissions push Global Temperature past the tipping point (approximately 1.5-2.0\u00b0C above pre-industrial), the ice-albedo reinforcing loop activates forcefully. Ice Cover drops rapidly, Albedo Effect plummets, and the loop drives additional warming independent of emissions. Permafrost Methane Release activates as the second reinforcing loop. The two loops reinforce each other \u2014 cascading tipping points. Sea Level rise accelerates. The system enters a self-reinforcing warming trajectory."),
        ("Recovery Attempt Scenario", "Reducing CO2 Emissions to zero AFTER crossing the tipping point does NOT return the system to its original state. The activated reinforcing loops (ice-albedo and permafrost methane) continue driving warming from internal dynamics. Ice Cover continues declining, and Sea Level continues rising. This demonstrates irreversibility \u2014 the system has shifted to a new state that persists even after the external driver is removed. Thermal inertia means decades of additional warming are already committed.")
    ],
    "reflection_exemplars": [
        ("Why can't we just reverse the tipping point by reducing emissions?", "Once the reinforcing feedback loops activate, they become self-sustaining. The ice-albedo loop drives warming even without additional CO2 because less ice means less reflected sunlight. The permafrost loop adds greenhouse gases independent of human emissions. Even at zero human emissions, these internal loops continue warming the planet. It's like pushing a boulder over a cliff \u2014 you can stop pushing, but the boulder keeps falling. The system has shifted to a fundamentally different state that cannot be reversed by simply removing the original cause."),
        ("How do cascading tipping points make the situation more dangerous?", "Each tipping point in isolation is serious. But when one triggers another, the combined effect is far greater than either alone. The ice-albedo loop warms the planet enough to trigger the permafrost methane loop, which adds even more greenhouse gases, which accelerates the ice-albedo loop further. It's like dominoes \u2014 but dominoes that get bigger with each fall. This cascading effect is why scientists are so concerned about the 1.5\u00b0C threshold: it's not that 1.5\u00b0C of warming is catastrophic by itself, but that it may trigger a chain of self-reinforcing processes that push warming far beyond what we can control.")
    ],
    "stem_intro": "Present the challenge: A city government needs to understand climate tipping points to make policy decisions. They're not scientists \u2014 they need a visual, interactive dashboard that shows where we stand relative to critical thresholds and what happens if we cross them. Your team will design this dashboard using your model data, translating complex system dynamics into actionable information.",
    "stem_concepts": [
        ("Threshold Dynamics", "Tipping points are thresholds where system behavior changes fundamentally. Below the threshold, changes are gradual and potentially reversible. Above it, reinforcing feedback loops take over and drive rapid, irreversible change. The key insight is that the threshold itself may be invisible until it's crossed."),
        ("Reinforcing Feedback Cascades", "When multiple reinforcing loops interact, crossing one tipping point can trigger others. The ice-albedo loop warms the system enough to trigger the permafrost methane loop, which amplifies warming further. This cascading effect means the combined impact is far greater than any single loop."),
        ("Irreversibility and Committed Warming", "Thermal inertia means the full effects of today's emissions won't be felt for decades. Even at zero emissions, committed warming from ocean heat release and activated feedback loops will continue. This means decisions made now determine outcomes decades into the future.")
    ],
    "stem_eval": [
        ("Expert (4)", "Dashboard clearly visualizes multiple tipping points, shows current position relative to thresholds, communicates irreversibility, includes time-delay effects, and translates complex feedback dynamics into actionable information for non-scientists"),
        ("Proficient (3)", "Dashboard accurately represents tipping points and thresholds, uses model data, and communicates urgency clearly"),
        ("Developing (2)", "Dashboard shows some tipping point concepts but lacks clear threshold visualization or model data integration"),
        ("Beginning (1)", "Dashboard is incomplete or does not accurately represent tipping point dynamics")
    ],
    "support": [
        "Provide a physical ball-and-hill demonstration: roll a ball up a hill to show how the system behaves differently on either side of the threshold",
        "Use color-coded feedback loop diagrams with arrows students can physically trace",
        "Sentence frames: 'Once [component] crosses the threshold of ___, the reinforcing loop [activates/accelerates] because ___'",
        "Scaffolded comparison table for recording before-threshold vs. after-threshold behavior of each component"
    ],
    "extensions": [
        "Research the AMOC (Atlantic Meridional Overturning Circulation) collapse tipping point and add Thermohaline Circulation to the model",
        "Analyze real NASA/NOAA data on Arctic ice extent from 1979-present and compare observed trends to model predictions",
        "Investigate the concept of 'carbon budget' \u2014 how much more CO2 can be emitted before crossing the 1.5\u00b0C threshold",
        "Model the difference between 1.5\u00b0C and 2.0\u00b0C outcomes and calculate the economic cost of each scenario"
    ],
    "cross_curr": [
        ("Math", "Calculate the rate of Arctic ice loss using NASA data, fit an exponential curve, and extrapolate to predict when ice-free Arctic summers will occur"),
        ("ELA", "Write a policy brief for a government official explaining climate tipping points, using evidence from your model to support specific policy recommendations"),
        ("Social Studies", "Research climate justice: which countries contribute most to CO2 emissions, and which countries will be most affected by tipping point consequences?")
    ],
    "misconceptions": [
        ("Climate change is gradual and linear", "Climate change is NOT a smooth, steady process. The system contains tipping points \u2014 thresholds where behavior shifts dramatically. Below the threshold, changes may be gradual. But once a tipping point is crossed, reinforcing feedback loops drive rapid, accelerating change. The transition from 'manageable' to 'catastrophic' can happen much faster than the gradual buildup that preceded it.", "Slowly heat ice water while monitoring temperature. It rises slowly until 0\u00b0C, then stays at 0\u00b0C during melting (absorbing energy), then rises again. The relationship isn't linear \u2014 the same is true of climate systems at their thresholds."),
        ("If we stop emissions, the climate will go back to normal", "Even if all emissions stopped today, the climate would NOT return to pre-industrial conditions for centuries or millennia. Thermal inertia means decades of additional warming is already 'in the pipeline.' Activated feedback loops (ice-albedo, permafrost methane) continue independently. CO2 persists in the atmosphere for hundreds of years. The system has memory \u2014 you can't undo the damage by simply stopping the cause.", "Analogy: If you're speeding toward a wall and take your foot off the gas, the car doesn't instantly stop. Momentum carries you forward. Climate thermal inertia is like momentum \u2014 the system keeps moving even after the force is removed."),
        ("1.5\u00b0C of warming isn't a big deal", "1.5\u00b0C sounds small in everyday terms, but in climate science, it represents an enormous amount of energy added to Earth's system. The difference between today's climate and the last Ice Age is only about 5\u00b0C. More importantly, 1.5\u00b0C may be the threshold that activates reinforcing feedback loops, making the difference between 1.4\u00b0C and 1.6\u00b0C far more consequential than the difference between 0.4\u00b0C and 0.6\u00b0C.", "Ask: 'What's the difference between 99\u00b0C water and 101\u00b0C water? Just 2 degrees \u2014 but one is liquid and one is gas. Thresholds matter.' The same principle applies to climate tipping points.")
    ]
}

L03 = {
    "id": "G09L2-L03",
    "title": "Why Pandemics Go Exponential",
    "subtitle": "The Math Behind How One Infection Becomes a Global Crisis",
    "ngss": "HS-LS2-6, HS-ETS1-4",
    "ngss_desc": "Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints, including the analysis of system interactions and component interactions.",
    "big_question": "How does one person's infection become a global pandemic in weeks?",
    "objectives": [
        "Model SIR (Susceptible-Infected-Recovered) disease dynamics using a coupled compartment system",
        "Explain how contact rate and transmission rate drive exponential growth in the early stages of an outbreak",
        "Analyze how interventions (vaccination, quarantine) create balancing feedback that counteracts exponential spread",
        "Predict the effects of different intervention timing on total infections and peak hospital burden",
        "Evaluate the trade-offs between early aggressive intervention and delayed response"
    ],
    "vocabulary": [
        ("SIR Model", "A compartmental model dividing a population into Susceptible, Infected, and Recovered groups \u2014 individuals flow between compartments based on transmission and recovery rates"),
        ("R-naught (R\u2080)", "The basic reproduction number \u2014 the average number of new infections caused by one infected person in a fully susceptible population. If R\u2080 > 1, the epidemic grows; if R\u2080 < 1, it shrinks"),
        ("Exponential Growth", "Growth where the rate of increase is proportional to the current amount \u2014 the larger the infected population, the faster it grows, creating a J-shaped curve"),
        ("Herd Immunity Threshold", "The proportion of the population that must be immune to stop sustained transmission \u2014 calculated as 1 - (1/R\u2080)"),
        ("Flattening the Curve", "Interventions that reduce R\u2080 below 1, slowing the rate of new infections so healthcare systems are not overwhelmed"),
        ("Coupled Compartments", "A model structure where populations in different 'compartments' (S, I, R) are linked by flows that depend on the state of multiple compartments simultaneously")
    ],
    "components": [
        ("Susceptible Population", "The number of people who have not yet been infected and have no immunity \u2014 decreases as people get infected or vaccinated", False),
        ("Infected Population", "The number of people currently infectious and capable of spreading the disease \u2014 increases with new infections and decreases with recovery", False),
        ("Recovered Population", "The number of people who have recovered and gained immunity \u2014 increases as infected people recover and are removed from the transmission chain", False),
        ("Contact Rate", "The average number of close contacts per person per day \u2014 affected by social behavior, population density, and public health measures", True),
        ("Transmission Rate", "The probability that a contact between an infected and susceptible person results in transmission \u2014 determined by pathogen biology and hygiene practices", False),
        ("Vaccination Rate", "The number of susceptible people vaccinated per day, moving them directly from Susceptible to Recovered without going through infection", True),
        ("Quarantine Effectiveness", "How effectively quarantine measures reduce the Contact Rate \u2014 ranging from 0% (no quarantine) to near 100% (complete isolation)", True)
    ],
    "think_about_it": "In the early stages of a pandemic, every infected person contacts many susceptible people. But as more people get infected and recover, there are fewer susceptible people to infect. How does this natural depletion of the susceptible population create a balancing feedback loop \u2014 and why isn't that enough to prevent catastrophe?",
    "scenarios": [
        ("Uncontrolled Spread", "Set Contact Rate high, Vaccination Rate to zero, Quarantine Effectiveness to zero \u2014 observe the classic epidemic curve"),
        ("Early Quarantine", "Implement high Quarantine Effectiveness when Infected Population reaches 1% \u2014 observe the impact on peak infections"),
        ("Late Quarantine", "Implement the same Quarantine Effectiveness when Infected Population reaches 10% \u2014 compare with early intervention"),
        ("Vaccination Campaign", "Set Vaccination Rate to moderate levels throughout the simulation \u2014 observe how it changes the epidemic trajectory")
    ],
    "sim_scenarios": [
        ("Uncontrolled Epidemic", "High contact rate, no interventions", "What do you predict the shape of the Infected Population curve will look like over time? Will it keep growing forever, or will it peak and decline? Why?"),
        ("Early vs. Late Intervention", "Quarantine at 1% infected vs. 10% infected", "Do you predict that the TIMING of quarantine matters more than its strength? What will be the difference in total infections between early and late intervention?"),
        ("Vaccination Effect", "Moderate vaccination rate throughout epidemic", "How do you predict vaccination changes the herd immunity threshold? At what percentage of vaccinated population will the epidemic stop growing?")
    ],
    "discoveries": [
        "Pandemics grow exponentially because every infected person creates multiple new infections \u2014 each of whom creates multiple more",
        "The SIR model shows that epidemics naturally peak and decline as the susceptible population is depleted, but the damage before the peak can be catastrophic",
        "Timing of intervention matters enormously: the same quarantine implemented at 1% vs. 10% infection can reduce total infections by 50% or more",
        "Vaccination creates a shortcut from Susceptible to Recovered, building immunity without the disease \u2014 reducing both the peak and total infections",
        "R\u2080 determines epidemic dynamics: above 1, the epidemic grows; below 1, it shrinks. Every intervention aims to push R\u2080 below 1",
        "The three compartments (S, I, R) are coupled \u2014 changes in one directly affect the flows to and from the others"
    ],
    "answer": "One infection becomes a pandemic through exponential growth: if each infected person infects 2-3 others (R\u2080 of 2-3), one case becomes 3, then 9, then 27, then 81. Within 20 generations of transmission (which can take just weeks), millions are infected. The SIR model shows this happens because the Susceptible population is large and the transmission chain grows proportionally. Interventions work by reducing R\u2080 below 1 \u2014 through quarantine (reducing contact rate), vaccination (reducing susceptible population), or both. The critical insight is that timing matters enormously: early intervention prevents far more infections than the same intervention applied later.",
    "stem_title": "Design a Pandemic Response Decision Tool",
    "stem_mission": "Using your SIR model data, design a decision support tool that helps public health officials determine WHEN and HOW AGGRESSIVELY to implement interventions during an outbreak, showing the cost of delayed action.",
    "stem_scenario": "A county health department needs a tool that shows, in real time, where they are on the epidemic curve and what different intervention strategies would achieve. Your team will build this tool using your model data, emphasizing the critical importance of intervention timing.",
    "stem_questions": [
        "What is the single most important metric a health official needs to see during an outbreak?",
        "How can your tool show the 'cost of waiting' \u2014 the difference between acting now vs. acting later?",
        "What trade-offs must health officials consider when deciding intervention timing and intensity?"
    ],
    "stem_design_qs": [
        "How will your tool visualize the SIR compartments in real time as the epidemic progresses?",
        "How will you show the projected outcomes of different intervention strategies side by side?",
        "How will you communicate uncertainty \u2014 the fact that early in an epidemic, we don't know exact R\u2080 values?",
        "How will you help officials weigh health outcomes against economic and social costs of interventions?"
    ],
    "career": "Epidemiologists and Public Health Modelers study disease transmission patterns and design intervention strategies. They work at the CDC, WHO, state health departments, and academic research centers, earning $75,000\u2013$150,000/year. During the COVID-19 pandemic, their models directly informed decisions affecting billions of people.",
    "images": {
        "cover": ("G09L2-L03-cover.png", "A photorealistic, cinematic visualization of a network of connected people with infection spreading through connections shown as glowing pathways, transitioning from green (healthy) to red (infected) to blue (recovered), dark background with dramatic lighting"),
        "landscape": ("G09L2-L03-landscape.png", "A photorealistic image of diverse 14-15 year old students examining a large SIR model diagram on a classroom smartboard showing epidemic curves and population compartments, engaged and analytical expressions, modern science classroom"),
        "modeling": ("G09L2-L03-modeling.png", "A photorealistic image of diverse 14-15 year old students working on laptops running epidemic simulations with SIR curves and R-naught calculations visible on screens, modern classroom with public health data posters, collaborative focused atmosphere"),
        "discussion": ("G09L2-L03-discussion.png", "A photorealistic image of a diverse group of 14-15 year old students debating pandemic response strategies around a table with epidemic curve printouts, a teacher facilitating, pointing at a graph showing early vs. late intervention outcomes"),
        "stem": ("G09L2-L03-stem.png", "A photorealistic image of diverse 14-15 year old students designing pandemic response decision tools on tablets and whiteboards, with epidemic curves and intervention timelines visible, collaborative teamwork in a modern science classroom")
    },
    "pre_assessment": [
        "What do you remember about the COVID-19 pandemic? What measures were taken to slow the spread?",
        "Why do you think some diseases spread faster than others?",
        "What does 'exponential growth' mean, and why is it relevant to pandemics?",
        "Draw what you think the number of infections looks like over time during an uncontrolled epidemic."
    ],
    "extend_components": [
        ("Hospital Capacity", "The maximum number of patients the healthcare system can treat simultaneously \u2014 when exceeded, mortality increases dramatically"),
        ("Asymptomatic Transmission Rate", "The percentage of infected people who show no symptoms but can still transmit the disease, making detection and isolation much harder"),
        ("Reinfection Rate", "The rate at which recovered individuals lose immunity and become susceptible again, turning the SIR model into an SIRS model with no permanent recovery")
    ],
    "reflections": [
        "Why does the epidemic curve naturally peak and decline even without intervention? What does this tell you about the SIR model's built-in balancing feedback?",
        "Your model shows that the same quarantine implemented at 1% infection vs. 10% produces dramatically different outcomes. Why does timing matter so much in exponential systems?",
        "How does vaccination change the dynamics compared to quarantine? Which intervention affects which component of the SIR model?",
        "What real-world factors make pandemic modeling more complicated than the basic SIR model?",
        "If you were a public health official during the early days of an outbreak, what would you need to know to make good decisions?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students use the SIR compartmental model to quantitatively analyze disease transmission dynamics, calculate R\u2080, and predict the effects of interventions on epidemic trajectories."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics / ETS1.B Developing Solutions", "Complex interactions in populations (disease transmission) can maintain or disrupt stability. Students use computational models to evaluate intervention strategies for a complex real-world problem."),
        ("Crosscutting Concept", "Systems and System Models", "Students model populations as interconnected compartments where flows between compartments depend on the state of multiple components, demonstrating coupled system dynamics.")
    ],
    "cast_items": [
        "Model disease spread using the SIR compartmental framework with coupled dynamics",
        "Calculate and interpret R\u2080 as the key determinant of epidemic growth or decline",
        "Analyze the impact of intervention timing on total infections and peak burden",
        "Evaluate trade-offs between different pandemic response strategies using model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During an epidemic with R\u2080 = 3, approximately what percentage of the population must be immune (through infection or vaccination) to achieve herd immunity and stop sustained transmission?"),
        ("Constructed Response:", "Using the SIR model, explain why a quarantine implemented when 1% of the population is infected produces dramatically different outcomes than the same quarantine at 10% infection. Include in your explanation the role of exponential growth, the coupling between compartments, and the concept of R\u2080.")
    ],
    "background_intro": "This lesson uses a coupled compartment model (SIR dynamics) to explore how infectious diseases spread through populations. The model demonstrates coupled system dynamics \u2014 the flow between Susceptible, Infected, and Recovered compartments depends on the state of multiple compartments simultaneously. Students will explore exponential growth in the early epidemic phase, the natural balancing feedback as susceptible populations deplete, and how interventions (quarantine and vaccination) modify the system's behavior. The lesson connects mathematical reasoning (R\u2080, herd immunity threshold) with public health decision-making.",
    "background_sections": [
        ("The SIR Model", "The SIR model is one of the foundational tools in epidemiology. It divides a population into three compartments: Susceptible (S) \u2014 people who can be infected; Infected (I) \u2014 people who are currently infectious; and Recovered (R) \u2014 people who have recovered and are immune. People flow from S to I when infected, and from I to R when they recover. The rate of flow from S to I depends on the product of S, I, and the transmission rate \u2014 making it a coupled system where both compartments affect the flow simultaneously. This coupling is what creates exponential growth: more infected people create more opportunities for transmission."),
        ("R-naught and Exponential Growth", "R\u2080 (R-naught) is the basic reproduction number: the average number of new infections caused by one infected person in a fully susceptible population. If R\u2080 > 1, each infected person creates more than one new infection, and the epidemic grows exponentially. If R\u2080 < 1, the epidemic dies out. For context: measles has R\u2080 \u2248 12-18, COVID-19 original strain \u2248 2.5-3, seasonal flu \u2248 1.3. The exponential nature means that early in an epidemic, the infected population doubles at regular intervals. With R\u2080 = 3, one case becomes approximately 59,000 cases in just 10 generations of transmission."),
        ("Herd Immunity and Natural Balancing Feedback", "The SIR model contains a natural balancing feedback loop: as people get infected and recover, the susceptible population shrinks. With fewer susceptible people available, each infected person has fewer potential targets, and the effective reproduction number drops below 1. This is herd immunity \u2014 when enough people are immune that sustained transmission is impossible. The threshold is calculated as 1 - (1/R\u2080). For R\u2080 = 3, that's 67% immune. However, reaching herd immunity through natural infection means 67% of the population gets sick \u2014 with potentially catastrophic consequences."),
        ("Interventions: Changing the System", "Public health interventions work by modifying specific parameters of the SIR model. Quarantine reduces the Contact Rate, directly lowering R\u2080. Vaccination moves people from Susceptible to Recovered without going through Infected, reducing the susceptible pool and lowering the effective R\u2080. The critical insight is that intervention TIMING dramatically affects outcomes. In an exponential system, acting one week earlier can prevent more infections than acting one month later with greater intensity. This is because exponential growth means the infected population during that week of delay may double or triple, creating a vastly larger base for subsequent transmission."),
        ("Beyond Basic SIR", "Real epidemics are more complex than the basic SIR model. Asymptomatic transmission means some infected people spread disease without knowing they're sick. Waning immunity can turn the model into SIRS (where Recovered people become Susceptible again). Heterogeneous mixing means some people have many more contacts than others. Hospital capacity introduces a threshold effect: below capacity, mortality is manageable; above capacity, mortality spikes because patients can't receive care. Despite these complexities, the basic SIR model captures the essential dynamics that make pandemics so dangerous and interventions so time-sensitive.")
    ],
    "lever_L": "Students identify seven components across three types: three internal compartment variables (Susceptible, Infected, Recovered), one internal rate (Transmission Rate), and three external controls (Contact Rate, Vaccination Rate, Quarantine Effectiveness). Students recognize that the three compartments are coupled \u2014 changes in one directly affect flows to the others.",
    "lever_E": "Students map the coupled flows: Susceptible \u2192 Infected (driven by contact between S and I) and Infected \u2192 Recovered (driven by recovery time). They identify the reinforcing loop in early epidemic (more I \u2192 more new infections) and the natural balancing loop (more R \u2192 fewer S \u2192 fewer new infections). They determine how each external control modifies these flows.",
    "lever_V": "Students build a coupled compartment model showing how Contact Rate and Transmission Rate drive the flow from Susceptible to Infected, how recovery drives the flow from Infected to Recovered, and how Vaccination Rate and Quarantine Effectiveness modify these dynamics. The model must demonstrate exponential growth, natural peak, and decline.",
    "lever_Ev": "Students run uncontrolled, early intervention, late intervention, and vaccination scenarios. They quantify the difference in total infections and peak infected population between early and late quarantine, discovering that timing is often more important than intensity in exponential systems.",
    "lever_R": "Students extend the model with Hospital Capacity (threshold effect on mortality), Asymptomatic Transmission Rate, or Reinfection Rate to explore how real-world complexity changes the basic SIR dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Network visualization of infection spreading through connected people", "say": "In December 2019, a single person in Wuhan, China had a cough. Three months later, the entire world was in lockdown. How did ONE infection become a GLOBAL pandemic?", "do": "Show a visualization of COVID-19's global spread over time. Let students react. Ask: 'What mathematical pattern could explain something spreading this fast?'", "time": "3 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals, SIR diagram, and vocabulary", "say": "Today we're building the exact type of model that scientists used to predict COVID-19's spread and to design the interventions that saved millions of lives.", "do": "Introduce the SIR framework visually. Pre-teach R\u2080 with a concrete example: 'If one person infects 3 others, and each of those infects 3 more, how many are infected after 10 rounds?' Let students calculate (59,049).", "time": "4 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does one person's infection become a global pandemic in weeks?", "say": "The answer is exponential growth. And the terrifying thing about exponential growth is that it's almost impossible for human brains to intuit. Let me show you why.", "do": "Classic doubling problem: 'If a pond has lily pads that double daily and the pond is full on day 30, when was it half full?' (Day 29.) 'When was it 1% full?' (Day 23.) This illustrates why exponential problems seem manageable until they're catastrophic.", "time": "4 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with SIR compartment overview", "say": "We're building a coupled compartment model \u2014 three population groups connected by flows that depend on each other. This is the most sophisticated model type we've built.", "do": "Draw S, I, and R boxes on the board with arrows. Ask: 'What determines how fast people move from S to I? What determines how fast they move from I to R?' Build intuition for the coupled dynamics.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards with compartment and control sorting", "say": "We have three populations that people flow between, plus external controls that modify the flows. Sort them \u2014 but think carefully about which are internal dynamics and which are human decisions.", "do": "Guide component sorting. Key insight: Susceptible, Infected, and Recovered are coupled internal compartments. Contact Rate, Vaccination Rate, and Quarantine Effectiveness are external because humans control them. Transmission Rate is internal (determined by pathogen biology).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Coupled compartment flow diagram with intervention points", "say": "Map the flows between compartments. The critical question: why does the flow from S to I depend on BOTH the number of Susceptible AND the number of Infected people?", "do": "Students map coupled flows. Emphasize: new infections require BOTH a susceptible person AND an infected person to make contact. This coupling is why the SIR model is more complex than a simple linear system. Identify where each intervention (quarantine, vaccination) modifies the system.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Epidemic curve comparisons: uncontrolled, early quarantine, late quarantine, vaccination", "say": "Four scenarios. Uncontrolled epidemic, early quarantine at 1%, late quarantine at 10%, and vaccination. Predict FIRST, then run. The timing comparison will surprise you.", "do": "Students predict outcomes before running each scenario. Key revelation: the same quarantine at 1% vs. 10% can reduce total infections by half or more. Have students calculate: if the epidemic doubles every 3 days, how many more people are infected in the 2 weeks between 1% and 10%? This quantifies the cost of delay.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with real-world COVID-19 comparisons", "say": "Your model just showed you what every epidemiologist tried to tell the world in March 2020: in exponential systems, acting one week early saves more lives than acting one month late with ten times the resources.", "do": "Connect model findings to real COVID-19 data. Compare countries that locked down early vs. late. Discuss: 'Why is it so hard for leaders to act early, when the numbers still look small?' This is the core challenge of exponential thinking.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Pandemic response decision tool design challenge", "say": "Build a tool that helps health officials make the hardest decision in public health: when to act. Your tool needs to show what happens if they act NOW versus if they wait.", "do": "Groups design decision support tools using model data. Key requirement: the tool must show the 'cost of waiting' clearly. Groups present and peer-evaluate on usability, accuracy, and decision-support value.", "time": "12 min"}
    ],
    "sort_reasoning": "Contact Rate, Vaccination Rate, and Quarantine Effectiveness are external components because they represent human decisions and interventions \u2014 we can choose to implement quarantine, vaccinate at a certain rate, or modify social behavior. Susceptible Population, Infected Population, and Recovered Population are internal because they are determined by the coupled flows between compartments. Transmission Rate is internal because it is determined by pathogen biology, not human choice (though hygiene can modify it). The key insight is that the three compartments are coupled \u2014 the flow from S to I depends on both S and I simultaneously, which is what creates exponential dynamics.",
    "relationships": [
        ("Contact Rate to Infected Population", "POSITIVE (+)", "Higher Contact Rate means each infected person encounters more susceptible people per day, increasing the rate of new infections. This is the primary target of quarantine interventions."),
        ("Susceptible Population to Infected Population", "POSITIVE (+) [Coupled]", "A larger Susceptible Population provides more potential targets for infection. As S decreases (through infection or vaccination), the rate of new infections naturally slows \u2014 this is the balancing feedback that eventually ends epidemics."),
        ("Infected Population to Susceptible Population", "NEGATIVE (-) [Coupled]", "More Infected individuals deplete the Susceptible population faster, as susceptible people become infected. This coupling means the flow rate depends on BOTH compartments simultaneously."),
        ("Infected Population to Recovered Population", "POSITIVE (+)", "More Infected individuals means more people recovering over time, increasing the Recovered population and building herd immunity."),
        ("Vaccination Rate to Susceptible Population", "NEGATIVE (-)", "Vaccination moves people directly from Susceptible to Recovered, reducing the susceptible pool without requiring infection. This is the most efficient path to herd immunity."),
        ("Quarantine Effectiveness to Contact Rate", "NEGATIVE (-)", "Higher Quarantine Effectiveness reduces the effective Contact Rate, lowering R\u2080 and slowing transmission. This intervention modifies the system's behavior without changing the pathogen itself."),
        ("Transmission Rate to Infected Population", "POSITIVE (+)", "Higher Transmission Rate means each contact is more likely to result in infection, increasing the flow from S to I and driving higher R\u2080.")
    ],
    "sim_answers": [
        ("Uncontrolled Epidemic Scenario", "Without intervention, the epidemic follows a classic bell curve. Infected Population grows exponentially as the large Susceptible Population provides abundant targets. The curve peaks when enough people have been infected and recovered that the Susceptible pool is depleted below the herd immunity threshold. The epidemic then declines naturally. However, the peak is extremely high \u2014 potentially overwhelming healthcare systems \u2014 and the total infected population reaches 60-80% before the epidemic ends."),
        ("Early vs. Late Quarantine Comparison", "Quarantine at 1% infection dramatically reduces both the peak Infected Population and total infections. Because the intervention is applied when exponential growth is still in its early stages, it prevents the massive amplification that occurs in the following weeks. The same quarantine at 10% infection has much less impact because the base of active infections is already 10x larger, and exponential growth has already generated enormous momentum. The model demonstrates that in exponential systems, early action is exponentially more effective than delayed action."),
        ("Vaccination Scenario", "Vaccination steadily reduces the Susceptible Population, moving people to Recovered without illness. This has two effects: it directly prevents those individuals from getting sick, and it reduces the pool of susceptible contacts available to infected people, lowering the effective R\u2080. When enough people are vaccinated to cross the herd immunity threshold, the epidemic cannot sustain transmission and collapses. Vaccination combined with early quarantine produces the best outcome.")
    ],
    "reflection_exemplars": [
        ("Why does timing matter so much in exponential systems?", "In exponential growth, the infected population doubles at regular intervals. Intervening when there are 1,000 cases prevents the doubling to 2,000, then 4,000, then 8,000. Waiting until there are 10,000 cases means the same intervention must prevent 20,000, then 40,000, then 80,000 new cases from a much larger base. The same action applied one week earlier in an exponential system can prevent more total infections than applying it later with much greater intensity. This is why public health experts emphasize speed over perfection in pandemic response."),
        ("How does the SIR model's natural balancing feedback eventually end an epidemic?", "The natural balancing feedback works through depletion: as people get infected and recover, they move from Susceptible to Recovered. Each recovery reduces the pool of people who can be infected. When the Susceptible population drops below the herd immunity threshold, each infected person infects fewer than one new person on average (R < 1), and the epidemic declines. However, this 'natural' end comes at enormous cost \u2014 it requires 60-80% of the population to be infected first. Vaccination achieves the same herd immunity without the disease, which is why it's the most important public health tool in the model.")
    ],
    "stem_intro": "Present the challenge: A county health department needs a real-time decision support tool for pandemic response. The tool must show where the epidemic currently stands (which phase of the SIR curve), project outcomes under different intervention strategies, and clearly communicate the cost of delayed action. Your model data is the foundation \u2014 translate it into a tool that saves lives by helping officials act faster.",
    "stem_concepts": [
        ("Coupled Compartment Dynamics", "The SIR model's compartments are coupled because the flow between them depends on the state of multiple compartments simultaneously. New infections require both a susceptible person and an infected person, making the transmission rate proportional to S \u00d7 I. This coupling is what produces exponential growth when S is large."),
        ("Exponential Growth and Intervention Timing", "In exponential systems, the current size of the problem determines the rate of growth. Acting when the problem is small prevents vastly more damage than acting when it's large, because every doubling period that passes without intervention doubles the total burden."),
        ("Herd Immunity as System Threshold", "Herd immunity is the threshold where the effective R drops below 1 and the epidemic cannot sustain transmission. It can be reached through infection (costly) or vaccination (efficient). The threshold value depends on R\u2080: more transmissible diseases require higher immunity levels to stop.")
    ],
    "stem_eval": [
        ("Expert (4)", "Tool clearly shows current epidemic phase, projects multiple intervention scenarios with timing comparisons, communicates the cost of delay quantitatively, and helps officials make evidence-based decisions under uncertainty"),
        ("Proficient (3)", "Tool accurately represents SIR dynamics, shows intervention comparisons, and communicates urgency of early action"),
        ("Developing (2)", "Tool shows some epidemic curve concepts but lacks clear intervention timing comparisons or decision-support features"),
        ("Beginning (1)", "Tool is incomplete or does not accurately represent SIR dynamics or intervention effects")
    ],
    "support": [
        "Provide pre-drawn SIR compartment diagrams with labeled arrows that students can annotate",
        "Use a physical demonstration: pass a ball (infection) around a circle of students, removing students who 'recover' to show how the susceptible pool shrinks",
        "Sentence frames: 'When [intervention] is implemented at [timing], R\u2080 changes from ___ to ___ because ___'",
        "Scaffolded epidemic curve templates where students plot predictions before running simulations"
    ],
    "extensions": [
        "Research COVID-19 R\u2080 values for different variants and model how increased transmissibility changes epidemic outcomes",
        "Extend the model to SEIR (adding an Exposed compartment with incubation period) and compare dynamics to basic SIR",
        "Analyze real-world data comparing countries with early vs. late pandemic responses and validate against model predictions",
        "Model the emergence of vaccine-resistant variants by adding a reinfection pathway from R back to S"
    ],
    "cross_curr": [
        ("Math", "Derive the herd immunity threshold formula (1 - 1/R\u2080) and calculate thresholds for diseases with different R\u2080 values. Create exponential growth projections for the first 30 days of an uncontrolled epidemic."),
        ("ELA", "Write a crisis communication press release for a health department announcing pandemic interventions, using model evidence to justify the timing and intensity of the response."),
        ("Social Studies", "Research how socioeconomic factors (housing density, healthcare access, essential worker status) create unequal pandemic impacts and analyze whose R\u2080 is effectively higher.")
    ],
    "misconceptions": [
        ("Pandemics grow at the same rate throughout", "Pandemics do NOT grow at a constant rate. They grow exponentially at first (when the susceptible pool is large), reach a peak, then decline as the susceptible population is depleted. The epidemic curve is bell-shaped, not linear. The model shows this clearly: the growth rate depends on the SIZE of both the Susceptible and Infected populations, which change over time.", "Draw a bell curve and ask: 'Why doesn't the epidemic keep growing forever? What resource runs out?' Answer: susceptible people. As more people get infected and recover, there are fewer people left to infect."),
        ("Quarantine and vaccination do the same thing", "Quarantine and vaccination work on DIFFERENT components of the SIR model. Quarantine reduces the Contact Rate \u2014 it doesn't change who's susceptible, but it reduces how often susceptible and infected people interact. Vaccination reduces the Susceptible Population \u2014 it moves people directly to Recovered without infection. Quarantine is temporary and must be maintained; vaccination is permanent (for that individual). Both reduce R\u2080, but through entirely different mechanisms.", "Draw the SIR diagram. Show where quarantine acts (the arrow between S and I, reducing contact) vs. where vaccination acts (moving people from S to R directly). They modify different parts of the system."),
        ("Herd immunity means nobody gets sick", "Herd immunity doesn't mean zero infections \u2014 it means sustained TRANSMISSION stops. Once enough people are immune, each infected person infects fewer than one new person on average, and chains of transmission die out. But individuals can still get infected; they just don't spark chain reactions. Herd immunity protects the POPULATION, not every individual.", "Analogy: Fire breaks in a forest don't prevent all trees from burning, but they prevent a small fire from becoming a wildfire by removing enough fuel (susceptible trees) to stop the fire from spreading indefinitely.")
    ]
}



L04 = {
    "id": "G09L2-L04",
    "title": "The Opioid Epidemic: When Medicine Becomes the Disease",
    "subtitle": "Modeling Neurochemical Feedback Loops in Addiction",
    "ngss": "HS-LS1-2, HS-ETS1-4",
    "ngss_desc": "Develop and use a model to illustrate the hierarchical organization of interacting systems. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem.",
    "big_question": "How does a pill prescribed by a doctor become the deadliest drug epidemic in American history?",
    "objectives": [
        "Model how opioid tolerance develops through neurochemical feedback loops that drive dose escalation",
        "Analyze the threshold dynamics that shift a patient from pain management to physical dependence",
        "Evaluate how social network effects amplify the epidemic beyond individual neurochemistry",
        "Design intervention strategies that target different components of the addiction feedback system"
    ],
    "vocabulary": [
        ("Tolerance", "A neurological adaptation where repeated opioid exposure reduces receptor sensitivity, requiring progressively higher doses to achieve the same effect"),
        ("Dependence", "A physiological state where the brain has adapted to constant opioid presence and cannot function normally without them"),
        ("Dopamine Receptor Downregulation", "The brain reduces the number or sensitivity of dopamine receptors in response to chronic overstimulation"),
        ("Withdrawal", "Severe physical and psychological symptoms that occur when opioid-dependent individuals stop taking the drug abruptly")
    ],
    "components": [
        ("Prescription Rate", "The frequency and dosage of opioid prescriptions in a community", True),
        ("Tolerance Development", "The progressive decrease in opioid effectiveness as brain receptors adapt", False),
        ("Addiction Level", "The degree of compulsive drug-seeking behavior driven by neurochemical dependence", False),
        ("Dopamine Receptor Sensitivity", "The responsiveness of the brain reward system, which decreases with chronic exposure", False),
        ("Social Network Exposure", "The probability of encountering opioids through community connections", True),
        ("Pain Threshold", "The pain tolerance level, which paradoxically decreases with chronic opioid use", False),
        ("Withdrawal Severity", "The intensity of symptoms when opioid levels drop below the adapted baseline", False)
    ],
    "think_about_it": "When Tolerance Development increases, what happens to the effective dose needed? How does this create a reinforcing feedback loop with Addiction Level?",
    "scenarios": [
        ("Short-Term Prescription", "Set Prescription Rate to moderate briefly then stop -- observe whether dependence develops"),
        ("Chronic High-Dose Use", "Set Prescription Rate to high and maintain -- track tolerance-driven dose escalation"),
        ("Community Spread", "Start with one high Prescription Rate individual and observe Social Network Exposure propagation")
    ],
    "sim_scenarios": [
        ("Short-Term Use", "Moderate prescription, 2-week duration", "What happens to Dopamine Receptor Sensitivity after a short prescription?"),
        ("Chronic Escalation", "High prescription maintained over months", "At what point does Tolerance make the original dose ineffective?"),
        ("Network Effects", "One prescription feeds social exposure", "How does one person's leftover pills create new users?")
    ],
    "discoveries": [
        "Opioid tolerance creates a reinforcing feedback loop: reduced sensitivity requires higher dose which causes faster adaptation",
        "There is a neurochemical threshold past which dependence becomes physiological",
        "Chronic opioid use paradoxically INCREASES pain sensitivity via hyperalgesia",
        "Social network effects amplify a medical problem into an epidemic"
    ],
    "answer": "A doctor prescribes opioids for pain. The brain adapts through tolerance as receptors become less sensitive, requiring higher doses. This triggers a reinforcing feedback loop. Past the dependence threshold, the brain is physically rewired. When prescriptions end, withdrawal drives patients to seek opioids elsewhere. Unused pills enter social networks creating new exposures. One prescription becomes a community epidemic through cascading feedback loops.",
    "stem_title": "Design an Opioid Crisis Intervention Dashboard",
    "stem_mission": "Design a data-driven intervention system that identifies at-risk communities and recommends targeted interventions at different crisis stages.",
    "stem_scenario": "A state health department has $50 million to combat the opioid crisis. Your team must design a dashboard that identifies which communities need which interventions based on real-time data.",
    "stem_questions": [
        "Which data indicators signal early vs. advanced stages of an opioid crisis?",
        "How would you prioritize interventions when budgets are limited?",
        "At what point in the feedback loop is intervention most cost-effective?"
    ],
    "stem_design_qs": [
        "What data sources would feed your dashboard?",
        "How would you visualize risk levels for decision-makers?",
        "How would you account for the lag between prescription changes and overdose outcomes?",
        "How would you measure whether your intervention is working?"
    ],
    "career": "Epidemiologists study disease spread through populations, tracking prescription patterns and intervention effectiveness, earning $60,000-$120,000/year at CDC, state health departments, and universities.",
    "images": {
        "cover": ("G09L2-L04-cover.png", "A photorealistic cinematic image of a medicine cabinet with prescription bottles casting dramatic shadows, pills on counter, family photo blurred in background"),
        "landscape": ("G09L2-L04-landscape.png", "Diverse 14-15 year old students examining brain scan images on monitors showing dopamine receptor activity in a modern neuroscience lab"),
        "modeling": ("G09L2-L04-modeling.png", "Diverse 14-15 year old students at computers building computational models of addiction feedback loops with flow diagrams on screens"),
        "discussion": ("G09L2-L04-discussion.png", "A teacher leading a sensitive discussion with diverse 14-15 year old students about neuroscience of addiction, brain diagram on smartboard"),
        "stem": ("G09L2-L04-stem.png", "Diverse 14-15 year old students designing a community health dashboard on large monitors with maps and data visualizations")
    },
    "pre_assessment": [
        "Why do you think some people become addicted to prescription painkillers while others do not?",
        "What do you think happens in the brain when someone takes an opioid repeatedly?",
        "Draw a diagram showing how a person goes from taking medicine for pain to being unable to stop.",
        "What does tolerance mean in the context of drug use, and why is it dangerous?"
    ],
    "extend_components": [
        ("Naloxone Availability", "Accessibility of opioid overdose reversal medication, which saves lives but does not address underlying addiction"),
        ("Medication-Assisted Treatment Access", "Availability of evidence-based treatments like methadone and buprenorphine"),
        ("Illicit Fentanyl Contamination", "Presence of ultra-potent synthetic fentanyl in the drug supply, dramatically increasing overdose risk")
    ],
    "reflections": [
        "How does your model demonstrate that addiction is a neurochemical process rather than a moral failing?",
        "At what point in the feedback loop would intervention be most effective and why?",
        "How do social network effects transform an individual problem into a community epidemic?",
        "What are the ethical implications of modeling addiction?",
        "How does opioid-induced hyperalgesia create a particularly cruel feedback loop?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students build multi-feedback-loop models of neurochemical tolerance, dependence, and social network epidemic effects."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "The brain dopamine reward system adapts to chronic opioid exposure through receptor downregulation."),
        ("Crosscutting Concept", "Cause and Effect: Mechanism and Prediction", "Students trace the causal chain from prescription to dependence to epidemic, identifying threshold effects.")
    ],
    "cast_items": [
        "Model how neurochemical feedback loops drive opioid tolerance and dose escalation",
        "Analyze threshold dynamics that determine the transition from use to dependence",
        "Evaluate intervention strategies targeting different stages of the addiction feedback system"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Which feedback loop is MOST responsible for driving dose escalation?"),
        ("Constructed Response:", "Explain why a patient on opioids for 6 months faces a fundamentally different neurochemical situation than one on them for 2 weeks.")
    ],
    "background_intro": "The opioid epidemic has killed over 500,000 Americans since 1999. Understanding how prescribed medicine becomes lethal addiction requires modeling neurochemical feedback loops that hijack the brain reward system.",
    "background_sections": [
        ("The Neurochemistry of Tolerance", "Opioids bind to mu-opioid receptors, triggering dopamine release. With repeated exposure, the brain reduces receptor number and sensitivity. This is tolerance: the same dose produces less effect."),
        ("The Dependence Threshold", "After sufficient exposure, the brain baseline neurochemistry shifts. It now REQUIRES opioids to function normally. Without them, severe withdrawal occurs."),
        ("Opioid-Induced Hyperalgesia", "Chronic opioid use can paradoxically INCREASE pain sensitivity. The brain compensates by amplifying pain signals, creating a second feedback loop."),
        ("The Social Network Effect", "Leftover pills became community exposure vectors. When prescriptions tightened, demand shifted to illicit heroin and fentanyl.")
    ],
    "lever_L": "Students identify the 7 interacting components of the opioid crisis system.",
    "lever_E": "Students map multiple feedback loops: tolerance-dose escalation, hyperalgesia-pain-use, and social exposure-new users.",
    "lever_V": "Students build a computational model with 7 components, identifying reinforcing loops and thresholds.",
    "lever_Ev": "Students run short-term, chronic, and community-spread scenarios to test intervention timing.",
    "lever_R": "Students add naloxone, MAT, or fentanyl contamination to model real-world interventions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Prescription bottles image", "say": "Every day, 130 Americans die from opioid overdose. Most started with a doctor prescription.", "do": "Show the statistic. Establish safe, scientific frame.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Goals and vocabulary", "say": "Today we model what happens in the brain with repeated opioid exposure. Neuroscience, not moral judgment.", "do": "Pre-teach tolerance, dependence, receptor downregulation.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does medicine become an epidemic?", "say": "Doctors prescribed these drugs to help. How did helping become harming?", "do": "Quick-write: What do you know about the opioid crisis?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "This model has MULTIPLE feedback loops. That makes it Level 2.", "do": "Preview: 7 components, multiple reinforcing loops, threshold effects.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "7 component cards", "say": "Which can doctors or policymakers control? Which are internal brain processes?", "do": "Guide sorting of external vs internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect", "visual": "Multi-loop diagram", "say": "This system has at least THREE reinforcing feedback loops. Find them.", "do": "Identify tolerance loop, hyperalgesia loop, social spread loop.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulate", "visual": "Scenarios", "say": "Find the dependence threshold. When does the brain cross the point of no return?", "do": "Students run scenarios and identify threshold transitions.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Your model shows why addiction is a disease, not a choice.", "do": "Evidence-based discussion connecting model to real data.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Dashboard design", "say": "You have $50 million for a state in crisis. Where do you invest?", "do": "Groups design dashboards. Justify with model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Prescription Rate and Social Network Exposure are external because they are modifiable by policy. Tolerance, Addiction Level, Dopamine Sensitivity, Pain Threshold, and Withdrawal Severity are internal neurochemical responses.",
    "relationships": [
        ("Prescription Rate to Tolerance", "POSITIVE (+)", "Higher prescriptions mean more exposure, accelerating tolerance."),
        ("Tolerance to Addiction Level", "POSITIVE (+)", "Higher tolerance requires higher doses, deepening dependence."),
        ("Addiction to Dopamine Sensitivity", "NEGATIVE (-)", "Increasing addiction drives receptor downregulation."),
        ("Dopamine Sensitivity to Tolerance", "NEGATIVE (-)", "Less sensitive receptors mean same dose does less, driving tolerance up."),
        ("Addiction to Pain Threshold", "NEGATIVE (-)", "Chronic use causes hyperalgesia, lowering pain threshold."),
        ("Pain Threshold to Prescription Rate", "NEGATIVE (-)", "Lower pain thresholds drive patients to seek more medication."),
        ("Social Exposure to Addiction", "POSITIVE (+)", "Greater community exposure increases non-medical use."),
        ("Addiction to Withdrawal Severity", "POSITIVE (+)", "Deeper addiction produces more severe withdrawal.")
    ],
    "sim_answers": [
        ("Short-Term Scenario", "With moderate prescription over 2 weeks, Tolerance begins mildly. Dopamine Sensitivity recovers after cessation. System returns to baseline."),
        ("Chronic Scenario", "With sustained high-dose use, tolerance-addiction loop accelerates. System crosses dependence threshold around 4-8 weeks. Stopping produces severe withdrawal.")
    ],
    "reflection_exemplars": [
        ("Why is addiction a disease?", "The model shows addiction involves physical rewiring. Tolerance and dependence are automatic biological processes. Once the threshold is crossed, medical intervention is needed."),
        ("Where is intervention most effective?", "Early intervention before the dependence threshold is vastly more effective. Once past the threshold, medication-assisted treatment is required.")
    ],
    "stem_intro": "A state health department needs a data-driven system to allocate its opioid crisis budget across communities at different epidemic stages.",
    "stem_concepts": [
        ("Epidemiological Surveillance", "Real-time monitoring of prescription rates, ER visits, overdose deaths identifies communities at different stages."),
        ("Intervention Staging", "Prevention works early; treatment works mid-stage; harm reduction works late-stage."),
        ("Feedback-Informed Allocation", "Understanding feedback loops predicts which communities escalate fastest.")
    ],
    "stem_eval": [
        ("Expert (4)", "Dashboard integrates multiple data streams, stages communities, recommends interventions with model evidence"),
        ("Proficient (3)", "Dashboard identifies risk levels, recommends interventions with model support"),
        ("Developing (2)", "Dashboard shows indicators but lacks clear connection to epidemic stage"),
        ("Beginning (1)", "Dashboard is incomplete or disconnected from the addiction model")
    ],
    "support": [
        "Pre-drawn diagram showing three feedback loops with labeled arrows",
        "Thermostat analogy: brain tries to maintain normal but the definition keeps shifting",
        "Sentence frames: When __ increases past the threshold, __ shifts because the feedback loop __"
    ],
    "extensions": [
        "Research medication-assisted treatment and model how methadone affects tolerance and withdrawal components",
        "Investigate pharmaceutical marketing role in setting initial Prescription Rates",
        "Compare the US opioid epidemic to the 19th-century opium crisis in China"
    ],
    "cross_curr": [
        ("Math", "Calculate exponential growth of opioid prescriptions 1999-2012 and model overdose deaths as a lagged function."),
        ("ELA", "Write a first-person narrative of prescription-to-dependence journey using the neurochemical model."),
        ("Social Studies", "Research Purdue Pharma and analyze how corporate decisions affected the Prescription Rate component nationally.")
    ],
    "misconceptions": [
        ("Addiction is a moral failure", "The feedback model shows addiction is a predictable neurochemical outcome. Past the dependence threshold, willpower cannot override altered neurochemistry.", "Ask: Does it take willpower to digest food? Tolerance and dependence are equally automatic."),
        ("Only certain people become addicted", "Anyone with a brain can develop dependence. The variables are dosage, duration, and genetics, not character.", "The opioid crisis affected every demographic equally. The feedback loop does not check your resume."),
        ("People take opioids to get high", "Past the dependence threshold, people take opioids to avoid feeling terrible, not to feel good. Motivation shifts from reward-seeking to punishment-avoidance.", "If someone needs insulin to function, are they taking it to get high?")
    ]
}

L05 = {
    "id": "G09L2-L05",
    "title": "Coral Reef Collapse: Death of an Underwater City",
    "subtitle": "Modeling Cascading Ecosystem Failure Through Coupled Feedback Loops",
    "ngss": "HS-LS2-6, HS-ESS3-3",
    "ngss_desc": "Evaluate claims, evidence, and reasoning that complex interactions in ecosystems maintain relatively consistent numbers and types of organisms. Create a computational simulation of a natural system.",
    "big_question": "How can a 1 degree C temperature change destroy an ecosystem that took 10,000 years to build?",
    "objectives": [
        "Model the coupled feedback loops between coral bleaching, algae overgrowth, and fish population collapse",
        "Analyze threshold dynamics that determine whether a reef can recover or crosses the point of no return",
        "Evaluate how multiple stressors interact to amplify ecosystem collapse",
        "Design reef restoration strategies that target the most effective leverage points"
    ],
    "vocabulary": [
        ("Coral Bleaching", "The expulsion of symbiotic zooxanthellae from coral tissue due to thermal stress, depriving coral of its primary energy source"),
        ("Zooxanthellae", "Photosynthetic dinoflagellates living within coral tissue providing up to 90 percent of the coral energy through photosynthesis"),
        ("Phase Shift", "An ecosystem state change from coral-dominated to algae-dominated that is extremely difficult to reverse once established"),
        ("Biogeochemical Coupling", "The interconnection between biological and chemical processes in reef systems")
    ],
    "components": [
        ("Ocean Temperature", "Sea surface temperature in the reef zone, triggering bleaching above a critical threshold", True),
        ("Coral Bleaching Rate", "Percentage of coral colonies expelling zooxanthellae per unit time", False),
        ("Algae Overgrowth", "Rate at which macroalgae colonize dead or weakened coral surfaces", False),
        ("Fish Population", "Abundance of herbivorous fish that graze algae and keep it from smothering coral", False),
        ("Water Acidity", "Ocean pH level, which decreases as CO2 is absorbed, hindering coral skeleton building", True),
        ("Symbiotic Zooxanthellae", "Density of photosynthetic symbionts within coral tissue providing energy", False),
        ("Reef Structural Integrity", "Physical framework strength providing habitat and coastal buffering", False)
    ],
    "think_about_it": "When Ocean Temperature rises and Coral Bleaching increases, what happens to Zooxanthellae? Without them, what happens to coral energy? If coral dies, where do fish go? Without fish, what happens to algae?",
    "scenarios": [
        ("Mild Warming", "Raise temperature 0.5 C for one season then return to normal -- observe recovery"),
        ("Sustained Warming", "Raise temperature 1.5 C and maintain -- track cascade to phase shift"),
        ("Combined Stressors", "Raise temperature AND acidity while reducing fish -- observe multiplicative effects")
    ],
    "sim_scenarios": [
        ("Mild Warming", "Temperature +0.5 C for one season", "Can coral recover if temperature returns to normal?"),
        ("Sustained Warming", "Temperature +1.5 C maintained", "At what point does bleaching become irreversible?"),
        ("Triple Threat", "Temperature +1 C, acidity +0.1 pH, high fishing", "Are 3 small problems worse than 1 big one?")
    ],
    "discoveries": [
        "Coral bleaching creates a cascading feedback loop from heat through starvation to permanent phase shift",
        "There is a temperature threshold beyond which bleaching accelerates faster than recovery",
        "Multiple moderate stressors can trigger collapse when no single stressor alone would be sufficient",
        "The phase shift to algae dominance represents a stable alternative state that persists even after stress removal"
    ],
    "answer": "A 1 degree change triggers cascading coupled feedback loops. Thermal stress causes coral to expel zooxanthellae. Without photosynthetic partners, coral loses 90 percent of its energy and dies. Dead surfaces are colonized by algae. As reef structure degrades, herbivorous fish lose habitat. Without fish, algae smother remaining coral. The system reaches a phase shift -- a new algae-dominated state that is self-reinforcing even if temperatures normalize.",
    "stem_title": "Design a Reef Resilience Monitoring System",
    "stem_mission": "Design a monitoring system that detects early warnings of reef collapse and triggers interventions before the phase shift becomes irreversible.",
    "stem_scenario": "The Great Barrier Reef has experienced three mass bleaching events in five years. Design an early-warning system that predicts which reef sections are approaching the tipping point.",
    "stem_questions": [
        "What indicators serve as earliest warnings of approaching phase shift?",
        "How would you distinguish a recoverable reef from one past the tipping point?",
        "Which interventions are most effective at which stages of decline?"
    ],
    "stem_design_qs": [
        "What sensors and monitoring technologies would you deploy?",
        "How would you build a predictive model for at-risk reef sections?",
        "How would you triage interventions across hundreds of sections?",
        "How would you validate your interventions are preventing phase shifts?"
    ],
    "career": "Marine Ecologists study ocean ecosystem dynamics and conservation, working for NOAA, marine parks, and environmental NGOs, earning $55,000-$110,000/year.",
    "images": {
        "cover": ("G09L2-L05-cover.png", "A photorealistic split-image showing vibrant colorful coral reef on left transitioning to bleached white coral reef on right, dramatic underwater lighting"),
        "landscape": ("G09L2-L05-landscape.png", "Diverse 14-15 year old students examining coral samples and marine data on monitors in a marine biology classroom"),
        "modeling": ("G09L2-L05-modeling.png", "Diverse 14-15 year old students at computers building coral reef ecosystem models with interconnected diagrams"),
        "discussion": ("G09L2-L05-discussion.png", "A teacher leading discussion with diverse students about ecosystem tipping points, before-and-after reef photos on smartboard"),
        "stem": ("G09L2-L05-stem.png", "Diverse students designing reef monitoring systems with sensors, maps, and data visualizations at lab tables")
    },
    "pre_assessment": [
        "What causes coral to turn white and why is that a problem?",
        "How can a tiny temperature change destroy an entire ecosystem?",
        "Draw a diagram showing relationships between coral, algae, fish, and water temperature.",
        "What does tipping point mean in an ecosystem?"
    ],
    "extend_components": [
        ("Coral Recruitment Rate", "Rate at which new coral larvae settle and grow, determining reef regeneration ability"),
        ("Sedimentation Rate", "Amount of sediment from coastal development that smothers coral and blocks light"),
        ("Marine Protected Area Coverage", "Percentage of reef protected from fishing and development")
    ],
    "reflections": [
        "How does your model demonstrate that reef collapse is a cascading system failure?",
        "Why is the phase shift so difficult to reverse even if temperatures stabilize?",
        "How do multiple moderate stressors interact differently than a single severe stressor?",
        "What does your model suggest about conservation vs. restoration?",
        "How might reef loss affect coastal human communities?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students use computational models to simulate threshold dynamics and phase shifts in a coupled ecosystem."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Coral reef stability depends on mutualistic relationships, trophic cascades, and structural integrity that can fail catastrophically."),
        ("Crosscutting Concept", "Stability and Change", "Students model how stable ecosystems undergo rapid irreversible phase shifts when feedback loops push past tipping points.")
    ],
    "cast_items": [
        "Model cascading feedback loops from thermal stress through bleaching to ecosystem phase shift",
        "Analyze how coupled stressors interact to lower the collapse threshold",
        "Evaluate intervention strategies targeting different components and stages"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Which scenario is MOST likely to cause irreversible phase shift: (a) single +2 C event, (b) three +1 C events with moderate overfishing, (c) moderate acidification alone, (d) heavy fishing alone?"),
        ("Constructed Response:", "Explain why restoring a phase-shifted reef requires interventions on MULTIPLE components simultaneously.")
    ],
    "background_intro": "Coral reefs cover less than 1 percent of the ocean but support 25 percent of all marine species. Understanding collapse requires modeling coupled feedback between thermal stress, symbiosis, trophic interactions, and ocean chemistry.",
    "background_sections": [
        ("The Coral-Zooxanthellae Symbiosis", "Zooxanthellae provide up to 90 percent of coral energy through photosynthesis. When thermal stress disrupts the partnership, the coral loses its energy source AND its color."),
        ("Thermal Stress Thresholds", "A rise of just 1 C above summer peak for 4+ weeks triggers bleaching. If brief, recovery occurs in 6-12 months. If prolonged, coral starves and dies."),
        ("The Phase Shift Cascade", "Dead coral is colonized by algae. If algae outpaces fish grazing, it smothers remaining coral and prevents larvae settlement, creating a self-reinforcing algae state."),
        ("Ocean Acidification Coupling", "CO2 acidifies ocean water, weakening coral skeletons AND lowering the temperature threshold for bleaching. The two stressors are multiplicative.")
    ],
    "lever_L": "Students identify the 7 interacting reef system components.",
    "lever_E": "Students map cascading feedback loops through thermal, chemical, and biological pathways.",
    "lever_V": "Students build a model showing how coupled stressors cascade to produce phase shift.",
    "lever_Ev": "Students run mild, sustained, and combined-stressor scenarios to identify thresholds.",
    "lever_R": "Students add coral recruitment, sedimentation, or marine protection to explore intervention strategies.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split healthy/bleached reef", "say": "This reef took 10,000 years to grow. It died in 10 years.", "do": "Show before/after images.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Goals and vocabulary", "say": "Today we model the coupled feedback loops that make reefs both productive and fragile.", "do": "Pre-teach zooxanthellae and phase shift.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does 1 C destroy a 10,000-year ecosystem?", "say": "Your body at 37 C is fine. At 40 C your organs fail. Corals are the same.", "do": "Quick-write: How many connections can you identify?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "Seven components with cascading connections.", "do": "Preview coupled biological + chemical + structural pathways.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "7 component cards", "say": "Which can humans directly control?", "do": "Temperature and acidity are external; rest are ecological responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect", "visual": "Cascading diagram", "say": "Two pathways to destruction -- thermal and chemical -- and they INTERACT.", "do": "Map both pathways. Show how acidification lowers bleaching threshold.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulate", "visual": "Three scenarios", "say": "Is one big problem worse than three small ones?", "do": "Students discover combined stressors exceed single severe stressor.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Phase shift diagram", "say": "Once the phase shift happens, there is no going back.", "do": "Discuss irreversibility and climate urgency.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Monitoring system design", "say": "You are chief scientist for the Great Barrier Reef. What is your plan?", "do": "Groups design monitoring and intervention systems.", "time": "12 min"}
    ],
    "sort_reasoning": "Ocean Temperature and Water Acidity are external inputs driven by human carbon emissions. Bleaching Rate, Algae Overgrowth, Fish Population, Zooxanthellae, and Structural Integrity are internal ecological responses.",
    "relationships": [
        ("Ocean Temperature to Bleaching Rate", "POSITIVE (+)", "Higher temperatures trigger thermal stress and bleaching."),
        ("Bleaching Rate to Zooxanthellae", "NEGATIVE (-)", "Bleaching expels zooxanthellae from coral tissue."),
        ("Zooxanthellae to Structural Integrity", "POSITIVE (+)", "Healthy symbionts provide energy for coral growth and skeleton maintenance."),
        ("Structural Integrity to Fish Population", "POSITIVE (+)", "Reef structure provides habitat for herbivorous fish."),
        ("Fish Population to Algae Overgrowth", "NEGATIVE (-)", "Herbivorous fish graze algae, preventing smothering."),
        ("Algae Overgrowth to Bleaching Rate", "POSITIVE (+)", "Algae smother coral, adding stress that accelerates death."),
        ("Water Acidity to Structural Integrity", "NEGATIVE (-)", "Acidification weakens coral skeletons."),
        ("Water Acidity to Bleaching Rate", "POSITIVE (+)", "Acidification lowers the temperature threshold for bleaching.")
    ],
    "sim_answers": [
        ("Mild Warming", "A 0.5 C increase causes mild bleaching. When temperature normalizes, zooxanthellae recolonize over 6-12 months. The system demonstrates resilience and returns to coral-dominated state."),
        ("Combined Stressors", "Temperature, acidity, and fishing each lower thresholds for the others. The cascade accelerates dramatically. The reef crosses phase-shift threshold in half the time of temperature alone. 1+1+1 is greater than 3.")
    ],
    "reflection_exemplars": [
        ("Why is the phase shift hard to reverse?", "Algae create self-reinforcing conditions. They smother coral larvae, preventing settlement. Without coral, reef erodes, losing fish habitat. Without fish, algae grow unchecked. Even if temperature normalizes, the algae state persists."),
        ("How do stressors interact?", "Stressors interact multiplicatively. Acidification lowers the bleaching threshold. Overfishing removes algae control. Three moderate stressors together can push the system past its tipping point when none alone would.")
    ],
    "stem_intro": "The Great Barrier Reef needs an early-warning and intervention system after three mass bleaching events in five years.",
    "stem_concepts": [
        ("Remote Sensing", "Satellite thermal imaging detects temperature anomalies. Underwater sensors measure pH and dissolved oxygen. AI assesses coral cover."),
        ("Tipping Point Indicators", "Early warnings include stress markers, declining herbivore abundance, and increasing algae colonization."),
        ("Intervention Triage", "Not all sections can be saved. Triage prioritizes sections not yet past the tipping point with high biodiversity value.")
    ],
    "stem_eval": [
        ("Expert (4)", "System integrates multiple technologies, uses model-derived indicators, implements triage framework, and includes effectiveness measures"),
        ("Proficient (3)", "System monitors key indicators, identifies at-risk sections, recommends appropriate interventions"),
        ("Developing (2)", "System monitors some indicators but does not clearly distinguish recoverable from shifted sections"),
        ("Beginning (1)", "System is incomplete or disconnected from the reef model")
    ],
    "support": [
        "Pre-drawn cascade diagram showing thermal and chemical pathways converging",
        "Jenga tower analogy: each stressor removes a block until critical threshold",
        "Sentence frames: When stressor increases, component responds by __, triggering __ in the next component"
    ],
    "extensions": [
        "Research coral assisted evolution -- breeding heat-tolerant strains -- and model how this changes the temperature threshold",
        "Investigate bright spots -- reefs healthy despite stressors -- and analyze what explains their resilience",
        "Model the economic cascade: reef collapse to tourism loss to coastal erosion to property damage"
    ],
    "cross_curr": [
        ("Math", "Calculate compound stressor effects: if temperature causes 20 percent bleaching and acidity causes 15 percent alone but 50 percent together, what is the interaction coefficient?"),
        ("ELA", "Write a scientific policy brief arguing for emergency reef protection funding using model evidence."),
        ("Social Studies", "Research how Indigenous Australian communities managed reef resources for 60,000 years and compare to modern management.")
    ],
    "misconceptions": [
        ("Bleaching means coral is dead", "Bleaching is stress, not death. Coral is alive but starving. If stress is removed within weeks, zooxanthellae recolonize. Death occurs with prolonged bleaching.", "Timeline: Healthy > Bleached (alive, recoverable) > Dead (irreversible). At which stage can we still intervene?"),
        ("If we stop warming reefs will recover", "Stopping warming is necessary but not sufficient after a phase shift. Algae maintain dominance through their own feedback loops. Recovery requires active multi-component intervention.", "If a house burns down and you put out the fire, do you have a house? Stopping warming is putting out the fire. Restoration is rebuilding."),
        ("Reefs will migrate to cooler water", "Reef migration is not feasible. Reefs need specific conditions and centuries to build structure. Warming rates are 50-100x faster than natural migration.", "Can you move a 500-year-old forest? Reefs face the same timescale problem.")
    ]
}

L06 = {
    "id": "G09L2-L06",
    "title": "The Water-Energy-Food Nexus: Three Crises, One System",
    "subtitle": "Modeling Coupled Resource Systems Under Population Pressure",
    "ngss": "HS-ESS3-4, HS-ETS1-2",
    "ngss_desc": "Evaluate or refine a technological solution that reduces impacts of human activities on natural systems. Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems.",
    "big_question": "Why does solving one resource crisis often make another worse?",
    "objectives": [
        "Model how water, energy, and food production systems are interconnected through feedback loops",
        "Analyze trade-offs that occur when optimizing one resource at the expense of others",
        "Evaluate how population growth amplifies stress across all three coupled systems",
        "Design sustainable resource management strategies that balance competing demands"
    ],
    "vocabulary": [
        ("Nexus Thinking", "An analytical approach that considers the interconnections between water, energy, and food systems rather than managing them in isolation"),
        ("Resource Trade-off", "A situation where increasing the supply of one resource requires consuming more of another, creating competition between systems"),
        ("Carrying Capacity", "The maximum population that a region can sustain given its water, energy, and food production capabilities"),
        ("Circular Economy", "An economic system that minimizes waste by recycling outputs from one process as inputs to another")
    ],
    "components": [
        ("Water Availability", "Total freshwater accessible for human use from rivers, aquifers, and reservoirs", True),
        ("Energy Production", "Total energy generated from all sources including fossil fuels, nuclear, and renewables", False),
        ("Agricultural Output", "Total food production from crops and livestock in a region", False),
        ("Population Demand", "The total resource consumption driven by population size and per-capita usage", True),
        ("Industrial Usage", "Water and energy consumed by manufacturing, mining, and other industrial processes", False),
        ("Wastewater Recycling", "The percentage of used water that is treated and returned to the supply for reuse", True)
    ],
    "think_about_it": "If you increase Energy Production to meet Population Demand, what happens to Water Availability? If Water drops, what happens to Agricultural Output? How do you solve all three simultaneously?",
    "scenarios": [
        ("Growing City", "Increase Population Demand steadily -- observe cascading effects on all resources"),
        ("Drought Conditions", "Reduce Water Availability sharply -- track which systems fail first"),
        ("Recycling Investment", "Increase Wastewater Recycling to maximum -- observe how circular approaches help")
    ],
    "sim_scenarios": [
        ("Growing City", "Population +30 percent over decade", "Which resource bottleneck appears first as population grows?"),
        ("Drought", "Water -40 percent sudden reduction", "When water drops, does energy or food fail first?"),
        ("Circular Economy", "Wastewater recycling at 90 percent", "Can recycling break the competition between water users?")
    ],
    "discoveries": [
        "Water, energy, and food systems are so interconnected that solving one crisis in isolation can worsen the others",
        "Energy production is the largest industrial water consumer -- power plants use more water than agriculture in many regions",
        "Population growth creates compounding pressure because each additional person demands ALL three resources simultaneously",
        "Circular economy approaches like wastewater recycling can partially decouple the systems and reduce competition"
    ],
    "answer": "Solving one crisis worsens another because water, energy, and food systems share the same finite resources. Growing more food requires more water AND more energy for irrigation. Producing more energy requires water for cooling. Increasing water treatment requires energy. Population growth multiplies all demands simultaneously. Only integrated nexus thinking that optimizes all three systems together can avoid the trap of solving one problem by creating two more.",
    "stem_title": "Design a Sustainable City Resource Plan",
    "stem_mission": "Design an integrated water-energy-food management plan for a growing city that avoids resource trade-off traps.",
    "stem_scenario": "A city of 2 million is expected to grow to 3 million in 15 years. Water supply is already strained, energy costs are rising, and surrounding farmland is being developed. Design a plan that meets all three resource needs sustainably.",
    "stem_questions": [
        "Which resource bottleneck will hit first given current growth trends?",
        "How can circular economy approaches reduce resource competition?",
        "What trade-offs are you willing to accept in your plan?"
    ],
    "stem_design_qs": [
        "How would you allocate water between energy production, agriculture, and households?",
        "What mix of energy sources minimizes water consumption?",
        "How would you integrate wastewater recycling into the food production system?",
        "How would your plan adapt if drought reduces water supply by 30 percent?"
    ],
    "career": "Environmental Systems Engineers design integrated resource management solutions for cities and regions, earning $65,000-$130,000/year at consulting firms, utilities, and government agencies.",
    "images": {
        "cover": ("G09L2-L06-cover.png", "A photorealistic aerial view of a modern city showing the intersection of water treatment plants, power stations, and agricultural fields, interconnected infrastructure visible"),
        "landscape": ("G09L2-L06-landscape.png", "Diverse 14-15 year old students studying water-energy-food data on monitors showing interconnected resource flows in a modern classroom"),
        "modeling": ("G09L2-L06-modeling.png", "Diverse students at computers building nexus models with resource flow diagrams showing water, energy, and food connections"),
        "discussion": ("G09L2-L06-discussion.png", "A teacher leading discussion with diverse students about resource trade-offs, Venn diagram of water-energy-food on smartboard"),
        "stem": ("G09L2-L06-stem.png", "Diverse students collaboratively designing a sustainable city plan with maps, charts, and resource allocation models")
    },
    "pre_assessment": [
        "How much water do you think it takes to produce electricity?",
        "Why might solving a water shortage cause an energy crisis?",
        "Draw a diagram showing how water, energy, and food production might be connected.",
        "What happens to all three resources when a city population doubles?"
    ],
    "extend_components": [
        ("Desalination Capacity", "Energy-intensive conversion of seawater to freshwater, trading energy for water"),
        ("Renewable Energy Fraction", "Percentage of energy from low-water sources like solar and wind"),
        ("Urban Agriculture", "Food production within city limits using vertical farms and hydroponics")
    ],
    "reflections": [
        "How does your model show that resource crises are interconnected rather than independent?",
        "Why does optimizing one resource in isolation often make another worse?",
        "What role does Wastewater Recycling play in decoupling the competing systems?",
        "How does population growth create compounding rather than linear pressure?",
        "What trade-offs did you accept in your sustainable city design?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students design integrated resource management solutions that account for coupled system dynamics."),
        ("Disciplinary Core Idea", "ESS3.A Natural Resources", "Water, energy, and food systems share finite resources, creating trade-offs that require integrated management as demand grows."),
        ("Crosscutting Concept", "Systems and System Models", "Students model how coupled subsystems create emergent trade-offs not visible when each system is analyzed in isolation.")
    ],
    "cast_items": [
        "Model how water, energy, and food production systems compete for shared resources",
        "Analyze trade-offs that emerge when optimizing one resource system",
        "Design integrated management strategies that balance competing demands"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Which intervention would MOST reduce competition between water and energy systems: (a) building more reservoirs, (b) switching to solar/wind energy, (c) importing food, (d) rationing water?"),
        ("Constructed Response:", "Using your model, explain why a city that solves its energy crisis by building natural gas plants might simultaneously worsen its water crisis.")
    ],
    "background_intro": "Water, energy, and food are often managed by separate agencies with separate budgets. But they share the same finite resources, and decisions in one system cascade through the others.",
    "background_sections": [
        ("Water for Energy", "Thermoelectric power plants use 40 percent of US freshwater withdrawals for cooling. Even natural gas plants need water. Only solar PV and wind require minimal water."),
        ("Energy for Water", "Moving, treating, and heating water consumes 13 percent of US electricity. Desalination is extremely energy-intensive at 3-4 kWh per cubic meter."),
        ("Water for Food", "Agriculture uses 70 percent of global freshwater. Irrigated agriculture produces 40 percent of food on 20 percent of farmland."),
        ("Population Multiplier", "Each additional person needs all three resources simultaneously. A city growing 50 percent needs roughly 50 percent more of everything, but the interactions make it more than 50 percent due to coupling.")
    ],
    "lever_L": "Students identify water availability, energy production, agricultural output, population demand, industrial usage, and wastewater recycling as nexus components.",
    "lever_E": "Students map bidirectional connections: energy needs water, water needs energy, food needs both, population drives all demand.",
    "lever_V": "Students build a model showing coupled resource competition and identify leverage points for sustainable management.",
    "lever_Ev": "Students run growth, drought, and recycling scenarios to test how different interventions affect all three systems.",
    "lever_R": "Students add desalination, renewable energy, or urban agriculture to explore decoupling strategies.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Aerial city showing interconnected infrastructure", "say": "Your city needs more water, more energy, AND more food. But solving one problem makes another worse. Why?", "do": "Show the nexus concept visually.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Goals and vocabulary", "say": "Today we model why resource crises come in threes.", "do": "Pre-teach nexus thinking and resource trade-offs.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does solving one crisis worsen another?", "say": "California built desalination plants for water but needed massive energy. Texas expanded energy but drained aquifers.", "do": "Quick-write: How are water, energy, and food connected?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "Six components, all connected to each other. This is a true system.", "do": "Preview the coupled nature of resource competition.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "6 component cards", "say": "Which of these can city planners directly control?", "do": "Sort external inputs from system responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect", "visual": "Nexus diagram", "say": "Every connection goes BOTH ways. Water needs energy, energy needs water.", "do": "Map bidirectional relationships. Identify competition points.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulate", "visual": "Three scenarios", "say": "What happens when the city grows 50 percent? What if drought hits?", "do": "Students test growth, drought, and circular economy scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "You cannot solve water, energy, or food in isolation. They are one system.", "do": "Discuss implications for city planning and policy.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "City planning challenge", "say": "Your city doubles in 15 years. Design a plan that does not rob Peter to pay Paul.", "do": "Groups design integrated resource plans.", "time": "12 min"}
    ],
    "sort_reasoning": "Water Availability, Population Demand, and Wastewater Recycling are external because they can be directly influenced by policy and infrastructure investment. Energy Production, Agricultural Output, and Industrial Usage are internal system responses to the external conditions.",
    "relationships": [
        ("Population Demand to Water Availability", "NEGATIVE (-)", "More people consume more water, reducing availability."),
        ("Water Availability to Energy Production", "POSITIVE (+)", "More available water supports power plant cooling and hydroelectric generation."),
        ("Water Availability to Agricultural Output", "POSITIVE (+)", "More water enables more irrigation and crop production."),
        ("Energy Production to Water Availability", "NEGATIVE (-)", "Energy production consumes water for cooling, reducing availability."),
        ("Agricultural Output to Water Availability", "NEGATIVE (-)", "Agriculture is the largest water consumer, depleting supply."),
        ("Wastewater Recycling to Water Availability", "POSITIVE (+)", "Recycling treated water returns it to supply, increasing availability."),
        ("Population Demand to Energy Production", "POSITIVE (+)", "More people drive higher energy demand and production.")
    ],
    "sim_answers": [
        ("Growing City", "As Population Demand increases 30 percent, Water Availability drops due to all sectors competing. Energy Production strains because power plants need water. Agricultural Output falls as irrigation water is diverted to cities. The bottleneck is water -- it limits both other systems."),
        ("Circular Economy", "At 90 percent wastewater recycling, water competition decreases significantly. Energy and agriculture both benefit from more available water. However, recycling itself requires energy, creating a smaller secondary trade-off. Net effect is strongly positive.")
    ],
    "reflection_exemplars": [
        ("Why do resource crises come in threes?", "The model shows water, energy, and food share finite resources. Increasing one consumption necessarily decreases supply for others. Population growth multiplies all demands simultaneously, and coupling means each shortage cascades into the others."),
        ("How does recycling help?", "Wastewater recycling partially decouples systems by returning water to supply instead of losing it. This reduces competition between energy, agriculture, and households. But recycling requires energy, so it shifts rather than eliminates the trade-off.")
    ],
    "stem_intro": "A growing city faces simultaneous water, energy, and food challenges. Students design integrated plans that avoid solving one crisis by creating another.",
    "stem_concepts": [
        ("Nexus Analysis", "Modeling resource flows reveals hidden dependencies. A water policy IS an energy policy because they share infrastructure."),
        ("Circular Resource Flows", "Wastewater recycling, waste-to-energy, and food waste composting create circular flows that reduce total demand."),
        ("Adaptive Management", "Plans must adapt to changing conditions like drought or population surges. Static solutions fail in dynamic systems.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses all three resources simultaneously, quantifies trade-offs, includes circular economy strategies, and adapts to scenarios like drought"),
        ("Proficient (3)", "Plan addresses multiple resources, identifies key trade-offs, and includes sustainable strategies"),
        ("Developing (2)", "Plan addresses resources but does not account for their interconnections or trade-offs"),
        ("Beginning (1)", "Plan addresses only one resource or does not use model evidence")
    ],
    "support": [
        "Pre-drawn Venn diagram showing water-energy-food overlaps with specific examples in each intersection",
        "Use a household budget analogy: water, energy, and food are like rent, food, and transportation -- when one goes up, you have less for the others",
        "Sentence frames: When we increase __ to meet demand, it requires more __ which reduces __ because __"
    ],
    "extensions": [
        "Research Singapore water management strategy (NEWater, desalination, rainwater) and model their nexus approach",
        "Calculate the water footprint of different diets (beef vs. plant-based) and model how dietary shifts affect the nexus",
        "Investigate the virtual water trade -- how importing food is equivalent to importing water from other regions"
    ],
    "cross_curr": [
        ("Math", "Calculate water-energy equivalencies: if a power plant uses X gallons per MWh and a city needs Y MWh, how much water goes to energy vs. drinking?"),
        ("ELA", "Write a policy proposal for a city council that explains the nexus concept and recommends integrated resource management using model evidence."),
        ("Social Studies", "Research water conflicts in the Middle East or Central Asia and analyze how water scarcity drives energy and food insecurity.")
    ],
    "misconceptions": [
        ("Water, energy, and food are separate problems", "They share the same finite resources. Energy production is the largest industrial water consumer. Agriculture uses 70 percent of freshwater. Solving one in isolation often makes another worse.", "Example: California desalination solves water but requires massive energy. Texas fracking provides energy but drains aquifers. They are ONE system."),
        ("Technology will solve resource scarcity", "Technology can improve efficiency but cannot create resources from nothing. Desalination makes water but needs energy. Solar panels need water to manufacture. Every solution has trade-offs within the nexus.", "Ask: If every solution requires another resource as input, can technology alone solve scarcity?"),
        ("Population growth creates linear resource pressure", "Population growth creates COMPOUNDING pressure because each person needs ALL three resources, and the coupling means shortages cascade. A 50 percent population increase creates more than 50 percent more demand due to system interactions.", "Model it: Add 50 percent population and watch the cascade. Total system stress increases by more than 50 percent.")
    ]
}

L07 = {
    "id": "G09L2-L07",
    "title": "Urban Heat Islands: Why Cities Are Hotter Than Forests",
    "subtitle": "Modeling How Built Environments Amplify Extreme Heat",
    "ngss": "HS-ESS3-4, HS-PS3-4",
    "ngss_desc": "Evaluate or refine a technological solution that reduces human impacts on natural systems. Plan and conduct an investigation to provide evidence that energy transfer through heating changes particle motion.",
    "big_question": "Why can a city be 10 degrees hotter than the forest just 20 miles away, and who suffers most?",
    "objectives": [
        "Model how impervious surfaces, green space loss, and air conditioning create self-reinforcing urban heat loops",
        "Analyze how urban heat islands disproportionately affect low-income communities",
        "Evaluate cooling interventions at different scales from building to city-wide",
        "Design an equitable urban cooling strategy that targets the most vulnerable neighborhoods"
    ],
    "vocabulary": [
        ("Urban Heat Island", "A metropolitan area significantly warmer than surrounding rural areas due to heat-absorbing surfaces, reduced vegetation, and waste heat from buildings and vehicles"),
        ("Albedo", "The reflectivity of a surface; dark surfaces like asphalt have low albedo and absorb heat, while light or vegetated surfaces have high albedo and reflect it"),
        ("Thermal Mass", "The ability of a material to absorb, store, and later release heat; concrete and asphalt store daytime heat and radiate it at night"),
        ("Environmental Justice", "The principle that no community should bear a disproportionate share of environmental hazards due to race, income, or political power")
    ],
    "components": [
        ("Impervious Surface Area", "Percentage of land covered by heat-absorbing surfaces like asphalt, concrete, and rooftops", True),
        ("Green Space Coverage", "Percentage of land covered by vegetation including trees, parks, and green roofs that cool through evapotranspiration", True),
        ("Ambient Temperature", "The local air temperature experienced at ground level in different neighborhoods", False),
        ("Energy Consumption (AC)", "Electricity used for air conditioning, which generates waste heat that warms outdoor air", False),
        ("Air Quality Index", "Measure of air pollution concentration, which increases with heat-driven chemical reactions and AC emissions", False),
        ("Heat-Related Health Risk", "Probability of heat stroke, dehydration, and death in vulnerable populations", False)
    ],
    "think_about_it": "When Impervious Surface Area is high and Green Space is low, what happens to Ambient Temperature? If temperature rises, what happens to AC use? And if AC pumps heat outside, what happens to outdoor temperature? Find the reinforcing loop.",
    "scenarios": [
        ("Wealthy vs. Poor Neighborhood", "Compare high green space/low impervious vs. low green space/high impervious -- observe temperature and health disparities"),
        ("Heat Wave", "Increase baseline temperature by 5 degrees -- observe how the urban heat island amplifies the extreme event"),
        ("Green Infrastructure", "Increase Green Space Coverage from 10 to 40 percent -- measure cooling effect across all components")
    ],
    "sim_scenarios": [
        ("Neighborhood Comparison", "Wealthy area vs. underserved area", "How much hotter is the concrete neighborhood vs. the tree-lined one?"),
        ("Heat Wave Amplification", "Baseline +5 C with urban heat island", "How much does the city amplify a regional heat wave?"),
        ("Green Intervention", "Green space from 10 to 40 percent", "How much cooling does tree planting provide? Is it enough?")
    ],
    "discoveries": [
        "Urban heat islands create a reinforcing loop: heat drives AC use which pumps more heat outside which drives more AC use",
        "The temperature difference between wealthy and poor neighborhoods can exceed 10 degrees F due to green space inequality",
        "Air conditioning is both a solution and a cause -- it cools indoor spaces while warming outdoor spaces and consuming energy",
        "Green infrastructure breaks the reinforcing loop by providing passive cooling through evapotranspiration"
    ],
    "answer": "Cities are hotter because dark impervious surfaces absorb solar energy, concrete stores heat and releases it at night, and removing vegetation eliminates natural cooling. This creates a reinforcing feedback loop: higher temperatures drive AC use, which pumps waste heat outdoors, raising temperatures further. The communities with the most concrete and least green space -- typically low-income neighborhoods and communities of color -- experience the worst heat. Environmental justice demands that cooling investments target the most vulnerable, not the most politically powerful.",
    "stem_title": "Design an Equitable Urban Cooling Plan",
    "stem_mission": "Design a neighborhood cooling strategy that prioritizes environmental justice by targeting interventions to the most heat-vulnerable communities.",
    "stem_scenario": "A city has funding for urban cooling but limited budget. Some neighborhoods are 10+ degrees hotter than others. Design a plan that allocates cooling interventions equitably based on heat vulnerability, not political influence.",
    "stem_questions": [
        "Which neighborhoods should receive cooling interventions first and why?",
        "What mix of interventions provides the most cooling per dollar?",
        "How do you balance immediate relief with long-term structural change?"
    ],
    "stem_design_qs": [
        "How would you map heat vulnerability across the city?",
        "What combination of green infrastructure and cool surfaces would you deploy?",
        "How would you ensure that cooling investments do not cause gentrification?",
        "How would you measure whether your plan actually reduced heat inequality?"
    ],
    "career": "Urban Climate Scientists study how built environments modify local weather and design heat mitigation strategies, earning $60,000-$120,000/year at city planning departments, universities, and environmental firms.",
    "images": {
        "cover": ("G09L2-L07-cover.png", "A photorealistic aerial thermal image showing a city with hot zones in red over concrete areas and cool blue zones over parks and tree-lined streets, dramatic contrast"),
        "landscape": ("G09L2-L07-landscape.png", "Diverse 14-15 year old students using thermal cameras to measure surface temperatures in a schoolyard, comparing asphalt to grass areas"),
        "modeling": ("G09L2-L07-modeling.png", "Diverse students at computers building urban heat island models with neighborhood maps and temperature overlays on screens"),
        "discussion": ("G09L2-L07-discussion.png", "A teacher leading discussion with diverse students about environmental justice, thermal map of city neighborhoods on smartboard"),
        "stem": ("G09L2-L07-stem.png", "Diverse students designing a neighborhood cooling plan with city maps, green infrastructure diagrams, and equity metrics")
    },
    "pre_assessment": [
        "Why do you think cities are hotter than surrounding countryside?",
        "Have you noticed temperature differences between different neighborhoods? Why might that be?",
        "Draw a diagram showing how concrete, trees, and air conditioning might affect local temperature.",
        "What is environmental justice and how might it relate to heat?"
    ],
    "extend_components": [
        ("Cool Roof Coverage", "Percentage of buildings with reflective roofing that reduces heat absorption"),
        ("Public Transit Usage", "Percentage of commuters using public transit vs. cars, reducing vehicle waste heat"),
        ("Nighttime Temperature", "Minimum temperature at night, which fails to drop in dense urban areas due to stored heat release")
    ],
    "reflections": [
        "How does your model show that the urban heat island is a self-reinforcing system?",
        "Why do wealthy and poor neighborhoods experience such different temperatures?",
        "How does air conditioning act as both a solution and a cause of urban heat?",
        "What does environmental justice mean in the context of heat vulnerability?",
        "What trade-offs exist between rapid cooling solutions and long-term structural change?"
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze temperature data across neighborhoods to identify patterns of heat inequality and evaluate intervention effectiveness."),
        ("Disciplinary Core Idea", "PS3.B Conservation of Energy and Energy Transfer", "Heat energy absorbed by dark surfaces is stored in thermal mass and radiated, creating measurable temperature differences between urban and rural environments."),
        ("Crosscutting Concept", "Cause and Effect", "Students model how the built environment creates feedback loops that amplify heat, and how targeted interventions can break these loops.")
    ],
    "cast_items": [
        "Model how impervious surfaces and green space loss create reinforcing urban heat loops",
        "Analyze how heat island effects disproportionately impact vulnerable communities",
        "Design equitable cooling interventions based on model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Which intervention would provide the MOST cooling: (a) AC for all buildings, (b) 30 percent increase in tree canopy, (c) cool roofs on commercial buildings, (d) reducing traffic?"),
        ("Constructed Response:", "Using your model, explain why a heat wave that is survivable in a suburban neighborhood with trees can be deadly in an urban neighborhood with concrete.")
    ],
    "background_intro": "Urban heat islands are not just uncomfortable -- they are deadly. Heat kills more Americans than hurricanes, tornadoes, and floods combined. Understanding why some neighborhoods are dangerously hotter than others requires modeling the physics of the built environment.",
    "background_sections": [
        ("The Physics of Urban Heat", "Dark surfaces absorb up to 95 percent of incoming solar radiation and convert it to heat. Concrete and asphalt store this heat in their thermal mass and release it at night, preventing cooling. Vegetation cools through evapotranspiration, but cities have replaced trees with pavement."),
        ("The AC Feedback Loop", "Air conditioning is both salvation and curse. It cools indoor spaces but pumps waste heat outdoors, adding 1-2 degrees to local air temperature in dense areas. Higher outdoor temperatures drive more AC use, which pumps more heat, creating a reinforcing loop."),
        ("Environmental Justice", "Heat vulnerability maps closely mirror poverty and racial segregation maps. Historically redlined neighborhoods have 30-40 percent less tree canopy. Low-income residents are less likely to have AC, more likely to have outdoor jobs, and more likely to have health conditions exacerbated by heat."),
        ("Green Infrastructure Solutions", "Trees provide shade AND evapotranspiration cooling. A single mature tree can provide the cooling equivalent of 10 room air conditioners. Cool roofs reflect solar radiation. Green roofs combine both. But these solutions take years to decades to mature.")
    ],
    "lever_L": "Students identify impervious surfaces, green space, ambient temperature, AC energy consumption, air quality, and health risk as the 6 components.",
    "lever_E": "Students map the reinforcing heat-AC loop and the environmental justice dimension of heat inequality.",
    "lever_V": "Students build a model comparing wealthy and underserved neighborhoods to reveal the structural roots of heat inequality.",
    "lever_Ev": "Students run neighborhood comparison, heat wave, and green infrastructure scenarios.",
    "lever_R": "Students add cool roofs, transit, or nighttime temperature to explore additional cooling strategies.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Thermal city map", "say": "This map shows temperature. The red zones are 10+ degrees hotter. Who lives there?", "do": "Show a real thermal map of a city. Ask students to guess which neighborhoods are hottest.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Goals and vocabulary", "say": "Today we model why your neighborhood temperature depends on your zip code.", "do": "Pre-teach urban heat island and albedo.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why are cities hotter than forests?", "say": "And more importantly -- why are SOME neighborhoods hotter than others?", "do": "Quick-write: What makes a place hot or cool?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "Six components with a sneaky reinforcing loop.", "do": "Preview the AC feedback loop concept.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "6 component cards", "say": "Which can city planners change? Which are consequences?", "do": "Sort components. Discuss why impervious surfaces and green space are policy choices.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect", "visual": "Heat loop diagram", "say": "Find the reinforcing loop. Hint: AC is both a solution and a cause.", "do": "Map the heat-AC feedback loop. Discuss environmental justice dimension.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulate", "visual": "Neighborhood comparison scenarios", "say": "Compare two neighborhoods. One has trees, one has concrete. What happens during a heat wave?", "do": "Students run scenarios and quantify the equity gap.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with equity data", "say": "Heat inequality is structural. It was designed into our cities.", "do": "Connect model findings to historical redlining and investment patterns.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Equitable cooling plan", "say": "You have the budget. Where do you plant the trees?", "do": "Groups design cooling plans prioritizing environmental justice.", "time": "12 min"}
    ],
    "sort_reasoning": "Impervious Surface Area and Green Space Coverage are external because they represent land-use decisions that planners can modify. Ambient Temperature, AC Energy Consumption, Air Quality, and Health Risk are internal system responses.",
    "relationships": [
        ("Impervious Surface to Ambient Temperature", "POSITIVE (+)", "More dark surfaces absorb more solar radiation, raising local temperature."),
        ("Green Space to Ambient Temperature", "NEGATIVE (-)", "Vegetation cools through evapotranspiration and shade."),
        ("Ambient Temperature to Energy Consumption", "POSITIVE (+)", "Higher temperatures drive more AC use."),
        ("Energy Consumption to Ambient Temperature", "POSITIVE (+)", "AC pumps waste heat outdoors, creating a reinforcing loop."),
        ("Ambient Temperature to Air Quality", "NEGATIVE (-)", "Heat accelerates ozone formation and traps pollutants."),
        ("Ambient Temperature to Health Risk", "POSITIVE (+)", "Higher temperatures increase heat stroke, dehydration, and mortality risk."),
        ("Air Quality to Health Risk", "POSITIVE (+)", "Poor air quality compounds heat-related health effects.")
    ],
    "sim_answers": [
        ("Neighborhood Comparison", "The high-impervious, low-green neighborhood shows temperatures 5-10 degrees higher, 40 percent more AC use, worse air quality, and significantly higher health risk. The tree-lined neighborhood stays cooler through evapotranspiration and shade, with less AC needed."),
        ("Green Intervention", "Increasing green space from 10 to 40 percent reduces ambient temperature by 3-5 degrees, cuts AC demand by 20-30 percent, improves air quality, and significantly reduces health risk. The reinforcing loop is weakened by passive cooling.")
    ],
    "reflection_exemplars": [
        ("How is urban heat self-reinforcing?", "Heat drives AC use, which pumps waste heat outside, making it hotter, driving more AC use. The model shows this positive feedback loop. Without intervention, the loop amplifies itself. Green infrastructure breaks the loop by providing passive cooling that does not generate waste heat."),
        ("Why is heat an environmental justice issue?", "The model shows that neighborhoods with more impervious surfaces and less green space are structurally hotter. These neighborhoods correlate with historically redlined, low-income, and communities of color. The heat inequality is not natural -- it was created by decades of unequal investment in urban infrastructure.")
    ],
    "stem_intro": "A city has cooling funds but limited budget. Temperature inequality across neighborhoods exceeds 10 degrees. Students design equitable cooling plans.",
    "stem_concepts": [
        ("Heat Vulnerability Mapping", "Combining surface temperature data with demographic data reveals which populations face the greatest heat risk."),
        ("Green Infrastructure ROI", "Trees provide decades of cooling. Cool roofs are faster to install. The optimal mix depends on budget and timeline."),
        ("Anti-Gentrification Safeguards", "Green improvements can increase property values and displace the residents they were meant to help. Plans must include safeguards.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan targets most vulnerable neighborhoods, uses model evidence for intervention selection, includes equity metrics, and addresses gentrification risk"),
        ("Proficient (3)", "Plan addresses heat inequality, selects appropriate interventions, and uses model evidence"),
        ("Developing (2)", "Plan includes cooling interventions but does not prioritize by vulnerability or address equity"),
        ("Beginning (1)", "Plan is incomplete or does not connect interventions to the heat island model")
    ],
    "support": [
        "Pre-drawn feedback loop diagram showing the heat-AC reinforcing cycle",
        "Use a real thermal map of a familiar city to make the concept concrete",
        "Sentence frames: Neighborhood A is hotter than B because it has more __ and less __, which means __ absorbs more heat and __ cannot cool it"
    ],
    "extensions": [
        "Research historical redlining maps and overlay them with modern heat island data to demonstrate structural inequality",
        "Calculate the number of trees needed to cool a specific neighborhood by 5 degrees and estimate the cost and timeline",
        "Design a cool corridor network connecting parks through tree-lined streets to create heat refuges"
    ],
    "cross_curr": [
        ("Math", "Calculate albedo-weighted solar absorption for different surface mixes and determine the optimal ratio of cool to dark surfaces for a target temperature."),
        ("ELA", "Write an op-ed for a local newspaper arguing that heat is a civil rights issue, using model evidence and historical context."),
        ("Social Studies", "Research the history of urban planning decisions -- highway placement, park investment, zoning -- that created today's heat inequality.")
    ],
    "misconceptions": [
        ("Urban heat islands are just uncomfortable", "Urban heat kills more people than any other weather event. The 2003 European heat wave killed 70,000 people, mostly in cities. Heat strokes, dehydration, and cardiovascular events are medical emergencies.", "Show data: Heat kills more Americans annually than hurricanes, tornadoes, and floods combined. It is the deadliest weather."),
        ("AC solves the heat problem", "AC cools individuals while warming the city. Every BTU removed from indoor spaces is pumped outdoors plus waste heat from the AC unit itself. Dense AC use can add 1-2 degrees to outdoor temperature, worsening the problem for those without AC.", "Demonstrate: If everyone turns on AC, who benefits? Those with AC cool down. Those without AC (often the poorest) get even hotter from the waste heat."),
        ("Heat affects everyone equally", "Heat vulnerability is deeply unequal. Low-income residents are less likely to have AC, more likely to work outdoors, more likely to live in heat-absorbing neighborhoods, and more likely to have pre-existing conditions. Race and income predict heat death rates better than temperature does.", "Map it: Overlay heat data with income and race data. The correlation is not coincidence -- it is the result of decades of unequal investment.")
    ]
}

L08 = {
    "id": "G09L2-L08",
    "title": "CRISPR Gene Drives: Rewriting Evolution",
    "subtitle": "Modeling How Engineered Genes Spread Through Wild Populations",
    "ngss": "HS-LS3-1, HS-LS4-5",
    "ngss_desc": "Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits. Evaluate evidence supporting claims that changes in environmental conditions may result in increases in beneficial alleles and decreases in harmful alleles.",
    "big_question": "Should we have the power to edit an entire species -- and what happens if we get it wrong?",
    "objectives": [
        "Model how gene drives override normal Mendelian inheritance to spread engineered genes through populations",
        "Analyze how resistance evolution and fitness costs create countervailing feedback against gene drives",
        "Evaluate the ecological risks of releasing self-propagating genetic modifications into wild populations",
        "Design a gene drive deployment strategy that balances disease elimination goals with ecological safety"
    ],
    "vocabulary": [
        ("Gene Drive", "A genetic engineering technology that biases inheritance so an engineered gene is passed to nearly all offspring rather than the normal 50 percent"),
        ("Mendelian Inheritance", "The standard pattern where each parent contributes one allele with a 50 percent chance of passing either to offspring"),
        ("Fitness Cost", "A reduction in survival or reproduction caused by carrying an engineered gene, which natural selection acts against"),
        ("Resistance Allele", "A naturally occurring or spontaneous mutation that prevents the gene drive from copying itself, allowing normal inheritance to resume")
    ],
    "components": [
        ("Gene Drive Frequency", "The proportion of the population carrying the engineered gene drive construct", False),
        ("Wild-Type Allele Frequency", "The proportion carrying the original, unmodified gene version", False),
        ("Population Size", "Total number of organisms in the target species population", False),
        ("Fitness Cost", "The survival or reproductive disadvantage imposed by carrying the gene drive", True),
        ("Resistance Evolution", "The rate at which resistance mutations arise and spread through natural selection", False),
        ("Inheritance Bias", "The percentage of offspring that receive the gene drive, typically 95-99 percent vs. normal 50 percent", True),
        ("Ecological Impact", "The cascading effects on other species when the target population is suppressed or modified", False)
    ],
    "think_about_it": "If a gene drive gives itself to 99 percent of offspring instead of 50 percent, how fast will it spread? But if it has a Fitness Cost, natural selection pushes back. And if Resistance Evolution occurs, the drive stalls. Who wins?",
    "scenarios": [
        ("Ideal Gene Drive", "Set Inheritance Bias to 99 percent, Fitness Cost to zero -- observe how fast the drive spreads"),
        ("Realistic Drive", "Set Inheritance Bias to 95 percent with moderate Fitness Cost -- observe the balance between drive and selection"),
        ("Resistance Emergence", "Same as realistic but increase Resistance Evolution rate -- observe whether the drive succeeds or fails")
    ],
    "sim_scenarios": [
        ("Ideal Drive", "99 percent inheritance, no fitness cost", "How many generations until the drive reaches 100 percent of the population?"),
        ("Realistic Drive", "95 percent inheritance, moderate fitness cost", "Does the drive still reach fixation, or does natural selection slow it?"),
        ("Resistance Challenge", "95 percent inheritance, moderate cost, high resistance rate", "Can resistance alleles outcompete the gene drive?")
    ],
    "discoveries": [
        "Gene drives exploit a mathematical advantage: 95-99 percent inheritance vs 50 percent overcomes even moderate fitness costs",
        "Resistance evolution is inevitable given enough time and population size -- the question is whether suppression occurs first",
        "Ecological impacts cascade unpredictably because removing one species affects all species connected to it in the food web",
        "There is a critical race between drive spread speed and resistance evolution speed that determines success or failure"
    ],
    "answer": "Gene drives rewrite evolution by cheating inheritance -- giving themselves to 95-99 percent of offspring instead of 50 percent. This mathematical advantage can push an engineered gene through an entire wild population in just 10-20 generations. But evolution fights back: resistance mutations arise naturally, and fitness costs slow the drive. The outcome is a race between the drive spreading and resistance evolving. If we release a gene drive to eliminate malaria mosquitoes and resistance stops it halfway, we have modified a species without achieving our goal -- with unknown ecological consequences.",
    "stem_title": "Design a Gene Drive Safety Protocol",
    "stem_mission": "Design a gene drive deployment strategy for malaria mosquito suppression that maximizes disease reduction while minimizing ecological risk.",
    "stem_scenario": "Malaria kills 600,000 people per year, mostly children in sub-Saharan Africa. A gene drive targeting Anopheles mosquitoes could potentially eliminate malaria. But the ecological consequences of removing a species are unknown. Design a phased deployment with safety mechanisms.",
    "stem_questions": [
        "What safety mechanisms would prevent the drive from spreading beyond the target area?",
        "How would you monitor for resistance evolution and ecological cascades?",
        "At what point would you halt deployment if unexpected effects occur?"
    ],
    "stem_design_qs": [
        "Would you use a suppression drive (reduce population) or modification drive (make mosquitoes unable to carry malaria)?",
        "How would you contain the drive to a specific geographic region?",
        "What monitoring systems would detect ecological side effects?",
        "How would you obtain informed consent from communities where the drive is released?"
    ],
    "career": "Genetic Engineers and Bioethicists work at the intersection of technology and society, designing safe genetic modifications and evaluating their ethical implications, earning $70,000-$150,000/year at biotech companies, universities, and government agencies.",
    "images": {
        "cover": ("G09L2-L08-cover.png", "A photorealistic cinematic image of a mosquito in extreme macro detail with glowing CRISPR gene editing visualization overlaid, dramatic scientific lighting"),
        "landscape": ("G09L2-L08-landscape.png", "Diverse 14-15 year old students in a genetics lab examining DNA sequence visualizations on screens with molecular models on desks"),
        "modeling": ("G09L2-L08-modeling.png", "Diverse students at computers building population genetics models showing gene drive spread through generations"),
        "discussion": ("G09L2-L08-discussion.png", "A teacher leading ethical debate with diverse students about gene drives, Punnett square and gene drive diagram on smartboard"),
        "stem": ("G09L2-L08-stem.png", "Diverse students designing gene drive safety protocols with maps, decision trees, and risk assessment matrices")
    },
    "pre_assessment": [
        "What is CRISPR and how does it edit genes?",
        "If you could eliminate all mosquitoes to stop malaria, should you? What might go wrong?",
        "Draw a Punnett square showing normal 50-50 inheritance. Now imagine one allele gets passed 99 percent of the time.",
        "What does it mean to edit an entire wild species?"
    ],
    "extend_components": [
        ("Daisy Chain Mechanism", "A self-limiting gene drive design where the drive loses power after a set number of generations"),
        ("Off-Target Species Effects", "The probability of the gene drive accidentally transferring to related species through hybridization"),
        ("Community Consent Level", "The degree of informed consent from local communities where the gene drive would be released")
    ],
    "reflections": [
        "How does your model show the race between gene drive spread and resistance evolution?",
        "Why is ecological impact the hardest component to predict in your model?",
        "What ethical considerations arise when one country releases a gene drive that could cross borders?",
        "How would you decide whether the benefit of eliminating malaria outweighs the ecological risk?",
        "What safety mechanisms could make gene drives reversible?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students evaluate competing claims about gene drive safety using model evidence and population genetics principles."),
        ("Disciplinary Core Idea", "LS3.A Inheritance of Traits", "Gene drives exploit the molecular mechanism of inheritance to bias allele transmission, overriding Mendelian ratios."),
        ("Crosscutting Concept", "Cause and Effect", "Students model how an engineered cause (biased inheritance) produces population-level effects that cascade through ecosystems.")
    ],
    "cast_items": [
        "Model how gene drives override Mendelian inheritance to spread through populations",
        "Analyze the competing dynamics of drive spread, fitness cost, and resistance evolution",
        "Evaluate ecological and ethical implications of releasing self-propagating genetic modifications"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A gene drive with 95 percent inheritance bias and moderate fitness cost is released. What MOST determines whether it succeeds: (a) initial release size, (b) resistance mutation rate, (c) population mobility, (d) weather?"),
        ("Constructed Response:", "Explain why a gene drive that eliminates 80 percent of malaria mosquitoes but then stalls due to resistance might be worse than one that eliminates 100 percent.")
    ],
    "background_intro": "CRISPR gene drives represent perhaps the most powerful and controversial biotechnology ever developed -- the ability to permanently modify an entire wild species. The potential to eliminate malaria is matched by the potential for catastrophic unintended consequences.",
    "background_sections": [
        ("How Gene Drives Work", "Normal inheritance gives each allele a 50 percent chance of being passed on. Gene drives use CRISPR to cut the chromosome without the drive and paste a copy of the drive into the break. The result: 95-99 percent of offspring inherit the drive instead of 50 percent."),
        ("The Malaria Application", "Anopheles mosquitoes kill 600,000 people per year by transmitting Plasmodium parasites. A gene drive could either suppress mosquito populations or modify them to be unable to carry the parasite. Either approach could save hundreds of thousands of lives annually."),
        ("Resistance Evolution", "Natural selection never stops. Any mutation that prevents the drive from copying itself will be strongly favored by selection. Lab experiments show resistance evolving within 10-25 generations. The question is whether the drive suppresses the population before resistance spreads."),
        ("Ecological Cascades", "Mosquitoes are food for birds, bats, fish, and dragonflies. They pollinate some plants. Removing them could cascade through food webs in unpredictable ways. Or the ecological gap might be filled by other insects. We do not know -- and we cannot un-release a gene drive.")
    ],
    "lever_L": "Students identify gene drive frequency, wild-type allele, population size, fitness cost, resistance evolution, inheritance bias, and ecological impact as components.",
    "lever_E": "Students map the competition between drive spread (powered by inheritance bias) and natural selection (powered by fitness cost and resistance).",
    "lever_V": "Students build a model showing how gene drive dynamics play out across generations with competing evolutionary forces.",
    "lever_Ev": "Students run ideal, realistic, and resistance scenarios to identify conditions for drive success or failure.",
    "lever_R": "Students add daisy chain mechanisms, off-target effects, or community consent to explore safety and ethics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Macro mosquito with gene editing overlay", "say": "We can now edit an entire species. Should we?", "do": "Show the dual nature: 600,000 malaria deaths vs. unknown ecological risk.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Goals and vocabulary", "say": "Today we model the most powerful and controversial biotechnology ever invented.", "do": "Pre-teach gene drive, inheritance bias, and resistance.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Should we rewrite evolution?", "say": "Malaria kills a child every 2 minutes. We have the technology to stop it. But at what risk?", "do": "Quick-write: If you could eliminate mosquitoes, would you? Why or why not?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "Seven components. Evolution vs. engineering. Who wins?", "do": "Preview the race between drive spread and resistance.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "7 component cards", "say": "What can scientists control? What does evolution control?", "do": "Sort engineered vs. evolutionary components.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect", "visual": "Drive vs. resistance diagram", "say": "The drive pushes the gene forward. Natural selection pushes back. Map the battle.", "do": "Map competing forces and identify the tipping point.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulate", "visual": "Three scenarios across generations", "say": "Does the drive win or does evolution win? It depends on the parameters.", "do": "Students run ideal, realistic, and resistance scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "The outcome is not guaranteed. And we cannot recall a released gene drive.", "do": "Discuss irreversibility and the precautionary principle.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Safety protocol design", "say": "600,000 lives per year. Unknown ecological risk. Design the safest possible deployment.", "do": "Groups design phased deployment with safety mechanisms and halt criteria.", "time": "12 min"}
    ],
    "sort_reasoning": "Fitness Cost and Inheritance Bias are external because they are engineering parameters set by scientists. Gene Drive Frequency, Wild-Type Frequency, Population Size, Resistance Evolution, and Ecological Impact are internal evolutionary and ecological responses.",
    "relationships": [
        ("Inheritance Bias to Gene Drive Frequency", "POSITIVE (+)", "Higher inheritance bias spreads the drive faster through the population."),
        ("Gene Drive Frequency to Wild-Type Frequency", "NEGATIVE (-)", "As the drive spreads, wild-type alleles are replaced."),
        ("Fitness Cost to Gene Drive Frequency", "NEGATIVE (-)", "Higher fitness cost means drive carriers survive and reproduce less."),
        ("Gene Drive Frequency to Resistance Evolution", "POSITIVE (+)", "As drive frequency increases, selection pressure for resistance mutations intensifies."),
        ("Resistance Evolution to Gene Drive Frequency", "NEGATIVE (-)", "Resistance alleles block the drive mechanism, slowing its spread."),
        ("Gene Drive Frequency to Population Size", "NEGATIVE (-)", "If the drive is suppressive, higher drive frequency reduces total population."),
        ("Population Size to Ecological Impact", "POSITIVE (+)", "Population reduction cascades through food webs affecting predators, competitors, and prey.")
    ],
    "sim_answers": [
        ("Ideal Drive", "With 99 percent inheritance and zero fitness cost, the drive reaches fixation in 10-15 generations. Wild-type alleles are completely replaced. No resistance evolves because there is no selection pressure for it when fitness cost is zero."),
        ("Resistance Challenge", "With high resistance mutation rate, resistance alleles spread through the population as the gene drive creates strong selection pressure for them. The drive stalls at 60-80 percent frequency. The population is modified but not suppressed, with unknown ecological consequences.")
    ],
    "reflection_exemplars": [
        ("Who wins: drive or evolution?", "The outcome depends on three parameters: inheritance bias, fitness cost, and resistance mutation rate. If inheritance bias greatly exceeds fitness cost and resistance is slow, the drive wins. If resistance evolves fast enough, evolution wins. The model shows this is a quantitative race, not a guaranteed outcome."),
        ("Why is 80 percent suppression possibly worse than 100 percent?", "At 80 percent, the population is severely disrupted but not eliminated. Ecosystem effects are triggered but the disease vector still exists. Resistance alleles stabilize at this point, making further suppression impossible. You get the ecological costs without the disease elimination benefit.")
    ],
    "stem_intro": "Malaria kills 600,000 per year. Gene drives could eliminate it. But the technology is irreversible once released. Students design the safest possible deployment strategy.",
    "stem_concepts": [
        ("Self-Limiting Drives", "Daisy chain designs lose drive power after a set number of generations, providing temporal containment."),
        ("Phased Deployment", "Testing in contained environments, then islands, then mainland reduces risk but delays benefits."),
        ("Ecological Monitoring", "Tracking predator and pollinator populations near release sites detects cascading effects early.")
    ],
    "stem_eval": [
        ("Expert (4)", "Strategy includes containment mechanisms, phased deployment, ecological monitoring, halt criteria, community consent, and model-justified parameter choices"),
        ("Proficient (3)", "Strategy includes safety mechanisms, monitoring plan, and addresses ecological risk with model evidence"),
        ("Developing (2)", "Strategy includes some safety measures but lacks ecological monitoring or justified parameters"),
        ("Beginning (1)", "Strategy is incomplete or does not address resistance, ecological risk, or safety")
    ],
    "support": [
        "Pre-drawn Punnett squares comparing normal 50-50 inheritance to 95 percent gene drive inheritance",
        "Use a relay race analogy: the gene drive runs at 95 mph and resistance runs at 50 mph, but resistance gets a head start",
        "Sentence frames: If Inheritance Bias is __ and Fitness Cost is __, the drive will spread at __ rate because __"
    ],
    "extensions": [
        "Research the Target Malaria project in Burkina Faso and evaluate their phased approach against your model predictions",
        "Model a reversal drive designed to undo the original gene drive and analyze whether reversal is practically achievable",
        "Investigate the legal and sovereignty questions: who decides whether to release a gene drive that will cross national borders?"
    ],
    "cross_curr": [
        ("Math", "Calculate the probability of resistance arising in a population of 10 million mosquitoes if the per-generation mutation rate is 0.001 percent. How many generations until resistance is likely?"),
        ("ELA", "Write a debate speech either FOR or AGAINST gene drive release for malaria elimination, using model evidence and ethical reasoning."),
        ("Social Studies", "Research the ethics of testing powerful biotechnologies in developing nations. Who bears the risk? Who reaps the benefit? Who decides?")
    ],
    "misconceptions": [
        ("Gene drives are permanent and unstoppable", "Gene drives face evolutionary pressure from resistance mutations. Lab experiments show resistance evolving within 10-25 generations. The drive can stall or fail. However, even partial spread may cause irreversible ecological changes.", "Show the resistance scenario: the drive does not reach 100 percent. But it still changed 80 percent of the population. Is that reversible?"),
        ("Removing mosquitoes would have no ecological effect", "Mosquitoes are food for birds, bats, dragonflies, and fish. They pollinate some plants. Their larvae filter water. Removing them could cascade through food webs. Or the gap could be filled by other species. We genuinely do not know.", "List all the species that eat mosquitoes. Now imagine those species lose 80 percent of their food. What happens next in the food chain?"),
        ("CRISPR gene drives are precise and controllable", "CRISPR is remarkably precise but not perfect. Off-target cuts occur, resistance evolves, and mechanisms can fail unpredictably. Lab experiments show gene drives reaching only 60-80 percent effectiveness before resistance plateaus the effect.", "Show lab data: gene drives in contained mosquito populations stalled at 60-80 percent. What does that mean for a continental release?")
    ]
}

L09 = {
    "id": "G09L2-L09",
    "title": "Microplastics in the Food Chain: The Invisible Invasion",
    "subtitle": "Modeling Bioaccumulation and Trophic Transfer of Persistent Pollutants",
    "ngss": "HS-LS2-6, HS-ESS3-3",
    "ngss_desc": "Evaluate claims that complex interactions in ecosystems maintain relatively consistent conditions. Create a computational simulation of a natural system.",
    "big_question": "How does a plastic bag thrown away in Kansas end up inside a fish you eat in California?",
    "objectives": [
        "Model how microplastics move through food chains via bioaccumulation and trophic transfer",
        "Analyze the amplification effect where toxin concentration increases at each trophic level",
        "Evaluate how decomposition resistance creates a one-way accumulation problem",
        "Design monitoring and intervention strategies targeting the most effective points in the plastic pathway"
    ],
    "vocabulary": [
        ("Microplastics", "Plastic particles smaller than 5mm resulting from degradation of larger plastics or manufactured as microbeads, persistent in the environment for centuries"),
        ("Bioaccumulation", "The progressive buildup of a substance in an organism over time because intake exceeds the rate of excretion or metabolism"),
        ("Trophic Transfer", "The movement of accumulated substances from prey to predator, concentrating toxins at higher levels of the food chain"),
        ("Biomagnification", "The increasing concentration of a persistent substance at successively higher trophic levels in a food chain")
    ],
    "components": [
        ("Plastic Input Rate", "The volume of plastic entering the environment from waste, industry, and consumer products", True),
        ("Microplastic Concentration", "The density of microplastic particles in water, soil, or sediment per unit volume", False),
        ("Bioaccumulation Factor", "The ratio of microplastic concentration in an organism relative to its environment", False),
        ("Trophic Transfer", "The efficiency with which microplastics are passed from prey organisms to predators", False),
        ("Marine Organism Health", "The overall fitness and survival rate of organisms exposed to microplastic ingestion", False),
        ("Decomposition Rate", "The extremely slow rate at which plastics break down, measured in centuries", True),
        ("Human Exposure Level", "The amount of microplastics consumed by humans through seafood, water, and air", False)
    ],
    "think_about_it": "If Plastic Input Rate stays high and Decomposition Rate is near zero, what happens to Microplastic Concentration over decades? How does Bioaccumulation amplify this at each trophic level? What does this mean for human exposure?",
    "scenarios": [
        ("Current Trajectory", "Maintain current Plastic Input Rate with near-zero Decomposition -- project 50 years forward"),
        ("Plastic Reduction", "Reduce Plastic Input Rate by 50 percent -- observe how slowly concentrations decline due to persistence"),
        ("Trophic Amplification", "Track microplastic concentration from water to plankton to fish to humans -- observe biomagnification at each level")
    ],
    "sim_scenarios": [
        ("Current Trajectory", "Current input, zero decomposition, 50 years", "How much does ocean microplastic concentration increase over 50 years?"),
        ("50 Percent Reduction", "Half current input, existing stock persists", "If we cut plastic input in half today, how long until ocean concentrations drop?"),
        ("Trophic Cascade", "Track concentration through 4 trophic levels", "How much more microplastic does a tuna have compared to the water it swims in?")
    ],
    "discoveries": [
        "Microplastic concentration in the environment is essentially a one-way ratchet because decomposition is negligible compared to input",
        "Bioaccumulation amplifies concentration by 10-100x at each trophic level, meaning top predators carry enormously higher loads",
        "Reducing plastic input slows but does not reverse the problem because existing plastics persist for centuries",
        "Human exposure is significant and growing -- the average person ingests a credit card worth of plastic per week"
    ],
    "answer": "A plastic bag degrades into microplastics that enter waterways, flow to the ocean, and are ingested by plankton. Small fish eat thousands of plankton, concentrating the plastic. Larger fish eat hundreds of small fish, amplifying further. A tuna at the top of the chain carries millions of times more microplastic than the water around it. When you eat that tuna, you inherit the accumulated plastic from the entire food chain below it. Because plastic does not decompose, this is a one-way accumulation that only gets worse.",
    "stem_title": "Design a Microplastic Monitoring and Reduction System",
    "stem_mission": "Design a system that monitors microplastic levels across the food chain and identifies the most cost-effective intervention points.",
    "stem_scenario": "A coastal city's seafood industry is threatened by rising microplastic contamination. Design a monitoring system that tracks plastic from source to plate and a reduction strategy targeting the highest-impact intervention points.",
    "stem_questions": [
        "Where in the plastic pathway is intervention most effective -- at the source or in the environment?",
        "How would you monitor microplastic levels at different trophic levels?",
        "What is the lag time between reducing plastic input and seeing lower levels in seafood?"
    ],
    "stem_design_qs": [
        "What monitoring technologies would you deploy at each stage of the food chain?",
        "How would you prioritize between preventing new plastic input vs. removing existing microplastics?",
        "How would you communicate risk to consumers without destroying the fishing industry?",
        "What data would prove your intervention is working given the decades-long timescale?"
    ],
    "career": "Environmental Toxicologists study how pollutants move through ecosystems and affect organism health, earning $60,000-$115,000/year at EPA, consulting firms, and universities.",
    "images": {
        "cover": ("G09L2-L09-cover.png", "A photorealistic image showing microplastic particles visible in ocean water with marine life in the background, scientific macro photography style"),
        "landscape": ("G09L2-L09-landscape.png", "Diverse 14-15 year old students examining water samples under microscopes looking for microplastic particles in a modern lab"),
        "modeling": ("G09L2-L09-modeling.png", "Diverse students at computers building food chain bioaccumulation models showing concentration increasing at each trophic level"),
        "discussion": ("G09L2-L09-discussion.png", "A teacher leading discussion with diverse students about plastic pollution, food chain diagram with concentration data on smartboard"),
        "stem": ("G09L2-L09-stem.png", "Diverse students designing a coastal monitoring system with water sampling equipment, maps, and data analysis tools")
    },
    "pre_assessment": [
        "Where do you think the plastic from a water bottle ends up after you throw it away?",
        "What are microplastics and how do they get into the ocean?",
        "Draw a food chain and predict how a pollutant might move through it.",
        "How might eating fish expose you to microplastics?"
    ],
    "extend_components": [
        ("Chemical Leaching", "Rate at which toxic additives like phthalates and BPA leach from plastic particles into organism tissue"),
        ("Wastewater Treatment Efficiency", "Percentage of microplastics removed during municipal water treatment before discharge"),
        ("Bioremediation Potential", "The capacity of engineered organisms or enzymes to break down microplastics in the environment")
    ],
    "reflections": [
        "Why is microplastic accumulation essentially a one-way ratchet in your model?",
        "How does biomagnification create a disproportionate burden on top predators and humans?",
        "Why does reducing plastic input today not immediately solve the contamination problem?",
        "What are the limitations of modeling microplastic fate with only 7 components?",
        "How should society balance the benefits of plastic with its environmental persistence?"
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze how microplastic concentrations change across trophic levels and over time to identify patterns of bioaccumulation."),
        ("Disciplinary Core Idea", "LS2.B Cycles of Matter and Energy Transfer", "Matter cycles through ecosystems, but persistent pollutants like microplastics accumulate rather than cycle, concentrating at higher trophic levels."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students model how small-scale plastic inputs create large-scale concentration effects through biomagnification across trophic levels.")
    ],
    "cast_items": [
        "Model how microplastics bioaccumulate through food chains via trophic transfer",
        "Analyze why persistent pollutants create one-way accumulation problems",
        "Evaluate monitoring and intervention strategies at different points in the plastic pathway"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Which strategy would MOST reduce human microplastic exposure from seafood: (a) ocean cleanup, (b) reducing new plastic production, (c) cooking fish differently, (d) eating farmed fish?"),
        ("Constructed Response:", "Using your model, explain why a 50 percent reduction in plastic input today would take decades to produce a measurable reduction in seafood microplastic levels.")
    ],
    "background_intro": "An estimated 8 million metric tons of plastic enter the oceans every year. This plastic does not decompose -- it breaks into smaller and smaller pieces that enter food chains and accumulate in organisms, including humans.",
    "background_sections": [
        ("Sources of Microplastics", "Microplastics come from degradation of larger plastic waste, synthetic clothing fibers released in laundry, microbeads in personal care products, and tire wear. A single wash of synthetic clothing releases 700,000 microfibers."),
        ("Bioaccumulation Mechanics", "Organisms ingest microplastics by mistaking them for food or passively filtering contaminated water. Because plastic cannot be digested or excreted efficiently, it accumulates in tissues over the organism lifetime."),
        ("Trophic Amplification", "A small fish eats thousands of contaminated plankton. A larger fish eats hundreds of small fish. At each level, the predator inherits the accumulated plastic of all its prey. By the time you reach a top predator, concentrations can be millions of times higher than in the water."),
        ("Human Health Implications", "The average person ingests approximately 5 grams of plastic per week -- roughly the weight of a credit card. Microplastics have been found in human blood, lungs, and placenta. Health effects are still being studied but include inflammation, endocrine disruption, and cellular damage.")
    ],
    "lever_L": "Students identify plastic input, microplastic concentration, bioaccumulation, trophic transfer, organism health, decomposition rate, and human exposure as system components.",
    "lever_E": "Students map the one-way accumulation pathway from input through trophic levels to human exposure, identifying amplification at each step.",
    "lever_V": "Students build a model showing how bioaccumulation and biomagnification create disproportionate contamination at higher trophic levels.",
    "lever_Ev": "Students run current trajectory, reduction, and trophic amplification scenarios to understand timescales and intervention effectiveness.",
    "lever_R": "Students add chemical leaching, wastewater treatment, or bioremediation to explore additional intervention strategies.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Microplastics in ocean water", "say": "You eat a credit card worth of plastic every week. How does it get from a trash can to your dinner plate?", "do": "Show the statistic. Display microplastic images.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Goals and vocabulary", "say": "Today we trace the invisible journey of plastic through the entire food chain to your body.", "do": "Pre-teach bioaccumulation and biomagnification.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Kansas bag to California fish?", "say": "How does plastic from the middle of a continent end up in ocean fish thousands of miles away?", "do": "Quick-write: Trace the path of a plastic bag from trash to table.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "Seven components. A one-way ratchet. The plastic never goes away.", "do": "Preview why this system only accumulates.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "7 component cards", "say": "What can humans control? What is beyond our current ability to change?", "do": "Sort components. Discuss why decomposition rate is effectively zero.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect", "visual": "Food chain accumulation diagram", "say": "At each level of the food chain, concentration INCREASES. Why?", "do": "Map the amplification pathway. Calculate concentration ratios.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulate", "visual": "Three scenarios over decades", "say": "Even if we stopped ALL plastic today, how long until the ocean is clean?", "do": "Students discover the persistence problem through scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with concentration data", "say": "This is a problem that gets worse even when we start fixing it. That is the nature of persistence.", "do": "Discuss the timescale mismatch between human action and environmental response.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Monitoring system design", "say": "A fishing industry is at stake. Consumers are worried. Design a system that tracks and reduces the threat.", "do": "Groups design monitoring and intervention systems.", "time": "12 min"}
    ],
    "sort_reasoning": "Plastic Input Rate and Decomposition Rate are external because input can be controlled by policy and decomposition is a material property of plastic. Microplastic Concentration, Bioaccumulation, Trophic Transfer, Organism Health, and Human Exposure are internal ecosystem responses.",
    "relationships": [
        ("Plastic Input Rate to Microplastic Concentration", "POSITIVE (+)", "More plastic entering the environment increases the concentration of microplastic particles."),
        ("Decomposition Rate to Microplastic Concentration", "NEGATIVE (-)", "Faster decomposition would reduce concentration, but plastic decomposition is effectively zero."),
        ("Microplastic Concentration to Bioaccumulation Factor", "POSITIVE (+)", "Higher environmental concentration leads to more ingestion and accumulation in organisms."),
        ("Bioaccumulation to Trophic Transfer", "POSITIVE (+)", "More accumulated plastic in prey means more transferred to predators."),
        ("Trophic Transfer to Human Exposure", "POSITIVE (+)", "Higher trophic transfer concentrates more plastic in seafood consumed by humans."),
        ("Bioaccumulation to Marine Organism Health", "NEGATIVE (-)", "Higher plastic loads cause inflammation, organ damage, and reduced fitness."),
        ("Marine Organism Health to Trophic Transfer", "NEGATIVE (-)", "If organisms die from contamination, fewer are available as prey, potentially reducing but not eliminating transfer.")
    ],
    "sim_answers": [
        ("Current Trajectory", "With continued input and zero decomposition, ocean microplastic concentration roughly doubles every 15-20 years. Bioaccumulation and biomagnification mean top predator contamination increases even faster. Human exposure through seafood grows proportionally."),
        ("50 Percent Reduction", "Cutting plastic input by half slows the accumulation rate but does NOT reduce existing concentrations. Because decomposition is negligible, the ocean is essentially a one-way sink. Concentrations continue to rise, just more slowly. Meaningful reduction in seafood contamination would take decades to centuries.")
    ],
    "reflection_exemplars": [
        ("Why is this a one-way ratchet?", "The model shows that microplastic concentration can only increase over time because input is substantial while decomposition is negligible. Even reducing input to zero would not reduce existing concentrations. The only pathway for removal is physical extraction, which is impractical at ocean scale. This is fundamentally different from biodegradable pollutants that cycle through the system."),
        ("How does biomagnification work?", "At each trophic level, an organism consumes many individuals from the level below. A fish eats thousands of contaminated plankton, inheriting the accumulated plastic from all of them. A tuna eats hundreds of fish. The concentration amplifies at each step because plastic is ingested but not excreted. By the top of the food chain, concentrations are millions of times higher than in the water.")
    ],
    "stem_intro": "A coastal city's seafood industry faces microplastic contamination threats. Students design monitoring systems and reduction strategies targeting the highest-impact intervention points.",
    "stem_concepts": [
        ("Multi-Level Monitoring", "Tracking microplastic concentrations at multiple trophic levels reveals where amplification is greatest and where intervention would be most effective."),
        ("Source Reduction vs. Environmental Cleanup", "Preventing plastic from entering the environment is orders of magnitude more cost-effective than removing it from the ocean."),
        ("Timescale Mismatch", "Policy changes today will not produce measurable seafood contamination reductions for decades due to the persistence of existing plastic. Expectations must be set accordingly.")
    ],
    "stem_eval": [
        ("Expert (4)", "System monitors multiple trophic levels, identifies highest-impact intervention points, addresses the persistence timescale, and communicates risk responsibly"),
        ("Proficient (3)", "System monitors contamination levels, recommends source-reduction strategies, and uses model evidence"),
        ("Developing (2)", "System monitors some contamination but does not address the timescale problem or trophic amplification"),
        ("Beginning (1)", "System is incomplete or does not connect monitoring to the food chain accumulation model")
    ],
    "support": [
        "Pre-drawn food chain diagram with concentration increasing at each level shown numerically",
        "Use a savings account analogy: if you deposit money daily and never withdraw, the balance only goes up. Plastic in the ocean works the same way.",
        "Sentence frames: At trophic level __, concentration is __ times higher than level __ because each predator consumes __ prey organisms"
    ],
    "extensions": [
        "Research plastic-eating enzymes like PETase and model how introducing bioremediation would change the Decomposition Rate component",
        "Calculate the total mass of microplastic in the ocean using current concentration data and ocean volume, then project 50 years forward",
        "Compare microplastic biomagnification to DDT biomagnification in the 1960s and analyze why we did not learn from history"
    ],
    "cross_curr": [
        ("Math", "Calculate biomagnification factors: if plankton has 1 particle per gram, small fish has 100 per gram, and tuna has 10,000 per gram, what is the transfer efficiency at each trophic level?"),
        ("ELA", "Write a consumer guide explaining microplastic risks in seafood, balancing scientific accuracy with accessible communication."),
        ("Social Studies", "Research the global plastic waste trade and analyze why developing nations disproportionately bear the burden of plastic pollution from wealthy nations.")
    ],
    "misconceptions": [
        ("The ocean is so big that plastic gets diluted to harmless levels", "The ocean is large but plastic does not dilute -- it concentrates. Bioaccumulation means organisms collect and concentrate plastic from the water. Biomagnification means each trophic level amplifies further. A tuna contains millions of times more microplastic per gram than the ocean water it swims in.", "If you drink a glass of water with 1 particle per liter, that seems harmless. Now eat a fish that drank 10,000 liters. You just ingested 10,000 particles in one meal."),
        ("Recycling solves the plastic problem", "Only 9 percent of all plastic ever made has been recycled. Most plastic is used once and discarded. Recycling slows input but does not address the 5+ billion metric tons already in the environment. And recycled plastic still eventually becomes microplastic.", "Ask: If 91 percent of your homework went in the trash, would you call your system working?"),
        ("Microplastics are too small to cause harm", "Microplastics carry toxic additives like phthalates and BPA that leach into tissue. They cause physical inflammation when lodged in organs. They have been found in human blood, lungs, liver, and placenta. The health effects of chronic low-level exposure are still being studied, but early evidence suggests inflammation, endocrine disruption, and cellular damage.", "Would you eat a credit card? You already are -- approximately 5 grams per week.")
    ]
}

L10 = {
    "id": "G09L2-L10",
    "title": "Renewable Energy Grid Optimization: Powering the Future",
    "subtitle": "Modeling the Complex Challenge of a 100 Percent Clean Energy Grid",
    "ngss": "HS-PS3-3, HS-ETS1-3",
    "ngss_desc": "Design, build, and refine a device that works within given constraints to convert one form of energy into another. Evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs.",
    "big_question": "Why can't we just replace all fossil fuel power plants with solar panels and wind turbines tomorrow?",
    "objectives": [
        "Model how intermittent renewable energy sources interact with grid demand, storage, and backup systems",
        "Analyze the optimization challenge of balancing cost, reliability, and emissions across an 8-component grid system",
        "Evaluate trade-offs between different energy mixes under varying demand and weather conditions",
        "Design a grid management strategy that achieves maximum renewable penetration while maintaining reliability"
    ],
    "vocabulary": [
        ("Grid Intermittency", "The variable and partially unpredictable nature of solar and wind energy production, which depends on weather rather than human control"),
        ("Energy Storage", "Technologies like batteries, pumped hydro, and hydrogen that store excess renewable energy for use when production is low"),
        ("Dispatchable Generation", "Power sources like natural gas or hydroelectric that can be turned on and off on demand to fill gaps in renewable production"),
        ("Grid Balancing", "The continuous process of matching electricity supply to demand in real time, which becomes more complex with intermittent sources")
    ],
    "components": [
        ("Solar Output", "Electricity generated from photovoltaic panels, varying with time of day, season, and cloud cover", False),
        ("Wind Output", "Electricity generated from wind turbines, varying with wind speed and weather patterns", False),
        ("Battery Storage", "Energy stored in lithium-ion or other battery systems that can be charged when supply exceeds demand", False),
        ("Grid Demand", "Total electricity consumption by residential, commercial, and industrial users at any given time", True),
        ("Fossil Fuel Backup", "Natural gas or other dispatchable generation used to fill gaps when renewables and storage cannot meet demand", True),
        ("Transmission Efficiency", "The percentage of generated electricity that reaches consumers after transmission and distribution losses", False),
        ("Cost per kWh", "The total cost of electricity including generation, storage, transmission, and backup costs", False),
        ("Carbon Emissions", "Total CO2 and equivalent greenhouse gas emissions from the energy system", False)
    ],
    "think_about_it": "When Solar Output drops to zero at night and Wind Output is calm, how does Grid Demand get met? What happens to Cost per kWh when Battery Storage runs out and Fossil Fuel Backup kicks in? How do you minimize Carbon Emissions while keeping the lights on?",
    "scenarios": [
        ("Sunny Windy Day", "Maximum solar and wind output -- observe how excess is stored and costs drop"),
        ("Calm Winter Night", "Zero solar, minimal wind -- observe battery depletion and fossil backup activation"),
        ("Optimal Mix", "Find the combination of solar, wind, storage, and backup that minimizes both cost and emissions")
    ],
    "sim_scenarios": [
        ("Sunny Windy Day", "Peak solar, strong wind, moderate demand", "What happens to battery storage when supply exceeds demand? Where does the excess go?"),
        ("Worst Case", "Zero solar, calm wind, peak demand", "How long do batteries last? When does fossil backup kick in?"),
        ("Optimization", "Vary mix to minimize cost and emissions", "What percentage of renewables achieves the best balance of cost, reliability, and emissions?")
    ],
    "discoveries": [
        "The last 10-20 percent of fossil fuel replacement is exponentially harder than the first 80 percent due to intermittency gaps",
        "Battery storage is essential but currently too expensive to cover multi-day renewable droughts without fossil backup",
        "Overbuilding renewable capacity to handle worst-case scenarios dramatically increases cost but reduces emissions",
        "Geographic diversity helps -- connecting solar-rich and wind-rich regions reduces the probability of system-wide intermittency"
    ],
    "answer": "We cannot simply swap fossil plants for renewables because the sun and wind are intermittent -- they produce power when nature allows, not when humans need it. At night, on calm days, and during storms, renewable output drops to zero. Batteries can bridge short gaps but cannot economically cover multi-day droughts. Some fossil fuel backup remains necessary for reliability until storage technology improves dramatically. The optimization challenge is finding the mix of solar, wind, storage, and backup that minimizes cost AND emissions while keeping the grid reliable 99.97 percent of the time.",
    "stem_title": "Design a Regional Clean Energy Grid",
    "stem_mission": "Design the optimal energy mix for a region that achieves maximum renewable penetration while maintaining grid reliability and minimizing cost.",
    "stem_scenario": "A region of 5 million people must achieve 90 percent clean energy by 2035. Design the energy portfolio: how much solar, wind, storage, and backup do you need? What does it cost? How reliable is it during extreme weather?",
    "stem_questions": [
        "What energy mix provides the best balance of cost, emissions, and reliability?",
        "How much battery storage is needed to bridge typical renewable gaps?",
        "What happens to your grid during a week-long cloudy calm period?"
    ],
    "stem_design_qs": [
        "How would you distribute solar and wind installations geographically?",
        "What types of storage would you deploy -- batteries, pumped hydro, hydrogen?",
        "How would you handle seasonal variation in solar output?",
        "What is the minimum fossil fuel backup needed to maintain 99.97 percent reliability?"
    ],
    "career": "Grid Engineers and Energy Systems Analysts design and optimize electrical grids for the clean energy transition, earning $75,000-$140,000/year at utilities, grid operators, energy companies, and government agencies.",
    "images": {
        "cover": ("G09L2-L10-cover.png", "A photorealistic cinematic image of a modern wind and solar farm at golden hour with massive battery storage containers in the foreground, power lines stretching to a city skyline"),
        "landscape": ("G09L2-L10-landscape.png", "Diverse 14-15 year old students studying energy grid data on monitors showing real-time solar and wind output graphs"),
        "modeling": ("G09L2-L10-modeling.png", "Diverse students at computers building energy grid optimization models with supply-demand curves and storage levels on screens"),
        "discussion": ("G09L2-L10-discussion.png", "A teacher leading discussion with diverse students about energy trade-offs, pie charts of energy mixes on smartboard"),
        "stem": ("G09L2-L10-stem.png", "Diverse students designing a regional energy grid with maps, energy mix calculators, and cost-emission optimization dashboards")
    },
    "pre_assessment": [
        "Why can't we just replace all power plants with solar panels?",
        "What happens to electricity supply when the sun sets or the wind stops?",
        "Draw a diagram showing how electricity gets from a solar panel to your home.",
        "What are the pros and cons of different energy sources?"
    ],
    "extend_components": [
        ("Hydrogen Storage", "Long-duration energy storage using excess renewable electricity to produce hydrogen via electrolysis"),
        ("Nuclear Baseload", "Constant-output nuclear power providing reliable baseload electricity independent of weather"),
        ("Demand Response", "Smart grid systems that shift flexible electricity demand to match renewable availability")
    ],
    "reflections": [
        "Why is the last 20 percent of decarbonization so much harder than the first 80 percent?",
        "What role does energy storage play in enabling higher renewable penetration?",
        "How do trade-offs between cost, emissions, and reliability constrain grid design?",
        "Why might geographic diversity of renewable installations reduce intermittency risk?",
        "What technology breakthroughs would most change your optimal grid design?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students optimize multi-variable energy systems, balancing competing objectives using computational models and scenario analysis."),
        ("Disciplinary Core Idea", "PS3.D Energy in Chemical Processes and Everyday Life", "Energy transformation from solar radiation and wind kinetic energy to electrical energy involves efficiency losses and intermittency challenges."),
        ("Crosscutting Concept", "Energy and Matter", "Students model energy flows through a grid system, tracking generation, storage, transmission losses, and consumption.")
    ],
    "cast_items": [
        "Model how intermittent renewable sources interact with storage and backup to meet grid demand",
        "Analyze the optimization trade-offs between cost, reliability, and carbon emissions",
        "Design a grid energy mix that achieves maximum renewable penetration with acceptable reliability"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Which factor MOST limits how much renewable energy a grid can use: (a) panel/turbine cost, (b) storage cost and capacity, (c) transmission distance, (d) public opinion?"),
        ("Constructed Response:", "Using your model, explain why a grid with 80 percent renewables might cost twice as much as one with 50 percent renewables, even though the additional solar panels are cheap.")
    ],
    "background_intro": "The clean energy transition is the defining engineering challenge of our generation. While renewable energy costs have plummeted, the fundamental challenge of intermittency remains: the sun does not always shine, the wind does not always blow, and society demands electricity 24/7.",
    "background_sections": [
        ("The Intermittency Challenge", "Solar produces maximum power at noon but zero at night. Wind varies hourly and seasonally. Grid operators must match supply to demand in real time. Even a few minutes of mismatch causes blackouts. Fossil fuel plants can be turned on and off as needed -- renewables cannot."),
        ("The Storage Gap", "Current battery technology can bridge hours of intermittency but not days or weeks. A week-long calm, cloudy period would exhaust any economically feasible battery system. Alternative storage like pumped hydro and hydrogen is promising but limited by geography and cost."),
        ("The Last 20 Percent Problem", "Getting to 50-60 percent renewables is relatively straightforward. Getting to 80 percent requires massive storage. Getting to 100 percent requires solving multi-day and seasonal intermittency gaps that current technology cannot economically address. Each additional percent of renewables costs more than the last."),
        ("Grid Physics", "Electricity must be consumed the instant it is generated. The grid operates at exactly 60 Hz and must be balanced continuously. Too much supply raises frequency; too little drops it. Either extreme damages equipment and causes cascading failures. This physical constraint makes grid management fundamentally different from other optimization problems.")
    ],
    "lever_L": "Students identify solar output, wind output, battery storage, grid demand, fossil backup, transmission efficiency, cost per kWh, and carbon emissions as the 8 grid components.",
    "lever_E": "Students map supply-demand dynamics: renewables feed demand directly, excess charges batteries, batteries discharge when needed, fossil backup fills remaining gaps.",
    "lever_V": "Students build a model optimizing the trade-offs between cost, emissions, and reliability across different energy mixes.",
    "lever_Ev": "Students run sunny, worst-case, and optimization scenarios to find the best achievable energy mix.",
    "lever_R": "Students add hydrogen storage, nuclear baseload, or demand response to explore advanced grid strategies.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Solar/wind farm with battery storage and city", "say": "Why can't we just flip a switch to clean energy? The answer is more complicated than you think.", "do": "Show the intermittency problem visually: solar output over 24 hours vs. demand.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Goals and vocabulary", "say": "Today we optimize the most complex engineering problem of our generation.", "do": "Pre-teach intermittency and grid balancing.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why not just use solar and wind?", "say": "Solar panels are cheap. Wind turbines work great. So why are we still burning fossil fuels?", "do": "Quick-write: What happens to electricity supply at night?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "Eight components. Three competing objectives. This is real engineering.", "do": "Preview the optimization challenge: minimize cost, minimize emissions, maximize reliability.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "8 component cards", "say": "Which of these can we control? Which are set by physics?", "do": "Sort components. Discuss why weather determines solar and wind output.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect", "visual": "Supply-demand flow diagram", "say": "Energy flows from generation through storage to demand. Map the pathways.", "do": "Map energy flows. Identify where gaps occur and how each component fills them.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulate", "visual": "Optimization scenarios", "say": "Find the mix that keeps the lights on AND saves the planet. What trade-offs do you make?", "do": "Students optimize energy mix across competing objectives.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with optimization curves", "say": "The last 20 percent is the hardest. Your model shows you why.", "do": "Discuss the exponential difficulty curve and what technology changes would help.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Regional grid design", "say": "5 million people need 90 percent clean energy by 2035. Design the grid.", "do": "Groups design complete energy portfolios with cost and emissions analysis.", "time": "12 min"}
    ],
    "sort_reasoning": "Grid Demand and Fossil Fuel Backup are external because demand is set by consumers and backup is a policy choice. Solar Output, Wind Output, Battery Storage, Transmission Efficiency, Cost per kWh, and Carbon Emissions are internal system responses determined by the energy mix and physics.",
    "relationships": [
        ("Solar Output to Battery Storage", "POSITIVE (+)", "Excess solar output beyond demand charges batteries."),
        ("Wind Output to Battery Storage", "POSITIVE (+)", "Excess wind output charges batteries."),
        ("Grid Demand to Battery Storage", "NEGATIVE (-)", "Higher demand depletes battery reserves faster."),
        ("Battery Storage to Fossil Fuel Backup", "NEGATIVE (-)", "More available storage reduces the need for fossil backup."),
        ("Fossil Fuel Backup to Carbon Emissions", "POSITIVE (+)", "More fossil fuel use directly increases carbon emissions."),
        ("Fossil Fuel Backup to Cost per kWh", "POSITIVE (+)", "Fossil fuel operation adds fuel costs to the electricity price."),
        ("Battery Storage to Cost per kWh", "POSITIVE (+)", "Storage infrastructure is expensive, raising overall cost."),
        ("Transmission Efficiency to Cost per kWh", "NEGATIVE (-)", "Higher efficiency reduces waste and lowers per-unit cost.")
    ],
    "sim_answers": [
        ("Sunny Windy Day", "With maximum solar and wind, supply far exceeds demand. Excess energy charges batteries to full capacity. Fossil backup is not needed. Cost per kWh is at its lowest and carbon emissions approach zero. This is the ideal scenario that occurs perhaps 30-40 percent of the time."),
        ("Worst Case", "With zero solar and calm wind, batteries discharge rapidly. Depending on capacity, they last 4-12 hours. Once depleted, fossil backup activates, sharply increasing emissions and cost. This scenario reveals why 100 percent renewables requires solving the multi-day storage problem.")
    ],
    "reflection_exemplars": [
        ("Why is the last 20 percent hardest?", "Getting to 80 percent renewables mostly requires overbuilding solar and wind to handle average demand. But the last 20 percent requires handling the WORST-CASE scenario: multiple days of low sun and wind. The storage needed for worst-case is vastly more expensive than for average-case. Each additional percentage point requires exponentially more storage investment."),
        ("What trade-offs constrain grid design?", "Cost, reliability, and emissions form a three-way trade-off. Minimizing emissions requires massive renewable overbuilding and storage (expensive). Minimizing cost favors some fossil backup (increases emissions). Maximizing reliability requires dispatchable backup (either expensive storage or fossil fuel). No design optimizes all three simultaneously.")
    ],
    "stem_intro": "A region of 5 million people must reach 90 percent clean energy by 2035. Students design the optimal portfolio balancing solar, wind, storage, and backup.",
    "stem_concepts": [
        ("Capacity Factor", "Solar panels produce power about 25 percent of the time, wind turbines about 35 percent. You must install 3-4x the capacity to generate the equivalent of a 100 percent-available source."),
        ("Duration Matching", "Batteries handle hourly gaps. Pumped hydro handles daily gaps. Hydrogen or nuclear handles seasonal gaps. The right storage depends on the gap duration."),
        ("Geographic Diversification", "Connecting distant solar and wind regions reduces the probability of system-wide intermittency. When one region is cloudy, another may be sunny.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design optimizes all three objectives with quantified trade-offs, handles worst-case scenarios, uses geographic diversity, and justifies all choices with model evidence"),
        ("Proficient (3)", "Design achieves high renewable penetration, addresses storage needs, and quantifies cost and emissions"),
        ("Developing (2)", "Design includes renewables and storage but does not address worst-case scenarios or quantify trade-offs"),
        ("Beginning (1)", "Design is incomplete or does not account for intermittency and grid reliability")
    ],
    "support": [
        "Pre-drawn supply-demand graph showing solar output, wind output, battery charge/discharge, and fossil backup over 24 hours",
        "Use a bank account analogy: renewables are your income (variable), batteries are your savings, fossil is a credit card (costly but always available)",
        "Sentence frames: When renewable output drops below demand by __ MW, batteries can cover __ hours before fossil backup must provide __ MW"
    ],
    "extensions": [
        "Research the duck curve phenomenon in California and model how overproduction midday creates grid management challenges",
        "Calculate the battery capacity needed to power your city for 3 days of zero renewable output and estimate the cost",
        "Compare grid strategies: Germany's wind-heavy approach vs. Australia's solar-heavy approach vs. France's nuclear baseload"
    ],
    "cross_curr": [
        ("Math", "Calculate the capacity factor-adjusted cost: if solar panels cost $1 per watt but produce power 25 percent of the time, what is the effective cost per watt of reliable power?"),
        ("ELA", "Write an opinion piece evaluating whether 100 percent renewable energy is achievable by 2050, using model evidence to support your argument."),
        ("Social Studies", "Research energy justice: who benefits from cheap renewables and who is burdened by grid infrastructure like transmission lines and battery factories?")
    ],
    "misconceptions": [
        ("Renewables are too expensive", "Solar and wind are now the CHEAPEST sources of new electricity generation. The cost challenge is in STORAGE and grid integration, not generation. The total system cost including storage is higher than generation alone, but still competitive with new fossil fuel plants in most regions.", "Separate the costs: solar panels are cheap. Batteries are expensive. The headline cost of solar is misleading because it does not include the storage needed to make it reliable."),
        ("We can go 100 percent renewable immediately", "The intermittency problem makes 100 percent renewables extremely challenging with current technology. Multi-day and seasonal gaps require storage capacity that does not yet exist at affordable scale. A rapid transition without adequate storage would cause blackouts.", "Model it: run your grid through a week of cloudy calm weather. How much storage do you need? Now price it. That is why the transition takes time."),
        ("Nuclear is too dangerous for clean energy", "Modern nuclear power has the lowest death rate per unit of energy of any source, including solar and wind. It provides reliable, zero-carbon baseload power that complements intermittent renewables. The main challenges are cost, construction time, and waste storage -- not safety.", "Compare data: nuclear causes 0.03 deaths per TWh. Coal causes 24.6. Even solar causes 0.05 from manufacturing and installation accidents. Nuclear is statistically the safest.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
