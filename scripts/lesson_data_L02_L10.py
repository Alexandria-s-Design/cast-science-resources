#!/usr/bin/env python3
"""Complete lesson data for G05-L02 through G05-L10"""

L02 = {
    "id": "G05-L02",
    "title": "Nature's Recycling System",
    "subtitle": "Why Earth Doesn't Fill Up with Dead Stuff",
    "ngss": "5-LS2-1",
    "ngss_desc": "Develop a model to describe the movement of matter among plants, animals, decomposers, and the environment.",
    "big_question": "Why doesn't Earth fill up with dead stuff?",
    "objectives": [
        "Identify decomposers as a key component of matter cycling",
        "Model how soil moisture and organic matter affect decomposer activity",
        "Trace how dead matter is converted into nutrients for living plants",
        "Predict what happens when decomposer activity slows down"
    ],
    "vocabulary": [
        ("Decomposer", "An organism that breaks down dead organic material"),
        ("Nutrient", "Minerals and compounds that living things need to grow"),
        ("Organic Matter", "Any material that came from a living organism"),
        ("Matter Cycle", "The movement of matter through an ecosystem")
    ],
    "components": [
        ("Dead Organic Matter", "Leaves, fallen trees, dead animals that decomposers break down", True),
        ("Soil Moisture", "Water content that enables decomposer survival", True),
        ("Decomposer Activity", "Bacteria, fungi, worms actively breaking down dead material", False),
        ("Nutrient Release", "Nitrogen, phosphorus, carbon returning to soil for plants", False)
    ],
    "think_about_it": "When there's more dead organic matter, do decomposers have more or less work to do?",
    "scenarios": [
        ("Healthy Ecosystem", "Set Dead Organic Matter and Soil Moisture to normal levels"),
        ("Drought Conditions", "Lock Soil Moisture to 0% and observe what happens"),
        ("Recovery Phase", "Unlock Soil Moisture and watch the system recover")
    ],
    "sim_scenarios": [
        ("Healthy Ecosystem", "Normal organic matter, normal moisture", "What do you predict will happen to Nutrient Release?"),
        ("Drought Simulation", "Lock Soil Moisture to 0%", "What do you predict will happen to Decomposer Activity?"),
        ("Recovery Phase", "Restore moisture levels", "How quickly does the system recover?")
    ],
    "discoveries": [
        "Decomposers need both food (organic matter) AND moisture to work",
        "When conditions are right, nutrient release keeps pace with dead matter input",
        "Drought causes dead matter to pile up because decomposers can't work",
        "The system recovers when moisture returns, but not instantly"
    ],
    "answer": "Decomposers break down all the dead stuff and release nutrients back into the soil for living things to use!",
    "stem_title": "Design a Better Compost System",
    "stem_mission": "Design a backyard composting system that maximizes decomposer activity year-round.",
    "stem_scenario": "Your school wants to compost cafeteria food waste. You need to design a system that works even in dry summer months.",
    "stem_questions": [
        "What conditions do decomposers need to work effectively?",
        "How will you maintain moisture in dry weather?",
        "What materials break down fastest? Slowest?"
    ],
    "stem_design_qs": [
        "What size should your compost bin be?",
        "How will you add moisture without overwatering?",
        "What's the right mix of brown (carbon) and green (nitrogen) materials?",
        "How will you know when compost is ready to use?"
    ],
    "career": "Soil Scientists and Bioremediation Specialists use decomposers to clean up contaminated sites and restore damaged soil. They earn $75,000-$120,000/year.",
    "images": {
        "cover": ("cover-decomposition.png", "A forest floor covered in fallen autumn leaves with visible mushrooms and rich dark soil, showing the process of decomposition in a lush woodland setting"),
        "landscape": ("landscape-forest-floor.png", "5th grade students examining soil samples in a forest, looking at earthworms and mushrooms, with a magnifying glass, educational science activity"),
        "modeling": ("modeling-decomposition.png", "A diverse group of 5th grade students working together on laptops, building a digital model on screen, classroom setting with science posters"),
        "discussion": ("discussion-decomposers.png", "A teacher leading a discussion with engaged 5th grade students about decomposition, some students raising hands, classroom with natural light"),
        "stem": ("stem-compost.png", "5th grade students building a compost bin outside their school, working as a team, carrying leaves and food scraps, sunny day")
    },
    "pre_assessment": [
        "Why doesn't Earth fill up with dead stuff?",
        "What do you think decomposers are? What do they do?",
        "Draw an arrow showing how dead leaves become nutrients for plants.",
        "Name one type of decomposer you know about."
    ],
    "extend_components": [
        ("Temperature", "Decomposers work faster in warmth"),
        ("Earthworms", "They shred material before bacteria process it"),
        ("pH Level", "Acidic soil slows certain bacteria")
    ],
    "reflections": [
        "What happens to a forest ecosystem when decomposers slow down?",
        "If nutrients stop being released, what happens to living plants?",
        "Why do tropical forests have almost no dead material on the ground?",
        "How is your backyard compost bin similar to this model?",
        "What role do decomposers play in the larger matter cycle?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to describe matter cycling through decomposers."),
        ("Disciplinary Core Idea", "LS2.B Cycles of Matter and Energy Transfer", "Matter cycles between living and nonliving parts of an ecosystem."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the ecosystem as a system with inputs and outputs.")
    ],
    "cast_items": [
        "Identify the role of decomposers in matter cycling",
        "Predict how changes in conditions affect decomposer activity",
        "Trace the path of matter from dead organisms to living plants"
    ],
    "cast_questions": [
        ("Multiple Choice:", "When soil moisture decreases, what happens to decomposer activity?"),
        ("Constructed Response:", "Explain how dead leaves eventually become nutrients that plants can use.")
    ],
    "background_intro": "Decomposition is the process by which dead organic matter is broken down into simpler substances. This process is essential for nutrient cycling and soil health.",
    "background_sections": [
        ("The Decomposer Community", "Decomposers include bacteria, fungi, and invertebrates like earthworms. Fungi are particularly important because they can break down tough materials like lignin in wood."),
        ("Moisture Requirements", "Decomposers need moisture to survive and transport nutrients. In dry conditions, bacteria become dormant and fungi retreat, dramatically slowing decomposition."),
        ("Temperature Effects", "Decomposition speeds up in warm temperatures and slows in cold. This explains why leaves accumulate on forest floors in winter but quickly disappear in summer."),
        ("The Nitrogen Cycle", "Decomposers play a crucial role in the nitrogen cycle by breaking down proteins in dead matter and releasing nitrogen compounds that plants can absorb.")
    ],
    "lever_L": "Students identify decomposers, dead organic matter, soil moisture, and nutrient release as system components.",
    "lever_E": "Students determine that moisture and organic matter have positive effects on decomposer activity.",
    "lever_V": "Students build the decomposition model showing how inputs drive activity and output.",
    "lever_Ev": "Students run drought scenarios and observe the cascade of effects on nutrient release.",
    "lever_R": "Students add temperature or other factors to make the model more realistic.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with decomposition imagery", "say": "Today we're exploring nature's recycling system.", "do": "Generate curiosity with the question: Why doesn't Earth fill up with dead stuff?", "time": "1 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "These are our learning goals for today.", "do": "Have students read objectives aloud.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "The driving question for the lesson", "say": "This is the question our model will help us answer.", "do": "Poll students for initial ideas.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll use the LEVER framework to build our model.", "do": "Briefly explain each step.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "Let's identify the parts of our decomposition system.", "do": "Guide students through sorting components.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Now let's connect our components with positive and negative relationships.", "do": "Demonstrate how to draw arrows in ModelIt.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions", "say": "Let's test our model by running simulations.", "do": "Have students run drought scenario and record observations.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "What did our model reveal about decomposition?", "do": "Lead class discussion on findings.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Compost design challenge", "say": "Now apply what you learned to design a better compost system.", "do": "Distribute design materials, circulate to assist.", "time": "10 min"}
    ],
    "sort_reasoning": "Dead Organic Matter and Soil Moisture are external because nature produces them constantly and students can't control them. Decomposer Activity and Nutrient Release are internal because they change based on the external conditions.",
    "relationships": [
        ("Dead Organic Matter to Decomposer Activity", "POSITIVE (+)", "More dead stuff gives decomposers more food to process."),
        ("Soil Moisture to Decomposer Activity", "POSITIVE (+)", "Decomposers need water to survive and work."),
        ("Decomposer Activity to Nutrient Release", "POSITIVE (+)", "More decomposition means more nutrients released.")
    ],
    "sim_answers": [
        ("Drought Scenario", "When soil moisture drops to 0%, decomposer activity falls dramatically. Nutrient release crashes. Dead organic matter starts accumulating because it's not being processed."),
        ("Recovery Scenario", "When moisture returns, decomposer activity gradually increases. The accumulated dead matter is processed, causing a spike in nutrient release before returning to equilibrium.")
    ],
    "reflection_exemplars": [
        ("What happens when decomposer activity slows?", "Dead matter accumulates on the forest floor. Plants can't get nutrients. The ecosystem becomes stressed because the recycling system has stopped working."),
        ("Why do tropical forests have almost no dead leaves?", "Tropical forests are warm and moist year-round, creating ideal conditions for decomposers. Dead material is processed within weeks instead of months.")
    ],
    "stem_intro": "Introduce the challenge by discussing food waste at school. Connect to the model: composting is controlled decomposition.",
    "stem_concepts": [
        ("Moisture Balance", "Too dry slows decomposition; too wet creates anaerobic conditions that smell bad."),
        ("Carbon-Nitrogen Ratio", "A 30:1 ratio of brown to green materials optimizes decomposer activity."),
        ("Aeration", "Decomposers need oxygen; turning the pile speeds decomposition.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses moisture, aeration, and materials ratio; explains connection to model"),
        ("Proficient (3)", "Design addresses 2 of 3 key factors with scientific reasoning"),
        ("Developing (2)", "Design addresses 1 factor; limited connection to model"),
        ("Beginning (1)", "Design lacks scientific reasoning or doesn't address key factors")
    ],
    "support": [
        "Provide sentence frames: 'When __ goes up, __ goes __ because...'",
        "Use visual diagrams showing matter flow",
        "Pair with partner for model building"
    ],
    "extensions": [
        "Calculate decomposition rate changes with temperature",
        "Research mycorrhizal networks and add to model",
        "Compare decomposition rates in different biomes"
    ],
    "cross_curr": [
        ("Math", "Calculate the percentage of original leaf mass remaining over time"),
        ("ELA", "Write a narrative from the perspective of a decomposer"),
        ("Social Studies", "Research composting practices in different cultures")
    ],
    "misconceptions": [
        ("Decomposers only work on dead animals", "Decomposers break down ALL organic material including leaves, wood, and food waste.", "Ask: What happens to fallen leaves every year? Where do they go?"),
        ("Dirt is just dirt", "Healthy soil is a living ecosystem with billions of organisms per teaspoon.", "Bring in soil samples; use a magnifying glass to observe organisms."),
        ("Decomposition destroys matter", "Matter is transformed, not destroyed. Nutrients are released back into the ecosystem.", "Connect to conservation of matter from previous lesson.")
    ]
}

L03 = {
    "id": "G05-L03",
    "title": "Powered by the Sun",
    "subtitle": "How Pizza, Basketball, and Your Heartbeat Are All Solar Energy",
    "ngss": "5-PS3-1",
    "ngss_desc": "Use models to describe that energy in animals' food was once energy from the sun.",
    "big_question": "How does energy from the sun become the energy in your body?",
    "objectives": [
        "Trace the energy chain from the sun through plants to animals",
        "Model how sunlight intensity affects photosynthesis rate",
        "Explain how temperature influences plant energy production",
        "Predict what happens to animals when sunlight availability drops"
    ],
    "vocabulary": [
        ("Photosynthesis", "The process plants use to convert sunlight into sugar"),
        ("Producer", "An organism that makes its own food using sunlight"),
        ("Consumer", "An organism that eats other organisms for energy"),
        ("Energy Transfer", "The movement of energy from one organism to another")
    ],
    "components": [
        ("Sunlight Intensity", "Amount of solar energy reaching plants", True),
        ("Temperature", "Ambient warmth that affects photosynthesis efficiency", True),
        ("Photosynthesis Rate", "How fast plants convert sunlight to sugar", False),
        ("Energy Available to Animals", "How much food energy exists for consumers", False)
    ],
    "think_about_it": "When sunlight increases, what happens to the amount of energy available in the ecosystem?",
    "scenarios": [
        ("Summer Conditions", "Set Sunlight and Temperature to high levels"),
        ("Winter Conditions", "Lock Sunlight to 25% and Temperature to 25%"),
        ("Total Eclipse", "Lock Sunlight to 0% and observe the cascade")
    ],
    "sim_scenarios": [
        ("Summer Conditions", "High sunlight, warm temperature", "What do you predict will happen to Energy Available to Animals?"),
        ("Winter Simulation", "Lock both Sunlight and Temperature to 25%", "What do you predict will happen to Photosynthesis Rate?"),
        ("Eclipse/No Sun", "Lock Sunlight to 0%", "What happens to the entire energy chain?")
    ],
    "discoveries": [
        "All energy in food originally came from sunlight",
        "Photosynthesis converts solar energy into chemical energy (sugar)",
        "When sunlight drops, the entire food chain is affected",
        "Animals hibernate and migrate because winter reduces available energy"
    ],
    "answer": "The sun's energy is captured by plants through photosynthesis, stored as sugar, and transferred to animals when they eat plants!",
    "stem_title": "Design a Greenhouse for Mars",
    "stem_mission": "Design a greenhouse that could grow food for astronauts on Mars, where sunlight is weaker.",
    "stem_scenario": "NASA is planning a Mars colony. They need you to design a greenhouse that maximizes photosynthesis with limited sunlight.",
    "stem_questions": [
        "How much weaker is sunlight on Mars compared to Earth?",
        "What conditions do plants need for maximum photosynthesis?",
        "How could you supplement natural sunlight?"
    ],
    "stem_design_qs": [
        "What light sources will you use?",
        "How will you control temperature in the harsh Martian environment?",
        "Which crops grow best in low-light conditions?",
        "How will you conserve energy while maximizing plant growth?"
    ],
    "career": "Sports Nutritionists and Exercise Physiologists optimize how athletes convert food energy into performance. They earn $55,000-$90,000/year.",
    "images": {
        "cover": ("cover-solar-energy.png", "A dramatic split image showing the blazing sun on one side and 5th grade students playing basketball on the other, with a glowing energy chain connecting them"),
        "landscape": ("landscape-wheat-field.png", "A golden wheat field under bright sunlight with 5th grade students examining wheat stalks, connecting to the food chain concept"),
        "modeling": ("modeling-photosynthesis.png", "Diverse 5th grade students at computers, building a photosynthesis model, excited expressions, modern classroom"),
        "discussion": ("discussion-energy-chain.png", "Teacher at whiteboard drawing energy chain while engaged students watch, colorful classroom environment"),
        "stem": ("stem-greenhouse.png", "5th grade students designing a futuristic greenhouse model, working with blueprints and plant samples")
    },
    "pre_assessment": [
        "Where does the energy in your food come from? Trace it back as far as you can.",
        "Why do you think bears hibernate in winter but not summer?",
        "Draw an arrow showing how the sun's energy gets into fruit you eat.",
        "What would happen to animals if all plants suddenly disappeared?"
    ],
    "extend_components": [
        ("Water", "Plants need water for photosynthesis"),
        ("CO2", "Carbon dioxide is the raw material plants use"),
        ("Herbivore Population", "Number of animals eating plants")
    ],
    "reflections": [
        "Why do ecosystems in tropical regions support more animal life?",
        "Why do many animals store fat before winter?",
        "If the sun provided half as much energy, what would Earth look like?",
        "How is a fossil fuel like coal actually stored solar energy?",
        "Trace the energy in something you ate today back to the sun."
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to trace energy flow from sun to organisms."),
        ("Disciplinary Core Idea", "PS3.D Energy in Chemical Processes", "Energy from the sun is transferred to organisms through photosynthesis."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace how energy flows through systems.")
    ],
    "cast_items": [
        "Trace energy from the sun to an animal",
        "Explain the role of photosynthesis in energy transfer",
        "Predict effects of reduced sunlight on ecosystems"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A plant in a dark room will eventually die because it cannot perform photosynthesis. What happens to animals that depend on this plant?"),
        ("Constructed Response:", "Explain how the energy in a hamburger can be traced back to the sun.")
    ],
    "background_intro": "All life on Earth runs on solar energy captured through photosynthesis. This fundamental process converts light energy into chemical energy.",
    "background_sections": [
        ("Photosynthesis Basics", "Plants use chlorophyll to capture light energy. This energy powers the reaction that combines CO2 and water to produce glucose (sugar) and oxygen."),
        ("The 10% Rule", "Only about 10% of energy is transferred between trophic levels. The rest is lost as heat. This explains why food chains rarely have more than 4-5 levels."),
        ("Temperature Effects", "Photosynthesis is a chemical reaction that proceeds faster at moderate temperatures. Too cold or too hot reduces efficiency."),
        ("Seasonal Changes", "Winter reduces both sunlight intensity and day length, dramatically decreasing photosynthesis and available food energy.")
    ],
    "lever_L": "Students identify sunlight, temperature, photosynthesis rate, and energy available to animals as key components.",
    "lever_E": "Students establish that sunlight and temperature positively affect photosynthesis, which positively affects available energy.",
    "lever_V": "Students build the energy flow model showing the solar energy chain.",
    "lever_Ev": "Students run winter and eclipse scenarios to see the cascade effect on animal energy.",
    "lever_R": "Students add water or CO2 to make the model more complete.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Sun to athlete energy chain", "say": "Everything you do is powered by the sun.", "do": "Ask students what they ate for breakfast, trace it back.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we trace energy from sun to you.", "do": "Have students predict the chain.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "The driving question", "say": "How does sunlight become your energy?", "do": "Quick partner discussion.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll use LEVER to build our model.", "do": "Review each step briefly.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for energy chain", "say": "Let's identify the parts of our energy system.", "do": "Guide sorting of external vs internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "All three relationships are positive. Why?", "do": "Discuss why energy flows one direction.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Winter scenario graph", "say": "What happens in winter? Let's test it.", "do": "Have students run winter scenario.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about energy", "say": "This explains why animals hibernate!", "do": "Connect to real animal behaviors.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Mars greenhouse design", "say": "Design a greenhouse for Mars astronauts.", "do": "Distribute design materials.", "time": "10 min"}
    ],
    "sort_reasoning": "Sunlight Intensity and Temperature are external because they come from the environment. Photosynthesis Rate and Energy Available are internal because they respond to environmental conditions.",
    "relationships": [
        ("Sunlight Intensity to Photosynthesis Rate", "POSITIVE (+)", "More sunlight provides more energy for photosynthesis."),
        ("Temperature to Photosynthesis Rate", "POSITIVE (+)", "Warmer temperatures speed up the chemical reactions."),
        ("Photosynthesis Rate to Energy Available", "POSITIVE (+)", "More photosynthesis produces more plant sugar for animals to eat.")
    ],
    "sim_answers": [
        ("Winter Scenario", "When sunlight and temperature both drop, photosynthesis rate falls dramatically. Energy Available to Animals decreases, explaining why many animals must hibernate, migrate, or store fat."),
        ("Eclipse Scenario", "With zero sunlight, photosynthesis stops completely. Energy Available to Animals begins to crash as no new plant energy is being produced.")
    ],
    "reflection_exemplars": [
        ("Why do tropical regions support more life?", "Tropical regions receive more consistent, intense sunlight year-round. This maximizes photosynthesis, producing abundant plant energy that supports large animal populations."),
        ("How is coal stored solar energy?", "Coal formed from ancient plants that captured solar energy through photosynthesis. That chemical energy was preserved for millions of years and is released when we burn it.")
    ],
    "stem_intro": "Present the Mars challenge: Mars receives only 43% of the sunlight Earth gets. How do we grow enough food?",
    "stem_concepts": [
        ("Light Intensity", "Plants need sufficient light; artificial lights can supplement weak Martian sunlight."),
        ("Photoperiod", "Plants respond to day length; grow lights can extend effective day length."),
        ("Efficiency", "Choose high-yield, low-light crops like leafy greens and potatoes.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses light, temperature, and crop selection with scientific reasoning"),
        ("Proficient (3)", "Design addresses 2 of 3 factors with sound reasoning"),
        ("Developing (2)", "Design addresses 1 factor; limited connection to model"),
        ("Beginning (1)", "Design lacks scientific reasoning about plant needs")
    ],
    "support": [
        "Provide visual food chain diagram",
        "Use sentence frames: 'Energy flows from __ to __ because...'",
        "Physical demonstration with flashlight and plant"
    ],
    "extensions": [
        "Calculate the 10% rule through multiple trophic levels",
        "Research how much food astronauts would need on Mars",
        "Model deep-sea ecosystems that don't depend on sunlight"
    ],
    "cross_curr": [
        ("Math", "Calculate energy loss through a 5-level food chain"),
        ("ELA", "Write a 'biography' of a calorie from sun to athlete"),
        ("Social Studies", "Research how agricultural societies tracked seasons")
    ],
    "misconceptions": [
        ("Plants get energy from soil", "Plants get MINERALS from soil but ENERGY from sunlight through photosynthesis.", "Ask: If plants got energy from soil, why would they need leaves facing the sun?"),
        ("Animals make their own energy", "Animals get ALL their energy from food, which traces back to photosynthesis.", "Trace any meal back through the food chain to plants."),
        ("The sun is optional for life", "With few exceptions (deep sea vents), all life depends on solar energy.", "Discuss what would happen if the sun disappeared for a year.")
    ]
}

L04 = {
    "id": "G05-L04",
    "title": "Earth's Hidden Water",
    "subtitle": "97% Is Undrinkable, 2% Is Frozen. We Live on the Rest.",
    "ngss": "5-ESS2-2",
    "ngss_desc": "Describe and graph the amounts of water and fresh water in various reservoirs to provide evidence about the distribution of water on Earth.",
    "big_question": "What controls how much fresh water is available for communities to use?",
    "objectives": [
        "Describe the distribution of Earth's water across major reservoirs",
        "Model how precipitation and temperature control freshwater availability",
        "Explain how evaporation reduces accessible water",
        "Predict how climate patterns affect freshwater supplies"
    ],
    "vocabulary": [
        ("Precipitation", "Any form of water falling from clouds (rain, snow, hail)"),
        ("Evaporation", "Water turning into vapor and rising into the atmosphere"),
        ("Freshwater", "Water that is safe to drink and use"),
        ("Reservoir", "A natural or artificial storage place for water")
    ],
    "components": [
        ("Precipitation Amount", "Rainfall and snowfall controlled by weather patterns", True),
        ("Temperature", "Ambient warmth that drives evaporation rates", True),
        ("Freshwater Availability", "Usable fresh water accessible to communities", False),
        ("Evaporation Rate", "How fast water leaves the surface into atmosphere", False)
    ],
    "think_about_it": "When temperature rises, what happens to water in lakes and rivers?",
    "scenarios": [
        ("Normal Conditions", "Set both Precipitation and Temperature to moderate levels"),
        ("Drought + Heat Wave", "Lock Precipitation to 10% and Temperature to 90%"),
        ("Winter Snowpack", "Lock Temperature to 20% and Precipitation to 80%")
    ],
    "sim_scenarios": [
        ("Normal Balance", "Moderate precipitation and temperature", "Where does Freshwater Availability stabilize?"),
        ("Drought + Heat Wave", "Precipitation LOW, Temperature HIGH", "What happens to Evaporation Rate and Freshwater?"),
        ("Winter Snowpack", "Precipitation HIGH, Temperature LOW", "How does cold affect water storage?")
    ],
    "discoveries": [
        "Less than 1% of Earth's water is accessible fresh water",
        "Precipitation ADDS to freshwater availability",
        "Evaporation REMOVES from freshwater availability",
        "Hot, dry conditions create water crises for communities"
    ],
    "answer": "The balance between precipitation adding water and evaporation removing it determines how much fresh water is available!",
    "stem_title": "Design a Water Conservation Plan",
    "stem_mission": "Design a water conservation plan for a city facing drought conditions.",
    "stem_scenario": "A city is running low on water. They need to reduce usage by 40% without hurting residents.",
    "stem_questions": [
        "Which uses of water are essential vs. optional?",
        "How can you reduce evaporation from reservoirs?",
        "What technologies can recycle or reuse water?"
    ],
    "stem_design_qs": [
        "What are the biggest water uses in a city?",
        "Which cuts would have the least impact on daily life?",
        "How would you communicate restrictions to residents?",
        "What incentives could encourage conservation?"
    ],
    "career": "Hydrologists and Water Resource Managers protect community water supplies and predict droughts. They earn $75,000-$110,000/year.",
    "images": {
        "cover": ("cover-water-distribution.png", "Earth from space showing blue oceans with a magnified droplet representing the tiny fraction of drinkable fresh water"),
        "landscape": ("landscape-water-cycle.png", "A dramatic landscape showing mountains with snow, a river flowing to a city, and clouds forming - the complete water cycle"),
        "modeling": ("modeling-water-system.png", "Diverse 5th grade students working on computers, building a water cycle model, engaged and collaborative"),
        "discussion": ("discussion-water-crisis.png", "Teacher showing images of drought conditions while students discuss, concerned but engaged expressions"),
        "stem": ("stem-water-plan.png", "5th grade students presenting a water conservation poster with charts and diagrams to classmates")
    },
    "pre_assessment": [
        "Shade a pie chart to show what percent of Earth's water is saltwater, frozen, and drinkable.",
        "What controls whether a city has enough water to drink?",
        "Have you heard of a city running out of water? What happened?",
        "Why do you think some places have water shortages while others don't?"
    ],
    "extend_components": [
        ("Human Water Use", "Agriculture uses 70% of all fresh water"),
        ("Groundwater Pumping", "Underground water being used faster than it refills"),
        ("Glacier Melt", "Ice melting provides temporary water before disappearing")
    ],
    "reflections": [
        "Why does California depend so heavily on mountain snowpack?",
        "What happens to freshwater availability as global temperatures rise?",
        "Which conditions create the greatest risk for communities?",
        "How is the water you drink connected to weather hundreds of miles away?",
        "What is one thing humans do that decreases freshwater availability?"
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze how different conditions affect water distribution."),
        ("Disciplinary Core Idea", "ESS2.C The Roles of Water in Earth's Processes", "Water cycles through Earth's systems in various forms."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the freshwater system with competing inputs and outputs.")
    ],
    "cast_items": [
        "Describe the distribution of water on Earth",
        "Explain how precipitation and evaporation affect freshwater",
        "Predict effects of climate changes on water availability"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During a heat wave with no rain, what happens to the amount of fresh water available in a reservoir?"),
        ("Constructed Response:", "Explain why high temperatures AND low precipitation together create severe water shortages.")
    ],
    "background_intro": "Earth is a water planet, but most of that water isn't usable. Understanding water distribution is essential for managing this critical resource.",
    "background_sections": [
        ("Water Distribution", "97% of Earth's water is saltwater in oceans. 2% is frozen in glaciers and ice caps. Less than 1% is accessible fresh water in rivers, lakes, and groundwater."),
        ("The Water Cycle", "Water moves continuously between reservoirs through evaporation, condensation, and precipitation. This cycle is powered by solar energy."),
        ("Evaporation Factors", "Higher temperatures increase evaporation rates. Hot, dry conditions can cause water to evaporate faster than precipitation can replace it."),
        ("Real-World Crisis", "In 2018, Cape Town, South Africa nearly ran out of water during a severe drought. They called it 'Day Zero' - the day taps would be turned off.")
    ],
    "lever_L": "Students identify precipitation, temperature, freshwater availability, and evaporation as system components.",
    "lever_E": "Students establish that precipitation increases freshwater while evaporation decreases it - a key negative relationship.",
    "lever_V": "Students build the water balance model showing competing forces.",
    "lever_Ev": "Students run drought scenarios and observe freshwater availability crashing.",
    "lever_R": "Students add human water use to see how human activity affects the system.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Earth's water distribution", "say": "97% of Earth's water is undrinkable. 2% is frozen.", "do": "Let that statistic sink in.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model what controls freshwater availability.", "do": "Define key vocabulary.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "The driving question", "say": "What determines if your city has enough water?", "do": "Discuss local water sources.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model of the water balance.", "do": "Preview the activities.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for water system", "say": "Let's identify inputs and outputs of the water system.", "do": "Emphasize the competing forces.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Notice: evaporation has a NEGATIVE effect on freshwater.", "do": "Ensure students understand why.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Cape Town Day Zero scenario", "say": "Let's simulate the Cape Town water crisis.", "do": "Students run drought + heat scenario.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about water", "say": "This is why water managers worry about droughts.", "do": "Connect to student experiences with water.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Water conservation design", "say": "Design a plan to save a city's water supply.", "do": "Form groups and distribute materials.", "time": "10 min"}
    ],
    "sort_reasoning": "Precipitation Amount and Temperature are external - they come from weather patterns communities can't control. Freshwater Availability and Evaporation Rate are internal - they change based on conditions.",
    "relationships": [
        ("Precipitation to Freshwater Availability", "POSITIVE (+)", "More rain/snow adds more water to rivers, lakes, and groundwater."),
        ("Temperature to Evaporation Rate", "POSITIVE (+)", "Higher temperatures cause water to evaporate faster."),
        ("Evaporation Rate to Freshwater Availability", "NEGATIVE (-)", "More evaporation removes water before communities can use it.")
    ],
    "sim_answers": [
        ("Drought + Heat Wave", "With precipitation at 10% and temperature at 90%, evaporation rate spikes while input drops. Freshwater availability crashes toward zero - exactly what Cape Town experienced."),
        ("Winter Snowpack", "Cold temperatures reduce evaporation. Heavy precipitation accumulates as snow. Freshwater availability builds up for later use when temperatures rise.")
    ],
    "reflection_exemplars": [
        ("Why does California depend on snowpack?", "Mountain snow acts as a natural reservoir. It stores winter precipitation and slowly releases it as meltwater through summer when rainfall is low."),
        ("What happens as global temperatures rise?", "Higher temperatures increase evaporation everywhere. Less precipitation falls as snow. Both effects reduce freshwater availability.")
    ],
    "stem_intro": "Present the crisis scenario: Your city's reservoir is at 30% capacity. Without action, you'll run out in 6 months.",
    "stem_concepts": [
        ("Conservation Tiers", "Mandatory restrictions for different shortage levels."),
        ("Recycled Water", "Treated wastewater can be used for irrigation and industry."),
        ("Reservoir Management", "Covering reservoirs reduces evaporation by up to 90%.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses multiple conservation strategies with scientific reasoning"),
        ("Proficient (3)", "Plan addresses 2-3 strategies with solid reasoning"),
        ("Developing (2)", "Plan addresses 1 strategy with limited reasoning"),
        ("Beginning (1)", "Plan lacks scientific connection to the water system model")
    ],
    "support": [
        "Provide water budget worksheet showing inputs vs. outputs",
        "Use visual balance scale metaphor",
        "Offer sentence frames for explaining relationships"
    ],
    "extensions": [
        "Research the Ogallala Aquifer depletion crisis",
        "Calculate water footprint of common foods",
        "Design a rainwater harvesting system for school"
    ],
    "cross_curr": [
        ("Math", "Create pie charts showing global water distribution"),
        ("ELA", "Write a public service announcement about water conservation"),
        ("Social Studies", "Research water rights and water conflicts")
    ],
    "misconceptions": [
        ("There's plenty of water everywhere", "Less than 1% of Earth's water is accessible fresh water - and it's not evenly distributed.", "Show the pie chart: 97% salt, 2% frozen, <1% drinkable."),
        ("Rain refills everything quickly", "Groundwater can take centuries to recharge. Aquifers being depleted now may not refill in our lifetimes.", "Research the Ogallala Aquifer depletion rate."),
        ("Water disappears when it evaporates", "Water cycles back eventually, but not necessarily to the same place. It might rain far away.", "Track where water vapor goes using wind patterns.")
    ]
}

L05 = {
    "id": "G05-L05",
    "title": "The Disappearing Act",
    "subtitle": "Ice Melts, But the Mass Never Leaves",
    "ngss": "5-PS1-2",
    "ngss_desc": "Measure and graph quantities to provide evidence that the total weight of matter is conserved regardless of the type of change.",
    "big_question": "How does the total mass of matter stay the same when it changes form?",
    "objectives": [
        "Observe and explain why mass doesn't change during state changes",
        "Model how temperature shifts matter between solid and liquid form",
        "Predict what happens to each state as temperature changes",
        "Apply conservation of matter to everyday physical changes"
    ],
    "vocabulary": [
        ("Conservation", "The principle that matter cannot be created or destroyed"),
        ("State of Matter", "Solid, liquid, or gas - the form matter takes"),
        ("Physical Change", "A change in shape or form without creating new substance"),
        ("Mass", "The amount of matter in an object")
    ],
    "components": [
        ("Air Temperature", "The warmth or cold of the environment", True),
        ("Starting Mass", "The total amount of matter - stays constant!", True),
        ("Ice Amount", "How much substance is in solid form", False),
        ("Liquid Water Amount", "How much substance is in liquid form", False)
    ],
    "think_about_it": "When ice melts, where does the mass go?",
    "scenarios": [
        ("Room Temperature", "Normal conditions with some ice and liquid"),
        ("Freezing Conditions", "Lock Temperature to 10% and observe"),
        ("Melting Conditions", "Lock Temperature to 90% and observe")
    ],
    "sim_scenarios": [
        ("Room Temperature", "Normal temperature conditions", "What do you predict happens to Ice and Liquid amounts?"),
        ("Freezing", "Lock Temperature to 10%", "What happens to Ice Amount vs Liquid Water Amount?"),
        ("Melting", "Lock Temperature to 90%", "Watch Ice Amount decrease - does Starting Mass change?")
    ],
    "discoveries": [
        "Mass is conserved - it doesn't disappear when ice melts",
        "Ice Amount and Liquid Water Amount are mirror images of each other",
        "Starting Mass stays completely flat regardless of temperature",
        "State changes are physical changes that conserve mass"
    ],
    "answer": "The mass never goes anywhere - it just changes form from solid to liquid! Ice and liquid water are the same matter in different states.",
    "stem_title": "Solve the Burning Mystery",
    "stem_mission": "Explain where the 'missing' mass goes when wood burns and only ash remains.",
    "stem_scenario": "A 10 kg log burns down to 0.5 kg of ash. Where did 9.5 kg of mass go?",
    "stem_questions": [
        "Is burning a physical change or a chemical change?",
        "What gases are released when wood burns?",
        "How could you prove the mass wasn't destroyed?"
    ],
    "stem_design_qs": [
        "What would you need to capture to prove conservation?",
        "What equipment would you need?",
        "How would you weigh gases?",
        "Draw your experimental setup."
    ],
    "career": "Forensic Chemists use conservation of matter to solve crimes - they can reconstruct what substances were present at crime scenes. They earn $65,000-$100,000/year.",
    "images": {
        "cover": ("cover-conservation.png", "Two images side by side: ice cube on scale showing 50g, then same scale with water showing 50g, with student amazed expression"),
        "landscape": ("landscape-states-matter.png", "A beautiful landscape showing water in all three states: snow-capped mountains, liquid lake, steam rising in morning light"),
        "modeling": ("modeling-state-change.png", "5th grade students at computers creating a state change model, pointing at screens showing graphs"),
        "discussion": ("discussion-conservation.png", "Teacher demonstrating ice melting experiment while students observe and take notes"),
        "stem": ("stem-burning.png", "5th grade students safely observing a candle burning experiment with teacher supervision, discussing where mass goes")
    },
    "pre_assessment": [
        "An ice cube weighs 50 grams. It melts completely. How much does the water weigh?",
        "When wood burns, the ash weighs less than the wood. Where did the mass go?",
        "Draw what happens to atoms inside an ice cube when it melts.",
        "Does matter disappear or change form? Explain your thinking."
    ],
    "extend_components": [
        ("Water Vapor Amount", "Gas state when water evaporates"),
        ("Time", "Duration of heating or cooling"),
        ("Container Type", "Open vs. closed system")
    ],
    "reflections": [
        "Does it matter if matter is solid or liquid - is the mass the same?",
        "Why does ice LOOK like it's disappearing when it melts?",
        "Can you think of other examples where matter changes form but not mass?",
        "If you weigh yourself before and after breathing out, are you lighter?",
        "When you eat food, does it disappear? Where does the mass go?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students investigate whether mass changes during state changes."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Matter is conserved in all physical and chemical changes."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students measure and compare mass before and after changes.")
    ],
    "cast_items": [
        "Explain conservation of matter during physical changes",
        "Predict mass after state changes",
        "Apply conservation to novel situations"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student puts 100g of ice in a closed container. After the ice melts, the total mass will be:"),
        ("Constructed Response:", "A candle starts at 50g. After burning for an hour, only 30g remains. Using conservation of matter, explain where the missing 20g went.")
    ],
    "background_intro": "The law of conservation of matter states that matter cannot be created or destroyed, only transformed. This is one of the most fundamental principles in science.",
    "background_sections": [
        ("Conservation Law", "Antoine Lavoisier established the law of conservation of mass in 1789. He carefully measured chemical reactions and found that total mass always remained constant."),
        ("State Changes", "When ice melts, water molecules don't disappear - they just move faster and spread apart. The same number of molecules exists in the liquid as in the solid."),
        ("Combustion", "Burning appears to destroy matter, but actually converts solid carbon into CO2 gas and water vapor. If you capture the gases, total mass equals starting mass."),
        ("Digestion", "When you digest food, the matter becomes part of your body, is exhaled as CO2, or is eliminated as waste. Nothing is destroyed.")
    ],
    "lever_L": "Students identify temperature, starting mass, ice amount, and liquid water amount as components.",
    "lever_E": "Students establish that ice and liquid have a NEGATIVE relationship - they trade mass between them.",
    "lever_V": "Students build the state change model with the key constraint of constant total mass.",
    "lever_Ev": "Students run heating and cooling scenarios, observing that Starting Mass never changes.",
    "lever_R": "Students add water vapor as a third state to model complete water cycle.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Ice cube before/after", "say": "The ice 'disappeared' - but did it really?", "do": "Set up demonstration if possible.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we prove that mass is conserved.", "do": "Define conservation.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "The driving question", "say": "Where does the mass GO when ice melts?", "do": "Take predictions.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model state changes.", "do": "Preview activities.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for states", "say": "Starting Mass is our constant - it never changes.", "do": "Emphasize this key insight.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Ice and Liquid are NEGATIVE because they share the same mass.", "do": "Demonstrate with a fixed amount of water.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Mirror graphs", "say": "Watch Starting Mass - it never moves!", "do": "Students run multiple temperature scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Conservation proven", "say": "Conservation of matter is a LAW, not a suggestion.", "do": "Discuss implications.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Burning log mystery", "say": "Apply conservation to solve a burning mystery.", "do": "Guide investigation of combustion.", "time": "10 min"}
    ],
    "sort_reasoning": "Air Temperature and Starting Mass are external because they're set conditions. Ice Amount and Liquid Water Amount are internal - they change in response to temperature but always add up to Starting Mass.",
    "relationships": [
        ("Air Temperature to Ice Amount", "NEGATIVE (-)", "Higher temperature means less ice (it melts)."),
        ("Air Temperature to Liquid Water Amount", "POSITIVE (+)", "Higher temperature means more liquid (from melting)."),
        ("Ice Amount to Liquid Water Amount", "NEGATIVE (-)", "They share the same mass - when one goes up, the other must go down.")
    ],
    "sim_answers": [
        ("Freezing Scenario", "When temperature drops, Ice Amount increases and Liquid Water Amount decreases. They mirror each other perfectly. Starting Mass remains completely flat - proving conservation."),
        ("Melting Scenario", "When temperature rises, Ice Amount drops and Liquid Water Amount rises by the same amount. Total mass never changes - matter transformed from solid to liquid.")
    ],
    "reflection_exemplars": [
        ("Why does ice look like it's disappearing?", "Ice takes up more space than liquid water (ice floats!). When it melts, it occupies less volume even though the mass is exactly the same."),
        ("Where does food mass go when you digest it?", "Food becomes part of your cells, provides energy (you exhale CO2 and water vapor), and the rest is eliminated. Nothing is destroyed, just transformed.")
    ],
    "stem_intro": "Present the burning mystery: A 10 kg log becomes 0.5 kg of ash. This seems to violate conservation. Or does it?",
    "stem_concepts": [
        ("Combustion Chemistry", "Burning combines carbon with oxygen to make CO2 gas and releases water vapor."),
        ("Gas Has Mass", "CO2 and water vapor are matter too - they just float away as invisible gas."),
        ("Closed Systems", "In a sealed container, the total mass before and after burning would be identical.")
    ],
    "stem_eval": [
        ("Expert (4)", "Correctly identifies gases as the 'missing' mass and explains how to capture them"),
        ("Proficient (3)", "Identifies that mass becomes gas; partially explains capture method"),
        ("Developing (2)", "Recognizes something leaves but doesn't identify it as gas"),
        ("Beginning (1)", "Thinks mass was destroyed; doesn't apply conservation")
    ],
    "support": [
        "Provide before/after diagrams with labeled masses",
        "Use physical balance scale demonstration",
        "Offer visual of molecules rearranging, not disappearing"
    ],
    "extensions": [
        "Calculate mass of CO2 produced from burning a specific amount of carbon",
        "Design an experiment to prove conservation during dissolution",
        "Research how forensic scientists use mass conservation"
    ],
    "cross_curr": [
        ("Math", "Calculate and balance mass equations for chemical reactions"),
        ("ELA", "Write an argument proving conservation of matter"),
        ("History", "Research Lavoisier's experiments that proved conservation")
    ],
    "misconceptions": [
        ("Ice weighs more than water because it's solid", "Same mass, different density. Ice actually takes up MORE space than the same mass of water.", "Demonstrate that ice floats because it's less dense."),
        ("Matter disappears when it evaporates", "Water vapor is still matter - it's just invisible gas molecules. The mass is in the air.", "Weigh a wet towel before and after drying - compare to dry room air."),
        ("Burning destroys matter", "Combustion converts solid to gases (CO2, H2O). Capture the gases and total mass is conserved.", "Research Lavoisier's famous combustion experiments.")
    ]
}

L06 = {
    "id": "G05-L06",
    "title": "Where Does a Tree's Mass Come From?",
    "subtitle": "A 1-Ton Tree Got Most of Its Weight From Air",
    "ngss": "5-LS1-1",
    "ngss_desc": "Support an argument that plants get the materials they need for growth chiefly from air and water.",
    "big_question": "Where does a tree get the materials it needs to grow?",
    "objectives": [
        "Explain that plants get most of their mass from CO2 in the air, not soil",
        "Model how CO2 and sunlight drive photosynthesis",
        "Trace how photosynthesis converts air into tree mass",
        "Predict what happens to tree growth when CO2 or sunlight is removed"
    ],
    "vocabulary": [
        ("Photosynthesis", "The process plants use to convert light, CO2, and water into sugar"),
        ("CO2 (Carbon Dioxide)", "The gas plants use as raw material for growth"),
        ("Biomass", "The total mass of living material in an organism"),
        ("Glucose", "The sugar produced by photosynthesis - plant food and building material")
    ],
    "components": [
        ("CO2 in Air", "Carbon dioxide concentration in atmosphere that plants absorb", True),
        ("Sunlight", "Solar energy available for photosynthesis", True),
        ("Photosynthesis Rate", "How fast plants convert CO2 to sugar", False),
        ("Tree Biomass", "The actual physical mass/weight of the tree", False)
    ],
    "think_about_it": "If trees don't get mass from soil, where do the carbon atoms in wood come from?",
    "scenarios": [
        ("Normal Growth", "CO2 and Sunlight at normal levels"),
        ("No CO2", "Lock CO2 to 0% - sealed environment"),
        ("Greenhouse Boost", "Both CO2 and Sunlight at high levels")
    ],
    "sim_scenarios": [
        ("Normal Growth", "Normal CO2 and sunlight levels", "Watch Tree Biomass grow steadily."),
        ("CO2 Removed", "Lock CO2 to 0%", "What happens to Photosynthesis Rate and Tree Biomass?"),
        ("Maximum Growth", "Both CO2 and Sunlight at HIGH", "How fast can a tree grow?")
    ],
    "discoveries": [
        "Trees get most of their mass from CO2 in the air - not from soil",
        "Soil provides minerals but not the bulk mass of the tree",
        "Remove CO2 and tree growth stops completely",
        "This is why deforestation releases stored carbon back to atmosphere"
    ],
    "answer": "Trees get their mass from carbon dioxide in the AIR! They pull CO2 through their leaves and use photosynthesis to build it into solid wood.",
    "stem_title": "Design a Carbon Capture Forest",
    "stem_mission": "Design a reforestation project to capture the most CO2 possible.",
    "stem_scenario": "Your city wants to offset carbon emissions by planting trees. Design the most effective carbon capture forest.",
    "stem_questions": [
        "Which tree species capture the most CO2?",
        "How much CO2 does one tree absorb per year?",
        "Where should the forest be located for maximum growth?"
    ],
    "stem_design_qs": [
        "What tree species will you choose and why?",
        "How will you arrange the trees for maximum sunlight?",
        "How will you ensure trees survive long enough to grow large?",
        "How will you calculate total carbon captured?"
    ],
    "career": "Plant Biologists and Agricultural Scientists optimize photosynthesis to feed 8 billion people. They earn $65,000-$105,000/year.",
    "images": {
        "cover": ("cover-tree-mass.png", "Giant towering redwood tree with CO2 molecules visibly flowing from air into leaves, students looking up in awe"),
        "landscape": ("landscape-forest.png", "Lush forest with sunlight streaming through canopy, diverse 5th grade students examining tree rings and leaves"),
        "modeling": ("modeling-tree-growth.png", "5th grade students at computers building a photosynthesis model, excited to see tree biomass growing"),
        "discussion": ("discussion-photosynthesis.png", "Teacher with diagram of photosynthesis equation while students discuss where tree mass comes from"),
        "stem": ("stem-planting.png", "5th grade students planting tree seedlings outside their school, working as a team in sunshine")
    },
    "pre_assessment": [
        "A giant tree weighs 1 million pounds. Where do you think all that mass came from?",
        "What do plants need to grow? List everything you can think of.",
        "A scientist grew a tree in a pot for 5 years. The tree gained 164 lbs. The soil lost 2 ounces. What does this prove?",
        "What is photosynthesis and why do plants need it?"
    ],
    "extend_components": [
        ("Water", "H2O is also a raw material for photosynthesis"),
        ("Temperature", "Affects photosynthesis rate - too hot or cold slows it"),
        ("Chlorophyll", "The green pigment that captures light energy")
    ],
    "reflections": [
        "If you weigh a seed, plant it, and weigh the full tree, where did the extra mass come from?",
        "Why is deforestation a climate problem? (Think about stored carbon.)",
        "If CO2 in atmosphere is rising, does that mean plants should grow faster?",
        "Why can't plants grow in completely dark environments?",
        "What does the photosynthesis equation tell us about inputs and outputs?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students construct an explanation for where plant mass comes from."),
        ("Disciplinary Core Idea", "LS1.C Organization for Matter and Energy Flow", "Plants acquire material for growth chiefly from air and water."),
        ("Crosscutting Concept", "Matter and Energy", "Students trace matter from air into plant biomass.")
    ],
    "cast_items": [
        "Identify the primary source of plant mass",
        "Explain the role of photosynthesis in plant growth",
        "Connect deforestation to atmospheric carbon"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Where do trees get most of the mass they need to grow?"),
        ("Constructed Response:", "A greenhouse farmer wants maximum plant growth. Based on your model, what two things should she increase?")
    ],
    "background_intro": "The discovery that plants get mass from air, not soil, is one of the most counterintuitive findings in biology. Van Helmont's 1648 experiment began the investigation.",
    "background_sections": [
        ("Van Helmont's Experiment", "In 1648, Van Helmont grew a willow tree for 5 years in a weighed pot of soil. The tree gained 164 pounds while the soil lost only 2 ounces. He concluded (partially correctly) that the mass came from water."),
        ("Photosynthesis Discovery", "Later scientists discovered the complete picture: 6CO2 + 6H2O + light energy --> C6H12O6 + 6O2. Carbon dioxide from air provides the carbon atoms that become plant tissue."),
        ("Carbon Storage", "Trees are essentially solidified carbon dioxide. When we cut down forests, that stored carbon returns to the atmosphere as CO2."),
        ("Climate Connection", "The Amazon rainforest stores about 90 billion tons of carbon. Deforestation releases this stored carbon, accelerating climate change.")
    ],
    "lever_L": "Students identify CO2, sunlight, photosynthesis rate, and tree biomass as system components.",
    "lever_E": "Students establish that both CO2 and sunlight positively affect photosynthesis, which positively affects tree mass.",
    "lever_V": "Students build the tree growth model showing how air becomes wood.",
    "lever_Ev": "Students run no-CO2 scenarios and observe tree growth completely stopping.",
    "lever_R": "Students add water to complete the photosynthesis equation.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Giant tree with CO2 flowing in", "say": "This tree weighs 1 million pounds. Where did it come from?", "do": "Take predictions - most will say soil.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we discover plants' surprising source of mass.", "do": "Define key vocabulary.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Van Helmont experiment", "say": "Van Helmont proved it wasn't soil. So what is it?", "do": "Share the 164 lbs vs 2 oz result.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how trees grow.", "do": "Preview activities.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "CO2, sunlight, photosynthesis, biomass", "say": "CO2 is the raw material - the carbon atoms.", "do": "Connect to the air around them.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "All positive relationships", "say": "Both inputs drive photosynthesis which builds mass.", "do": "Discuss why all positive.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "No-CO2 scenario", "say": "Remove the CO2. Watch the tree stop growing.", "do": "Students run the revealing scenario.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Trees are solidified CO2", "say": "Every tree is made of air that became solid.", "do": "Connect to climate change.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Carbon capture forest", "say": "Design a forest to capture maximum carbon.", "do": "Research tree species and CO2 absorption.", "time": "10 min"}
    ],
    "sort_reasoning": "CO2 in Air and Sunlight are external - they come from the environment and the tree can't control them. Photosynthesis Rate and Tree Biomass are internal - they change based on available CO2 and sunlight.",
    "relationships": [
        ("CO2 in Air to Photosynthesis Rate", "POSITIVE (+)", "More CO2 means more raw material for building sugar."),
        ("Sunlight to Photosynthesis Rate", "POSITIVE (+)", "More light energy powers faster photosynthesis."),
        ("Photosynthesis Rate to Tree Biomass", "POSITIVE (+)", "More photosynthesis produces more glucose which becomes more wood.")
    ],
    "sim_answers": [
        ("No-CO2 Scenario", "When CO2 is locked to 0%, photosynthesis rate drops to zero and tree biomass stops growing. Without CO2, there's no raw material to build new tissue."),
        ("Greenhouse Scenario", "With high CO2 and high sunlight, photosynthesis maxes out and tree biomass grows rapidly. This is exactly what commercial greenhouses do to boost crop yields.")
    ],
    "reflection_exemplars": [
        ("Where does tree mass come from?", "Most tree mass (about 95%) comes from carbon dioxide in the air. Trees absorb CO2 through tiny pores in their leaves and use photosynthesis to convert it into solid wood, bark, and leaves."),
        ("Why is deforestation a climate problem?", "Trees store carbon as solid wood. When we cut them down, that carbon returns to the atmosphere as CO2, contributing to climate change. A single large tree can store hundreds of pounds of carbon.")
    ],
    "stem_intro": "Present the challenge: Your city emits 1 million tons of CO2 per year. How many trees would you need to offset that?",
    "stem_concepts": [
        ("Carbon Sequestration", "One mature tree absorbs about 48 pounds of CO2 per year."),
        ("Tree Selection", "Fast-growing species absorb more CO2 but may not live as long."),
        ("Long-term Storage", "Old-growth forests store the most carbon but take centuries to develop.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design specifies tree species, arrangement, and calculates total carbon capture with scientific reasoning"),
        ("Proficient (3)", "Design addresses species and arrangement with solid reasoning"),
        ("Developing (2)", "Design mentions trees but lacks specific calculations"),
        ("Beginning (1)", "Design doesn't connect tree planting to CO2 capture")
    ],
    "support": [
        "Provide Van Helmont experiment visual summary",
        "Use photosynthesis equation with pictures",
        "Demonstrate with seedlings and growth measurements"
    ],
    "extensions": [
        "Calculate how much CO2 a school forest would absorb",
        "Research carbon credits and carbon markets",
        "Model deforestation effects on atmospheric CO2"
    ],
    "cross_curr": [
        ("Math", "Calculate CO2 absorption rates for different tree species"),
        ("ELA", "Write a persuasive essay for tree planting"),
        ("Social Studies", "Research deforestation in the Amazon and its global effects")
    ],
    "misconceptions": [
        ("Plants get mass from soil", "Soil provides minerals and water, but the MASS comes from CO2 in the air. Van Helmont proved this in 1648.", "Reference the 164 lbs tree / 2 oz soil experiment."),
        ("Trees take in oxygen", "Trees produce oxygen through photosynthesis. They take in CO2.", "Show the photosynthesis equation: CO2 in, O2 out."),
        ("Plants don't need sunlight, just water", "Sunlight is the energy source that powers photosynthesis. No light = no photosynthesis = no growth.", "Try growing plants in darkness - they die.")
    ]
}

L07 = {
    "id": "G05-L07",
    "title": "The Mushroom Network Under Your Feet",
    "subtitle": "Trees Share Food and Warnings Through Underground Internet",
    "ngss": "5-LS2-1",
    "ngss_desc": "Develop a model to describe the movement of matter among plants, animals, decomposers, and the environment.",
    "big_question": "How do underground conditions control how much trees can share with each other?",
    "objectives": [
        "Identify mycorrhizal fungi as active participants in ecosystem matter cycling",
        "Model how organic matter and moisture drive fungal network health",
        "Explain how the fungal network enables nutrient transfer between trees",
        "Predict what happens to forest health when the network is disrupted"
    ],
    "vocabulary": [
        ("Mycorrhizal", "Related to fungi that form partnerships with plant roots"),
        ("Mutualism", "A relationship where both organisms benefit"),
        ("Hyphae", "Tiny thread-like structures that form fungal networks"),
        ("Nutrient", "Substances that living things need to grow and survive")
    ],
    "components": [
        ("Leaf Litter / Organic Matter", "Dead leaves and material that feeds the fungal network", True),
        ("Soil Moisture", "Water content that enables fungal survival and growth", True),
        ("Mycorrhizal Fungal Network Activity", "How active the underground threads are", False),
        ("Nutrient Transfer Between Trees", "How much food and signals move between trees", False)
    ],
    "think_about_it": "If fungi need food and water, what happens to the forest network during a drought?",
    "scenarios": [
        ("Healthy Forest", "Normal organic matter and soil moisture"),
        ("Drought", "Lock Soil Moisture to 10%"),
        ("Clear-Cut Aftermath", "Lock Leaf Litter to 0%")
    ],
    "sim_scenarios": [
        ("Healthy Forest", "Normal organic matter and moisture", "Watch the network thrive and nutrients transfer."),
        ("Drought Scenario", "Lock Soil Moisture to 10%", "What happens to network activity and nutrient transfer?"),
        ("Deforestation", "Lock Leaf Litter to 0%", "What happens when there's no organic matter to feed fungi?")
    ],
    "discoveries": [
        "Trees are connected underground through fungal threads",
        "The network allows trees to share sugar and warnings",
        "Drought isolates trees by shutting down the network",
        "Replanting a cleared forest takes decades because the network must rebuild"
    ],
    "answer": "Trees share nutrients through an underground 'internet' of fungal threads. This network needs both organic matter and moisture to function!",
    "stem_title": "Design Forest Recovery Plan",
    "stem_mission": "Design a plan to restore the mycorrhizal network in a cleared forest.",
    "stem_scenario": "A forest was clear-cut 5 years ago. New trees are struggling. Design a plan to restore the underground network.",
    "stem_questions": [
        "How can you reintroduce mycorrhizal fungi to the soil?",
        "What conditions do fungi need to establish themselves?",
        "How can you maintain moisture and organic matter?"
    ],
    "stem_design_qs": [
        "Will you use fungi from nearby healthy forests?",
        "How will you protect new fungal growth?",
        "What organic matter will you add?",
        "How long will full recovery take?"
    ],
    "career": "Mycologists and Forest Ecologists study the underground networks that hold forests together. They earn $55,000-$90,000/year.",
    "images": {
        "cover": ("cover-mycorrhizal.png", "Split image showing forest above ground and glowing golden fungal network below, diverse students peering through 'window' in earth"),
        "landscape": ("landscape-forest-floor.png", "Forest floor covered in fallen leaves with visible mushrooms, 5th grade students examining soil with magnifying glasses"),
        "modeling": ("modeling-network.png", "5th grade students at computers building network model, excited expressions, modern classroom"),
        "discussion": ("discussion-wood-wide-web.png", "Teacher showing diagram of connected trees while students discuss, engaged classroom"),
        "stem": ("stem-restoration.png", "5th grade students spreading mulch and organic matter in a restoration area, working together outdoors")
    },
    "pre_assessment": [
        "Do trees in a forest compete, cooperate, or both? Explain.",
        "What do mushrooms/fungi do in an ecosystem?",
        "If trees could share food underground, what would have to be doing the sharing?",
        "What is the Wood Wide Web? Have you heard of it?"
    ],
    "extend_components": [
        ("Soil pH", "Acidic soil from acid rain damages fungi"),
        ("Tree Species Diversity", "Different species connect differently"),
        ("Mother Tree Presence", "Oldest trees are network hubs")
    ],
    "reflections": [
        "Why might a cleared forest take decades to recover even with replanting?",
        "How does drought affect the entire forest community, not just individual trees?",
        "What does this network tell us about competition vs. cooperation in nature?",
        "How is the mycorrhizal network similar to and different from the internet?",
        "Why are 'mother trees' so important to protect?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students model matter movement through the mycorrhizal network."),
        ("Disciplinary Core Idea", "LS2.B Cycles of Matter and Energy Transfer", "Matter cycles through ecosystems including decomposers."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the forest as an interconnected system.")
    ],
    "cast_items": [
        "Describe the role of fungi in ecosystem matter cycling",
        "Explain how environmental conditions affect the mycorrhizal network",
        "Predict effects of disturbance on forest connectivity"
    ],
    "cast_questions": [
        ("Multiple Choice:", "What happens to nutrient transfer between trees during a severe drought?"),
        ("Constructed Response:", "Explain why replanting a clear-cut forest with new trees doesn't immediately restore it to its original state.")
    ],
    "background_intro": "The Wood Wide Web is a relatively recent scientific discovery. Dr. Suzanne Simard proved in the 1990s that trees communicate and share resources through underground fungal networks.",
    "background_sections": [
        ("Discovery", "Dr. Suzanne Simard traced radioactive carbon from one tree to its neighbors through fungal threads. She proved trees were actively sharing resources."),
        ("The Deal", "Trees and fungi have a mutualistic relationship. Trees give fungi sugar from photosynthesis. Fungi give trees water and minerals they can't access alone."),
        ("Network Structure", "Mother trees - the largest, oldest trees - are hubs connecting many neighbors. When they die or are cut, dozens of other trees lose their connections."),
        ("Warning Signals", "Trees can send chemical alarm signals through the network when attacked by insects. Neighboring trees ramp up their defenses in response.")
    ],
    "lever_L": "Students identify leaf litter, soil moisture, fungal network activity, and nutrient transfer as components.",
    "lever_E": "Students establish that organic matter and moisture both positively affect network activity, which positively affects nutrient transfer.",
    "lever_V": "Students build the forest network model showing inputs driving connectivity.",
    "lever_Ev": "Students run drought and deforestation scenarios to see network collapse.",
    "lever_R": "Students add soil pH to model acid rain effects on the network.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Trees above, fungal network below", "say": "Trees talk to each other. Through mushrooms. Underground.", "do": "Let that statement sink in.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model the forest's underground internet.", "do": "Define mycorrhizal.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Dr. Simard's discovery", "say": "Dr. Simard proved trees share. How does it work?", "do": "Show her research context.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model what keeps the network healthy.", "do": "Preview activities.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Network components", "say": "Fungi need food and water, just like us.", "do": "Connect to decomposition lesson.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "All positive relationships", "say": "All positive - when conditions are good, everyone benefits.", "do": "Discuss mutualism.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Drought scenario", "say": "Drought doesn't just hurt trees - it isolates them.", "do": "Students run drought scenario.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Forest as community", "say": "A forest is one connected community, not separate trees.", "do": "Discuss implications for conservation.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Forest restoration", "say": "Design a plan to restore a damaged forest network.", "do": "Research mycorrhizal restoration.", "time": "10 min"}
    ],
    "sort_reasoning": "Leaf Litter and Soil Moisture are external - nature provides them continuously. Fungal Network Activity and Nutrient Transfer are internal - they change based on how well the fungi are doing.",
    "relationships": [
        ("Leaf Litter to Fungal Network Activity", "POSITIVE (+)", "More organic matter provides more food for fungi to grow."),
        ("Soil Moisture to Fungal Network Activity", "POSITIVE (+)", "Fungi need moisture to grow and transport nutrients."),
        ("Fungal Network Activity to Nutrient Transfer", "POSITIVE (+)", "More active network means more sharing between trees.")
    ],
    "sim_answers": [
        ("Drought Scenario", "When soil moisture drops, fungal threads retreat and can't transport nutrients. Nutrient transfer between trees collapses. Each tree becomes isolated."),
        ("Deforestation Scenario", "Without leaf litter, fungi starve. Even with moisture, the network can't sustain itself. This is why replanted forests take so long to recover.")
    ],
    "reflection_exemplars": [
        ("Why does forest recovery take decades?", "The underground fungal network takes 50+ years to fully re-establish. New trees are isolated without it. They don't have access to shared nutrients or warnings from neighbors."),
        ("How is the network like the internet?", "Both connect distant points to share information. Both have hubs (mother trees / servers). Both break when connections are severed. But the Wood Wide Web is biological and evolved over millions of years.")
    ],
    "stem_intro": "Present the restoration challenge: A clear-cut forest was replanted 5 years ago. Trees are struggling. Why? The underground network was destroyed.",
    "stem_concepts": [
        ("Inoculation", "Adding mycorrhizal fungi to soil around new seedlings."),
        ("Organic Matter", "Mulch and leaf litter provide food for fungi to establish."),
        ("Nurse Trees", "Keeping some old trees preserves network connections for new trees to join.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses fungi, organic matter, moisture, and timeline with scientific reasoning"),
        ("Proficient (3)", "Design addresses 2-3 key factors with solid reasoning"),
        ("Developing (2)", "Design mentions fungi but lacks specific strategy"),
        ("Beginning (1)", "Design doesn't connect to mycorrhizal network science")
    ],
    "support": [
        "Provide diagram of tree-fungi mutualism with labels",
        "Use internet analogy throughout",
        "Offer visual of network connections"
    ],
    "extensions": [
        "Research specific mycorrhizal fungi species",
        "Model how mother tree removal affects neighbors",
        "Calculate how much carbon moves through networks"
    ],
    "cross_curr": [
        ("Math", "Calculate network connectivity using graph theory basics"),
        ("ELA", "Write a story from the perspective of a mother tree"),
        ("Social Studies", "Research Indigenous knowledge of forest relationships")
    ],
    "misconceptions": [
        ("Mushrooms are plants", "Fungi are their own kingdom - neither plant nor animal. They have unique properties.", "Show fungi characteristics: no chlorophyll, cell walls of chitin not cellulose."),
        ("Fungi just decompose things", "Mycorrhizal fungi are PARTNERS with living trees, not decomposers.", "Explain the difference between decomposer fungi and mycorrhizal fungi."),
        ("Trees only compete", "Trees compete AND cooperate simultaneously. The Wood Wide Web shows extensive cooperation.", "Share research on mother trees supporting their offspring.")
    ]
}

L08 = {
    "id": "G05-L08",
    "title": "How Soap Actually Destroys Viruses",
    "subtitle": "The Chemical Reaction That Saves Millions of Lives Every Year",
    "ngss": "5-PS1-4",
    "ngss_desc": "Conduct an investigation to determine whether the mixing of two or more substances results in new substances.",
    "big_question": "How does soap destroy viruses at the molecular level?",
    "objectives": [
        "Explain that soap destroys viruses through chemical interaction, not just rinsing",
        "Model how soap concentration and water determine effectiveness",
        "Trace how soap effectiveness leads to virus membrane disruption",
        "Apply the model to explain why proper handwashing technique matters"
    ],
    "vocabulary": [
        ("Lipid", "A fat or oil molecule that makes up virus outer coatings"),
        ("Membrane", "A thin layer that surrounds and protects a cell or virus"),
        ("Amphiphilic", "A molecule attracted to both water AND oil/fat"),
        ("Pathogen", "Any microorganism that can cause disease")
    ],
    "components": [
        ("Soap Concentration", "How much soap is being applied", True),
        ("Water Present", "Whether running water activates the soap", True),
        ("Soap Effectiveness", "How well soap can attack virus membranes", False),
        ("Virus Survival Rate", "Percentage of viruses surviving handwashing", False)
    ],
    "think_about_it": "Why would washing with just water be less effective than soap and water?",
    "scenarios": [
        ("Water Only", "Soap at 0%, Water at 100%"),
        ("Dry Soap", "Soap at 100%, Water at 0%"),
        ("Proper Handwashing", "Both Soap and Water at high levels")
    ],
    "sim_scenarios": [
        ("Water Only", "Soap at 0%, Water at 100%", "Can water alone destroy virus membranes?"),
        ("Dry Soap", "Soap at 100%, Water at 0%", "Is soap alone effective without water?"),
        ("Proper Handwashing", "Both at HIGH", "Watch Virus Survival Rate drop toward zero.")
    ],
    "discoveries": [
        "Soap DESTROYS viruses by breaking apart their lipid membranes",
        "Water alone can't disrupt the virus's protective coating",
        "Soap needs water to spread and work effectively",
        "This is why 20 seconds of proper handwashing matters"
    ],
    "answer": "Soap molecules have one end that loves water and one end that loves fat. They wedge into the virus's fatty membrane and break it apart - destroying the virus!",
    "stem_title": "Design a Handwashing Campaign",
    "stem_mission": "Design a school campaign to improve handwashing and reduce illness.",
    "stem_scenario": "Your school has had several flu outbreaks. Design a science-based campaign to teach effective handwashing.",
    "stem_questions": [
        "What's the minimum time needed for soap to work?",
        "Which areas of hands are most often missed?",
        "How would you convince people to wash properly?"
    ],
    "stem_design_qs": [
        "What visuals will show why soap works?",
        "How will you demonstrate proper technique?",
        "Where will you display your campaign?",
        "How will you measure if it's working?"
    ],
    "career": "Public Health Scientists and Virologists study how diseases spread and how to stop them. They earn $70,000-$115,000/year.",
    "images": {
        "cover": ("cover-handwashing.png", "Close-up of hands being washed with soap bubbles, microscopic inset showing soap molecules attacking virus membrane"),
        "landscape": ("landscape-hygiene.png", "Modern school bathroom with 5th grade students demonstrating proper handwashing technique at sinks"),
        "modeling": ("modeling-soap.png", "Diverse 5th grade students at computers, building a soap effectiveness model, engaged expressions"),
        "discussion": ("discussion-soap-science.png", "Teacher showing molecular diagram of soap attacking virus while students watch, colorful classroom"),
        "stem": ("stem-campaign.png", "5th grade students creating handwashing posters and infographics, working as a team")
    },
    "pre_assessment": [
        "Why do you wash your hands with soap? What does soap actually do?",
        "Which is MORE effective: water only, soap only, or soap + water together?",
        "What do you think happens to viruses when soap touches them?",
        "Why do you think we're told to wash for 20 seconds?"
    ],
    "extend_components": [
        ("Scrubbing Time", "More time = more soap contact with surfaces"),
        ("Water Temperature", "Warm water helps soap molecules move"),
        ("Surface Area Covered", "Missed spots still harbor viruses")
    ],
    "reflections": [
        "Why isn't rinsing with water alone enough to kill viruses?",
        "Why is hand sanitizer (alcohol) useful but different from soap?",
        "What percentage of viruses survive proper handwashing?",
        "If soap is so effective, why do diseases still spread?",
        "How did understanding soap chemistry help during COVID-19?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students investigate substance mixing and its effects."),
        ("Disciplinary Core Idea", "PS1.B Chemical Reactions", "Substances interact and new substances may form."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify cause and effect in chemical interactions.")
    ],
    "cast_items": [
        "Explain how soap interacts with virus membranes",
        "Predict effectiveness under different conditions",
        "Apply chemical principles to health behaviors"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student washes their hands with plenty of soap but only for 5 seconds. Why might this be less effective than washing for 20 seconds?"),
        ("Constructed Response:", "Explain why soap is more effective than water alone for destroying viruses with lipid membranes.")
    ],
    "background_intro": "Handwashing with soap is one of the most powerful public health interventions ever discovered. The chemistry explains why it works so well.",
    "background_sections": [
        ("Soap Chemistry", "Soap molecules are amphiphilic - one end is hydrophilic (loves water) and the other is lipophilic (loves fat). This lets them bridge between water and lipids."),
        ("Virus Structure", "Many viruses, including influenza and coronavirus, have a lipid membrane - a fatty outer coating that protects them and allows them to infect cells."),
        ("The Destruction", "When soap contacts a lipid membrane, the lipophilic tails wedge between the fat molecules, breaking the membrane apart. Without its membrane, the virus falls apart."),
        ("Semmelweis Story", "In the 1840s, Dr. Semmelweis proved handwashing saved lives. The medical establishment rejected him. He died in an asylum while millions died of preventable infections.")
    ],
    "lever_L": "Students identify soap concentration, water, soap effectiveness, and virus survival as components.",
    "lever_E": "Students establish that soap and water positively affect effectiveness, while effectiveness NEGATIVELY affects virus survival.",
    "lever_V": "Students build the handwashing chemistry model with the key negative relationship.",
    "lever_Ev": "Students compare water-only, soap-only, and proper handwashing scenarios.",
    "lever_R": "Students add scrubbing time to model why 20 seconds matters.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Soap attacking virus", "say": "Soap doesn't just wash viruses away - it DESTROYS them.", "do": "Show molecule animation if available.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we learn the chemistry of clean hands.", "do": "Define amphiphilic.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "The driving question", "say": "HOW does soap destroy viruses?", "do": "Take initial ideas.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model molecular demolition.", "do": "Preview activities.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Handwashing system components", "say": "We want Virus Survival Rate as close to ZERO as possible.", "do": "Emphasize the goal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Positive and negative relationships", "say": "The NEGATIVE relationship is the whole point - effectiveness REDUCES survival.", "do": "Ensure understanding.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Three scenario comparison", "say": "Let's test water only, soap only, and proper handwashing.", "do": "Students run all three.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Why 20 seconds matters", "say": "Every second gives soap more time to find viruses.", "do": "Practice 20-second wash.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Campaign design", "say": "Use your science knowledge to create a campaign.", "do": "Form groups for campaign design.", "time": "10 min"}
    ],
    "sort_reasoning": "Soap Concentration and Water Present are external - the handwasher controls them. Soap Effectiveness and Virus Survival Rate are internal - they respond to the conditions created.",
    "relationships": [
        ("Soap Concentration to Soap Effectiveness", "POSITIVE (+)", "More soap molecules available to attack virus membranes."),
        ("Water Present to Soap Effectiveness", "POSITIVE (+)", "Water activates and spreads soap across all surfaces."),
        ("Soap Effectiveness to Virus Survival Rate", "NEGATIVE (-)", "More effective soap = fewer viruses survive. This is the goal!")
    ],
    "sim_answers": [
        ("Water Only", "Without soap, Soap Effectiveness stays near zero. Virus Survival Rate remains high. Water can rinse away some particles but can't destroy lipid membranes."),
        ("Proper Handwashing", "With both soap and water at high levels, Soap Effectiveness maxes out. Virus Survival Rate drops toward zero as soap destroys membrane-coated viruses.")
    ],
    "reflection_exemplars": [
        ("Why isn't water enough?", "Water can't break the chemical bonds in virus lipid membranes. Only soap's amphiphilic structure can wedge into the membrane and break it apart."),
        ("Why does time matter?", "Soap molecules need time to spread across all hand surfaces, reach into crevices, and break apart virus membranes. 20 seconds provides enough contact time.")
    ],
    "stem_intro": "Present the campaign challenge: Your school has had 3 flu outbreaks this year. Design a campaign using today's science.",
    "stem_concepts": [
        ("20-Second Rule", "Research shows 20 seconds provides adequate contact time."),
        ("Common Missed Spots", "Between fingers, under nails, back of hands, thumbs."),
        ("Visual Evidence", "Glow-in-dark lotion shows where handwashing misses spots.")
    ],
    "stem_eval": [
        ("Expert (4)", "Campaign accurately explains soap science and demonstrates proper technique"),
        ("Proficient (3)", "Campaign includes science reasoning and technique demonstration"),
        ("Developing (2)", "Campaign mentions science but lacks clear explanation"),
        ("Beginning (1)", "Campaign doesn't connect to soap chemistry")
    ],
    "support": [
        "Provide diagram of soap molecule structure",
        "Use animation showing membrane disruption",
        "Practice handwashing technique together"
    ],
    "extensions": [
        "Research enveloped vs non-enveloped viruses",
        "Compare soap to alcohol hand sanitizer chemistry",
        "Calculate how many lives handwashing saves annually"
    ],
    "cross_curr": [
        ("Math", "Calculate reduction percentages with different wash times"),
        ("ELA", "Write a narrative from the perspective of a soap molecule"),
        ("Social Studies", "Research Semmelweis and the history of handwashing")
    ],
    "misconceptions": [
        ("Soap just rinses germs away", "Soap DESTROYS many viruses by breaking apart their lipid membranes. They don't survive to be washed away.", "Show molecular animation of membrane disruption."),
        ("Water alone is enough", "Water can't break the chemical bonds in lipid membranes. Only amphiphilic molecules like soap can.", "Compare water-only vs soap+water scenarios."),
        ("Antibacterial soap is better for viruses", "Antibacterial chemicals target bacteria, not viruses. Regular soap is equally effective against viruses.", "Explain the different targets of different cleaning agents.")
    ]
}

L09 = {
    "id": "G05-L09",
    "title": "Whose Air Is This?",
    "subtitle": "Why Kids Near Freeways Have Higher Asthma Rates",
    "ngss": "5-ESS3-1",
    "ngss_desc": "Obtain and combine information about ways individual communities use science ideas to protect the Earth's resources and environment.",
    "big_question": "How do vehicle traffic and wind patterns determine what a community breathes?",
    "objectives": [
        "Model how vehicle traffic and wind patterns determine air pollution levels",
        "Explain why communities near freeways experience higher respiratory illness",
        "Predict how changes in traffic or wind affect community health",
        "Identify scientific and community-based approaches to improving air quality"
    ],
    "vocabulary": [
        ("Air Quality Index", "A number measuring how clean or polluted the air is"),
        ("Particulate Matter", "Tiny solid or liquid particles floating in the air"),
        ("Respiratory", "Relating to the lungs and breathing system"),
        ("Environmental Justice", "The fair distribution of environmental risks")
    ],
    "components": [
        ("Vehicle Traffic Density", "Volume of cars and trucks in the area", True),
        ("Wind Speed", "How fast air is moving - natural dispersal force", True),
        ("Air Pollution Concentration", "Buildup of exhaust, particulates, and gases", False),
        ("Respiratory Health Impact", "Health effects on the community - asthma, hospitalizations", False)
    ],
    "think_about_it": "If wind disperses pollution, what happens on calm, still days?",
    "scenarios": [
        ("Normal Day", "Moderate traffic, moderate wind"),
        ("Rush Hour + Still Air", "High traffic, low wind - worst case"),
        ("Holiday", "Low traffic, moderate wind - best case")
    ],
    "sim_scenarios": [
        ("Normal Day", "Moderate traffic and wind", "Where does Respiratory Health Impact settle?"),
        ("Rush Hour + Still Air", "Traffic 90%, Wind 10%", "What happens to Air Pollution and Health Impact?"),
        ("Holiday/Weekend", "Traffic 20%, Wind moderate", "How much does air quality improve?")
    ],
    "discoveries": [
        "Traffic ADDS pollution, wind REMOVES it - it's a competition",
        "Children near freeways breathe measurably worse air",
        "Air quality varies day to day based on wind conditions",
        "This is both a science problem AND a justice problem"
    ],
    "answer": "Air pollution concentration depends on the balance between traffic (adding pollution) and wind (dispersing it). Communities near freeways face higher exposure every day.",
    "stem_title": "Design an Air Quality Solution",
    "stem_mission": "Propose a science-based solution to improve air quality near a freeway.",
    "stem_scenario": "A community near a freeway has high asthma rates. They can't move the freeway. Design a solution to help.",
    "stem_questions": [
        "Can you reduce traffic pollution at the source?",
        "Can you block or filter pollution before it reaches homes?",
        "How will you measure if your solution works?"
    ],
    "stem_design_qs": [
        "What specific intervention will you propose?",
        "How does it connect to your model?",
        "What are the costs and benefits?",
        "Who needs to take action for it to happen?"
    ],
    "career": "Environmental Health Scientists and Air Quality Monitors protect communities from pollution. They earn $60,000-$95,000/year.",
    "images": {
        "cover": ("cover-air-quality.png", "Split view: busy freeway with visible exhaust on left, diverse students in classroom near freeway on right, one using inhaler"),
        "landscape": ("landscape-freeway.png", "Aerial view of freeway through residential neighborhood, visible smog layer, houses close to highway"),
        "modeling": ("modeling-air-quality.png", "5th grade students at computers building air quality model, focused expressions, modern classroom"),
        "discussion": ("discussion-environmental-justice.png", "Teacher showing map of pollution and demographics while students engage in serious discussion"),
        "stem": ("stem-trees.png", "5th grade students planting trees along a sound wall near a freeway, community service activity")
    },
    "pre_assessment": [
        "Do all neighborhoods have the same air quality? Explain.",
        "What causes air pollution in a neighborhood?",
        "Children near freeways have higher asthma rates. What explains this?",
        "Is it fair that some neighborhoods have worse air than others?"
    ],
    "extend_components": [
        ("Green Infrastructure / Trees", "Trees capture particulate matter"),
        ("Electric Vehicle Percentage", "EVs produce no tailpipe emissions"),
        ("Temperature Inversion", "Warm air trapping pollution near ground")
    ],
    "reflections": [
        "Why does high wind reduce respiratory health impact in your model?",
        "Why might a community near a freeway NOT be able to solve this alone?",
        "What is one solution communities are using to improve air quality?",
        "Is this a science problem, a justice problem, or both?",
        "What role should science play in community advocacy?"
    ],
    "dimensions": [
        ("Science Practice", "Obtaining, Evaluating, and Communicating Information", "Students research and communicate about air quality solutions."),
        ("Disciplinary Core Idea", "ESS3.C Human Impacts on Earth Systems", "Human activities affect Earth's environment."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships in air quality systems.")
    ],
    "cast_items": [
        "Identify sources and effects of air pollution",
        "Explain how communities use science to address environmental problems",
        "Propose evidence-based solutions"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During a heat wave with no wind, what happens to air pollution levels near a freeway?"),
        ("Constructed Response:", "A community near a freeway wants to reduce asthma rates. Based on your model, suggest TWO science-based approaches.")
    ],
    "background_intro": "Air quality disparities are well-documented: communities near freeways experience higher rates of asthma and other respiratory illnesses. This is both a scientific and a social justice issue.",
    "background_sections": [
        ("The Data", "Studies show children within 500 meters of freeways have higher asthma rates, lower lung function, and more ER visits than those living farther away."),
        ("The Science", "Vehicle exhaust contains CO, NOx, and PM2.5 particulates. These particles are small enough to enter the bloodstream through the lungs."),
        ("The Justice Dimension", "Freeways were often built through communities with less political power. Low-income communities and communities of color are disproportionately affected."),
        ("Solutions in Action", "Communities are fighting back: planting tree barriers, advocating for electric buses, and using air quality sensors to document the problem.")
    ],
    "lever_L": "Students identify traffic, wind, pollution concentration, and health impact as components.",
    "lever_E": "Students establish that traffic increases pollution (positive), wind decreases it (negative), and pollution increases health impact (positive).",
    "lever_V": "Students build the air quality model with competing forces.",
    "lever_Ev": "Students run rush hour vs. holiday scenarios to see dramatic differences.",
    "lever_R": "Students add green infrastructure to model a community solution.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Freeway next to school", "say": "Kids near freeways have higher asthma rates. It's not a coincidence.", "do": "Let the seriousness land.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model why location matters for air quality.", "do": "Define key terms.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "The driving question", "say": "What determines the air your community breathes?", "do": "Check local AQI at airnow.gov.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model air quality as a system.", "do": "Preview activities.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Air quality system components", "say": "Traffic adds pollution. Wind removes it.", "do": "Establish the competition.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Positive and negative relationships", "say": "Wind is the community's natural defense.", "do": "Emphasize the negative relationship.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Rush hour vs. holiday", "say": "Let's simulate morning rush hour on a still day.", "do": "Students run scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Environmental justice connection", "say": "This is science AND justice.", "do": "Discuss fair distribution of risks.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Community solutions", "say": "Communities are fighting back. Design a solution.", "do": "Research real interventions.", "time": "10 min"}
    ],
    "sort_reasoning": "Vehicle Traffic and Wind Speed are external - the community can't easily control them. Air Pollution Concentration and Respiratory Health Impact are internal - they respond to these conditions.",
    "relationships": [
        ("Vehicle Traffic to Air Pollution", "POSITIVE (+)", "More vehicles produce more exhaust and particulates."),
        ("Wind Speed to Air Pollution", "NEGATIVE (-)", "Wind disperses and dilutes pollution, reducing concentration."),
        ("Air Pollution to Respiratory Health Impact", "POSITIVE (+)", "Higher pollution concentration causes more health problems.")
    ],
    "sim_answers": [
        ("Rush Hour + Still Air", "With traffic at 90% and wind at 10%, pollution concentration spikes. Respiratory health impact rises significantly. This is exactly what communities near freeways experience on calm mornings."),
        ("Holiday Scenario", "With traffic at 20%, pollution concentration drops dramatically. Scientists have measured this: air quality measurably improves on holidays with reduced traffic.")
    ],
    "reflection_exemplars": [
        ("Why can't the community solve this alone?", "They didn't build the freeway and can't remove it. Traffic comes from throughout the region. Solutions require action from government, industry, and broader society."),
        ("What solutions are communities using?", "Tree planting as barriers, advocating for electric vehicles and buses, community air monitoring to document the problem, demanding regulations and traffic diversion.")
    ],
    "stem_intro": "Present the challenge: A community has 3x higher asthma rates than city average. They're located next to a major freeway. Design solutions.",
    "stem_concepts": [
        ("Green Barriers", "Trees can capture 50%+ of particulate matter."),
        ("Electrification", "Electric vehicles produce zero tailpipe emissions."),
        ("Traffic Reduction", "Every car removed is fewer emissions.")
    ],
    "stem_eval": [
        ("Expert (4)", "Solution directly connects to model, addresses root causes, considers feasibility"),
        ("Proficient (3)", "Solution connects to model and is scientifically sound"),
        ("Developing (2)", "Solution mentions pollution but lacks clear connection to model"),
        ("Beginning (1)", "Solution doesn't address the air quality system")
    ],
    "support": [
        "Provide AQI color chart for reference",
        "Use campfire smoke analogy for still vs. windy conditions",
        "Offer sentence frames for justice discussion"
    ],
    "extensions": [
        "Research local air quality data and map against demographics",
        "Interview community members about air quality concerns",
        "Design an air quality monitoring network for school"
    ],
    "cross_curr": [
        ("Math", "Analyze AQI data and calculate averages for different neighborhoods"),
        ("ELA", "Write a persuasive letter to city council about air quality"),
        ("Social Studies", "Research the history of freeway placement decisions")
    ],
    "misconceptions": [
        ("Air pollution only matters in cities", "Rural areas near industrial sites and agriculture face pollution challenges too.", "Research agricultural air quality issues."),
        ("This affects everyone equally", "Environmental justice research documents significant disparities in who bears the burden.", "Map pollution sources against demographic data."),
        ("Individual behavior causes this", "Vehicle infrastructure is a systems-level issue requiring systems-level solutions.", "Discuss the limits of individual action.")
    ]
}

L10 = {
    "id": "G05-L10",
    "title": "The Light You're Seeing Is Already Old",
    "subtitle": "When You Look at a Star, You're Seeing the Past",
    "ngss": "5-ESS1-1",
    "ngss_desc": "Support an argument that differences in the apparent brightness of the sun compared to other stars is due to their relative distances from Earth.",
    "big_question": "How do a star's distance and luminosity determine how bright it appears from Earth?",
    "objectives": [
        "Explain that apparent brightness depends on both distance and actual luminosity",
        "Model how distance affects both light travel time and apparent brightness",
        "Predict how apparent brightness changes with distance",
        "Articulate that observing stars means observing the past"
    ],
    "vocabulary": [
        ("Light Year", "The distance light travels in one year (~6 trillion miles)"),
        ("Luminosity", "The actual amount of energy a star produces"),
        ("Apparent Brightness", "How bright a star appears when viewed from Earth"),
        ("Inverse Square Law", "Brightness decreases by the square of the distance")
    ],
    "components": [
        ("Star Distance", "How far the star is from Earth", True),
        ("Star Actual Luminosity", "How much light the star actually produces", True),
        ("Light Travel Time", "How old the light is when it reaches us", False),
        ("Apparent Brightness", "How bright the star looks to us from Earth", False)
    ],
    "think_about_it": "If a star is very far away, why might we still be able to see it?",
    "scenarios": [
        ("The Sun", "Distance very low, Luminosity moderate"),
        ("Nearby Dim Star", "Distance low, Luminosity very low"),
        ("Distant Supergiant", "Distance very high, Luminosity very high")
    ],
    "sim_scenarios": [
        ("The Sun", "Distance VERY LOW, Luminosity MODERATE", "Why does the sun dominate our sky?"),
        ("Nearby Dim Star", "Distance LOW, Luminosity LOW", "Can proximity save a dim star?"),
        ("Distant Supergiant", "Distance HIGH, Luminosity VERY HIGH", "Can extreme brightness overcome distance?")
    ],
    "discoveries": [
        "The sun looks brightest because it's CLOSE, not because it's special",
        "Distance has a NEGATIVE effect on apparent brightness",
        "Very luminous stars can be visible from thousands of light years away",
        "Light travel time means we're always seeing the past"
    ],
    "answer": "Apparent brightness depends on both distance (closer = brighter) and luminosity (more luminous = brighter). The sun looks brightest because it's the closest star by far!",
    "stem_title": "Design a Star Observation Mission",
    "stem_mission": "Design a mission to study a specific star using what you know about light travel time.",
    "stem_scenario": "NASA wants to study a star 100 light years away. What would observing it teach us? What are the challenges?",
    "stem_questions": [
        "If we send a signal, how long until we get a response?",
        "What are we actually 'seeing' when we observe this star?",
        "How do we learn about stars we can never visit?"
    ],
    "stem_design_qs": [
        "What star will you observe and why?",
        "What information can you gather from its light?",
        "What does light travel time mean for your observations?",
        "How would you communicate findings to the public?"
    ],
    "career": "Astronomers and Astrophysicists study everything beyond Earth using the principles you modeled today. They earn $90,000-$145,000/year.",
    "images": {
        "cover": ("cover-starlight.png", "Diverse 5th grade students lying on hillside looking up at star-filled night sky, subtle distance labels above stars"),
        "landscape": ("landscape-night-sky.png", "Stunning night sky over a landscape with varying star brightness visible, Milky Way band visible"),
        "modeling": ("modeling-starlight.png", "5th grade students at computers building a starlight model, pointing at screens with excitement"),
        "discussion": ("discussion-light-years.png", "Teacher with timeline showing light travel from different stars while students react with wonder"),
        "stem": ("stem-telescope.png", "5th grade students looking through a telescope at night, guided by a teacher, expressions of awe")
    },
    "pre_assessment": [
        "Why do you think the sun looks so much brighter than other stars?",
        "If light travels at 186,000 miles/second, and the nearest star is 4 light years away, how old is its light?",
        "True or False: When you look at a distant star, you're seeing it as it is right now.",
        "What is a light year?"
    ],
    "extend_components": [
        ("Star Color / Temperature", "Hotter stars are bluer and more luminous"),
        ("Interstellar Dust", "Dust clouds can block and dim starlight"),
        ("Star Age", "Stars change luminosity over their lifetime")
    ],
    "reflections": [
        "Why does the sun appear so much brighter than other stars?",
        "If a star is 1,000 light years away, how old is the light reaching us tonight?",
        "What makes a star appear BRIGHTER even at great distance?",
        "Could we be looking at a star that no longer exists? Explain.",
        "What is the farthest thing human eyes can see without a telescope?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students use models to understand relationships between distance and brightness."),
        ("Disciplinary Core Idea", "ESS1.A The Universe and Its Stars", "The sun is a star that appears larger and brighter than other stars because it is closer."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students use appropriate scales to understand astronomical distances.")
    ],
    "cast_items": [
        "Explain why the sun appears brightest",
        "Predict apparent brightness based on distance and luminosity",
        "Apply the concept of light travel time"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Star A is twice as far from Earth as Star B. If both stars have the same luminosity, how will their apparent brightness compare?"),
        ("Constructed Response:", "Explain why the sun appears so much brighter than other stars even though many other stars are actually much larger and more luminous.")
    ],
    "background_intro": "When we look at the night sky, we're looking at the past. Light takes time to travel across the vast distances of space, so we never see stars as they are 'now.'",
    "background_sections": [
        ("Light Speed", "Light travels at 186,000 miles per second - fast, but the universe is enormous. Light from the nearest star takes 4 years to reach us."),
        ("Inverse Square Law", "As distance doubles, brightness decreases by a factor of 4. Triple the distance, 9 times dimmer. This is why nearby stars appear so much brighter."),
        ("The Sun's Proximity", "The sun is about 93 million miles away. The next nearest star is about 25 trillion miles away. The sun appears bright because it's incomparably close."),
        ("Hubble Deep Field", "In 1995, Hubble pointed at 'empty' sky for 10 days. It revealed 10,000 galaxies, each containing billions of stars. The farthest light was 12 billion years old.")
    ],
    "lever_L": "Students identify distance, luminosity, light travel time, and apparent brightness as components.",
    "lever_E": "Students establish that distance increases travel time (positive) but decreases brightness (negative), while luminosity increases brightness (positive).",
    "lever_V": "Students build the starlight model with competing influences on apparent brightness.",
    "lever_Ev": "Students compare sun, dim nearby star, and distant supergiant scenarios.",
    "lever_R": "Students add star color/temperature to predict luminosity.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Students looking at stars", "say": "The light you're seeing is already old. Some of it is ancient.", "do": "Create a sense of wonder.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model why stars look the way they do.", "do": "Define light year.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Light travel timeline", "say": "How do we figure out why some stars look brighter?", "do": "Show travel times to different stars.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the night sky.", "do": "Preview activities.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Starlight system components", "say": "Two forces affect apparent brightness - one helps, one hurts.", "do": "Set up the competition.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Positive and negative relationships", "say": "Distance is NEGATIVE for brightness. This is the key.", "do": "Use streetlight analogy.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Three star comparison", "say": "Let's compare the sun to distant supergiants.", "do": "Students run all three scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Night sky as time machine", "say": "You're looking at the past. Some stars might not exist anymore.", "do": "Let existential wonder land.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Space observation mission", "say": "Design a mission to observe a distant star.", "do": "Discuss what we can learn from light.", "time": "10 min"}
    ],
    "sort_reasoning": "Star Distance and Actual Luminosity are external - they're properties of the star we can't change. Light Travel Time and Apparent Brightness are internal - they're what we experience based on those properties.",
    "relationships": [
        ("Star Distance to Light Travel Time", "POSITIVE (+)", "Farther stars mean light takes longer to reach us."),
        ("Star Distance to Apparent Brightness", "NEGATIVE (-)", "Farther stars appear dimmer because light spreads out."),
        ("Star Luminosity to Apparent Brightness", "POSITIVE (+)", "More luminous stars appear brighter at the same distance.")
    ],
    "sim_answers": [
        ("The Sun Scenario", "With distance near zero and moderate luminosity, apparent brightness is maximized. The sun dominates our sky not because it's special, but because it's incomparably close."),
        ("Distant Supergiant", "Even with extremely high luminosity, the enormous distance reduces apparent brightness. Light travel time is very long - we're seeing ancient light.")
    ],
    "reflection_exemplars": [
        ("Why is the sun the brightest?", "The sun is about 93 million miles away. The next nearest star is 25 TRILLION miles away - over 250,000 times farther. Even a much more luminous star at that distance appears as a dim point of light."),
        ("Could we see a dead star?", "Yes! If a star 1,000 light years away exploded today, we wouldn't see it for 1,000 years. We might be looking at stars right now that no longer exist.")
    ],
    "stem_intro": "Present the mission challenge: Choose a star to study. What can we learn just from its light?",
    "stem_concepts": [
        ("Spectroscopy", "Breaking light into colors reveals a star's composition."),
        ("Brightness Changes", "Variable brightness can tell us about star size and companions."),
        ("Redshift", "Light stretching tells us how fast a star is moving away.")
    ],
    "stem_eval": [
        ("Expert (4)", "Mission plan addresses light travel time, observational methods, and scientific goals"),
        ("Proficient (3)", "Mission plan includes scientific goals and methods"),
        ("Developing (2)", "Mission plan mentions observation but lacks detail"),
        ("Beginning (1)", "Mission plan doesn't connect to light and distance concepts")
    ],
    "support": [
        "Provide streetlight distance/brightness analogy",
        "Use visual timeline of light travel from different stars",
        "Offer calculator for light year distances"
    ],
    "extensions": [
        "Calculate light travel times for named stars",
        "Research what the Hubble Deep Field revealed",
        "Model how a supernova would appear from Earth"
    ],
    "cross_curr": [
        ("Math", "Calculate and graph the inverse square law"),
        ("ELA", "Write a story about receiving light from a dead star"),
        ("Social Studies", "Research how ancient cultures navigated by stars")
    ],
    "misconceptions": [
        ("Bigger stars are always brighter", "Apparent brightness depends on BOTH luminosity AND distance. A massive but distant star can appear dimmer than a small nearby one.", "Compare sun to Betelgeuse in your model."),
        ("The night sky shows current universe", "All starlight is from the past. Farther = older. We literally cannot see the present state of distant objects.", "Calculate light travel time from various stars."),
        ("The sun is a special star", "The sun is actually a fairly average star. It appears special only because it's so much closer than any other star.", "Show sun compared to other stars in size and luminosity.")
    ]
}

# Collect all lessons
ALL_LESSONS = [L02, L03, L04, L05, L06, L07, L08, L09, L10]

if __name__ == "__main__":
    print(f"Loaded {len(ALL_LESSONS)} lesson data dictionaries:")
    for lesson in ALL_LESSONS:
        print(f"  - {lesson['id']}: {lesson['title']}")
