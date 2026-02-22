#!/usr/bin/env python3
"""Complete lesson data for G08-L01 through G08-L10 (Grade 8 ModelIt! Lessons)"""

L01 = {
    "id": "G08-L01",
    "title": "Superbugs: Evolution You Can See",
    "subtitle": "Why Antibiotics Are Losing the War Against Bacteria",
    "ngss": "MS-LS4-4, MS-LS4-6",
    "ngss_desc": "Construct an explanation based on evidence that describes how genetic variations of traits in a population increase some individuals' probability of surviving and reproducing in a specific environment. Use mathematical representations to support explanations of how natural selection may lead to increases and decreases of specific traits in populations over time.",
    "big_question": "Why are bacteria becoming impossible to kill?",
    "objectives": [
        "Explain how random genetic mutations create variation in bacterial populations",
        "Model how antibiotic use selects for resistant bacteria over generations",
        "Predict how misuse of antibiotics accelerates resistance evolution",
        "Evaluate real-world strategies for slowing antibiotic resistance"
    ],
    "vocabulary": [
        ("Antibiotic Resistance", "The ability of bacteria to survive exposure to antibiotics that once killed them"),
        ("Natural Selection", "The process where organisms with favorable traits survive and reproduce more"),
        ("Mutation", "A random change in DNA that can create new traits"),
        ("Selective Pressure", "An environmental factor that favors certain traits over others")
    ],
    "components": [
        ("Antibiotic Use", "Frequency and dosage of antibiotic treatment in a population", True),
        ("Mutation Rate", "Rate at which random genetic changes occur in bacterial DNA", True),
        ("Resistant Bacteria", "Percentage of bacteria that survive antibiotic treatment", False),
        ("Treatment Effectiveness", "How well antibiotics kill bacterial infections", False)
    ],
    "think_about_it": "When antibiotic use increases, what happens to the percentage of resistant bacteria in the population over time?",
    "scenarios": [
        ("Normal Treatment", "Set Antibiotic Use and Mutation Rate to moderate levels"),
        ("Overuse Crisis", "Lock Antibiotic Use to 100% and observe what happens over 20 generations"),
        ("Smart Use", "Set Antibiotic Use to 30% and compare to overuse results")
    ],
    "sim_scenarios": [
        ("Normal Treatment", "Moderate antibiotic use, normal mutation rate", "What do you predict will happen to Treatment Effectiveness over time?"),
        ("Antibiotic Overuse", "Lock Antibiotic Use to 100%", "What do you predict will happen to the Resistant Bacteria population?"),
        ("Responsible Use", "Set Antibiotic Use to 30%", "How does this compare to the overuse scenario?")
    ],
    "discoveries": [
        "Random mutations create resistant bacteria BEFORE antibiotics are even used",
        "Antibiotics don't cause resistance — they SELECT for bacteria that already have it",
        "Overuse accelerates the evolution of resistant populations dramatically",
        "Reducing antibiotic use slows resistance evolution but doesn't reverse it instantly"
    ],
    "answer": "Antibiotics kill susceptible bacteria but leave resistant ones alive to reproduce. Over many generations, the population evolves to be mostly resistant — creating superbugs!",
    "stem_title": "Design a Hospital Antibiotic Policy",
    "stem_mission": "Design an evidence-based antibiotic use policy for a hospital that minimizes resistance evolution while still effectively treating infections.",
    "stem_scenario": "A hospital is seeing increasing antibiotic-resistant infections in patients. The medical director needs your team to propose a new policy using evidence from your model.",
    "stem_questions": [
        "What antibiotic use level minimizes resistance while still treating infections?",
        "How should doctors decide when to prescribe antibiotics vs. when to wait?",
        "What role does completing the full course of antibiotics play?"
    ],
    "stem_design_qs": [
        "What guidelines will you set for when antibiotics should be prescribed?",
        "How will you monitor resistance levels in the hospital?",
        "What education program will you create for patients?",
        "How will you measure if your policy is working?"
    ],
    "career": "Epidemiologists and Microbiologists track antibiotic resistance patterns worldwide and develop strategies to combat superbugs. They earn $80,000-$130,000/year.",
    "images": {
        "cover": ("cover-superbugs.png", "A dramatic microscope view of colorful bacteria colonies on a petri dish with some glowing resistant bacteria surviving, scientific laboratory setting"),
        "landscape": ("landscape-bacteria.png", "8th grade students in a modern science lab examining petri dishes under microscopes, wearing safety goggles, engaged and curious"),
        "modeling": ("modeling-evolution.png", "A diverse group of 8th grade students working together on laptops building a digital model, modern classroom with science posters about evolution"),
        "discussion": ("discussion-superbugs.png", "A teacher leading a discussion with engaged 8th grade students about antibiotic resistance, students debating with hands raised, classroom with natural light"),
        "stem": ("stem-hospital-policy.png", "8th grade students presenting a poster about hospital antibiotic policy to classmates, professional presentation style, modern classroom")
    },
    "pre_assessment": [
        "What are antibiotics and what do they do?",
        "Why do you think some infections are harder to treat than others?",
        "What does 'survival of the fittest' mean to you?",
        "Draw what you think happens when bacteria meet an antibiotic."
    ],
    "extend_components": [
        ("Horizontal Gene Transfer", "Bacteria can share resistance genes with nearby bacteria"),
        ("Immune System Strength", "A stronger immune system can fight bacteria alongside antibiotics"),
        ("Biofilm Formation", "Bacteria form protective communities that resist treatment")
    ],
    "reflections": [
        "Why is it dangerous to stop taking antibiotics when you feel better but before the course is done?",
        "How is antibiotic resistance an example of natural selection happening in real time?",
        "Why might using antibiotics in livestock farming increase resistance in human diseases?",
        "What would happen to modern medicine if antibiotics stop working completely?",
        "How does your model show that evolution is NOT random, even though mutations ARE random?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how natural selection drives antibiotic resistance."),
        ("Disciplinary Core Idea", "LS4.B Natural Selection", "Natural selection leads to the predominance of certain traits in a population and the suppression of others."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that antibiotic overuse CAUSES the selection pressure that leads to the EFFECT of resistant populations.")
    ],
    "cast_items": [
        "Explain how natural selection can change the traits of a population over time",
        "Use evidence to support how environmental changes affect survival",
        "Apply mathematical thinking to describe changes in trait frequencies"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A population of bacteria is exposed to an antibiotic. After 10 generations, 90% of the population is resistant. Which best explains this change?"),
        ("Constructed Response:", "Using the concept of natural selection, explain why antibiotic-resistant bacteria have become more common in hospitals over the past 50 years.")
    ],
    "background_intro": "Antibiotic resistance is one of the most urgent public health crises of the 21st century. The WHO has called it a 'global health emergency.' Understanding the evolutionary mechanisms behind resistance is essential for developing strategies to combat it.",
    "background_sections": [
        ("How Resistance Develops", "Bacterial populations contain natural genetic variation due to random mutations. Some bacteria happen to carry genes that provide resistance to antibiotics. When antibiotics are applied, susceptible bacteria die while resistant ones survive and reproduce, passing on their resistance genes. This is natural selection in action."),
        ("The Overuse Problem", "When antibiotics are overprescribed, used for viral infections (where they don't work), or not completed as prescribed, they create stronger selective pressures. Agricultural use of antibiotics in livestock accounts for roughly 70% of all antibiotic use in the U.S."),
        ("MRSA and Other Superbugs", "Methicillin-resistant Staphylococcus aureus (MRSA) is one of the most well-known superbugs. It evolved resistance to multiple antibiotics and kills approximately 20,000 Americans per year. Other concerning superbugs include CRE, VRE, and drug-resistant tuberculosis."),
        ("Mathematical Modeling", "Resistance evolution can be modeled mathematically using population genetics equations. The rate of resistance increase depends on: initial frequency of resistant alleles, strength of selective pressure (antibiotic use), fitness cost of resistance, and population size.")
    ],
    "lever_L": "Students identify antibiotic use, mutation rate, resistant bacteria percentage, and treatment effectiveness as system components.",
    "lever_E": "Students determine that antibiotic use positively affects resistant bacteria percentage (by selecting for them) but negatively affects treatment effectiveness.",
    "lever_V": "Students build the resistance evolution model showing how selection pressure drives population change.",
    "lever_Ev": "Students run overuse vs. responsible use scenarios and compare the rate of resistance evolution.",
    "lever_R": "Students add horizontal gene transfer or immune system components to make the model more realistic.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with superbug imagery", "say": "Have you ever taken antibiotics? What if they stopped working?", "do": "Share a real news headline about superbugs to build urgency.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're modeling evolution happening in real time — right now, in hospitals.", "do": "Have students read objectives. Pre-teach 'mutation' vs. 'natural selection.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why are bacteria becoming impossible to kill?", "say": "This isn't science fiction. The WHO calls this a global health emergency.", "do": "Poll: How many students have taken antibiotics? Why were they prescribed?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll use modeling to understand how evolution creates superbugs.", "do": "Briefly preview each LEVER step.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for resistance model", "say": "What are the key parts of this system? What can we control vs. what happens on its own?", "do": "Guide sorting; emphasize that mutation is RANDOM but selection is NOT.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Here's the key insight: antibiotics don't CAUSE resistance — they SELECT for it.", "do": "Demonstrate positive/negative relationships. Focus on the counterintuitive idea.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's see what happens when we overuse antibiotics vs. use them responsibly.", "do": "Have students predict before running. Compare overuse vs. smart use graphs.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "What did our model reveal? How does this change how you think about antibiotics?", "do": "Lead whole-class discussion. Connect to real MRSA data.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Hospital policy design challenge", "say": "You're now consultants for a hospital. Design a policy to fight superbugs.", "do": "Distribute materials. Circulate and ask probing questions about evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Antibiotic Use and Mutation Rate are external because they are inputs from outside the bacterial population — doctors control antibiotic use and mutation rate is a natural process. Resistant Bacteria and Treatment Effectiveness are internal because they change as a result of those external inputs.",
    "relationships": [
        ("Antibiotic Use to Resistant Bacteria", "POSITIVE (+)", "More antibiotic use creates stronger selective pressure, allowing resistant bacteria to outcompete susceptible ones."),
        ("Mutation Rate to Resistant Bacteria", "POSITIVE (+)", "Higher mutation rates create more genetic variation, increasing the chance of resistance genes appearing."),
        ("Resistant Bacteria to Treatment Effectiveness", "NEGATIVE (-)", "As the percentage of resistant bacteria increases, antibiotics become less effective at treating infections.")
    ],
    "sim_answers": [
        ("Overuse Scenario", "When Antibiotic Use is locked at 100%, Resistant Bacteria percentage climbs rapidly within 10-20 generations. Treatment Effectiveness crashes. The antibiotics are selecting so strongly that only resistant bacteria survive to reproduce."),
        ("Responsible Use Scenario", "At 30% Antibiotic Use, Resistant Bacteria still increase but MUCH more slowly. Treatment Effectiveness declines gradually rather than crashing. There's a much longer window where antibiotics remain useful.")
    ],
    "reflection_exemplars": [
        ("Why stop taking antibiotics early is dangerous?", "When you stop early, you kill the most susceptible bacteria but leave partially-resistant ones alive. Those survivors reproduce, and the next generation is harder to kill. You've essentially trained the bacteria to resist that antibiotic."),
        ("How is this natural selection in real time?", "The three requirements for natural selection are variation (mutations create different resistance levels), selection pressure (antibiotics kill susceptible ones), and inheritance (survivors pass resistance genes to offspring). All three are happening with every dose of antibiotics.")
    ],
    "stem_intro": "Present a scenario: A hospital reports that 40% of staph infections are now MRSA. The medical director needs your team's evidence-based policy recommendations.",
    "stem_concepts": [
        ("Antibiotic Stewardship", "Programs that optimize when and how antibiotics are prescribed to slow resistance."),
        ("Diagnostic Testing", "Rapid tests that identify whether an infection is bacterial before prescribing antibiotics."),
        ("Combination Therapy", "Using multiple antibiotics together makes it harder for bacteria to evolve resistance to all of them simultaneously.")
    ],
    "stem_eval": [
        ("Expert (4)", "Policy uses model evidence, addresses multiple strategies, and includes a monitoring plan"),
        ("Proficient (3)", "Policy references model data and includes at least two evidence-based strategies"),
        ("Developing (2)", "Policy mentions resistance but lacks specific evidence from the model"),
        ("Beginning (1)", "Policy doesn't connect to model findings or natural selection concepts")
    ],
    "support": [
        "Provide visual diagram showing bacteria generations (before/after antibiotic exposure)",
        "Use color-coded tokens to physically model resistant vs. susceptible bacteria",
        "Sentence frames: 'When antibiotic use increases, resistant bacteria __ because __'"
    ],
    "extensions": [
        "Research MRSA statistics and calculate the rate of increase over decades",
        "Model horizontal gene transfer as an additional component",
        "Debate: Should antibiotics in livestock farming be banned?"
    ],
    "cross_curr": [
        ("Math", "Calculate the percentage change in resistant bacteria per generation using exponential growth models"),
        ("ELA", "Write a persuasive letter to a hospital board recommending an antibiotic stewardship program"),
        ("Social Studies", "Research the global impact of antibiotic resistance on developing countries")
    ],
    "misconceptions": [
        ("Antibiotics make bacteria resistant", "Antibiotics don't CREATE resistance — they SELECT for bacteria that already have resistance due to random mutations. The resistance genes existed before the antibiotic was ever used.", "Ask: If I spray weed killer on a lawn and some weeds survive, did the weed killer teach them to survive?"),
        ("Evolution takes millions of years", "Bacteria can evolve noticeable resistance in days or weeks because they reproduce so quickly (every 20 minutes). Evolution by natural selection can be observed in real time.", "Show data on how quickly MRSA evolved from discovery of methicillin."),
        ("If I feel better, I can stop antibiotics", "Stopping early kills the weakest bacteria but leaves the most resistant ones alive to reproduce. Completing the full course ensures even partially-resistant bacteria are killed.", "Connect to the model: What happens in a half-dose scenario?")
    ]
}

L02 = {
    "id": "G08-L02",
    "title": "The Reef Is Bleaching",
    "subtitle": "Why the World's Most Colorful Ecosystems Are Turning White",
    "ngss": "MS-LS2-1, MS-LS2-4",
    "ngss_desc": "Analyze and interpret data to provide evidence for the effects of resource availability on organisms and populations of organisms in an ecosystem. Construct an argument supported by empirical evidence that changes to physical or biological components of an ecosystem affect populations.",
    "big_question": "Why are coral reefs turning white and dying?",
    "objectives": [
        "Explain the symbiotic relationship between coral and zooxanthellae algae",
        "Model how rising ocean temperature disrupts the coral reef ecosystem",
        "Predict cascade effects when one component of an ecosystem is disrupted",
        "Evaluate human impacts on marine ecosystems using model evidence"
    ],
    "vocabulary": [
        ("Coral Bleaching", "When stressed coral expels its symbiotic algae, turning white and losing its energy source"),
        ("Symbiosis", "A close, long-term relationship between two different organisms that benefits at least one"),
        ("Ecosystem Services", "The benefits that healthy ecosystems provide to humans"),
        ("Trophic Cascade", "A chain of effects through a food web when one level is disrupted")
    ],
    "components": [
        ("Ocean Temperature", "Average water temperature in the reef zone", True),
        ("Ocean Acidity (pH)", "How acidic the ocean water is, affected by CO2 absorption", True),
        ("Zooxanthellae Population", "Symbiotic algae living inside coral that provide food and color", False),
        ("Coral Health", "Overall survival and growth rate of coral colonies", False)
    ],
    "think_about_it": "When ocean temperature increases beyond normal levels, what do you think happens to the zooxanthellae living inside the coral?",
    "scenarios": [
        ("Healthy Reef", "Set Ocean Temperature and Acidity to normal levels"),
        ("Marine Heat Wave", "Lock Ocean Temperature to +3°C above normal and observe"),
        ("Double Threat", "Increase BOTH temperature and acidity simultaneously")
    ],
    "sim_scenarios": [
        ("Healthy Reef", "Normal ocean temperature and pH", "What do you predict will happen to Coral Health?"),
        ("Heat Wave Simulation", "Lock Ocean Temperature to +3°C above normal", "What do you predict will happen to Zooxanthellae Population?"),
        ("Double Threat", "Increase both temperature and acidity", "How does this compare to temperature alone?")
    ],
    "discoveries": [
        "Coral depends on zooxanthellae algae for up to 90% of its energy",
        "When water gets too warm, coral expels its algae — that's bleaching",
        "Ocean acidification makes it harder for coral to build its skeleton",
        "The combination of heat AND acidity is far worse than either alone"
    ],
    "answer": "Rising ocean temperatures cause coral to expel the symbiotic algae they depend on for food, turning white (bleaching) and eventually starving to death!",
    "stem_title": "Design a Coral Reef Rescue Plan",
    "stem_mission": "Design a science-based plan to protect and restore a bleaching coral reef using evidence from your model.",
    "stem_scenario": "The Great Barrier Reef has experienced its worst bleaching event ever. Your marine science team has been hired to propose a rescue and prevention plan.",
    "stem_questions": [
        "Which factors in your model can humans actually control?",
        "What temperature threshold triggers bleaching?",
        "How can we reduce ocean acidification locally?"
    ],
    "stem_design_qs": [
        "What immediate actions can protect existing coral?",
        "How would you restore zooxanthellae populations?",
        "What long-term climate actions would prevent future bleaching?",
        "How will you measure the success of your plan?"
    ],
    "career": "Marine Biologists and Coral Restoration Scientists work to understand and protect ocean ecosystems. They earn $60,000-$100,000/year and work in some of the world's most beautiful locations.",
    "images": {
        "cover": ("cover-coral-reef.png", "A dramatic split image showing a vibrant colorful coral reef on one side and a bleached white dead-looking reef on the other side, underwater photography"),
        "landscape": ("landscape-ocean-reef.png", "8th grade students on a beach field trip examining tide pool organisms, diverse group looking through water at marine life, educational setting"),
        "modeling": ("modeling-reef.png", "A diverse group of 8th grade students working on laptops building a coral ecosystem model, ocean-themed classroom with marine science posters"),
        "discussion": ("discussion-coral.png", "A teacher showing underwater coral reef footage on a screen while engaged 8th grade students take notes and discuss, modern classroom"),
        "stem": ("stem-reef-rescue.png", "8th grade students presenting coral reef rescue plans with diagrams and models, collaborative team presentation, modern classroom")
    },
    "pre_assessment": [
        "What do you know about coral reefs? Are they alive?",
        "What do you think causes coral bleaching?",
        "How might rising ocean temperatures affect marine life?",
        "Draw a food web that might exist on a coral reef."
    ],
    "extend_components": [
        ("Fish Population", "Fish depend on coral for food and shelter"),
        ("Algae Overgrowth", "Without coral, algae can take over the reef"),
        ("Human Tourism", "Tourism dollars fund conservation but also cause damage")
    ],
    "reflections": [
        "Why is it called 'bleaching' if the coral isn't being washed with bleach?",
        "How is the coral-zooxanthellae relationship similar to a business partnership?",
        "If coral reefs disappear, what happens to the 25% of marine species that depend on them?",
        "Why is the combination of heat and acidity worse than either factor alone?",
        "What can an 8th grader actually do to help coral reefs survive?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students build a model to analyze how changes in ocean conditions affect coral reef ecosystems."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Ecosystems are dynamic; disruptions to components can cascade through the system."),
        ("Crosscutting Concept", "Stability and Change", "Students identify conditions that maintain reef stability vs. changes that push the system toward collapse.")
    ],
    "cast_items": [
        "Analyze data showing how changes in one ecosystem component affect others",
        "Construct evidence-based arguments about ecosystem disruption",
        "Use models to predict effects of environmental changes on populations"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Ocean temperature rises 2°C above normal for 6 weeks. Which is the most likely immediate effect on a coral reef?"),
        ("Constructed Response:", "Using evidence from your model, explain how rising ocean temperatures lead to a cascade of effects that can collapse an entire coral reef ecosystem.")
    ],
    "background_intro": "Coral reefs cover less than 1% of the ocean floor but support approximately 25% of all marine species. Often called 'rainforests of the sea,' they are among the most biodiverse and economically valuable ecosystems on Earth.",
    "background_sections": [
        ("The Coral-Algae Symbiosis", "Coral polyps have a mutualistic relationship with microscopic algae called zooxanthellae. The algae live inside coral tissue, photosynthesizing and providing up to 90% of the coral's energy. In return, coral provides shelter and nutrients. The algae also give coral its vibrant colors."),
        ("The Bleaching Process", "When water temperatures rise 1-2°C above the normal summer maximum for 4+ weeks, coral becomes stressed and expels its zooxanthellae. Without the algae, the coral's white skeleton shows through — hence 'bleaching.' Bleached coral isn't dead yet, but without its algae it starves and becomes vulnerable to disease."),
        ("Ocean Acidification", "The ocean absorbs about 30% of atmospheric CO2. When CO2 dissolves in seawater, it forms carbonic acid, lowering pH. More acidic water makes it harder for coral to build its calcium carbonate skeleton. This is sometimes called 'osteoporosis of the sea.'"),
        ("Global Reef Status", "The Great Barrier Reef experienced mass bleaching events in 2016, 2017, 2020, 2022, and 2024. Scientists estimate that 50% of the world's coral reefs have already been lost since the 1950s. If current trends continue, 90% could be gone by 2050.")
    ],
    "lever_L": "Students identify ocean temperature, ocean acidity, zooxanthellae population, and coral health as system components.",
    "lever_E": "Students determine that temperature and acidity both negatively affect zooxanthellae, which positively affects coral health.",
    "lever_V": "Students build the coral reef model showing cascading effects from environmental stressors to ecosystem collapse.",
    "lever_Ev": "Students compare healthy reef, heat wave, and double threat scenarios.",
    "lever_R": "Students add fish population or algae overgrowth to model trophic cascades.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split healthy vs. bleached reef", "say": "This is the same reef — one year apart. What happened?", "do": "Show before/after images. Let students react.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model why the most colorful ecosystems on Earth are turning white.", "do": "Pre-teach symbiosis with a quick partner example.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why are coral reefs turning white?", "say": "Coral reefs support 25% of all marine life. What happens if they're gone?", "do": "Quick write: What do you already know about coral?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to understand ecosystem collapse.", "do": "Preview the LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Reef system components", "say": "What are the key parts of a coral reef system?", "do": "Emphasize the symbiosis between coral and zooxanthellae.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Temperature doesn't directly kill coral — it disrupts the symbiosis first.", "do": "Draw attention to the INDIRECT pathway of effects.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Heat wave simulation", "say": "Let's see what happens during a marine heat wave.", "do": "Students predict, then run. Compare single vs. double threat.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Why is the combination of heat and acidity so devastating?", "do": "Connect to real Great Barrier Reef data.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Reef rescue plan", "say": "You're marine scientists hired to save the Great Barrier Reef. What's your plan?", "do": "Teams design science-based rescue plans.", "time": "12 min"}
    ],
    "sort_reasoning": "Ocean Temperature and Ocean Acidity are external because they come from global climate conditions that are outside the reef system itself. Zooxanthellae Population and Coral Health are internal because they respond to and are shaped by those external conditions.",
    "relationships": [
        ("Ocean Temperature to Zooxanthellae Population", "NEGATIVE (-)", "When temperature rises above normal, coral expels its zooxanthellae, reducing their population."),
        ("Ocean Acidity to Coral Health", "NEGATIVE (-)", "Higher acidity makes it harder for coral to build its calcium carbonate skeleton."),
        ("Zooxanthellae Population to Coral Health", "POSITIVE (+)", "More zooxanthellae means more energy for coral through photosynthesis — up to 90% of its food.")
    ],
    "sim_answers": [
        ("Heat Wave Scenario", "When Ocean Temperature increases +3°C, Zooxanthellae Population drops rapidly as coral expels its algae. Coral Health then crashes because it loses its primary food source. This is the bleaching cascade."),
        ("Double Threat Scenario", "When BOTH temperature and acidity increase, the effects are compounded. Zooxanthellae are expelled AND coral can't rebuild its skeleton. Recovery becomes nearly impossible because both energy supply and structural integrity are compromised.")
    ],
    "reflection_exemplars": [
        ("Why is it called bleaching?", "The vibrant colors of coral come from the zooxanthellae algae living inside them. When stress causes coral to expel these algae, the transparent coral tissue reveals the white calcium carbonate skeleton underneath. It looks 'bleached' but it's actually starving."),
        ("What can an 8th grader do?", "Reducing carbon footprint helps slow ocean warming and acidification. Supporting reef-safe sunscreen, reducing plastic waste, and advocating for marine protected areas all help. Understanding the science — like you're doing now — means you can explain the urgency to others.")
    ],
    "stem_intro": "Show students news footage of Great Barrier Reef bleaching. Present the challenge: You've been hired as marine science consultants. Your plan needs to use evidence from your model.",
    "stem_concepts": [
        ("Coral Nurseries", "Growing heat-resistant coral in nurseries and transplanting them to damaged reefs."),
        ("Marine Protected Areas", "Limiting human activities like fishing and tourism in reef zones to reduce additional stress."),
        ("Carbon Reduction", "Addressing root cause by reducing CO2 emissions that drive ocean warming and acidification.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses both immediate rescue and long-term prevention, uses model evidence, includes measurable goals"),
        ("Proficient (3)", "Plan includes science-based strategies and references model data"),
        ("Developing (2)", "Plan mentions conservation but lacks specific model evidence"),
        ("Beginning (1)", "Plan doesn't connect to ecosystem dynamics or model findings")
    ],
    "support": [
        "Provide food web diagram showing coral reef trophic levels",
        "Use color-coded cards for before/during/after bleaching",
        "Sentence frames: 'When ocean temperature increases, zooxanthellae __ because __'"
    ],
    "extensions": [
        "Research and graph ocean temperature trends over the past 50 years",
        "Add fish population and algae overgrowth components to model trophic cascade",
        "Compare coral reef decline data from different oceans worldwide"
    ],
    "cross_curr": [
        ("Math", "Graph and analyze ocean temperature anomaly data from NOAA for the past 30 years"),
        ("ELA", "Write a news article explaining coral bleaching to a general audience using scientific evidence"),
        ("Social Studies", "Research how coral reef loss affects economies of island nations that depend on reef tourism")
    ],
    "misconceptions": [
        ("Coral is a plant or rock", "Coral is an ANIMAL — specifically, colonies of tiny polyps related to jellyfish. They build calcium carbonate skeletons but are very much alive.", "Show video of coral polyps feeding at night. Ask: Do rocks eat?"),
        ("Bleaching means the coral is dead", "Bleached coral is stressed and starving but not necessarily dead. If conditions improve within weeks, zooxanthellae can recolonize and the coral can recover. But prolonged bleaching leads to death.", "Analogy: Bleaching is like a high fever — dangerous but potentially survivable if treated."),
        ("Climate change only affects land", "The ocean absorbs 90% of excess heat from global warming and 30% of CO2. Marine ecosystems are being dramatically affected by rising temperatures and acidification.", "Show ocean temperature data alongside atmospheric temperature data.")
    ]
}

L03 = {
    "id": "G08-L03",
    "title": "Your Phone's Dirty Secret",
    "subtitle": "The Hidden Environmental Cost of the Device in Your Pocket",
    "ngss": "MS-ESS3-3, MS-ESS3-4",
    "ngss_desc": "Apply scientific principles to design a method for monitoring and minimizing a human impact on the environment. Construct an argument supported by evidence for how increases in human population and per-capita consumption of natural resources impact Earth's systems.",
    "big_question": "What is the true environmental cost of the phone in your pocket?",
    "objectives": [
        "Trace the lifecycle of a smartphone from raw materials to e-waste",
        "Model how increased demand for rare earth minerals affects Earth's systems",
        "Evaluate the environmental trade-offs of technology consumption",
        "Design solutions to minimize the environmental impact of electronics"
    ],
    "vocabulary": [
        ("Rare Earth Minerals", "A group of 17 metallic elements essential for modern electronics, found in limited locations"),
        ("E-Waste", "Discarded electronic devices that contain toxic and valuable materials"),
        ("Resource Extraction", "The process of removing raw materials from the Earth"),
        ("Lifecycle Analysis", "Studying the environmental impact of a product from creation to disposal")
    ],
    "components": [
        ("Consumer Demand", "Number of new phones purchased per year worldwide", True),
        ("Mining Intensity", "Amount of rare earth mineral extraction from the Earth", True),
        ("Environmental Damage", "Land destruction, water pollution, and carbon emissions from extraction", False),
        ("E-Waste Accumulation", "Amount of discarded electronics that end up in landfills", False)
    ],
    "think_about_it": "When consumer demand for new phones increases, what do you think happens to mining intensity and environmental damage?",
    "scenarios": [
        ("Current Trends", "Set Consumer Demand and Mining Intensity to current real-world levels"),
        ("Upgrade Every Year", "Lock Consumer Demand to maximum — everyone gets a new phone annually"),
        ("Circular Economy", "Set Consumer Demand to 50% and add a recycling component")
    ],
    "sim_scenarios": [
        ("Current Trends", "Normal demand and mining levels", "What do you predict will happen to E-Waste Accumulation over 10 years?"),
        ("Maximum Consumption", "Lock Consumer Demand to maximum", "What do you predict will happen to Environmental Damage?"),
        ("Reduced Demand", "Cut Consumer Demand by 50%", "How does this change the other components?")
    ],
    "discoveries": [
        "A single smartphone contains over 30 different minerals from mines across the world",
        "Mining rare earth minerals generates toxic waste that contaminates water and soil",
        "Only about 20% of e-waste is properly recycled — the rest goes to landfills or developing countries",
        "Reducing demand (keeping phones longer) has a bigger impact than recycling alone"
    ],
    "answer": "Every phone requires mining dozens of minerals from the Earth, creating environmental destruction. When billions of phones are discarded, the toxic e-waste accumulates faster than we can recycle it!",
    "stem_title": "Design a Sustainable Phone Program",
    "stem_mission": "Design a school or community program that reduces the environmental impact of smartphone consumption.",
    "stem_scenario": "Your school district wants to reduce its technology footprint. Design a program that balances student access to technology with environmental responsibility.",
    "stem_questions": [
        "How can you extend the useful life of electronic devices?",
        "What happens to phones when they're recycled vs. thrown away?",
        "Which stage of the phone's lifecycle creates the most environmental damage?"
    ],
    "stem_design_qs": [
        "How will your program reduce new device purchases?",
        "What's your plan for responsible e-waste disposal?",
        "How will you educate the community about electronic waste?",
        "How will you measure the environmental impact of your program?"
    ],
    "career": "Environmental Engineers and Sustainability Consultants help companies reduce their environmental footprint and design greener products. They earn $70,000-$120,000/year.",
    "images": {
        "cover": ("cover-phone-mining.png", "A dramatic split image showing a sleek modern smartphone on one side and a massive open-pit mine on the other side, connecting consumer tech to resource extraction"),
        "landscape": ("landscape-ewaste.png", "8th grade students examining electronic components and circuit boards in a science lab, wearing gloves, learning about the materials inside electronics"),
        "modeling": ("modeling-lifecycle.png", "A diverse group of 8th grade students at computers building a digital model of resource extraction, engaged expressions, modern classroom"),
        "discussion": ("discussion-ewaste.png", "A teacher showing a map of global mining operations while 8th grade students discuss and take notes, interactive classroom"),
        "stem": ("stem-sustainability.png", "8th grade students creating sustainability posters and recycling program plans, working in teams, colorful modern classroom")
    },
    "pre_assessment": [
        "Where do you think the materials in your phone come from?",
        "What happens to a phone when you throw it away?",
        "How many phones do you think are sold worldwide each year?",
        "Draw the journey of a smartphone from raw materials to your pocket to the trash."
    ],
    "extend_components": [
        ("Recycling Rate", "Percentage of old electronics properly recycled for materials"),
        ("Carbon Emissions", "CO2 released during mining, manufacturing, and shipping"),
        ("Water Pollution", "Toxic chemicals from mining that contaminate local water sources")
    ],
    "reflections": [
        "How does your personal technology use contribute to environmental damage?",
        "Why do you think only 20% of e-waste is properly recycled?",
        "Is it possible to have modern technology WITHOUT environmental destruction? How?",
        "Who bears the greatest cost of smartphone production — consumers or mining communities?",
        "What would you be willing to change about how you use technology?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to trace the impact of resource extraction and consumption on Earth's systems."),
        ("Disciplinary Core Idea", "ESS3.C Human Impacts on Earth Systems", "Human activities have significantly altered the biosphere, sometimes damaging or destroying natural habitats."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal chains from consumer demand through mining to environmental damage and e-waste accumulation.")
    ],
    "cast_items": [
        "Describe how human consumption of resources impacts Earth's systems",
        "Apply scientific principles to evaluate methods for minimizing environmental impact",
        "Construct evidence-based arguments about resource sustainability"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A company mines coltan for smartphone production. Which is the most likely environmental impact of increased mining operations?"),
        ("Constructed Response:", "Using evidence from your model, explain how increasing global smartphone demand creates a chain of environmental effects from mining to e-waste.")
    ],
    "background_intro": "The average smartphone contains over 30 different elements, many classified as rare earth minerals. The environmental cost of extracting, processing, manufacturing, and disposing of these devices is enormous — and growing as global demand increases.",
    "background_sections": [
        ("What's Inside Your Phone", "A typical smartphone contains: lithium (battery), cobalt (battery), gold and silver (circuit connections), rare earth elements like neodymium (speakers/vibration motor), indium (touchscreen), tantalum from coltan (capacitors), and silicon (processor). Many of these are mined in environmentally sensitive areas."),
        ("The Mining Problem", "Rare earth mineral mining is extremely destructive. It involves stripping large areas of land, using toxic chemicals to extract minerals, generating radioactive waste, and contaminating water supplies. The Democratic Republic of Congo produces 60% of the world's cobalt, often using child labor in dangerous conditions."),
        ("The E-Waste Crisis", "The world generates approximately 50 million tons of e-waste per year. Only about 20% is formally recycled. The rest ends up in landfills or is shipped to developing countries where it's dismantled by hand, exposing workers to lead, mercury, cadmium, and other toxins."),
        ("Solutions and Alternatives", "Strategies include: extending device lifespan (repair instead of replace), improving recycling technology, designing devices for disassembly, using recycled materials in new devices, and developing alternative materials. The 'circular economy' model aims to eliminate waste entirely.")
    ],
    "lever_L": "Students identify consumer demand, mining intensity, environmental damage, and e-waste accumulation as system components.",
    "lever_E": "Students determine that demand drives mining (positive), mining drives damage (positive), and demand drives e-waste (positive).",
    "lever_V": "Students build the lifecycle model showing how consumption drives a chain of environmental effects.",
    "lever_Ev": "Students compare current trends, maximum consumption, and circular economy scenarios.",
    "lever_R": "Students add recycling rate or carbon emissions to create a more complete lifecycle model.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Phone vs. mine split image", "say": "Look at your phone. Do you know what it took to make it?", "do": "Ask students to hold up their phones. Create cognitive dissonance.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we trace the hidden journey of your phone — from mine to pocket to landfill.", "do": "Define lifecycle analysis with a simple example first.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "The true cost question", "say": "Your phone cost a few hundred dollars. But what's the REAL cost?", "do": "Quick write: List everything you think goes into making a phone.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the environmental impact chain.", "do": "Preview how we'll trace cause and effect.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Lifecycle system components", "say": "What are the key parts of the phone's environmental impact system?", "do": "Sort components. Discuss what students can vs. can't control.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Every new phone purchase connects to a chain of environmental effects.", "do": "Map the cause-and-effect chain from demand to damage.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Consumption scenarios", "say": "What if everyone upgraded every year? What if we all kept phones twice as long?", "do": "Run all three scenarios. Calculate the difference.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "What surprised you most about your phone's environmental footprint?", "do": "Discuss personal responsibility vs. systemic change.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sustainable phone program", "say": "Your school district hired you to design a sustainable technology program.", "do": "Teams design evidence-based programs. Present to class.", "time": "12 min"}
    ],
    "sort_reasoning": "Consumer Demand and Mining Intensity are external because they represent inputs that drive the system — demand comes from consumers and mining decisions come from companies. Environmental Damage and E-Waste Accumulation are internal because they are consequences that result from those external drivers.",
    "relationships": [
        ("Consumer Demand to Mining Intensity", "POSITIVE (+)", "More demand for phones means more minerals need to be extracted from the Earth."),
        ("Mining Intensity to Environmental Damage", "POSITIVE (+)", "More mining means more land destruction, water pollution, and toxic waste."),
        ("Consumer Demand to E-Waste Accumulation", "POSITIVE (+)", "More phones purchased means more phones eventually discarded as e-waste.")
    ],
    "sim_answers": [
        ("Maximum Consumption Scenario", "When Consumer Demand is maximized, Mining Intensity increases dramatically, driving Environmental Damage to critical levels. E-Waste Accumulation accelerates as phones are discarded annually. The system is clearly unsustainable."),
        ("Reduced Demand Scenario", "When Consumer Demand is cut by 50% (keeping phones twice as long), all downstream effects decrease significantly. This shows that reducing consumption has a larger impact than any other single intervention.")
    ],
    "reflection_exemplars": [
        ("Why is only 20% of e-waste recycled?", "Recycling electronics is expensive and complex — a single phone contains 30+ different materials bonded together. Many countries lack the technology. It's often cheaper to mine new materials than to recover them from old devices. And many people don't know how to properly dispose of electronics."),
        ("Can we have tech without destruction?", "A circular economy approach could dramatically reduce impact: design phones for easy repair and disassembly, use recycled materials, extend product lifespans, and ensure 100% recycling. Companies like Fairphone are already attempting this, but the economics need to change.")
    ],
    "stem_intro": "Present shocking e-waste statistics. Show photos of e-waste dumps in developing countries. Challenge: Design a program your school could actually implement.",
    "stem_concepts": [
        ("Right to Repair", "Laws that require manufacturers to make devices repairable, extending their useful life."),
        ("Urban Mining", "Recovering valuable materials from discarded electronics instead of mining new ones."),
        ("Extended Producer Responsibility", "Making manufacturers responsible for the entire lifecycle of their products, including disposal.")
    ],
    "stem_eval": [
        ("Expert (4)", "Program addresses multiple lifecycle stages, uses model evidence, and includes measurable environmental goals"),
        ("Proficient (3)", "Program uses model data and addresses at least two strategies for reducing impact"),
        ("Developing (2)", "Program mentions recycling but lacks specific evidence or multiple strategies"),
        ("Beginning (1)", "Program doesn't connect to lifecycle analysis or model findings")
    ],
    "support": [
        "Provide a labeled diagram of phone components and their mineral sources",
        "Use a physical phone teardown to show the materials inside",
        "Sentence frames: 'When consumer demand increases, environmental damage __ because __'"
    ],
    "extensions": [
        "Calculate the total mass of minerals needed to make every phone sold in one year",
        "Research and compare the environmental policies of major phone manufacturers",
        "Design a lifecycle analysis infographic for a specific electronic device"
    ],
    "cross_curr": [
        ("Math", "Calculate and graph the exponential growth of global e-waste over the past 20 years"),
        ("ELA", "Write a persuasive essay arguing for or against the Right to Repair movement"),
        ("Social Studies", "Research the human rights implications of cobalt mining in the Democratic Republic of Congo")
    ],
    "misconceptions": [
        ("Recycling solves the e-waste problem", "Only 20% of e-waste is properly recycled. Even recycled electronics lose material in the process. REDUCING consumption (keeping devices longer) is far more effective than recycling alone.", "Show the 'reduce, reuse, recycle' hierarchy — reduce is FIRST for a reason."),
        ("My phone doesn't affect the environment", "Every phone requires mining tons of rock, uses energy from fossil fuels to manufacture, and generates toxic waste at end of life. Multiply by 1.5 billion phones sold per year and the impact is massive.", "Calculate: If each phone requires 75 lbs of raw materials, how much is that for all phones sold in a year?"),
        ("Technology is always progress", "Technology provides amazing benefits, but it also has environmental costs that we need to account for. The goal isn't to stop using technology, but to use it more responsibly and demand sustainable practices.", "Discuss: What's the difference between progress and unsustainable consumption?")
    ]
}

L04 = {
    "id": "G08-L04",
    "title": "Why Hurricanes Are Getting Angrier",
    "subtitle": "The Science Behind Supercharged Storms",
    "ngss": "MS-ESS2-5, MS-ESS2-6",
    "ngss_desc": "Collect data to provide evidence for how the motions and complex interactions of air masses results in changes in weather conditions. Develop and use a model to describe how unequal heating of the Earth causes patterns of atmospheric and oceanic circulation that determine regional climates.",
    "big_question": "Why are hurricanes getting stronger and more destructive?",
    "objectives": [
        "Explain how warm ocean water provides energy for hurricane formation",
        "Model how rising sea surface temperatures intensify hurricanes",
        "Predict how climate patterns affect hurricane strength and frequency",
        "Evaluate the relationship between ocean temperature and storm damage"
    ],
    "vocabulary": [
        ("Sea Surface Temperature", "The temperature of the ocean's surface layer, which fuels tropical storms"),
        ("Rapid Intensification", "When a hurricane's wind speed increases by 35+ mph in 24 hours"),
        ("Storm Surge", "Abnormal rise in sea level during a storm, pushed by wind and low pressure"),
        ("Convection", "The rising of warm air and sinking of cool air that drives weather patterns")
    ],
    "components": [
        ("Sea Surface Temperature", "Temperature of the ocean surface where the hurricane forms", True),
        ("Atmospheric Moisture", "Amount of water vapor available in the air", True),
        ("Hurricane Wind Speed", "Maximum sustained wind speed of the storm", False),
        ("Storm Surge Height", "Height of ocean water pushed onto shore by the storm", False)
    ],
    "think_about_it": "When sea surface temperature increases, what do you think happens to the amount of energy available to fuel a hurricane?",
    "scenarios": [
        ("Category 1 Storm", "Set Sea Surface Temperature to 80°F and Moisture to moderate"),
        ("Supercharged Storm", "Lock Sea Surface Temperature to 90°F and observe rapid intensification"),
        ("Cool Water Encounter", "Start at 90°F then drop to 75°F — watch the hurricane weaken")
    ],
    "sim_scenarios": [
        ("Category 1 Storm", "Normal warm ocean temperature, moderate moisture", "What do you predict will happen to Hurricane Wind Speed?"),
        ("Supercharged Storm", "Lock Sea Surface Temperature to 90°F", "What do you predict will happen to Storm Surge Height?"),
        ("Cool Water Encounter", "Drop temperature from 90°F to 75°F", "What happens to the hurricane's intensity?")
    ],
    "discoveries": [
        "Hurricanes are heat engines — warm ocean water is their fuel",
        "Just a few degrees of extra ocean warmth dramatically increases storm intensity",
        "Rapid intensification is becoming more common as oceans warm",
        "When hurricanes hit cool water or land, they lose their energy source and weaken"
    ],
    "answer": "Warmer ocean water provides more energy for hurricanes through evaporation and convection. As climate change heats the oceans, hurricanes have more fuel to intensify rapidly and produce devastating storm surges!",
    "stem_title": "Design a Hurricane-Resilient Community",
    "stem_mission": "Design a coastal community plan that can withstand Category 5 hurricanes based on what your model reveals about storm behavior.",
    "stem_scenario": "A coastal city that experienced a devastating hurricane has hired your team to redesign their community to survive future storms that may be even stronger.",
    "stem_questions": [
        "Based on your model, how strong could future hurricanes become?",
        "What is the most destructive element of a hurricane — wind or water?",
        "How can building design reduce hurricane damage?"
    ],
    "stem_design_qs": [
        "Where should buildings be located relative to the coast?",
        "What building materials and designs resist hurricane forces?",
        "How will you protect against storm surge flooding?",
        "What emergency systems does your community need?"
    ],
    "career": "Meteorologists and Climate Scientists study weather patterns and develop forecasting models. Hurricane Hunters fly INTO storms to collect data! They earn $70,000-$120,000/year.",
    "images": {
        "cover": ("cover-hurricane.png", "A dramatic satellite view of a massive Category 5 hurricane from space, showing the eye of the storm with swirling clouds, Earth visible below"),
        "landscape": ("landscape-storm.png", "8th grade students in a science lab analyzing weather maps and satellite data on large screens, engaged in weather pattern analysis"),
        "modeling": ("modeling-hurricane.png", "A diverse group of 8th grade students working on laptops building a hurricane model, weather maps on classroom walls, excited expressions"),
        "discussion": ("discussion-storms.png", "A teacher showing hurricane damage photos on screen while 8th grade students discuss and take notes, engaged classroom discussion"),
        "stem": ("stem-resilient-city.png", "8th grade students building physical models of hurricane-resilient buildings and communities, working with craft materials, collaborative learning")
    },
    "pre_assessment": [
        "What causes hurricanes to form?",
        "Why do you think some hurricanes are stronger than others?",
        "What do you think happens to hurricane strength if the ocean gets warmer?",
        "Draw a diagram showing how you think a hurricane gets its energy."
    ],
    "extend_components": [
        ("Wind Shear", "Strong winds at different altitudes that can tear apart hurricanes"),
        ("Rainfall Intensity", "Amount of rain the storm produces, linked to moisture"),
        ("Coastal Population Density", "Number of people in the storm's path, affecting damage")
    ],
    "reflections": [
        "Why is a Category 5 hurricane over warm water more dangerous than one over cool water?",
        "How does the concept of 'rapid intensification' make hurricane forecasting harder?",
        "If ocean temperatures continue to rise, what does your model predict for future storms?",
        "Why do hurricanes weaken when they hit land?",
        "Should people continue to build communities in hurricane-prone coastal areas? Why or why not?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how ocean temperature and atmospheric conditions determine hurricane intensity."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate", "Complex interactions of air masses, ocean temperatures, and atmospheric conditions drive weather patterns."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace the flow of thermal energy from ocean water through evaporation into the kinetic energy of hurricane winds.")
    ],
    "cast_items": [
        "Explain how air mass interactions create weather patterns",
        "Use models to describe how unequal heating drives atmospheric circulation",
        "Collect and analyze data about weather conditions and climate patterns"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Sea surface temperatures in the Gulf of Mexico rise from 82°F to 88°F. A tropical storm enters this region. What is the most likely result?"),
        ("Constructed Response:", "Using your model, explain the chain of events from warm ocean water to destructive storm surge in a coastal city.")
    ],
    "background_intro": "Hurricanes are the most powerful weather events on Earth. A single hurricane can release energy equivalent to 10,000 nuclear bombs. Understanding the science behind their formation and intensification is critical as climate change alters ocean temperatures.",
    "background_sections": [
        ("Hurricane Formation", "Hurricanes form over warm ocean water (above 80°F/26.5°C). Warm water evaporates, and the moist air rises rapidly through convection. As it rises, it cools and condenses, releasing latent heat that further fuels the rising air. The Coriolis effect from Earth's rotation causes the system to spin."),
        ("The Energy Connection", "A hurricane is essentially a heat engine. The warmer the ocean surface, the more water evaporates, and the more energy is available to fuel the storm. The relationship between sea surface temperature and maximum potential hurricane intensity is well-established in atmospheric science."),
        ("Rapid Intensification", "Rapid intensification occurs when a hurricane's maximum sustained winds increase by 35+ mph in 24 hours. Hurricane Patricia (2015) went from tropical storm to Category 5 in just 24 hours. Studies show RI events have increased in frequency as oceans warm, making hurricanes harder to forecast and evacuate for."),
        ("Climate Change Connection", "Global average sea surface temperatures have risen about 1.5°F since 1900. The proportion of Category 4 and 5 hurricanes has increased significantly since 1980. Climate models predict continued intensification as oceans absorb more heat, with the strongest storms getting even stronger.")
    ],
    "lever_L": "Students identify sea surface temperature, atmospheric moisture, hurricane wind speed, and storm surge height as system components.",
    "lever_E": "Students determine that warmer water and more moisture both increase wind speed (positive), and wind speed increases storm surge (positive).",
    "lever_V": "Students build the hurricane model showing how ocean heat translates to storm intensity.",
    "lever_Ev": "Students compare normal, supercharged, and cool water scenarios to see the energy relationship.",
    "lever_R": "Students add wind shear or coastal population to explore additional factors.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Satellite hurricane image", "say": "This storm has the energy of 10,000 nuclear bombs. Where does all that power come from?", "do": "Show dramatic satellite footage. Let the scale sink in.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model the engine that drives the most powerful storms on Earth.", "do": "Discuss recent hurricanes students may remember.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why are hurricanes getting stronger?", "say": "Hurricane records show storms are intensifying faster than ever. Why?", "do": "Show before/after photos of hurricane damage.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to understand what fuels these monster storms.", "do": "Preview the modeling process.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Hurricane system components", "say": "What inputs fuel a hurricane? What outputs do we measure?", "do": "Guide sorting. Emphasize the ocean as the energy source.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Energy flow arrows", "say": "Warm water is the FUEL. More fuel = more powerful engine.", "do": "Map the energy pathway from ocean to wind to surge.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Storm intensity scenarios", "say": "Let's see what a few degrees of ocean warming does to storm strength.", "do": "Students predict, then run. The supercharged scenario is dramatic.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Just 6°F of warmer water turned a Category 1 into a Category 5.", "do": "Connect to real hurricane data and climate trends.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Resilient community design", "say": "A coastal city was devastated. They hired YOU to redesign the community.", "do": "Teams design hurricane-resilient communities.", "time": "12 min"}
    ],
    "sort_reasoning": "Sea Surface Temperature and Atmospheric Moisture are external because they represent environmental conditions that exist before the hurricane forms. Hurricane Wind Speed and Storm Surge Height are internal because they are outputs produced by the storm system itself.",
    "relationships": [
        ("Sea Surface Temperature to Hurricane Wind Speed", "POSITIVE (+)", "Warmer water evaporates more, providing more energy through latent heat to fuel stronger winds."),
        ("Atmospheric Moisture to Hurricane Wind Speed", "POSITIVE (+)", "More moisture means more condensation, which releases more latent heat to power the storm."),
        ("Hurricane Wind Speed to Storm Surge Height", "POSITIVE (+)", "Stronger winds push more ocean water onto shore, creating higher and more destructive storm surges.")
    ],
    "sim_answers": [
        ("Supercharged Storm Scenario", "At 90°F sea surface temperature, Hurricane Wind Speed rapidly increases as the abundant warm water provides massive energy through evaporation. Storm Surge Height climbs proportionally. The storm intensifies much faster than at lower temperatures."),
        ("Cool Water Encounter", "When temperature drops to 75°F, the hurricane's energy source is cut off. Wind speed decreases rapidly as the storm can no longer sustain itself. Storm surge drops accordingly. This is why hurricanes weaken over land — no warm water fuel.")
    ],
    "reflection_exemplars": [
        ("Why does rapid intensification make forecasting harder?", "If a storm can go from Category 1 to Category 5 in 24 hours, there may not be enough time to issue warnings and evacuate. Traditional forecasting assumes more gradual changes. Rapid intensification is essentially 'surprise strength' that catches communities off guard."),
        ("Should people build in hurricane zones?", "This is a complex question involving risk assessment, economics, and equity. Many coastal communities have existed for centuries. The key is building WITH hurricane awareness: elevated structures, storm-resistant designs, robust evacuation plans, and acknowledging that stronger storms are coming.")
    ],
    "stem_intro": "Show footage of a recent devastating hurricane. Present the challenge: The city needs to be rebuilt, but the next storm could be even stronger. What does your model tell you about the future?",
    "stem_concepts": [
        ("Building Codes", "Stricter construction standards that require hurricane-resistant design features."),
        ("Natural Barriers", "Mangroves, sand dunes, and wetlands that absorb storm surge energy."),
        ("Elevation Design", "Building critical infrastructure above predicted storm surge heights.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses multiple hazards (wind, surge, flooding), uses model evidence for future projections, and includes practical details"),
        ("Proficient (3)", "Design uses model data and addresses at least two hurricane hazards"),
        ("Developing (2)", "Design mentions hurricane protection but lacks specific evidence from model"),
        ("Beginning (1)", "Design doesn't connect to hurricane science or model findings")
    ],
    "support": [
        "Provide a diagram showing how warm water fuels hurricane formation",
        "Use a pan of warm water and a fan to demonstrate convection currents",
        "Sentence frames: 'When sea surface temperature increases, hurricane wind speed __ because __'"
    ],
    "extensions": [
        "Research and graph the increase in Category 4-5 hurricanes over the past 40 years",
        "Add wind shear component and model why some storms weaken unexpectedly",
        "Compare hurricane tracks and intensities from the 1970s vs. 2020s"
    ],
    "cross_curr": [
        ("Math", "Calculate and graph the relationship between sea surface temperature and maximum wind speed"),
        ("ELA", "Write a breaking news story about a rapidly intensifying hurricane making landfall"),
        ("Social Studies", "Research how hurricane damage disproportionately affects low-income communities")
    ],
    "misconceptions": [
        ("Hurricanes are getting more frequent", "The total NUMBER of hurricanes hasn't clearly increased, but the PROPORTION of intense storms (Category 4-5) has increased significantly. Fewer storms, but the ones that form are stronger.", "Show data comparing total hurricane counts vs. major hurricane counts over time."),
        ("Wind is the most dangerous part", "Storm surge actually causes the most deaths and property damage during hurricanes. A 15-foot wall of ocean water pushed inland is more destructive than wind alone.", "Show storm surge vs. wind damage statistics from recent hurricanes."),
        ("Climate change creates hurricanes", "Climate change doesn't CREATE hurricanes — they've always existed. But warmer oceans provide more FUEL for storms that do form, making them stronger and more likely to rapidly intensify.", "Analogy: A bigger gas tank doesn't start the car, but it lets the engine run harder and longer.")
    ]
}

L05 = {
    "id": "G08-L05",
    "title": "The Roller Coaster Equation",
    "subtitle": "How Physics Turns Height Into Speed and Screams Into Science",
    "ngss": "MS-PS3-1, MS-PS3-2",
    "ngss_desc": "Construct and interpret graphical displays of data to describe the relationships of kinetic energy to the mass of an object and to the speed of an object. Develop a model to describe that when the arrangement of objects interacting at a distance changes, different amounts of potential energy are stored in the system.",
    "big_question": "How does a roller coaster turn height into speed without an engine?",
    "objectives": [
        "Explain the relationship between potential energy and kinetic energy",
        "Model how height, mass, and speed are connected in energy transformations",
        "Predict the speed of a coaster at any point on the track using energy conservation",
        "Evaluate real roller coaster designs using energy transformation principles"
    ],
    "vocabulary": [
        ("Kinetic Energy", "The energy of motion — increases with speed and mass"),
        ("Potential Energy", "Stored energy due to position or height — increases with height and mass"),
        ("Energy Conservation", "Energy cannot be created or destroyed, only transformed from one form to another"),
        ("Energy Transformation", "The process of energy changing from one type to another")
    ],
    "components": [
        ("Coaster Height", "The vertical position of the roller coaster on the track", True),
        ("Coaster Mass", "Total mass of the coaster car plus riders", True),
        ("Potential Energy", "Energy stored due to the coaster's height above the ground", False),
        ("Kinetic Energy (Speed)", "Energy of the coaster's motion — determines how fast it goes", False)
    ],
    "think_about_it": "When the coaster is at the TOP of the first hill, it has maximum potential energy. What happens to that energy as it drops?",
    "scenarios": [
        ("First Drop", "Set Coaster Height to maximum and watch the energy transformation"),
        ("Heavy vs. Light", "Compare a fully loaded coaster vs. a nearly empty one"),
        ("Loop the Loop", "Set height to include a loop and predict minimum speed needed")
    ],
    "sim_scenarios": [
        ("First Drop", "Maximum height, normal mass", "What do you predict will happen to Kinetic Energy as the coaster descends?"),
        ("Heavy Coaster", "Maximum height, double mass", "How does mass affect the speed at the bottom?"),
        ("Low Hill", "Set height to 50% of maximum", "What do you predict about the maximum speed compared to the tall hill?")
    ],
    "discoveries": [
        "At the top of the hill: maximum potential energy, minimum kinetic energy",
        "At the bottom: maximum kinetic energy, minimum potential energy — the energy TRANSFORMED",
        "The total energy stays the same (conservation!) — height energy becomes speed energy",
        "More mass means more of BOTH types of energy, but the speed at the bottom is the same"
    ],
    "answer": "A roller coaster converts potential energy (height) into kinetic energy (speed). The higher the first hill, the faster the coaster goes at the bottom — no engine needed!",
    "stem_title": "Design the Ultimate Roller Coaster",
    "stem_mission": "Design a roller coaster that achieves the maximum thrill while obeying the laws of energy conservation.",
    "stem_scenario": "A theme park has hired your engineering team to design their new signature roller coaster. It must be thrilling but physically possible — every hill, loop, and turn must obey energy conservation.",
    "stem_questions": [
        "Why can't the second hill be taller than the first?",
        "What's the minimum speed needed to safely complete a loop?",
        "How does friction affect your design?"
    ],
    "stem_design_qs": [
        "How tall will your first hill be?",
        "How many loops and hills will your coaster have?",
        "Why must each subsequent hill be shorter than the previous one?",
        "How will you account for energy lost to friction?"
    ],
    "career": "Roller Coaster Engineers and Mechanical Engineers design rides using physics principles. They use computer models to test designs before building. They earn $75,000-$130,000/year.",
    "images": {
        "cover": ("cover-rollercoaster.png", "A dramatic photo of a roller coaster at the peak of a massive first drop with riders' hands up, vivid blue sky, theme park setting, exciting and thrilling"),
        "landscape": ("landscape-coaster-physics.png", "8th grade students at a theme park with clipboards taking measurements and notes near a roller coaster, educational field trip, science in action"),
        "modeling": ("modeling-energy.png", "A diverse group of 8th grade students at computers building energy transformation models, one student pointing at a graph showing PE and KE curves"),
        "discussion": ("discussion-energy.png", "A teacher demonstrating energy conversion with a ball on a ramp while 8th grade students watch and discuss, hands-on physics lesson"),
        "stem": ("stem-coaster-design.png", "8th grade students building model roller coasters from foam tubes and marbles, testing their designs, collaborative engineering activity")
    },
    "pre_assessment": [
        "What makes a roller coaster go fast without an engine pushing it?",
        "Where on a roller coaster do you think you have the MOST energy?",
        "What's the difference between potential energy and kinetic energy?",
        "Draw an energy diagram for a ball rolling down a hill."
    ],
    "extend_components": [
        ("Friction", "Energy lost to heat as the coaster moves along the track"),
        ("Air Resistance", "Energy lost to pushing through the air"),
        ("G-Forces", "The feeling of being pushed or pulled on curves and drops")
    ],
    "reflections": [
        "Why does the first hill of a roller coaster have to be the tallest?",
        "If energy is conserved, why does a real roller coaster eventually stop?",
        "How would a coaster on the Moon be different from one on Earth?",
        "Why do you feel 'weightless' at the top of a hill but heavy at the bottom of a dip?",
        "How is a roller coaster similar to a pendulum or a bouncing ball?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to describe energy transformations between potential and kinetic energy."),
        ("Disciplinary Core Idea", "PS3.A Definitions of Energy / PS3.B Conservation of Energy", "Kinetic energy is proportional to mass and speed squared. Energy is conserved in transformations."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace energy as it flows and transforms between potential and kinetic forms throughout the system.")
    ],
    "cast_items": [
        "Interpret graphs showing relationships between kinetic energy, mass, and speed",
        "Use models to describe how changing position changes stored potential energy",
        "Apply conservation of energy to predict outcomes"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A roller coaster car is at the top of a 30-meter hill. As it rolls to the bottom, what happens to its potential and kinetic energy?"),
        ("Constructed Response:", "Using the principle of energy conservation, explain why a roller coaster's second hill can never be taller than its first hill (ignoring external energy sources).")
    ],
    "background_intro": "Roller coasters are elegant demonstrations of energy conservation. Every scream, every thrill, and every stomach drop is the result of energy transforming between two forms: potential and kinetic.",
    "background_sections": [
        ("Potential Energy", "Gravitational potential energy depends on height and mass: PE = mgh (mass × gravity × height). At the top of the first hill, the coaster has maximum PE. The chain lift does work against gravity to give the coaster this stored energy. A 500 kg coaster at 50 meters has PE = 500 × 9.8 × 50 = 245,000 Joules."),
        ("Kinetic Energy", "Kinetic energy depends on mass and speed: KE = ½mv² (half × mass × speed squared). Notice that speed is SQUARED — doubling speed quadruples kinetic energy. This is why the first drop feels so intense: small changes in height create large changes in speed."),
        ("Conservation of Energy", "In an ideal system (no friction), total energy = PE + KE = constant. At the top: high PE, low KE. At the bottom: low PE, high KE. The energy doesn't disappear — it transforms. In real coasters, some energy is lost to friction and air resistance as heat."),
        ("Real Coaster Design", "Engineers use these equations to design every hill, loop, and turn. The first hill must be the tallest because the coaster can never regain that height without additional energy input. Loop-the-loops require a minimum speed at the top to maintain contact with the track.")
    ],
    "lever_L": "Students identify coaster height, coaster mass, potential energy, and kinetic energy as system components.",
    "lever_E": "Students determine that height positively affects PE, and as PE decreases (going downhill), KE increases — they trade back and forth.",
    "lever_V": "Students build the energy transformation model showing the PE-KE seesaw.",
    "lever_Ev": "Students compare different heights and masses to see how they affect the energy balance.",
    "lever_R": "Students add friction to see why real coasters lose energy and eventually stop.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Coaster at peak of first drop", "say": "No engine. No fuel. Just height. How does a roller coaster hit 70 mph?", "do": "Show a first-person POV video of a big coaster drop.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we crack the code of how height becomes speed.", "do": "Define PE and KE with quick physical demos.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does height become speed?", "say": "The chain lift takes you up... then lets go. Everything after is pure physics.", "do": "Poll: Where on the coaster do you have the most energy?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the energy seesaw that makes coasters work.", "do": "Preview the modeling process.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Energy system components", "say": "What are the key energy players in a roller coaster?", "do": "Sort components. Discuss what's controlled vs. what changes.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Energy transformation arrows", "say": "Here's the key: PE and KE are on opposite ends of a seesaw.", "do": "Demonstrate with a ball on a ramp. When one goes up, the other goes down.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Energy transformation graphs", "say": "Watch PE and KE trade places as the coaster moves.", "do": "Students run scenarios and sketch the PE-KE graphs.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "The total energy stays CONSTANT. Height and speed are the same energy in different forms.", "do": "Discuss: Why can't the second hill be taller?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Coaster design challenge", "say": "Design the ultimate coaster — but it must obey the laws of physics!", "do": "Teams design and test with marble tracks or simulations.", "time": "12 min"}
    ],
    "sort_reasoning": "Coaster Height and Coaster Mass are external because they are design inputs set before the ride begins. Potential Energy and Kinetic Energy are internal because they change dynamically throughout the ride based on the coaster's position.",
    "relationships": [
        ("Coaster Height to Potential Energy", "POSITIVE (+)", "Higher position means more stored gravitational energy."),
        ("Coaster Mass to Potential Energy", "POSITIVE (+)", "More mass at the same height means more stored energy."),
        ("Potential Energy to Kinetic Energy", "POSITIVE (+) (inverse seesaw)", "As PE decreases going downhill, KE increases by the same amount — energy is conserved.")
    ],
    "sim_answers": [
        ("First Drop Scenario", "Starting at maximum height, PE is at its maximum and KE is near zero. As the coaster descends, PE decreases smoothly while KE increases by exactly the same amount. At the bottom, KE is maximized — this is where the coaster is fastest."),
        ("Heavy vs. Light Coaster", "Doubling the mass doubles BOTH PE at the top and KE at the bottom. However, since KE = ½mv², the speed at the bottom is the same! More mass means more energy, but the speed doesn't change — a key insight.")
    ],
    "reflection_exemplars": [
        ("Why must the first hill be tallest?", "The chain lift gives the coaster all of its energy at the start by raising it to maximum height. After that, the total energy can only decrease (due to friction). Since PE = mgh, the coaster can never reach a height higher than it started because it doesn't have enough energy."),
        ("Why does the coaster eventually stop?", "In the real world, friction and air resistance convert kinetic energy into heat. This 'lost' energy reduces the total available for PE-KE transformation. The energy isn't destroyed — it becomes thermal energy — but it's no longer useful for motion.")
    ],
    "stem_intro": "Show a video of the world's tallest roller coasters. Challenge students: Your design must be thrilling AND physically accurate. Every hill, loop, and turn must obey conservation of energy.",
    "stem_concepts": [
        ("Loop Design", "The loop must have a minimum speed at the top for riders to maintain contact. This sets the minimum height for the preceding hill."),
        ("Friction Budget", "Real coasters lose about 10-15% of energy to friction per hill. Factor this into your design."),
        ("G-Force Limits", "The human body can safely handle about 3-4 G's briefly. Design transitions to stay within limits.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design obeys energy conservation, accounts for friction, includes calculations for key points, and is creative"),
        ("Proficient (3)", "Design obeys energy conservation and includes hills that decrease in height"),
        ("Developing (2)", "Design shows some energy awareness but has physics violations"),
        ("Beginning (1)", "Design doesn't consider energy conservation principles")
    ],
    "support": [
        "Provide a PE-KE bar chart template for tracking energy at each point",
        "Use a physical ball-and-ramp setup to demonstrate energy transformation",
        "Sentence frames: 'At the top, PE is __ and KE is __ because __'"
    ],
    "extensions": [
        "Calculate the exact speed at the bottom of a 50-meter drop using energy equations",
        "Research the physics of loop-the-loops and calculate minimum speed at the top",
        "Compare your model predictions to actual roller coaster speed data"
    ],
    "cross_curr": [
        ("Math", "Use PE = mgh and KE = ½mv² to calculate speed at various points on the track"),
        ("ELA", "Write a physics-based review of a roller coaster explaining the energy at each point"),
        ("Social Studies", "Research the history of roller coasters and how physics knowledge improved safety")
    ],
    "misconceptions": [
        ("Heavier coasters go faster", "Mass cancels out in energy calculations! A heavy coaster and a light coaster dropped from the same height reach the same speed (ignoring friction). They have different amounts of energy, but the speed is identical.", "Demo: Drop a heavy and light ball from the same height — they hit the ground at the same time."),
        ("The coaster has no energy at the top", "At the top, the coaster is moving slowly (low KE) but has MAXIMUM potential energy stored in its height. It's like a fully charged battery — the energy is there, just stored.", "Ask: Which has more energy — a rock on the ground or the same rock on top of a building?"),
        ("Energy is used up on the ride", "Energy is never created or destroyed — only transformed. 'Used up' energy actually became heat through friction. The total energy of the universe stays the same.", "Calculate: Track the total energy (PE + KE) at each point — it should be constant in an ideal system.")
    ]
}

L06 = {
    "id": "G08-L06",
    "title": "The Concussion Problem",
    "subtitle": "Why Helmets Can't Stop Your Brain from Slamming Into Your Skull",
    "ngss": "MS-PS2-1, MS-PS2-2",
    "ngss_desc": "Apply Newton's Third Law to design a solution to a problem involving the motion of two colliding objects. Plan an investigation to provide evidence that the change in an object's motion depends on the sum of the forces acting on the object and the mass of the object.",
    "big_question": "Why do football players still get concussions even while wearing helmets?",
    "objectives": [
        "Apply Newton's Laws of Motion to explain what happens during a collision",
        "Model how force, mass, and acceleration are related in impact scenarios",
        "Predict how changing collision speed or mass affects the force of impact",
        "Evaluate helmet designs based on force reduction principles"
    ],
    "vocabulary": [
        ("Newton's Third Law", "For every action force, there is an equal and opposite reaction force"),
        ("Impulse", "The change in momentum — equals force multiplied by time of contact"),
        ("Concussion", "A brain injury caused by the brain hitting the inside of the skull during sudden deceleration"),
        ("Deceleration", "Negative acceleration — the rate at which an object slows down")
    ],
    "components": [
        ("Collision Speed", "How fast the player is moving at the moment of impact", True),
        ("Player Mass", "The combined mass of the player and equipment", True),
        ("Impact Force", "The force experienced during the collision", False),
        ("Brain Acceleration", "How rapidly the brain decelerates inside the skull", False)
    ],
    "think_about_it": "When collision speed increases, what do you think happens to the force experienced by the brain inside the helmet?",
    "scenarios": [
        ("Jogging Speed Collision", "Set Collision Speed to 5 mph with normal Player Mass"),
        ("Full Sprint Collision", "Lock Collision Speed to 20 mph and observe the impact force"),
        ("Helmet Comparison", "Add a 'padding thickness' factor and compare thin vs. thick padding")
    ],
    "sim_scenarios": [
        ("Jogging Speed", "5 mph collision, normal mass", "What do you predict will happen to Impact Force?"),
        ("Full Sprint", "Lock Collision Speed to 20 mph", "What do you predict will happen to Brain Acceleration?"),
        ("Heavier Player", "Double Player Mass at 15 mph", "How does mass affect Impact Force compared to speed?")
    ],
    "discoveries": [
        "Force increases dramatically with speed — doubling speed more than doubles the force",
        "Helmets reduce force by EXTENDING the time of impact (impulse), not by blocking it",
        "The brain floats in fluid inside the skull — it keeps moving when the skull stops",
        "No helmet can eliminate concussion risk because the brain will always decelerate during impact"
    ],
    "answer": "During a collision, the skull stops suddenly but the brain keeps moving (Newton's First Law), slamming into the skull. Helmets extend the collision time to reduce force, but can't prevent the brain from decelerating inside the skull!",
    "stem_title": "Design a Better Helmet",
    "stem_mission": "Design a helmet that minimizes brain acceleration during impacts using the principles from your model.",
    "stem_scenario": "A sports equipment company has hired your team to improve their football helmet design. You must use physics principles to explain why your design reduces concussion risk.",
    "stem_questions": [
        "What physical principle makes current helmets work?",
        "How could you increase the time of impact to reduce force?",
        "What materials absorb energy best?"
    ],
    "stem_design_qs": [
        "What padding materials and thickness will you use?",
        "How will your design extend the time of impact?",
        "What's the trade-off between protection and weight/comfort?",
        "How will you test your helmet design?"
    ],
    "career": "Biomedical Engineers design safety equipment using physics and biology. Sports Biomechanists study forces on the human body during athletics. They earn $70,000-$120,000/year.",
    "images": {
        "cover": ("cover-concussion.png", "A dramatic close-up of a football helmet during a collision with visible impact effects, sports photography style, intense action moment"),
        "landscape": ("landscape-sports-physics.png", "8th grade students in a gym testing egg drop contraptions and impact-absorbing designs, wearing safety goggles, hands-on physics experiment"),
        "modeling": ("modeling-forces.png", "A diverse group of 8th grade students at computers building a collision force model, one student pointing at a force vs time graph on screen"),
        "discussion": ("discussion-concussion.png", "A teacher demonstrating Newton's Laws with a crash test demonstration while 8th grade students watch intently, science classroom"),
        "stem": ("stem-helmet-design.png", "8th grade students designing and testing protective helmet prototypes using craft materials, eggs, and drop tests, collaborative engineering")
    },
    "pre_assessment": [
        "What happens to a passenger when a car suddenly stops?",
        "Why do you think football players get concussions even with helmets?",
        "What does Newton's Third Law say about collisions?",
        "Draw what you think happens to the brain inside a skull during a sudden stop."
    ],
    "extend_components": [
        ("Padding Thickness", "Thicker padding extends the time of impact, reducing peak force"),
        ("Neck Strength", "Stronger neck muscles help stabilize the head during impact"),
        ("Impact Angle", "Glancing blows transfer less force than head-on collisions")
    ],
    "reflections": [
        "Why can't any helmet completely prevent concussions?",
        "How does Newton's First Law explain what happens to the brain during a collision?",
        "Why is a 20 mph collision so much more dangerous than a 10 mph collision?",
        "How is an egg drop contest similar to designing a better helmet?",
        "Should contact sports be modified to reduce collision speeds? What are the trade-offs?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to describe how force, mass, and acceleration interact during collisions."),
        ("Disciplinary Core Idea", "PS2.A Forces and Motion", "The motion of an object is determined by the sum of the forces acting on it. Newton's Third Law applies to all interactions."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships between collision speed, force magnitude, and brain injury severity.")
    ],
    "cast_items": [
        "Apply Newton's Third Law to analyze forces during a collision",
        "Plan an investigation to show how mass and force affect motion",
        "Design a solution that applies force and motion principles"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two football players collide head-on. Player A (100 kg) is running at 5 m/s. Player B (80 kg) is running at 6 m/s. According to Newton's Third Law, which statement is correct about the forces during the collision?"),
        ("Constructed Response:", "Explain why doubling the speed of a collision is more dangerous than doubling the mass of a player. Use the relationship between force, mass, and acceleration.")
    ],
    "background_intro": "Concussions are one of the most significant health concerns in contact sports. Understanding the physics of collisions — force, impulse, and deceleration — is essential for designing better protective equipment and safer sports rules.",
    "background_sections": [
        ("Newton's Laws in Collisions", "First Law (Inertia): The brain tends to keep moving when the skull suddenly stops. Second Law (F=ma): Force equals mass times acceleration — more speed means more deceleration force. Third Law: During a collision, both objects experience equal and opposite forces, regardless of size difference."),
        ("The Concussion Mechanism", "The brain floats in cerebrospinal fluid inside the skull. During a sudden deceleration, the brain continues moving forward and impacts the inside of the skull. This causes bruising, stretching of nerve fibers, and chemical changes that constitute a concussion. The brain can also bounce and hit the back of the skull (coup-contrecoup injury)."),
        ("Impulse and Helmets", "Impulse = Force × Time. A given change in momentum can happen with a BIG force over a SHORT time, or a SMALLER force over a LONGER time. Helmets work by crushing or deforming, which EXTENDS the collision time. This reduces the peak force. It's the same physics behind crumple zones in cars and air bags."),
        ("The Speed Problem", "Kinetic energy = ½mv². Because speed is SQUARED, doubling speed QUADRUPLES the kinetic energy that must be absorbed during the collision. A player running at 20 mph has 4x the kinetic energy of one running at 10 mph. This is why high-speed collisions are so much more dangerous.")
    ],
    "lever_L": "Students identify collision speed, player mass, impact force, and brain acceleration as system components.",
    "lever_E": "Students determine that speed strongly increases force (positive), mass moderately increases force (positive), and force increases brain acceleration (positive).",
    "lever_V": "Students build the collision model showing how inputs translate to brain injury risk.",
    "lever_Ev": "Students compare low-speed vs. high-speed and light vs. heavy player scenarios.",
    "lever_R": "Students add padding thickness to model how helmets reduce peak force.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Football helmet collision", "say": "Football helmets are engineered marvels. But players STILL get concussions. Why?", "do": "Ask students what they know about CTE and concussions in sports.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we use Newton's Laws to understand why brains get injured during impacts.", "do": "Quick review of Newton's Three Laws with everyday examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why helmets can't stop concussions", "say": "What if I told you that NO helmet can completely prevent concussions? Let's find out why.", "do": "Demo: Put a ball in a jar of water (brain in skull). Shake it suddenly.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the physics of what happens during a collision.", "do": "Preview the LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Collision system components", "say": "What factors determine how bad a collision is?", "do": "Sort components. Discuss what players can vs. can't control.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Force relationship arrows", "say": "Speed is the big one. Doubling speed QUADRUPLES the energy.", "do": "Emphasize the squared relationship between speed and energy.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Collision scenarios", "say": "Let's compare a jog-speed collision to a full-sprint collision.", "do": "Students predict, then run. The speed difference is dramatic.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Helmets help by extending time — but the brain still decelerates.", "do": "Connect to real CTE data. Discuss implications for sports safety.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Helmet design challenge", "say": "A sports company hired YOU to design a better helmet. Use physics!", "do": "Egg drop contest using helmet design principles.", "time": "12 min"}
    ],
    "sort_reasoning": "Collision Speed and Player Mass are external because they exist before the collision happens — they are the inputs to the impact event. Impact Force and Brain Acceleration are internal because they are produced by the collision itself.",
    "relationships": [
        ("Collision Speed to Impact Force", "POSITIVE (+)", "Higher speed means more kinetic energy must be absorbed, creating larger forces during the collision."),
        ("Player Mass to Impact Force", "POSITIVE (+)", "More mass at the same speed means more momentum to change, resulting in higher forces."),
        ("Impact Force to Brain Acceleration", "POSITIVE (+)", "Greater force on the skull causes greater deceleration of the brain inside, increasing concussion risk.")
    ],
    "sim_answers": [
        ("Full Sprint Scenario", "At 20 mph, Impact Force is dramatically higher than at 5 mph — roughly 16 times higher because kinetic energy scales with speed squared. Brain Acceleration reaches dangerous levels. This shows why high-speed collisions are so much more dangerous."),
        ("Heavy Player Scenario", "Doubling mass at the same speed doubles the Impact Force. However, the relationship between speed and force is much steeper than between mass and force. Reducing speed is more effective than reducing mass for preventing concussions.")
    ],
    "reflection_exemplars": [
        ("Why can't helmets prevent concussions?", "A helmet can reduce the force on the skull by extending the collision time (impulse). But the brain is floating INSIDE the skull. When the skull suddenly decelerates, the brain keeps moving (Newton's First Law) and impacts the skull wall. No external padding can prevent this internal deceleration."),
        ("Why is doubling speed worse than doubling mass?", "Kinetic energy = ½mv². Speed is SQUARED, so doubling speed quadruples kinetic energy. Doubling mass only doubles KE. In a collision at 20 mph vs. 10 mph, the force isn't just twice as bad — it's roughly 4 times worse. This is why speed reduction rules are more effective than weight limits.")
    ],
    "stem_intro": "Show slow-motion footage of a football collision. Present challenge: A company hired your team to design a better helmet. You must explain the physics behind your design.",
    "stem_concepts": [
        ("Crumple Zones", "Materials that deform on impact, extending the collision time and reducing peak force."),
        ("Multi-Layer Design", "Different material layers that absorb different impact speeds (hard outer shell + soft inner padding)."),
        ("Rotational Protection", "Systems like MIPS that allow the helmet shell to rotate slightly, reducing rotational forces on the brain.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design uses impulse principles, identifies specific materials, explains physics behind each feature, and addresses trade-offs"),
        ("Proficient (3)", "Design references force reduction and includes at least two physics-based features"),
        ("Developing (2)", "Design mentions protection but lacks specific physics reasoning"),
        ("Beginning (1)", "Design doesn't connect to force, impulse, or Newton's Laws")
    ],
    "support": [
        "Provide a force vs. time graph template showing how padding extends collision time",
        "Use egg drop activity as physical analogy for brain protection",
        "Sentence frames: 'When collision speed doubles, impact force __ because __'"
    ],
    "extensions": [
        "Calculate the force of a 100 kg player stopping from 20 mph in 0.01 seconds vs. 0.1 seconds",
        "Research MIPS technology and add rotational force component to model",
        "Compare concussion rates across sports with different collision speeds"
    ],
    "cross_curr": [
        ("Math", "Calculate force, impulse, and kinetic energy for different collision scenarios using F=ma and KE=½mv²"),
        ("ELA", "Write a research paper on the ethical debate about contact sports and brain injury"),
        ("Social Studies", "Research how concussion awareness has changed sports rules and culture over the past 20 years")
    ],
    "misconceptions": [
        ("Helmets prevent concussions", "Helmets reduce skull fractures and some force, but CANNOT prevent concussions because the brain still decelerates inside the skull. No amount of external padding can stop internal brain movement.", "Demo: Shake a ball in a jar of water. The jar stops but the ball keeps moving. That's your brain."),
        ("Bigger players get fewer concussions", "Bigger players generate and receive LARGER forces due to greater mass and momentum. While a bigger neck may help stabilize the head, overall concussion risk isn't lower for larger players.", "Show that F=ma means more mass = more force at the same speed."),
        ("Speed and force are directly proportional", "Force in a collision relates to KINETIC ENERGY, which scales with speed SQUARED. Doubling speed quadruples the force, not just doubles it. This non-linear relationship is why high-speed collisions are so much more dangerous.", "Graph KE vs. speed: 5 mph = 25 units, 10 mph = 100 units, 20 mph = 400 units.")
    ]
}

L07 = {
    "id": "G08-L07",
    "title": "How LeBron Turns Food Into Dunks",
    "subtitle": "The Cellular Science Behind Athletic Performance",
    "ngss": "MS-LS1-5, MS-LS1-7",
    "ngss_desc": "Construct a scientific explanation based on evidence for how environmental and genetic factors influence the growth of organisms. Develop a model to describe how food is rearranged through chemical reactions forming new molecules that support growth and/or release energy as this matter moves through an organism.",
    "big_question": "How does a chicken sandwich become a slam dunk?",
    "objectives": [
        "Trace the path of food molecules from digestion through cellular respiration",
        "Model how cells convert glucose and oxygen into ATP energy for movement",
        "Predict how exercise intensity affects energy demand and oxygen consumption",
        "Evaluate how nutrition choices affect athletic performance"
    ],
    "vocabulary": [
        ("Cellular Respiration", "The process cells use to convert glucose and oxygen into ATP energy and CO2"),
        ("ATP", "Adenosine triphosphate — the molecular 'energy currency' that powers all cell activities"),
        ("Glucose", "A simple sugar that serves as the primary fuel for cellular respiration"),
        ("Metabolism", "All the chemical reactions in an organism that convert food into energy and building materials")
    ],
    "components": [
        ("Food Intake (Glucose)", "Amount of glucose available from digested food", True),
        ("Oxygen Supply", "Amount of oxygen delivered to muscles through breathing and blood flow", True),
        ("ATP Production", "Amount of energy currency produced by cells for muscle contraction", False),
        ("Athletic Output", "Physical performance — speed, power, endurance of the athlete", False)
    ],
    "think_about_it": "When an athlete exercises harder, what happens to their oxygen demand? Why do you breathe harder during exercise?",
    "scenarios": [
        ("Resting State", "Set Food Intake and Oxygen Supply to baseline resting levels"),
        ("Maximum Effort", "Lock Food Intake to high and Oxygen to maximum — full sprint"),
        ("Running on Empty", "Lock Food Intake to 0% — what happens to performance?")
    ],
    "sim_scenarios": [
        ("Resting State", "Normal food intake, resting oxygen levels", "What do you predict about ATP Production at rest?"),
        ("Maximum Effort", "High glucose, maximum oxygen delivery", "What do you predict will happen to Athletic Output?"),
        ("No Fuel", "Lock Food Intake to 0%", "What happens to ATP Production and Athletic Output?")
    ],
    "discoveries": [
        "Food is literally rearranged into energy through chemical reactions in your cells",
        "Cellular respiration: Glucose + Oxygen → CO2 + Water + ATP (energy)",
        "Without enough oxygen, cells switch to anaerobic respiration — less efficient, produces lactic acid",
        "Athletes need more food AND more oxygen to sustain high performance"
    ],
    "answer": "Food molecules (glucose) are broken down through cellular respiration with oxygen, producing ATP energy that powers muscle contraction. LeBron's chicken sandwich is literally rearranged into the energy for a dunk!",
    "stem_title": "Design an Athlete's Nutrition Plan",
    "stem_mission": "Design an evidence-based nutrition and training plan for a student athlete to optimize their performance using cellular respiration science.",
    "stem_scenario": "Your school's basketball team is preparing for the championship. The coach hired your team to create a science-based nutrition plan for game day.",
    "stem_questions": [
        "What types of food provide the best glucose for cellular respiration?",
        "When should an athlete eat relative to game time?",
        "How does hydration affect cellular respiration?"
    ],
    "stem_design_qs": [
        "What foods will you include in the pre-game meal and why?",
        "How many hours before the game should the athlete eat?",
        "What should the athlete eat during halftime?",
        "How will you measure whether your plan improves performance?"
    ],
    "career": "Sports Nutritionists and Exercise Physiologists optimize athletic performance using science. They work with professional teams, Olympic athletes, and everyday people. They earn $55,000-$95,000/year.",
    "images": {
        "cover": ("cover-lebron-energy.png", "A dynamic action shot of a basketball player mid-dunk with artistic overlays showing molecular energy symbols and food molecules transforming into motion"),
        "landscape": ("landscape-athlete-nutrition.png", "8th grade students in a science lab testing food samples for calorie content using a calorimeter, wearing safety goggles, engaged experiment"),
        "modeling": ("modeling-respiration.png", "A diverse group of 8th grade students at computers building a cellular respiration model, molecule diagrams visible on screens"),
        "discussion": ("discussion-metabolism.png", "A teacher showing a diagram of cellular respiration while 8th grade students discuss and compare notes, active classroom"),
        "stem": ("stem-nutrition-plan.png", "8th grade students creating nutrition plan posters with food models and energy calculations, team collaboration, colorful classroom")
    },
    "pre_assessment": [
        "Where does the energy for your muscles come from?",
        "What happens in your body when you eat food?",
        "Why do you breathe harder when you exercise?",
        "Draw the journey of a piece of pizza from your plate to energy in your muscles."
    ],
    "extend_components": [
        ("Lactic Acid", "Builds up during intense exercise when oxygen is insufficient"),
        ("Heart Rate", "Increases to deliver more oxygen to working muscles"),
        ("Hydration Level", "Water is essential for chemical reactions in cells")
    ],
    "reflections": [
        "How is your body like a car engine that burns fuel?",
        "Why do marathon runners 'hit the wall' and suddenly lose energy?",
        "What's the connection between breathing and cellular respiration?",
        "Why do athletes need to eat more than non-athletes?",
        "How does your model explain why you feel tired after skipping lunch?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to describe how food molecules are rearranged through chemical reactions to release energy."),
        ("Disciplinary Core Idea", "LS1.C Organization for Matter and Energy Flow in Organisms", "Within individual organisms, food is broken down through chemical reactions that rearrange molecules and release energy."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace matter and energy as food molecules are transformed through cellular respiration into ATP energy and waste products.")
    ],
    "cast_items": [
        "Construct explanations for how food molecules provide energy through chemical reactions",
        "Develop models showing matter and energy flow in organisms",
        "Explain the relationship between environmental factors and organism growth"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During cellular respiration, glucose and oxygen are converted into carbon dioxide, water, and ATP. What type of process is this?"),
        ("Constructed Response:", "Explain the step-by-step process of how a banana you eat for breakfast provides the energy for running in gym class. Include the roles of glucose, oxygen, and ATP.")
    ],
    "background_intro": "Every movement you make — every heartbeat, every thought, every slam dunk — is powered by ATP, a molecule produced through cellular respiration. Understanding this process reveals how food literally becomes action.",
    "background_sections": [
        ("From Food to Glucose", "When you eat, digestion breaks complex food molecules into simpler ones. Carbohydrates are broken down into glucose (C6H12O6). This glucose enters the bloodstream and is delivered to every cell in your body. An average person's body contains about 4 grams of glucose in their blood at any time."),
        ("Cellular Respiration", "The equation: C6H12O6 + 6O2 → 6CO2 + 6H2O + ~36 ATP. This happens in the mitochondria of every cell. The process has three stages: glycolysis (splitting glucose), the Krebs cycle (extracting electrons), and the electron transport chain (making most of the ATP)."),
        ("ATP: The Energy Currency", "ATP is like cash for your cells. Every muscle contraction, nerve impulse, and chemical reaction is paid for with ATP. Your body produces and uses about 40 kg of ATP per day — roughly your body weight! But you only have about 250 grams at any given time, so it's constantly being recycled."),
        ("Aerobic vs. Anaerobic", "With oxygen (aerobic): 1 glucose → ~36 ATP (efficient). Without enough oxygen (anaerobic): 1 glucose → 2 ATP + lactic acid (inefficient). During intense exercise, muscles outpace oxygen delivery and switch to anaerobic respiration. The lactic acid buildup causes the burning feeling in your muscles.")
    ],
    "lever_L": "Students identify food intake, oxygen supply, ATP production, and athletic output as system components.",
    "lever_E": "Students determine that both food and oxygen are needed for ATP production (positive), and ATP drives athletic output (positive).",
    "lever_V": "Students build the cellular respiration model showing how food and oxygen become energy for movement.",
    "lever_Ev": "Students compare resting, maximum effort, and no-fuel scenarios.",
    "lever_R": "Students add lactic acid or heart rate to model anaerobic conditions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Basketball player with energy overlay", "say": "LeBron James eats a chicken sandwich. Two hours later, he dunks over three defenders. HOW?", "do": "Play a LeBron highlight. Ask: Where did the energy for that come from?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we trace the incredible journey from food to athletic performance.", "do": "Define cellular respiration as 'your cells burning fuel.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does food become a dunk?", "say": "A sandwich becomes a slam dunk. A banana becomes a sprint. How?", "do": "Quick write: Trace the energy from lunch to running.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how your body converts food into movement.", "do": "Preview the LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Metabolism system components", "say": "What inputs does your body need to produce energy?", "do": "Sort components. Emphasize that you need BOTH food AND oxygen.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Energy flow arrows", "say": "Without oxygen, your body switches to plan B — but it's way less efficient.", "do": "Map the pathway from food to ATP to movement.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Exercise intensity scenarios", "say": "What happens when you sprint but haven't eaten? Or eat but don't have enough oxygen?", "do": "Students run all three scenarios. Compare the graphs.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Your body is a chemical factory that turns food into motion. Every. Single. Move.", "do": "Discuss: Why do you breathe harder during exercise?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Nutrition plan challenge", "say": "The basketball team hired you to design their game-day nutrition plan.", "do": "Teams design evidence-based nutrition plans.", "time": "12 min"}
    ],
    "sort_reasoning": "Food Intake and Oxygen Supply are external because they come from outside the cell — food is eaten and oxygen is breathed in. ATP Production and Athletic Output are internal because they are the results of cellular processes that happen inside the organism.",
    "relationships": [
        ("Food Intake to ATP Production", "POSITIVE (+)", "More glucose available means more fuel for cellular respiration to produce ATP."),
        ("Oxygen Supply to ATP Production", "POSITIVE (+)", "More oxygen allows aerobic respiration, which produces ~18 times more ATP than anaerobic."),
        ("ATP Production to Athletic Output", "POSITIVE (+)", "More ATP means more energy available for muscle contraction, speed, and power.")
    ],
    "sim_answers": [
        ("Maximum Effort Scenario", "With high glucose and maximum oxygen, ATP Production is maximized. Athletic Output reaches peak levels. The model shows the body is efficiently converting food energy into motion through aerobic cellular respiration."),
        ("No Fuel Scenario", "Without food (glucose), ATP Production drops dramatically even if oxygen is plentiful. Athletic Output crashes. You can breathe all you want — without fuel, there's nothing to burn. This models what happens when an athlete 'hits the wall.'")
    ],
    "reflection_exemplars": [
        ("Why do marathon runners hit the wall?", "After about 90-120 minutes of intense exercise, the body depletes its stored glycogen (glucose reserves). Without glucose, ATP production drops dramatically. The runner suddenly feels exhausted, weak, and may have difficulty thinking clearly because the brain also needs glucose."),
        ("Why do you breathe harder during exercise?", "Exercise increases the demand for ATP, which increases the need for oxygen (a required input for efficient cellular respiration). Your brain detects rising CO2 levels (a waste product of respiration) and signals you to breathe faster and deeper to bring in more O2 and expel more CO2.")
    ],
    "stem_intro": "Show a clip of an elite athlete performing at peak level. Ask: What did they eat? When did they eat it? Connect to cellular respiration: nutrition IS energy science.",
    "stem_concepts": [
        ("Glycemic Index", "Foods with different rates of glucose release — fast-release for quick energy, slow-release for sustained performance."),
        ("Carb Loading", "Increasing glycogen stores before an endurance event by eating extra carbohydrates."),
        ("Recovery Nutrition", "Post-exercise eating that replenishes glycogen and provides protein for muscle repair.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan connects specific foods to cellular respiration, includes timing, and explains the science behind each choice"),
        ("Proficient (3)", "Plan references energy needs and includes science-based food choices with timing"),
        ("Developing (2)", "Plan mentions nutrition but doesn't connect to cellular respiration science"),
        ("Beginning (1)", "Plan is a generic food list without scientific reasoning")
    ],
    "support": [
        "Provide a simplified cellular respiration diagram with inputs and outputs",
        "Use an analogy: glucose = gasoline, oxygen = air intake, ATP = engine power",
        "Sentence frames: 'When food intake increases, ATP production __ because __'"
    ],
    "extensions": [
        "Calculate the ATP yield from a specific meal using calorie content",
        "Research and compare aerobic vs. anaerobic ATP production rates",
        "Add a lactic acid component and model the 'burn' during intense exercise"
    ],
    "cross_curr": [
        ("Math", "Calculate calories consumed vs. calories burned during different activities"),
        ("ELA", "Write a scientific explanation of the cellular respiration equation in student-friendly language"),
        ("Social Studies", "Research how food science and sports nutrition have evolved in professional athletics")
    ],
    "misconceptions": [
        ("Food gives you energy directly", "Food doesn't power muscles directly. Digestion breaks food into glucose, which cells convert to ATP through respiration. ATP is the actual energy molecule that powers all cellular work.", "Analogy: You can't pour crude oil into a car engine. It must be refined into gasoline first. Similarly, food must be 'refined' into ATP."),
        ("You only breathe to get oxygen", "You breathe for TWO reasons: to bring in O2 (input for respiration) AND to expel CO2 (waste product of respiration). Both are equally important. Too much CO2 is toxic.", "Show the full respiration equation — both sides matter."),
        ("Energy is created when you eat", "Energy is TRANSFORMED, not created. The chemical energy stored in food molecules (glucose) is converted to ATP energy through respiration. The total energy is conserved.", "Connect to conservation of energy from physics.")
    ]
}

L08 = {
    "id": "G08-L08",
    "title": "Why Do You Look Like That?",
    "subtitle": "The Genetic Lottery That Made You, You",
    "ngss": "MS-LS3-1, MS-LS3-2",
    "ngss_desc": "Develop and use a model to describe why structural changes to genes (mutations) located on chromosomes may affect proteins and may result in harmful, beneficial, or neutral effects to the structure and function of the organism. Develop and use a model to describe why asexual reproduction results in offspring with identical genetic information and sexual reproduction results in offspring with genetic variation.",
    "big_question": "Why do you look similar to your parents but not exactly like them?",
    "objectives": [
        "Explain how genes are passed from parents to offspring through chromosomes",
        "Model how sexual reproduction creates unique genetic combinations",
        "Predict trait inheritance patterns using dominant and recessive alleles",
        "Evaluate why genetic variation is important for species survival"
    ],
    "vocabulary": [
        ("Allele", "Different versions of the same gene — you inherit one from each parent"),
        ("Dominant", "An allele that is expressed even when only one copy is present"),
        ("Recessive", "An allele that is only expressed when two copies are present"),
        ("Genotype vs. Phenotype", "Genotype is the genetic code (Bb); phenotype is the observable trait (brown eyes)")
    ],
    "components": [
        ("Parent 1 Alleles", "The genetic contributions from one parent", True),
        ("Parent 2 Alleles", "The genetic contributions from the other parent", True),
        ("Offspring Genotype", "The combination of alleles the offspring inherits", False),
        ("Trait Expression (Phenotype)", "The observable physical trait that results from the genotype", False)
    ],
    "think_about_it": "If both parents carry one dominant and one recessive allele for eye color, what combinations could their child inherit?",
    "scenarios": [
        ("Both Dominant", "Set both parents to homozygous dominant (BB × BB)"),
        ("Carrier Parents", "Set both parents to heterozygous (Bb × Bb) — the classic cross"),
        ("One Recessive Parent", "Set one parent to bb and one to Bb")
    ],
    "sim_scenarios": [
        ("Both Dominant Parents", "BB × BB cross", "What do you predict about the offspring's trait expression?"),
        ("Carrier Cross", "Bb × Bb cross", "What percentage of offspring do you predict will show the recessive trait?"),
        ("Mixed Cross", "Bb × bb cross", "What are the possible genotypes of offspring?")
    ],
    "discoveries": [
        "You inherit ONE allele from each parent — your unique combination is why you're genetically unique",
        "Dominant alleles mask recessive ones, but recessive alleles are still passed on (carriers!)",
        "The classic Bb × Bb cross produces a 3:1 phenotype ratio (75% dominant, 25% recessive)",
        "Sexual reproduction creates variation through random allele combinations — that's evolution fuel"
    ],
    "answer": "You inherit a random combination of alleles from both parents. Because each parent has two alleles for every gene and you only get one from each, the combination creates a unique genetic blueprint that makes you similar to — but different from — both parents!",
    "stem_title": "Solve a Genetic Mystery",
    "stem_mission": "Use genetic inheritance patterns to solve a real-world mystery: determine the parents of an unknown organism based on trait evidence.",
    "stem_scenario": "A wildlife conservation team found a rare animal cub. They need to determine which adults are the parents to manage the breeding program. You have trait data for the cub and several potential parents.",
    "stem_questions": [
        "What traits does the cub express? What are its possible genotypes?",
        "Which parent combinations could produce this phenotype?",
        "How can you rule out impossible parent combinations?"
    ],
    "stem_design_qs": [
        "What evidence will you use to identify the parents?",
        "How will you test your hypothesis using Punnett squares?",
        "Can you identify the parents with certainty, or only probability?",
        "What additional tests might confirm your conclusion?"
    ],
    "career": "Genetic Counselors help families understand inherited conditions and make informed decisions. Forensic Geneticists use DNA to solve crimes. They earn $65,000-$110,000/year.",
    "images": {
        "cover": ("cover-genetics.png", "A creative image showing a family portrait with visible trait connections between parents and children, highlighting eye color, hair, and other features, warm family photo"),
        "landscape": ("landscape-dna.png", "8th grade students examining DNA models and Punnett square worksheets in a modern science lab, engaged in genetics hands-on learning"),
        "modeling": ("modeling-inheritance.png", "A diverse group of 8th grade students at computers building a genetic inheritance model, Punnett squares visible on screens"),
        "discussion": ("discussion-traits.png", "A teacher leading a discussion about inherited traits while 8th grade students compare their own features like attached earlobes and tongue rolling"),
        "stem": ("stem-genetic-mystery.png", "8th grade students working as 'genetic detectives' examining trait cards and solving a mystery with evidence boards, CSI-style classroom activity")
    },
    "pre_assessment": [
        "Why do you look similar to your parents but not identical?",
        "What do you think determines your eye color?",
        "Why might siblings look different from each other?",
        "Draw what you think a 'gene' looks like and what it does."
    ],
    "extend_components": [
        ("Mutations", "Random changes in DNA that create new alleles"),
        ("Environmental Factors", "Non-genetic influences that affect how traits are expressed"),
        ("Multiple Genes", "Many traits are controlled by more than one gene")
    ],
    "reflections": [
        "Why are you genetically unique even among siblings from the same parents?",
        "How does sexual reproduction create more variation than asexual reproduction?",
        "Why might genetic variation be important for a species' survival?",
        "If two brown-eyed parents have a blue-eyed child, how is that possible?",
        "How is a Punnett square similar to the model you built in ModelIt?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to describe how genes on chromosomes determine trait inheritance patterns."),
        ("Disciplinary Core Idea", "LS3.A Inheritance of Traits / LS3.B Variation of Traits", "Organisms reproduce sexually, producing offspring with genetic variation through random allele combination."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify how the CAUSE (specific allele combinations) leads to the EFFECT (observable traits in offspring).")
    ],
    "cast_items": [
        "Use models to describe how gene mutations may affect organisms",
        "Explain why sexual reproduction produces genetic variation",
        "Predict offspring phenotypes using inheritance models"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two parents are both heterozygous (Bb) for a trait. What is the probability that their offspring will show the recessive phenotype?"),
        ("Constructed Response:", "Explain why two siblings with the same parents can look very different from each other. Use the concepts of alleles, dominant/recessive traits, and random combination in your answer.")
    ],
    "background_intro": "Every human has approximately 20,000-25,000 genes on 23 pairs of chromosomes. The specific combination of alleles you inherit makes you genetically unique — unless you have an identical twin. Understanding inheritance is key to medicine, agriculture, and evolution.",
    "background_sections": [
        ("Chromosomes and Genes", "Humans have 23 pairs of chromosomes — one set from each parent. Each chromosome contains hundreds to thousands of genes. Each gene has a specific location (locus) on a chromosome. You have two copies of every gene (one from each parent), and these copies may be the same or different versions (alleles)."),
        ("Dominant and Recessive", "Dominant alleles (represented by capital letters, like B) are expressed when at least one copy is present. Recessive alleles (lowercase, like b) are only expressed when two copies are present (bb). Heterozygous individuals (Bb) carry the recessive allele but show the dominant trait — they are 'carriers.'"),
        ("Sexual vs. Asexual Reproduction", "Sexual reproduction mixes genetic material from two parents, creating unique offspring through random allele combination. Asexual reproduction produces genetically identical offspring (clones). Genetic variation from sexual reproduction is crucial for species survival because it provides the raw material for natural selection."),
        ("Beyond Simple Inheritance", "Most human traits aren't controlled by a single gene with simple dominant/recessive patterns. Traits like skin color, height, and intelligence are influenced by multiple genes (polygenic inheritance) AND environmental factors. This is why human diversity is so rich and complex.")
    ],
    "lever_L": "Students identify parent alleles, offspring genotype, and trait expression as system components.",
    "lever_E": "Students determine that parent alleles combine to create offspring genotype (positive), and genotype determines phenotype based on dominant/recessive rules.",
    "lever_V": "Students build the inheritance model showing how parental alleles combine in offspring.",
    "lever_Ev": "Students run different parent genotype combinations and observe phenotype ratios.",
    "lever_R": "Students add mutation or environmental factors to explore more complex inheritance.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Family trait comparison", "say": "Look at your hands. Your eyes. Why do they look the way they do?", "do": "Quick trait survey: Who can roll their tongue? Attached vs. detached earlobes?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we decode the genetic lottery that made you, you.", "do": "Pre-teach allele, dominant, recessive with simple examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why you look like your parents but not exactly", "say": "You got DNA from both parents. So why aren't you a 50-50 clone?", "do": "Show sibling photos that look very different. Discuss.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how genes are shuffled to create unique individuals.", "do": "Preview the LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Genetic system components", "say": "What goes INTO making your traits? What comes OUT?", "do": "Sort components. Emphasize: one allele from each parent.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Inheritance flow arrows", "say": "Dominant alleles are like volume — one copy is enough to be 'heard.'", "do": "Connect Punnett square logic to the model relationships.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Inheritance scenarios", "say": "What happens when two carriers have children? Let's see the ratios.", "do": "Students predict, then run. Discover the 3:1 ratio.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Every time you're conceived, it's a genetic lottery. The odds are never exactly the same.", "do": "Discuss: Why is variation important for species?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Genetic mystery", "say": "A rare animal cub was found. CSI: Genetics — figure out who the parents are!", "do": "Teams use trait evidence and Punnett squares to solve the mystery.", "time": "12 min"}
    ],
    "sort_reasoning": "Parent 1 Alleles and Parent 2 Alleles are external because they are the genetic inputs that existed before the offspring was conceived. Offspring Genotype and Trait Expression are internal because they are determined by the combination of those parental inputs.",
    "relationships": [
        ("Parent 1 Alleles to Offspring Genotype", "POSITIVE (+)", "Parent 1's alleles directly contribute to half of the offspring's genetic makeup."),
        ("Parent 2 Alleles to Offspring Genotype", "POSITIVE (+)", "Parent 2's alleles contribute the other half of the offspring's genetic makeup."),
        ("Offspring Genotype to Trait Expression", "POSITIVE (+)", "The specific allele combination determines which phenotype is expressed based on dominant/recessive rules.")
    ],
    "sim_answers": [
        ("Carrier Cross (Bb × Bb)", "The model produces offspring in a ~3:1 phenotype ratio: approximately 75% show the dominant trait (BB or Bb genotype) and 25% show the recessive trait (bb genotype). The genotype ratio is 1 BB : 2 Bb : 1 bb."),
        ("Mixed Cross (Bb × bb)", "The model produces offspring in a ~1:1 phenotype ratio: approximately 50% show the dominant trait (Bb) and 50% show the recessive trait (bb). Every offspring gets a recessive allele from the bb parent.")
    ],
    "reflection_exemplars": [
        ("How can two brown-eyed parents have a blue-eyed child?", "If both parents are carriers (Bb), each has one dominant brown allele and one recessive blue allele. There's a 25% chance they both pass on their recessive allele, creating a bb offspring with blue eyes. The recessive allele was hidden (masked by dominant) but still passed on."),
        ("Why is genetic variation important?", "Variation means a population has different traits. If the environment changes (new disease, climate shift), some individuals may have traits that help them survive. Without variation (like in asexual reproduction), every organism is identical and equally vulnerable. This connects to natural selection from L01.")
    ],
    "stem_intro": "Present the mystery: A wildlife team found a rare cub. They have trait data (coat color, pattern, etc.) for the cub and 4 potential parent pairs. Students must use genetics to identify the parents.",
    "stem_concepts": [
        ("Process of Elimination", "If a cub shows a recessive trait (bb), both parents MUST carry at least one recessive allele."),
        ("Probability", "Genetic inheritance deals in probabilities, not certainties. A 25% chance isn't zero."),
        ("Multiple Traits", "Using multiple trait analyses increases confidence in parent identification.")
    ],
    "stem_eval": [
        ("Expert (4)", "Uses Punnett squares for multiple traits, explains reasoning, identifies correct parents with evidence"),
        ("Proficient (3)", "Uses Punnett squares correctly and identifies likely parents"),
        ("Developing (2)", "Shows some inheritance understanding but makes errors in Punnett squares"),
        ("Beginning (1)", "Guesses parents without using genetic reasoning")
    ],
    "support": [
        "Provide pre-made Punnett square templates",
        "Use physical coin flips to model random allele selection",
        "Sentence frames: 'The offspring has genotype __ because it inherited __ from parent 1 and __ from parent 2'"
    ],
    "extensions": [
        "Research incomplete dominance and codominance and add to model",
        "Explore polygenic inheritance — why don't humans come in just two heights?",
        "Research genetic testing and its ethical implications"
    ],
    "cross_curr": [
        ("Math", "Calculate probability ratios for multi-trait crosses using multiplication rule"),
        ("ELA", "Write a narrative from the perspective of an allele being passed through three generations"),
        ("Social Studies", "Research the history of genetics from Mendel to the Human Genome Project")
    ],
    "misconceptions": [
        ("Traits blend like paint", "Traits don't blend — alleles maintain their identity. A Bb individual doesn't have 'medium' expression. The dominant allele is expressed and the recessive is masked but preserved.", "Show that blue-eyed children can come from brown-eyed parents — the blue allele was preserved, not blended away."),
        ("You look exactly 50% like each parent", "You inherit 50% of your DNA from each parent, but WHICH 50% is random. Siblings (except identical twins) get different random halves, which is why they can look very different from each other.", "Ask: If you flip two coins 10 times each, will you always get the same results?"),
        ("Dominant means better or more common", "Dominant only means the allele is expressed when one copy is present. It doesn't mean it's 'better' or more frequent. Polydactyly (extra fingers) is dominant but rare.", "List dominant traits that aren't more common in the population.")
    ]
}

L09 = {
    "id": "G08-L09",
    "title": "Your Music Is a Wave",
    "subtitle": "How Sound, Light, and WiFi All Follow the Same Rules",
    "ngss": "MS-PS4-1, MS-PS4-2",
    "ngss_desc": "Use mathematical representations to describe a simple model for waves that includes how the amplitude of a wave is related to the energy in a wave. Develop and use a model to describe that waves are reflected, absorbed, or transmitted through various materials.",
    "big_question": "How does a wave carry your favorite song from a speaker to your ear?",
    "objectives": [
        "Explain the relationship between wave properties (amplitude, frequency, wavelength)",
        "Model how changing amplitude and frequency affects the energy and pitch of sound",
        "Predict how waves behave when they encounter different materials",
        "Evaluate real-world applications of wave science in music and technology"
    ],
    "vocabulary": [
        ("Amplitude", "The height of a wave — determines loudness in sound and brightness in light"),
        ("Frequency", "How many wave cycles per second (Hz) — determines pitch in sound and color in light"),
        ("Wavelength", "The distance between two identical points on consecutive waves"),
        ("Medium", "The material through which a wave travels — can be air, water, solid, or vacuum (for light)")
    ],
    "components": [
        ("Wave Amplitude", "The height/intensity of the wave from the baseline", True),
        ("Wave Frequency", "Number of complete wave cycles per second", True),
        ("Wave Energy", "Total energy carried by the wave", False),
        ("Sound Perception", "What we hear — loudness and pitch", False)
    ],
    "think_about_it": "When you turn the volume UP on your speaker, what wave property are you changing? When you play a higher note, what changes?",
    "scenarios": [
        ("Whisper", "Set Amplitude to low and Frequency to medium"),
        ("Screaming High Note", "Lock Amplitude AND Frequency to maximum"),
        ("Bass Drop", "Set Amplitude to maximum but Frequency to minimum")
    ],
    "sim_scenarios": [
        ("Whisper", "Low amplitude, medium frequency", "What do you predict about the Wave Energy and Sound Perception?"),
        ("Screaming High Note", "Maximum amplitude and frequency", "What happens to Wave Energy at maximum settings?"),
        ("Bass Drop", "Maximum amplitude, minimum frequency", "How does this sound different from the high note?")
    ],
    "discoveries": [
        "Amplitude controls LOUDNESS — bigger waves carry more energy",
        "Frequency controls PITCH — more cycles per second = higher pitch",
        "Doubling the amplitude QUADRUPLES the energy (squared relationship!)",
        "Sound, light, radio, and WiFi are ALL waves following the same basic rules"
    ],
    "answer": "Sound travels as a wave through the air. The speaker vibrates, creating pressure waves. The amplitude determines how LOUD (energy), and the frequency determines the PITCH. Your ear converts these waves back into signals your brain interprets as music!",
    "stem_title": "Design a Concert Venue",
    "stem_mission": "Design a concert venue or music room that optimizes sound quality using wave behavior principles.",
    "stem_scenario": "A music school needs a new performance hall. The architect hired your team to make science-based recommendations for materials and design to ensure great acoustics.",
    "stem_questions": [
        "Which materials reflect sound? Which absorb it?",
        "How does room shape affect sound wave behavior?",
        "What causes echo and how can you control it?"
    ],
    "stem_design_qs": [
        "What shape will your venue be and why?",
        "What wall materials will you use to control sound?",
        "How will you prevent echo while maintaining volume?",
        "Where should speakers be placed for the best experience?"
    ],
    "career": "Acoustical Engineers design concert halls, studios, and noise-canceling headphones. Audio Engineers produce music using wave science. They earn $60,000-$110,000/year.",
    "images": {
        "cover": ("cover-sound-waves.png", "A visually striking image of sound waves emanating from headphones with colorful frequency visualization, music and science fusion aesthetic"),
        "landscape": ("landscape-music-science.png", "8th grade students in a music-science lab experimenting with tuning forks, oscilloscopes showing wave patterns, and sound meters"),
        "modeling": ("modeling-waves.png", "A diverse group of 8th grade students at computers building a wave model, one screen showing a sine wave graph with labeled parts"),
        "discussion": ("discussion-sound.png", "A teacher demonstrating sound waves with a speaker and a candle flame while 8th grade students observe, hands-on wave demonstration"),
        "stem": ("stem-concert-venue.png", "8th grade students building scale models of concert venues with different acoustic materials, testing sound quality, collaborative design activity")
    },
    "pre_assessment": [
        "What is a wave? Can you describe one?",
        "What makes a sound loud vs. quiet?",
        "What makes a sound high-pitched vs. low-pitched?",
        "Draw a wave and label any parts you know."
    ],
    "extend_components": [
        ("Medium Density", "How dense the material the wave travels through is"),
        ("Reflection", "Sound bouncing off hard surfaces (echoes)"),
        ("Absorption", "Sound energy being converted to heat in soft materials")
    ],
    "reflections": [
        "How is turning up the volume on your phone related to wave amplitude?",
        "Why does a bass guitar sound different from a piccolo if they play the same note?",
        "Why can you hear someone through a wall but not see them?",
        "How is a WiFi signal similar to a sound wave? How is it different?",
        "What would music sound like in a room with no wave absorption (all hard surfaces)?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model describing how amplitude and frequency affect wave energy and perception."),
        ("Disciplinary Core Idea", "PS4.A Wave Properties", "A simple wave has a repeating pattern with specific amplitude, frequency, and wavelength related to energy."),
        ("Crosscutting Concept", "Patterns", "Students identify the repeating pattern structure of waves and how changing pattern parameters changes energy and perception.")
    ],
    "cast_items": [
        "Use mathematical representations to describe wave amplitude and energy relationships",
        "Develop models showing how waves interact with different materials",
        "Describe wave properties using frequency, amplitude, and wavelength"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A sound wave has its amplitude doubled while frequency stays the same. What happens to the energy of the wave?"),
        ("Constructed Response:", "Using wave properties, explain why a concert sounds different in a carpeted room versus a room with all hard surfaces. Include the concepts of reflection and absorption.")
    ],
    "background_intro": "Every sound you hear, every color you see, every WiFi signal your phone receives — they're all waves. Understanding wave properties reveals the physics behind music, communication, and even medical imaging.",
    "background_sections": [
        ("Wave Basics", "A wave is a repeating disturbance that transfers energy without transferring matter. The key properties are: amplitude (height from baseline), frequency (cycles per second, measured in Hertz), wavelength (distance between identical points), and speed (depends on the medium)."),
        ("Amplitude and Energy", "Wave energy is proportional to amplitude SQUARED. This means doubling the amplitude quadruples the energy. In sound, amplitude determines loudness. In light, amplitude determines brightness. This squared relationship is why a small increase in volume requires a large increase in speaker power."),
        ("Frequency and Perception", "Humans can hear frequencies from about 20 Hz (deep bass) to 20,000 Hz (high pitch). Frequency determines the pitch of sound and the color of light. Musical notes correspond to specific frequencies: middle C is 262 Hz, the A above it is 440 Hz."),
        ("Wave Interactions with Materials", "When waves encounter a new material, they can be: reflected (bounced back — echo), absorbed (converted to heat — sound dampening), or transmitted (passed through). Most materials do all three to varying degrees. Hard surfaces reflect more sound; soft surfaces absorb more.")
    ],
    "lever_L": "Students identify wave amplitude, wave frequency, wave energy, and sound perception as system components.",
    "lever_E": "Students determine that amplitude strongly increases energy (squared relationship), and frequency affects pitch perception.",
    "lever_V": "Students build the wave model showing how properties connect to energy and perception.",
    "lever_Ev": "Students compare whisper, screaming high note, and bass drop scenarios.",
    "lever_R": "Students add medium density or reflection to model material interactions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Sound waves from headphones", "say": "Right now, invisible waves are passing through you. Sound, WiFi, radio — they're everywhere.", "do": "Play a short clip of music. Ask: How did that sound get from the speaker to your ears?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we decode the physics of music, sound, and all waves.", "do": "Pre-teach amplitude (loudness) and frequency (pitch) with hand waves.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does a wave carry music?", "say": "Your favorite song is just air molecules vibrating in a pattern. How?", "do": "Demo: speaker with visible cone vibration.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the wave properties that make music possible.", "do": "Preview the LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Wave property components", "say": "What properties define a wave? What can we control?", "do": "Sort components. Use a slinky or rope to demonstrate.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Wave property relationships", "say": "Here's the surprise: doubling amplitude QUADRUPLES energy. Not doubles — quadruples!", "do": "Map relationships. Emphasize the squared relationship.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Sound comparison scenarios", "say": "Let's hear the difference between a whisper and a scream in wave terms.", "do": "Students adjust amplitude and frequency, observe energy changes.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "ALL waves follow these same rules — sound, light, WiFi, ocean waves.", "do": "Connect to real-world wave applications.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Concert venue design", "say": "A music school hired YOU to design their performance hall. Acoustics matter!", "do": "Teams design venues considering reflection, absorption, and room shape.", "time": "12 min"}
    ],
    "sort_reasoning": "Wave Amplitude and Wave Frequency are external because they are properties controlled by the source (speaker, instrument). Wave Energy and Sound Perception are internal because they are the resulting effects determined by those input properties.",
    "relationships": [
        ("Wave Amplitude to Wave Energy", "POSITIVE (+)", "Higher amplitude means more energy — in fact, energy scales with amplitude SQUARED (double amplitude = 4x energy)."),
        ("Wave Frequency to Sound Perception", "POSITIVE (+)", "Higher frequency waves are perceived as higher pitch. Lower frequency = lower pitch (bass)."),
        ("Wave Energy to Sound Perception", "POSITIVE (+)", "More wave energy is perceived as louder sound. The wave carries more energy to your eardrum.")
    ],
    "sim_answers": [
        ("Screaming High Note", "At maximum amplitude AND frequency, Wave Energy is at its peak (amplitude squared). Sound Perception shows maximum loudness AND highest pitch. This represents the most energetic sound wave in our model."),
        ("Bass Drop", "At maximum amplitude but minimum frequency, Wave Energy is still high (amplitude drives energy). Sound Perception shows maximum loudness but lowest pitch. The deep bass vibration carries a lot of energy but at a low frequency — that's why you can FEEL bass in your chest.")
    ],
    "reflection_exemplars": [
        ("Why does bass feel different from treble?", "Bass waves have low frequency (long wavelength) and can actually vibrate your body because the wavelengths are long enough to physically move objects. High-frequency waves have shorter wavelengths that primarily affect your eardrums. That's why you feel bass in your chest at concerts."),
        ("Why does a room's material affect sound?", "Hard surfaces (concrete, glass) reflect most sound waves back into the room, creating echoes and reverb. Soft surfaces (carpet, curtains, foam) absorb sound energy by converting it to tiny amounts of heat. Good acoustics require the right balance of reflection and absorption.")
    ],
    "stem_intro": "Play the same song in the classroom vs. a hallway. Notice the difference? Challenge: Design a venue where music sounds amazing. Your recommendations must be based on wave science.",
    "stem_concepts": [
        ("Acoustic Panels", "Shaped surfaces that scatter sound waves to reduce echo while maintaining volume."),
        ("Bass Traps", "Special absorbers designed for low-frequency sounds that are hardest to control."),
        ("Diffusion", "Scattering sound waves in many directions to create an even sound field.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses reflection, absorption, and room shape with scientific reasoning for each choice"),
        ("Proficient (3)", "Design uses wave science principles and addresses at least two acoustic factors"),
        ("Developing (2)", "Design mentions acoustics but lacks specific wave science connections"),
        ("Beginning (1)", "Design doesn't connect to wave behavior or material properties")
    ],
    "support": [
        "Provide a labeled wave diagram with amplitude, frequency, and wavelength",
        "Use a slinky or rope to physically demonstrate wave properties",
        "Sentence frames: 'When amplitude increases, wave energy __ because __'"
    ],
    "extensions": [
        "Research the physics of noise-canceling headphones (destructive interference)",
        "Add medium density component and model how sound travels differently in air vs. water vs. steel",
        "Calculate the wavelength of your favorite song's bass note using v = fλ"
    ],
    "cross_curr": [
        ("Math", "Graph the squared relationship between amplitude and energy; calculate wavelength from frequency and speed"),
        ("ELA", "Write a technical explanation of how speakers convert electrical signals into sound waves"),
        ("Social Studies", "Research how different cultures use acoustics in architectural design (amphitheaters, cathedrals, etc.)")
    ],
    "misconceptions": [
        ("Sound can travel through empty space", "Sound requires a medium (matter) to travel through. Sound travels through air, water, and solids, but NOT through a vacuum. In space, no one can hear you scream!", "Ask: If sound needs air molecules to vibrate, what happens when there are no air molecules?"),
        ("Loud sounds travel faster", "Volume (amplitude) does NOT affect the speed of sound. A whisper and a scream travel at the same speed (~343 m/s in air). Amplitude only affects energy, not speed.", "Analogy: A big wave and a small wave in a pool move at the same speed — one is just taller."),
        ("Higher frequency means more energy", "Frequency affects pitch, not necessarily total energy. Amplitude is the primary driver of wave energy. A loud bass note (high amplitude, low frequency) can carry more energy than a quiet high note (low amplitude, high frequency).", "Compare: Which carries more energy — a whispered scream or a felt bass drop?")
    ]
}

L10 = {
    "id": "G08-L10",
    "title": "Hand Warmers and Hidden Reactions",
    "subtitle": "How Atoms Rearrange to Create Heat, Light, and Everything You Use",
    "ngss": "MS-PS1-4, MS-PS1-5",
    "ngss_desc": "Develop a model that predicts and describes changes in particle motion, temperature, and state of a pure substance when thermal energy is added or removed. Develop and use a model to describe how the total number of atoms does not change in a chemical reaction and thus mass is conserved.",
    "big_question": "How can a small packet create heat without fire, batteries, or electricity?",
    "objectives": [
        "Explain how chemical reactions rearrange atoms to form new substances",
        "Model how exothermic reactions release energy as heat",
        "Apply the law of conservation of mass to chemical reactions",
        "Predict whether a reaction is exothermic or endothermic based on temperature change"
    ],
    "vocabulary": [
        ("Chemical Reaction", "A process where atoms rearrange to form new substances with different properties"),
        ("Exothermic", "A reaction that RELEASES energy as heat — the surroundings get warmer"),
        ("Endothermic", "A reaction that ABSORBS energy as heat — the surroundings get cooler"),
        ("Conservation of Mass", "In a chemical reaction, the total mass of reactants equals the total mass of products")
    ],
    "components": [
        ("Iron Powder Amount", "The quantity of iron available for the reaction", True),
        ("Oxygen Exposure", "How much air (oxygen) the iron powder is exposed to", True),
        ("Reaction Rate", "How fast the iron oxidation reaction proceeds", False),
        ("Heat Output", "The thermal energy released by the exothermic reaction", False)
    ],
    "think_about_it": "When you open a hand warmer and expose the iron powder to more oxygen, what do you think happens to the temperature?",
    "scenarios": [
        ("Sealed Packet", "Set Oxygen Exposure to 0% — the reaction can't start"),
        ("Normal Use", "Set Iron Powder to normal and Oxygen Exposure to moderate"),
        ("Maximum Heat", "Lock both Iron Powder and Oxygen Exposure to maximum")
    ],
    "sim_scenarios": [
        ("Sealed (No Oxygen)", "Iron powder present, no oxygen", "What do you predict will happen to Heat Output?"),
        ("Normal Use", "Normal iron amount, moderate oxygen", "What do you predict about Reaction Rate and Heat Output over time?"),
        ("Maximum Exposure", "Maximum iron, maximum oxygen", "How does this compare to normal use?")
    ],
    "discoveries": [
        "Iron + Oxygen → Iron Oxide (rust) — this reaction RELEASES heat",
        "The same atoms exist before and after — they just rearranged (conservation of mass!)",
        "More reactants AND more oxygen = faster reaction = more heat",
        "The hand warmer eventually stops because the iron runs out — a limiting reactant!"
    ],
    "answer": "Hand warmers contain iron powder that reacts with oxygen in the air. This exothermic chemical reaction releases heat energy as atoms rearrange from iron and oxygen into iron oxide (rust) — the same total atoms, just in a new arrangement!",
    "stem_title": "Design a Better Hand Warmer",
    "stem_mission": "Design an improved hand warmer that provides consistent heat for a specific duration using your understanding of reaction rates and energy transfer.",
    "stem_scenario": "An outdoor equipment company wants to create a hand warmer that lasts exactly 8 hours at a comfortable temperature for winter hikers. Use your model to design the specifications.",
    "stem_questions": [
        "How can you control the rate of the reaction to make heat last longer?",
        "What factors determine how hot the hand warmer gets?",
        "How does the amount of iron relate to how long the warmer lasts?"
    ],
    "stem_design_qs": [
        "How much iron powder will you use?",
        "How will you control oxygen flow to regulate temperature?",
        "What insulating materials will you use?",
        "How will you verify that mass is conserved in your design?"
    ],
    "career": "Chemical Engineers design products using chemical reaction principles. Materials Scientists develop new materials with specific thermal properties. They earn $75,000-$130,000/year.",
    "images": {
        "cover": ("cover-hand-warmer.png", "A dramatic close-up of an opened hand warmer packet with iron powder visible, a person's hands warming up, winter outdoor setting with frost"),
        "landscape": ("landscape-chemistry.png", "8th grade students in a chemistry lab conducting an exothermic reaction experiment with temperature probes and safety goggles, engaged science class"),
        "modeling": ("modeling-reactions.png", "A diverse group of 8th grade students at computers building a chemical reaction model, molecular diagrams visible on screens"),
        "discussion": ("discussion-reactions.png", "A teacher demonstrating a chemical reaction while 8th grade students record temperature changes with digital thermometers, interactive classroom"),
        "stem": ("stem-hand-warmer.png", "8th grade students designing and testing hand warmer prototypes using iron powder, salt, and activated carbon, measuring temperature with probes")
    },
    "pre_assessment": [
        "How do you think a hand warmer works?",
        "What is a chemical reaction?",
        "What happens to the atoms during a chemical reaction?",
        "If you weigh the ingredients before a reaction and the products after, will the mass be different?"
    ],
    "extend_components": [
        ("Salt (Catalyst)", "Salt speeds up the iron-oxygen reaction without being consumed"),
        ("Carbon (Adsorbent)", "Activated carbon helps distribute heat evenly and holds moisture"),
        ("Insulation", "The packaging material that controls how quickly heat escapes")
    ],
    "reflections": [
        "Why does a hand warmer stop working eventually? Where did the iron go?",
        "How is rusting a nail the same chemical reaction as a hand warmer, just slower?",
        "If atoms aren't created or destroyed, why does the hand warmer feel like it 'created' heat?",
        "What's the difference between a hand warmer (exothermic) and an instant cold pack (endothermic)?",
        "How does controlling oxygen exposure control the reaction rate?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to describe how atoms rearrange in a chemical reaction while total mass is conserved."),
        ("Disciplinary Core Idea", "PS1.B Chemical Reactions", "Substances react chemically to form new substances with different properties. The total number of atoms is conserved."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace how matter (atoms) is conserved while energy is released as thermal energy in an exothermic reaction.")
    ],
    "cast_items": [
        "Predict changes in temperature when thermal energy is added or removed",
        "Describe how atoms rearrange in chemical reactions while mass is conserved",
        "Use models to explain exothermic and endothermic reactions"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Iron powder (10g) reacts with oxygen from the air inside a sealed hand warmer. After the reaction is complete, what is the total mass of the products?"),
        ("Constructed Response:", "Using the law of conservation of mass, explain what happens to the atoms during the chemical reaction inside a hand warmer. Where does the heat come from if atoms are neither created nor destroyed?")
    ],
    "background_intro": "Hand warmers are elegant examples of chemistry in action. The simple exothermic reaction of iron oxidation demonstrates both conservation of mass and energy transformation — making abstract chemistry concepts tangible and practical.",
    "background_sections": [
        ("The Chemistry of Hand Warmers", "Hand warmers contain: iron powder (reactant), salt (catalyst to speed the reaction), activated carbon (distributes heat and retains moisture), and vermiculite (insulation). When exposed to air, the iron reacts with oxygen: 4Fe + 3O2 → 2Fe2O3 + heat. This is the same reaction as rusting, but engineered to happen faster."),
        ("Exothermic vs. Endothermic", "Exothermic reactions release energy to the surroundings (hand warmers, combustion, cellular respiration). Endothermic reactions absorb energy from the surroundings (instant cold packs, photosynthesis, cooking an egg). The direction of energy flow determines whether you feel heat or cold."),
        ("Conservation of Mass", "Antoine Lavoisier discovered that mass is conserved in chemical reactions. In a hand warmer: the mass of iron + the mass of oxygen that reacts = the mass of iron oxide produced. No atoms are created or destroyed — they simply rearrange. If you weigh a sealed hand warmer before and after, the mass is identical."),
        ("Reaction Rates", "Several factors affect how fast a reaction occurs: surface area (powder reacts faster than a solid chunk), temperature (higher temp = faster), concentration of reactants (more oxygen = faster), and catalysts (salt speeds up the iron oxidation). Hand warmers are engineered to balance these factors for consistent, safe heat.")
    ],
    "lever_L": "Students identify iron powder amount, oxygen exposure, reaction rate, and heat output as system components.",
    "lever_E": "Students determine that both iron and oxygen positively affect reaction rate, and reaction rate positively affects heat output.",
    "lever_V": "Students build the chemical reaction model showing how inputs drive the reaction and produce heat.",
    "lever_Ev": "Students compare sealed (no reaction), normal use, and maximum exposure scenarios.",
    "lever_R": "Students add salt (catalyst) or insulation to model real hand warmer engineering.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Hand warmer in cold weather", "say": "This little packet creates heat for 8 hours. No batteries. No fire. No electricity. How?", "do": "Give students hand warmers to feel. Where does the heat come from?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we discover how atoms rearranging can create heat energy.", "do": "Define exothermic with everyday examples (warm things = exothermic).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How can a packet create heat?", "say": "No fuel is burning. No electricity flows. But it's warm. Chemistry is happening!", "do": "Quick write: Where do you think the heat comes from?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the chemical reaction that turns iron and air into heat.", "do": "Preview the LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Reaction system components", "say": "What ingredients does this reaction need? What does it produce?", "do": "Open a hand warmer. Identify the iron powder. Discuss what happens when exposed to air.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Reaction relationship arrows", "say": "Both iron AND oxygen are needed. Take away either one and the reaction stops.", "do": "Demonstrate: seal a hand warmer in a plastic bag — it stops getting warmer.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Reaction rate scenarios", "say": "What happens if we give the iron MORE oxygen? Less oxygen? No oxygen?", "do": "Students predict, then run. Focus on the limiting reactant concept.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "The atoms didn't disappear — they rearranged. Iron + oxygen = iron oxide + HEAT.", "do": "Weigh a sealed hand warmer before and after. Same mass! Conservation proven.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Better hand warmer design", "say": "A hiking company hired you to design a better hand warmer. Use chemistry!", "do": "Teams design hand warmers with specific heat and duration targets.", "time": "12 min"}
    ],
    "sort_reasoning": "Iron Powder Amount and Oxygen Exposure are external because they are the inputs you can control — how much iron is packed in and how much air reaches it. Reaction Rate and Heat Output are internal because they are the results of the chemical reaction between those inputs.",
    "relationships": [
        ("Iron Powder Amount to Reaction Rate", "POSITIVE (+)", "More iron powder means more reactant available, allowing a faster and longer-lasting reaction."),
        ("Oxygen Exposure to Reaction Rate", "POSITIVE (+)", "More oxygen allows more iron atoms to react simultaneously, speeding up the reaction."),
        ("Reaction Rate to Heat Output", "POSITIVE (+)", "A faster reaction releases more heat energy per unit time, making the hand warmer hotter.")
    ],
    "sim_answers": [
        ("Sealed (No Oxygen)", "With Oxygen Exposure at 0%, Reaction Rate stays at zero — no reaction can occur. Heat Output remains at baseline (room temperature). This is why hand warmers come in sealed packages — blocking oxygen prevents the reaction from starting early."),
        ("Maximum Exposure", "With maximum iron AND oxygen, Reaction Rate peaks rapidly and Heat Output is very high initially. However, the iron is consumed faster, so the total duration is shorter. More isn't always better — the company wants CONSISTENT heat over 8 hours, not a burst of heat followed by nothing.")
    ],
    "reflection_exemplars": [
        ("Why does the hand warmer stop?", "The hand warmer stops producing heat when one of the reactants is used up — usually the iron powder. This is the concept of a limiting reactant. All the iron has been converted to iron oxide (rust). The atoms still exist; they're just in a new arrangement that doesn't produce more heat."),
        ("Where does the heat come from?", "The heat comes from the REARRANGEMENT of chemical bonds. When iron atoms bond with oxygen atoms to form iron oxide, the new bonds are at a lower energy state than the original separate elements. The difference in energy is released as heat. No atoms are created or destroyed — only rearranged.")
    ],
    "stem_intro": "Open a hand warmer in class. Measure its temperature over time. Challenge: Design a hand warmer with specific performance targets (temperature range, duration, weight).",
    "stem_concepts": [
        ("Limiting Reactant", "The reactant that runs out first determines when the reaction stops. More iron = longer duration."),
        ("Reaction Rate Control", "Controlling oxygen flow (porosity of the packaging) controls how fast the reaction occurs and how hot it gets."),
        ("Insulation Engineering", "The outer packaging affects how much heat reaches the user vs. how much escapes to the environment.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design specifies amounts, addresses reaction rate control, explains conservation of mass, and meets duration/temperature targets"),
        ("Proficient (3)", "Design uses reaction rate principles and addresses at least two design parameters"),
        ("Developing (2)", "Design mentions chemistry but lacks specific engineering specifications"),
        ("Beginning (1)", "Design doesn't connect to chemical reaction principles")
    ],
    "support": [
        "Provide a before/after atom diagram showing iron + oxygen → iron oxide",
        "Use physical hand warmers with thermometers for real-time data",
        "Sentence frames: 'When oxygen exposure increases, the reaction rate __ because __'"
    ],
    "extensions": [
        "Balance the chemical equation 4Fe + 3O2 → 2Fe2O3 and verify atom conservation",
        "Research and compare different types of exothermic reactions used in consumer products",
        "Design an experiment to test how surface area (powder vs. filings vs. nails) affects reaction rate"
    ],
    "cross_curr": [
        ("Math", "Balance chemical equations by counting atoms on each side; graph temperature change over time"),
        ("ELA", "Write product instructions for a hand warmer that explain the science to a consumer"),
        ("Social Studies", "Research the history of chemical engineering from alchemy to modern materials science")
    ],
    "misconceptions": [
        ("Chemical reactions destroy matter", "No atoms are created or destroyed in a chemical reaction — they only rearrange. The total mass of reactants ALWAYS equals the total mass of products. This is the law of conservation of mass.", "Weigh a sealed hand warmer before and after activation — same mass!"),
        ("Heat means something is burning", "Exothermic reactions release heat but don't require visible combustion. Rusting, dissolving, and neutralization all release heat without flames. 'Burning' is just one type of exothermic reaction (combustion).", "Ask: Is a hand warmer on fire? No, but it's hot. Chemistry creates heat in many ways."),
        ("The hand warmer creates energy", "The hand warmer doesn't CREATE energy — it TRANSFORMS chemical potential energy stored in the bonds of iron and oxygen into thermal energy. Energy is conserved, just like mass.", "Connect to conservation of energy from the roller coaster lesson (L05).")
    ]
}

# Collect all lessons
ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]

if __name__ == "__main__":
    print(f"Loaded {len(ALL_LESSONS)} Grade 8 lesson data dictionaries:")
    for lesson in ALL_LESSONS:
        print(f"  - {lesson['id']}: {lesson['title']}")
