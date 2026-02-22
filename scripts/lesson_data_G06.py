#!/usr/bin/env python3
"""Complete lesson data for G06-L01 through G06-L10 (Grade 6 ModelIt! Lessons)"""

L01 = {
    "id": "G06-L01",
    "title": "Why Can't You See Your Own Cells?",
    "subtitle": "Exploring the Microscopic Building Blocks of Life",
    "ngss": "MS-LS1-1, MS-LS1-2",
    "ngss_desc": "Conduct an investigation to provide evidence that living things are made of cells; either one cell or many different numbers and types of cells. Develop and use a model to describe the function of a cell as a whole and ways the parts of cells contribute to the function.",
    "big_question": "If your body is made of 37 trillion cells, why can't you see a single one?",
    "objectives": [
        "Explain why cells are too small to see without magnification",
        "Model how cell size, nutrient supply, and oxygen level affect cell function",
        "Describe how waste buildup limits cell growth and survival",
        "Compare how single-celled and multi-celled organisms organize their cells"
    ],
    "vocabulary": [
        ("Cell", "The smallest unit of life that can carry out all life functions"),
        ("Organelle", "A specialized structure inside a cell that performs a specific job, like a tiny organ"),
        ("Cell Membrane", "The flexible boundary that controls what enters and exits a cell"),
        ("Microscope", "A tool that uses lenses to magnify objects too small for the naked eye")
    ],
    "components": [
        ("Cell Size", "The physical dimensions of a cell — smaller cells exchange materials more efficiently", False),
        ("Nutrient Supply", "The amount of food and energy molecules available to cells from the environment", True),
        ("Oxygen Level", "The concentration of oxygen reaching cells for cellular respiration", True),
        ("Waste Buildup", "The accumulation of metabolic waste products inside and around cells", False)
    ],
    "think_about_it": "When nutrient supply increases, what happens to cell size and waste buildup? Is the relationship positive or negative?",
    "scenarios": [
        ("Healthy Cell", "Set Nutrient Supply and Oxygen Level to moderate and observe cell function"),
        ("Starvation Mode", "Lock Nutrient Supply to 10% and observe what happens to Cell Size and Waste Buildup"),
        ("Oxygen Crisis", "Set Oxygen Level to 15% while keeping nutrients normal")
    ],
    "sim_scenarios": [
        ("Healthy Cell", "Moderate nutrient supply, normal oxygen", "What do you predict will happen to Waste Buildup when the cell is healthy?"),
        ("Starvation Mode", "Lock Nutrient Supply to 10%", "What do you predict will happen to Cell Size when nutrients are extremely low?"),
        ("Oxygen Crisis", "Set Oxygen Level to 15%", "How does low oxygen affect Waste Buildup compared to low nutrients?")
    ],
    "discoveries": [
        "Cells must stay small because nutrients and oxygen can only diffuse a short distance",
        "When nutrient supply drops, cells shrink and may stop dividing entirely",
        "Waste buildup is toxic — cells that can't remove waste lose function and die",
        "The surface-area-to-volume ratio explains why cells can't grow infinitely large"
    ],
    "answer": "Cells are microscopic because they MUST be small. A cell needs to exchange nutrients, oxygen, and waste across its membrane, and that exchange only works efficiently at tiny scales. If cells were bigger, the center would starve while waste piled up!",
    "stem_title": "Design a Cell City",
    "stem_mission": "Design a model city where each building represents a cell organelle, showing how resources flow in and waste flows out — just like a real cell.",
    "stem_scenario": "Your city planning team has been hired to design 'Cell City' — a community where every structure has a job, resources must reach every building, and waste removal is critical. Use your model to decide the best layout.",
    "stem_questions": [
        "Which organelle-buildings are most important for the city's survival?",
        "What happens to Cell City if the waste removal system breaks down?",
        "How does Cell City compare to a real cell under a microscope?"
    ],
    "stem_design_qs": [
        "What structures will represent the cell membrane, nucleus, and mitochondria?",
        "How will resources (nutrients, oxygen) be delivered throughout your city?",
        "What waste removal systems will you include?",
        "How will you show that every part of the city depends on every other part?"
    ],
    "career": "Cell Biologists and Biomedical Researchers use powerful microscopes and computer models to study cells and develop treatments for diseases. They earn $60,000–$120,000/year.",
    "images": {
        "cover": ("cover-cells.png", "A stunning, colorful microscope view of diverse human cells — red blood cells, white blood cells, and neurons — glowing with fluorescent staining on a dark background, scientific and dramatic"),
        "landscape": ("landscape-cells.png", "6th grade students looking through microscopes in a bright modern science lab, examining cell slides, excited expressions, natural light from windows"),
        "modeling": ("modeling-cells.png", "A diverse group of 6th grade students working together on laptops building a digital cell model, modern classroom with cell diagrams on the wall"),
        "discussion": ("discussion-cells.png", "A teacher leading an animated discussion with 6th grade students about cells, pointing at a large cell diagram on a smartboard, students with hands raised"),
        "stem": ("stem-cell-city.png", "6th grade students building a 3D model of a cell city using craft materials and markers, collaborative group work at tables, colorful project")
    },
    "pre_assessment": [
        "What do you think cells are? Where are they found?",
        "Why do you think you need a microscope to see cells?",
        "Draw what you think a cell looks like inside.",
        "If cells are alive, what do they need to survive?"
    ],
    "extend_components": [
        ("Cell Division Rate", "How quickly cells copy themselves to grow or repair tissue"),
        ("Temperature", "Temperature affects how fast chemical reactions happen inside cells"),
        ("pH Level", "The acidity of the cell's environment affects enzyme function")
    ],
    "reflections": [
        "Why can't a single cell grow to be the size of a basketball?",
        "How is a cell like a tiny factory? What are the 'machines' inside?",
        "What would happen to your body if your cells couldn't get rid of waste?",
        "Why do different cells in your body have different shapes and sizes?",
        "How does your model help explain something you can't see with your eyes?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how cell size, nutrients, oxygen, and waste interact to determine cell health."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "All living things are made up of cells, which is the smallest unit that can be said to be alive. Cells have specific structures that perform specific functions."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students explore why cells must remain at microscopic scales to function — connecting size to the efficiency of material exchange.")
    ],
    "cast_items": [
        "Explain how cell structures work together to keep a cell alive",
        "Use a model to describe the relationship between cell size and function",
        "Describe why organisms are organized at the cellular level"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist observes that cells in a low-oxygen environment stop growing and begin to die. Which best explains this observation based on cell structure and function?"),
        ("Constructed Response:", "Using what you know about cells, explain why a single cell cannot grow to be as large as a golf ball. Use the concepts of surface area, volume, and nutrient exchange in your answer.")
    ],
    "background_intro": "Cells are the fundamental units of life — every living organism on Earth is made of one or more cells. Understanding cell structure and function is the foundation of all biology and medicine.",
    "background_sections": [
        ("Cell Theory", "All living things are composed of cells. Cells are the basic unit of structure and function in living things. All cells come from pre-existing cells. This theory, developed in the 1830s-1850s by Schleiden, Schwann, and Virchow, is one of the foundational principles of modern biology."),
        ("Why Cells Are Small", "Cells must exchange materials (nutrients in, waste out) across their cell membrane. As a cell grows, its volume increases faster than its surface area (cube vs. square relationship). Eventually, the membrane can't supply the interior fast enough. This surface-area-to-volume ratio is the key constraint on cell size."),
        ("Cell Organelles", "Key organelles include the nucleus (DNA storage and control center), mitochondria (energy production), ribosomes (protein construction), endoplasmic reticulum (protein and lipid processing), and cell membrane (boundary and gatekeeper). Each plays a critical role in keeping the cell alive."),
        ("Cells in the Human Body", "The human body contains approximately 37.2 trillion cells of about 200 different types. Red blood cells carry oxygen, white blood cells fight infection, neurons transmit signals, and muscle cells enable movement. Despite their diversity, all share the same basic cellular machinery.")
    ],
    "lever_L": "Students identify cell size, nutrient supply, oxygen level, and waste buildup as key components affecting cell function.",
    "lever_E": "Students determine that nutrient supply positively affects cell function while waste buildup negatively affects it, and that oxygen is essential for energy production.",
    "lever_V": "Students build a model showing how inputs (nutrients, oxygen) and outputs (waste) determine whether a cell thrives, shrinks, or dies.",
    "lever_Ev": "Students run starvation and oxygen-crisis scenarios to observe how removing key inputs affects the entire system.",
    "lever_R": "Students add cell division rate or temperature to explore more complex interactions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with microscopic cell imagery", "say": "Did you know your body has more cells than there are stars in the Milky Way?", "do": "Show a quick video or image of cells under a microscope to build wonder.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're going to explore the invisible world inside YOU.", "do": "Have students read objectives aloud. Pre-teach 'organelle' and 'cell membrane.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "If you have 37 trillion cells, why can't you see one?", "say": "Think about this: right now, trillions of cells are working inside you and you can't see ANY of them.", "do": "Have students turn and talk: What's the smallest thing you've ever seen?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to understand why cells MUST be tiny.", "do": "Briefly preview each LEVER step. Connect to prior knowledge of models.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for cell model", "say": "What does a cell need to survive? What threatens it?", "do": "Guide sorting. Discuss why nutrient supply and oxygen come from OUTSIDE the cell.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "More nutrients help cells grow — but what happens when waste piles up?", "do": "Help students identify positive and negative relationships. Draw arrows.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's starve a cell and see what our model predicts!", "do": "Have students predict first, then run simulations. Compare healthy vs. starved cells.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So WHY can't cells be huge? What did our model reveal?", "do": "Lead discussion connecting surface-area-to-volume ratio to their model results.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Cell City design challenge", "say": "Now you're city planners — but your city IS a cell!", "do": "Distribute materials. Groups design Cell City showing resource flow and waste removal.", "time": "12 min"}
    ],
    "sort_reasoning": "Nutrient Supply and Oxygen Level are external because they come from the environment outside the cell — the cell depends on its surroundings for these inputs. Cell Size and Waste Buildup are internal because they are properties of the cell itself that change in response to external conditions.",
    "relationships": [
        ("Nutrient Supply to Cell Size", "POSITIVE (+)", "More nutrients allow the cell to grow and maintain its structures. Without nutrients, cells shrink and stop dividing."),
        ("Oxygen Level to Waste Buildup", "NEGATIVE (-)", "Higher oxygen levels allow cellular respiration to work efficiently, breaking down waste. Low oxygen causes waste to accumulate."),
        ("Waste Buildup to Cell Size", "NEGATIVE (-)", "As waste accumulates, it becomes toxic and damages cell structures, causing cells to shrink and eventually die.")
    ],
    "sim_answers": [
        ("Starvation Scenario", "When Nutrient Supply is locked at 10%, Cell Size decreases steadily. The cell cannot maintain its structures or produce energy. Waste Buildup increases because the cell can't power its cleanup systems. Eventually the cell would die."),
        ("Oxygen Crisis Scenario", "At 15% Oxygen Level, Waste Buildup skyrockets because the cell can't perform aerobic respiration efficiently. Cell Size also decreases as the cell shifts to less efficient energy production. This mimics what happens in tissues with poor blood flow.")
    ],
    "reflection_exemplars": [
        ("Why can't a cell be basketball-sized?", "As a cell grows, its volume (inside) increases much faster than its surface area (membrane). The membrane wouldn't be able to bring in enough nutrients or remove enough waste to keep the huge interior alive. The center of the cell would literally starve while drowning in its own waste."),
        ("How is a cell like a factory?", "A cell has a control center (nucleus/DNA), power plants (mitochondria), assembly lines (ribosomes), shipping department (ER and Golgi), and a security fence (cell membrane). Like a factory, if any department fails, the whole operation is affected.")
    ],
    "stem_intro": "Present the challenge: Your team has been hired to design Cell City. Every building has a job, resources must reach every corner, and waste removal is critical. Your city must demonstrate how a real cell works.",
    "stem_concepts": [
        ("Surface Area to Volume Ratio", "As objects get larger, their volume grows faster than their surface area. This limits how big cells can get because exchange happens at the surface."),
        ("Organelle Specialization", "Just like a city has specialized buildings (hospital, power plant, school), cells have specialized organelles that each perform a critical function."),
        ("Homeostasis", "Cells must maintain a stable internal environment. When waste builds up or nutrients run low, the cell's balance is disrupted and it can't function properly.")
    ],
    "stem_eval": [
        ("Expert (4)", "Cell City accurately represents 4+ organelles, shows resource flow AND waste removal, and connects to model evidence"),
        ("Proficient (3)", "Cell City represents 3+ organelles with clear resource flow, connects to lesson concepts"),
        ("Developing (2)", "Cell City shows some organelles but lacks clear resource/waste flow connections"),
        ("Beginning (1)", "Cell City is incomplete or doesn't connect building functions to cell organelle functions")
    ],
    "support": [
        "Provide a labeled diagram of a cell with organelle functions listed for reference",
        "Use physical manipulatives (blocks, beads) to demonstrate surface-area-to-volume ratio",
        "Sentence frames: 'When nutrient supply decreases, cell size __ because __'"
    ],
    "extensions": [
        "Research how cancer cells ignore the normal rules of cell size and division",
        "Calculate the surface-area-to-volume ratio for cubes of increasing size",
        "Compare plant cells to animal cells — what additional structures do plants have?"
    ],
    "cross_curr": [
        ("Math", "Calculate surface area and volume of cubes to demonstrate why the ratio changes as cells grow"),
        ("ELA", "Write a narrative from the perspective of a nutrient molecule traveling through a cell"),
        ("Art", "Create a detailed, labeled diagram of a cell using color-coding for different organelles")
    ],
    "misconceptions": [
        ("Cells are just blobs of jelly", "Cells are highly organized structures with specialized parts (organelles) that work together like a factory. Each organelle has a specific job critical to the cell's survival.", "Show electron microscope images of real cells to reveal the complex internal structure."),
        ("All cells look the same", "Human bodies have about 200 different cell types, each with a unique shape matched to its function. Red blood cells are disc-shaped for gas exchange, neurons are long for signal transmission, and muscle cells are fiber-shaped for contraction.", "Show images of different cell types and ask students to guess their function from their shape."),
        ("Cells are not alive", "Each cell independently carries out ALL life functions: obtaining energy, removing waste, growing, reproducing, and responding to its environment. A single-celled organism like an amoeba IS a complete living thing.", "Ask: Does a cell eat? Breathe? Grow? Reproduce? If yes to all, is it alive?")
    ]
}

L02 = {
    "id": "G06-L02",
    "title": "When the Earth Cracks Open",
    "subtitle": "The Powerful Forces That Shape Our Planet's Surface",
    "ngss": "MS-ESS2-2",
    "ngss_desc": "Construct an explanation based on evidence for how geoscience processes have changed Earth's surface at varying time and spatial scales.",
    "big_question": "Why do earthquakes and volcanoes happen in the same places over and over again?",
    "objectives": [
        "Explain how convection currents in the mantle drive plate movement",
        "Model how plate speed, mantle heat, rock density, and friction interact at plate boundaries",
        "Predict what happens when tectonic plates collide, separate, or slide past each other",
        "Connect plate tectonics to real-world earthquake and volcano patterns"
    ],
    "vocabulary": [
        ("Tectonic Plate", "A massive slab of Earth's lithosphere that floats on the semi-liquid mantle below"),
        ("Convection Current", "A circular flow of material caused by heating from below and cooling from above"),
        ("Plate Boundary", "The zone where two tectonic plates meet, interact, and create geological activity"),
        ("Seismic Wave", "A wave of energy that travels through Earth during an earthquake")
    ],
    "components": [
        ("Plate Movement Speed", "How fast tectonic plates move relative to each other, measured in centimeters per year", False),
        ("Mantle Heat", "The thermal energy from Earth's core that drives convection currents in the mantle", True),
        ("Rock Density", "How heavy and compressed the rock is — denser rock sinks, lighter rock rises", False),
        ("Boundary Friction", "The resistance created when two plates grind against each other at their boundary", False)
    ],
    "think_about_it": "When mantle heat increases, what happens to plate movement speed? Does more friction at a boundary make earthquakes more or less powerful?",
    "scenarios": [
        ("Slow Drift", "Set Mantle Heat and Plate Movement Speed to low levels and observe geological activity"),
        ("Heat Surge", "Lock Mantle Heat to maximum and observe how plates respond over time"),
        ("Friction Lockup", "Set Boundary Friction to maximum and watch what builds up before release")
    ],
    "sim_scenarios": [
        ("Slow Drift", "Low mantle heat, slow plate movement", "What do you predict happens to earthquake frequency when plates move slowly?"),
        ("Heat Surge", "Lock Mantle Heat to maximum", "What do you predict will happen to Plate Movement Speed when mantle heat is extreme?"),
        ("Friction Lockup", "Set Boundary Friction to maximum", "What do you predict happens when friction locks plates together for a long time?")
    ],
    "discoveries": [
        "Earthquakes and volcanoes cluster along plate boundaries — they're not random at all",
        "Higher mantle heat drives faster convection currents, pushing plates faster",
        "More boundary friction means energy builds up longer — resulting in BIGGER earthquakes when it finally releases",
        "The densest plates get pushed under lighter plates (subduction), creating deep ocean trenches and volcanoes"
    ],
    "answer": "Earthquakes and volcanoes happen in the same places because that's where tectonic plates meet. The boundaries between plates are zones of enormous stress, and the heat from Earth's interior keeps pushing plates together, apart, or sideways — creating predictable patterns of geological activity.",
    "stem_title": "Design an Earthquake-Ready City",
    "stem_mission": "Design a city near a plate boundary that can withstand earthquakes using evidence from your tectonic model about earthquake intensity and frequency.",
    "stem_scenario": "A new city is being planned near the San Andreas Fault in California. The city council needs your engineering team to recommend building designs, infrastructure, and emergency systems based on what your model reveals about earthquake patterns.",
    "stem_questions": [
        "Based on your model, how strong could earthquakes get at this boundary?",
        "What building designs would best survive the type of shaking your model predicts?",
        "How should emergency response systems be designed based on earthquake frequency patterns?"
    ],
    "stem_design_qs": [
        "What building materials and foundations will resist earthquake shaking?",
        "Where should emergency shelters and hospitals be located relative to the fault?",
        "What early warning systems will you include in your city design?",
        "How will your city's infrastructure (roads, bridges, water pipes) handle ground movement?"
    ],
    "career": "Seismologists and Geophysicists study earthquakes and Earth's interior to predict hazards and design safer communities. They earn $70,000–$130,000/year.",
    "images": {
        "cover": ("cover-tectonics.png", "A dramatic aerial view of a cracked desert landscape showing a visible fault line with tectonic stress, golden light illuminating the cracks, cinematic landscape photography"),
        "landscape": ("landscape-tectonics.png", "6th grade students examining rock samples and a globe in a modern science classroom, pointing at tectonic plate boundaries on a map"),
        "modeling": ("modeling-tectonics.png", "A diverse group of 6th grade students working on laptops building a plate tectonics model, classroom with Earth science posters and a globe on the desk"),
        "discussion": ("discussion-tectonics.png", "A teacher leading a discussion about earthquakes with engaged 6th grade students, pointing at a diagram of plate boundaries on a smartboard"),
        "stem": ("stem-earthquake-city.png", "6th grade students building model earthquake-resistant buildings with craft materials, testing them on a shake table, excited and collaborative")
    },
    "pre_assessment": [
        "Have you ever felt an earthquake or seen one on the news? What happened?",
        "Why do you think earthquakes happen in some places but not others?",
        "What do you think is beneath the ground under your feet?",
        "Draw what you think the inside of the Earth looks like."
    ],
    "extend_components": [
        ("Magma Pressure", "The buildup of molten rock beneath the surface that can cause volcanic eruptions"),
        ("Water Content", "Water in rock lowers its melting point, affecting where magma forms"),
        ("Plate Thickness", "Thicker plates resist bending while thinner plates are more flexible")
    ],
    "reflections": [
        "Why do earthquakes and volcanoes form a 'Ring of Fire' around the Pacific Ocean?",
        "How does friction at a plate boundary actually CAUSE bigger earthquakes, not smaller ones?",
        "If tectonic plates move so slowly (cm/year), how can they cause such violent events?",
        "What would Earth's surface look like if there were no tectonic plates?",
        "How does your model help predict where future earthquakes might occur?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how mantle heat, plate speed, rock density, and friction interact to produce geological events."),
        ("Disciplinary Core Idea", "ESS2.B Plate Tectonics and Large-Scale System Interactions", "The movement of tectonic plates is driven by convection in the mantle and results in continental drift, earthquakes, volcanoes, and mountain building."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how Earth's surface appears stable but is constantly changing due to slow, powerful tectonic forces — and how small changes build up to dramatic events.")
    ],
    "cast_items": [
        "Explain how convection currents in Earth's mantle drive tectonic plate movement",
        "Use evidence to describe patterns of earthquake and volcano locations worldwide",
        "Model how interactions at plate boundaries produce geological events"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Scientists observe that earthquakes along the San Andreas Fault occur in clusters every 100-150 years. Which best explains this pattern using plate tectonic theory?"),
        ("Constructed Response:", "Using your model of plate tectonics, explain why the west coast of South America has many volcanoes and earthquakes while the east coast does not.")
    ],
    "background_intro": "Plate tectonics is the grand unifying theory of geology. It explains earthquakes, volcanoes, mountain building, ocean floor spreading, and even the distribution of fossils across continents.",
    "background_sections": [
        ("Earth's Layers", "Earth consists of the crust (thin outer layer), mantle (thick semi-solid layer), outer core (liquid iron), and inner core (solid iron). The crust and uppermost mantle form the lithosphere, which is broken into tectonic plates that float on the more fluid asthenosphere below."),
        ("Convection Drives Plates", "Heat from Earth's core and radioactive decay in the mantle creates convection currents — huge circular flows of rock that rise when hot and sink when cool. These currents drag tectonic plates along, causing them to move 2-15 cm per year. This slow movement is responsible for all major geological features."),
        ("Types of Plate Boundaries", "Divergent boundaries: plates move apart, creating new crust (mid-ocean ridges). Convergent boundaries: plates collide, creating mountains or subduction zones. Transform boundaries: plates slide past each other, creating earthquake faults like the San Andreas. Each type produces different geological hazards."),
        ("The Ring of Fire", "About 75% of the world's volcanoes and 90% of earthquakes occur along the Ring of Fire — the boundaries of the Pacific Plate. This zone stretches from New Zealand through Japan, across Alaska, and down the west coast of the Americas. It's the most geologically active zone on Earth.")
    ],
    "lever_L": "Students identify plate movement speed, mantle heat, rock density, and boundary friction as the key components of the tectonic system.",
    "lever_E": "Students determine that mantle heat positively drives plate movement, while boundary friction negatively affects smooth plate motion but positively affects earthquake intensity when released.",
    "lever_V": "Students build a model showing how heat-driven plate movement interacts with friction to produce patterns of geological events.",
    "lever_Ev": "Students run scenarios comparing low friction (frequent small quakes) vs. high friction (rare but massive quakes) to understand earthquake patterns.",
    "lever_R": "Students add magma pressure or water content to model volcanic activity alongside earthquakes.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with cracked earth imagery", "say": "The ground beneath your feet is moving RIGHT NOW. You just can't feel it.", "do": "Show a short video of earthquake footage to create urgency and wonder.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're going to model the forces that crack open our planet.", "do": "Have students read objectives. Pre-teach 'tectonic plate' and 'convection current.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do earthquakes strike the same places?", "say": "Look at this earthquake map. Do you see a pattern? It's NOT random.", "do": "Show global earthquake/volcano map. Have students describe patterns they see.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to understand why California gets earthquakes but Florida doesn't.", "do": "Preview LEVER steps. Connect to students' earthquake experiences.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for tectonics model", "say": "What forces are at work beneath our feet? Which ones can we observe?", "do": "Guide sorting. Explain why mantle heat is external (comes from Earth's core).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Here's the tricky part: MORE friction doesn't mean fewer earthquakes — it means BIGGER ones.", "do": "Demonstrate with two erasers sliding past each other. More friction = more buildup = bigger snap.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's crank up the heat and see what happens to our plates!", "do": "Students predict before running. Compare low-friction vs. high-friction boundary scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now you know why earthquakes and volcanoes aren't random — they follow the plates.", "do": "Connect model results to real Ring of Fire data. Show plate boundary map.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Earthquake-ready city design", "say": "You're now engineers. Design a city that can survive what our model predicts.", "do": "Distribute materials. Groups design earthquake-resistant city with evidence from model.", "time": "12 min"}
    ],
    "sort_reasoning": "Mantle Heat is external because it originates from Earth's core — a source outside the plate system itself. Plate Movement Speed, Rock Density, and Boundary Friction are internal because they are properties of the plates themselves that respond to mantle heat and each other.",
    "relationships": [
        ("Mantle Heat to Plate Movement Speed", "POSITIVE (+)", "Higher mantle heat creates stronger convection currents, which push plates faster. The hotter the mantle, the more energy drives plate motion."),
        ("Plate Movement Speed to Boundary Friction", "POSITIVE (+)", "Faster-moving plates create more friction at boundaries where they meet. More speed means more grinding force."),
        ("Boundary Friction to Earthquake Intensity", "POSITIVE (+)", "More friction at a boundary means more energy builds up before release. When locked plates finally slip, the accumulated energy produces larger, more destructive earthquakes.")
    ],
    "sim_answers": [
        ("Heat Surge Scenario", "When Mantle Heat is locked at maximum, Plate Movement Speed increases significantly. This drives more geological activity at boundaries. The model shows that more heat = faster plates = more frequent boundary interactions."),
        ("Friction Lockup Scenario", "At maximum Boundary Friction, energy accumulates for longer periods. When it finally releases, the resulting earthquake is much more powerful. This explains why the San Andreas Fault can be quiet for decades, then produce a massive quake.")
    ],
    "reflection_exemplars": [
        ("Why does more friction cause bigger earthquakes?", "Friction locks plates together like pressing two erasers hard against each other. The more friction, the longer plates stay locked while stress builds. When the friction finally fails, ALL that stored energy releases at once — like letting go of a stretched rubber band. Less friction means frequent small releases; more friction means rare but devastating ones."),
        ("How can slow movement cause violent events?", "Even though plates move just centimeters per year, they are ENORMOUS — thousands of kilometers across and hundreds of kilometers thick. When something that massive moves and gets stuck, incredible amounts of energy accumulate. A few centimeters of movement across a plate that weighs billions of tons stores a phenomenal amount of energy.")
    ],
    "stem_intro": "Present the scenario: A new city is being planned 50 miles from the San Andreas Fault. The city council needs engineering recommendations based on your tectonic model data.",
    "stem_concepts": [
        ("Seismic Engineering", "Building designs that absorb or deflect earthquake energy, such as base isolation systems and flexible frames that sway without breaking."),
        ("Earthquake Recurrence Interval", "The average time between major earthquakes on a given fault. This helps predict future hazards and design for the right intensity."),
        ("Liquefaction", "During earthquakes, loose wet soil can behave like a liquid, causing buildings to sink. Foundation design must account for soil conditions.")
    ],
    "stem_eval": [
        ("Expert (4)", "City design uses model evidence for earthquake predictions, includes multiple engineering solutions, and addresses emergency response"),
        ("Proficient (3)", "City design references model data and includes at least two engineering solutions"),
        ("Developing (2)", "City design mentions earthquakes but doesn't connect engineering solutions to model evidence"),
        ("Beginning (1)", "City design is incomplete or doesn't connect to plate tectonics concepts")
    ],
    "support": [
        "Provide a pre-labeled diagram of Earth's layers with convection current arrows drawn in",
        "Use a physical demonstration: slide two textbooks past each other to show friction and sudden release",
        "Sentence frames: 'When mantle heat increases, plate movement __ because __'"
    ],
    "extensions": [
        "Research the 2011 Japan earthquake and explain it using plate tectonics theory",
        "Model a divergent boundary (mid-ocean ridge) vs. a convergent boundary — how do they differ?",
        "Calculate how far a plate moving at 5 cm/year would travel in 1 million years"
    ],
    "cross_curr": [
        ("Math", "Plot earthquake data on a coordinate grid to identify plate boundary locations statistically"),
        ("ELA", "Write a news report about a fictional earthquake, explaining the science behind it to the public"),
        ("Social Studies", "Research how ancient civilizations explained earthquakes and volcanoes before plate tectonics theory")
    ],
    "misconceptions": [
        ("The ground is solid and doesn't move", "Earth's surface is made of plates that are constantly moving, just very slowly (a few cm/year). Over millions of years, this movement reshapes continents, builds mountains, and opens oceans. We don't feel it because it's too slow.", "Demo: Slowly push two pieces of paper together on a desk — they buckle up like mountains forming."),
        ("Earthquakes happen randomly", "Earthquakes follow tectonic plate boundaries with remarkable precision. 90% of earthquakes occur along the Ring of Fire. If you plot earthquake locations on a map, they trace plate boundaries perfectly.", "Show an earthquake map and a plate boundary map side by side — they match almost exactly."),
        ("Volcanoes and earthquakes aren't related", "Both are caused by tectonic plate interactions. At convergent boundaries, subduction creates both deep earthquakes and volcanic chains. The same forces that cause one cause the other.", "Show the Ring of Fire map with both earthquake and volcano locations — they overlap along plate boundaries.")
    ]
}

L03 = {
    "id": "G06-L03",
    "title": "Why Your Hot Cocoa Betrays You",
    "subtitle": "The Science of Thermal Energy Transfer",
    "ngss": "MS-PS3-3, MS-PS3-4",
    "ngss_desc": "Apply scientific principles to design, construct, and test a device that either minimizes or maximizes thermal energy transfer. Plan an investigation to determine the relationships among the energy transferred, the type of matter, the mass, and the change in the average kinetic energy of the particles as measured by the temperature of the sample.",
    "big_question": "No matter what you do, your hot cocoa always gets cold — where does the heat actually go?",
    "objectives": [
        "Explain how thermal energy transfers from hot objects to cold surroundings through conduction, convection, and radiation",
        "Model how temperature difference, insulation, surface area, and air movement affect heat loss",
        "Design a system that minimizes thermal energy transfer to keep a drink hot longer",
        "Connect thermal energy transfer to real-world engineering problems"
    ],
    "vocabulary": [
        ("Thermal Energy", "The total kinetic energy of all particles in a substance — what we measure as temperature"),
        ("Conduction", "Heat transfer through direct contact between materials — like a hot mug warming your hands"),
        ("Convection", "Heat transfer through the movement of fluids (liquids or gases) — warm air rising, cool air sinking"),
        ("Insulation", "A material that slows down thermal energy transfer by trapping air pockets")
    ],
    "components": [
        ("Temperature Difference", "The gap between the hot cocoa temperature and the room temperature", True),
        ("Insulation Level", "How well the container prevents heat from escaping through its walls", False),
        ("Container Surface Area", "The total outer area of the container exposed to the cooler environment", False),
        ("Air Movement", "The speed of air flowing past the container, carrying heat away by convection", True)
    ],
    "think_about_it": "When insulation level increases, what happens to the rate of heat loss? Is a tall thin mug or a short wide mug better for keeping cocoa hot — and why?",
    "scenarios": [
        ("Open Mug", "Set Insulation Level to 0% with normal room conditions"),
        ("Travel Mug", "Set Insulation Level to 80% and observe heat loss over time"),
        ("Windy Day", "Lock Air Movement to maximum and compare heat loss to calm conditions")
    ],
    "sim_scenarios": [
        ("Open Mug", "No insulation, normal air movement", "How long do you predict it will take for your cocoa to reach room temperature?"),
        ("Travel Mug", "Insulation at 80%, normal conditions", "How much longer will the cocoa stay hot compared to the open mug?"),
        ("Windy Day", "Maximum air movement, no insulation", "What do you predict happens to heat loss rate on a windy day?")
    ],
    "discoveries": [
        "Heat ALWAYS flows from hot to cold — never the other way — until temperatures equalize",
        "Insulation doesn't add heat; it just slows down the transfer to the environment",
        "More surface area means faster heat loss because there's more area for energy to escape",
        "Moving air carries heat away much faster than still air (convection accelerates cooling)"
    ],
    "answer": "Your hot cocoa loses heat to its cooler surroundings through three mechanisms: conduction (through the mug), convection (warm air rising off the surface), and radiation (infrared energy). Heat always flows from hot to cold until both reach the same temperature — that's the Second Law of Thermodynamics in your kitchen!",
    "stem_title": "Design the Ultimate Hot Cocoa Keeper",
    "stem_mission": "Design and test a container that keeps hot cocoa above 50°C for as long as possible using your understanding of thermal energy transfer.",
    "stem_scenario": "A beverage company is holding a design competition. They need a new travel mug that keeps drinks hot for at least 2 hours without electricity. Your engineering team must use model evidence to design, build, and test a prototype.",
    "stem_questions": [
        "Which method of heat transfer causes the MOST heat loss from a typical mug?",
        "What materials and design features will minimize each type of thermal energy transfer?",
        "How will you test whether your design actually works better than a regular mug?"
    ],
    "stem_design_qs": [
        "What insulating materials will you use and why?",
        "How will you minimize the surface area exposed to air?",
        "Will your design include a lid? Why is the top surface important?",
        "How will you measure and compare your design's performance to a control mug?"
    ],
    "career": "Thermal Engineers and Materials Scientists design insulation systems for buildings, spacecraft, and products to control heat flow. They earn $70,000–$120,000/year.",
    "images": {
        "cover": ("cover-thermal.png", "A steaming cup of hot cocoa on a cold winter morning with visible steam rising, thermal imaging style showing heat gradients from red hot to blue cold, dramatic and scientific"),
        "landscape": ("landscape-thermal.png", "6th grade students conducting a heat transfer experiment with thermometers in different cups of water, recording data, bright science lab setting"),
        "modeling": ("modeling-thermal.png", "A diverse group of 6th grade students working on laptops building a thermal energy model, modern classroom with science equipment visible"),
        "discussion": ("discussion-thermal.png", "A teacher demonstrating heat transfer to 6th grade students using a hot and cold water experiment, students watching closely with notebooks"),
        "stem": ("stem-insulation.png", "6th grade students testing homemade insulated containers with thermometers, comparing different materials like foam and fabric, excited about results")
    },
    "pre_assessment": [
        "Why does a metal spoon feel colder than a wooden spoon at the same temperature?",
        "What happens to the temperature of hot soup if you leave it on the counter?",
        "Why do you think we wear coats in winter? Do coats create heat?",
        "Draw or describe how you think heat moves from a hot drink to the air around it."
    ],
    "extend_components": [
        ("Radiation Rate", "Heat loss through infrared energy that radiates from the hot surface to the surroundings"),
        ("Container Material", "Different materials conduct heat at different rates — metal vs. ceramic vs. foam"),
        ("Liquid Volume", "More liquid stores more thermal energy, taking longer to cool down")
    ],
    "reflections": [
        "Why does blowing on hot soup cool it down faster?",
        "If insulation doesn't create heat, how does a winter coat keep you warm?",
        "Why is a thermos designed with a vacuum layer? What does the vacuum prevent?",
        "Would your hot cocoa cool faster in a metal cup or a foam cup? Explain why.",
        "How could you use thermal energy transfer knowledge to keep an ice cream from melting?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how temperature difference, insulation, surface area, and air movement affect thermal energy transfer rates."),
        ("Disciplinary Core Idea", "PS3.A Definitions of Energy / PS3.B Conservation of Energy and Energy Transfer", "Temperature is a measure of the average kinetic energy of particles. Energy transfers from hot to cold objects through conduction, convection, and radiation."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students trace the flow of thermal energy from the hot drink through the container to the surrounding environment, understanding that energy is conserved but transferred.")
    ],
    "cast_items": [
        "Explain how thermal energy transfers between objects of different temperatures",
        "Apply understanding of heat transfer to design solutions that control energy flow",
        "Identify the relationship between particle motion and temperature"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student places a metal spoon and a wooden spoon in the same cup of hot water. After 2 minutes, the metal spoon feels much hotter. Which best explains this observation?"),
        ("Constructed Response:", "Design and describe a container that would keep an ice cube frozen for as long as possible. Explain how your design minimizes thermal energy transfer using conduction, convection, and radiation.")
    ],
    "background_intro": "Thermal energy transfer is one of the most fundamental and observable physics concepts. Every student has experienced a hot drink cooling down — this lesson connects that everyday experience to the science of energy flow.",
    "background_sections": [
        ("Three Methods of Heat Transfer", "Conduction: energy transfer through direct molecular contact (metal spoon in hot soup). Convection: energy transfer through fluid movement (warm air rising from a heater). Radiation: energy transfer through electromagnetic waves (feeling warmth from the sun). All three happen simultaneously with your hot cocoa."),
        ("Temperature and Particle Motion", "Temperature measures the average kinetic energy of particles. In a hot drink, water molecules are moving fast. They transfer their kinetic energy to slower-moving air molecules through collisions. This is conduction at the molecular level. The drink cools because its particles slow down."),
        ("Insulation Science", "Good insulators work by trapping pockets of air. Air is a poor conductor of heat, so trapped air layers create barriers to conduction. Foam cups, down jackets, and double-pane windows all use this principle. A vacuum (no air at all) is the best insulator — that's how a thermos works."),
        ("Real-World Applications", "Thermal engineering is critical in building design (insulation, HVAC systems), spacecraft (extreme temperature management), electronics (heat sinks), and food safety (keeping hot foods hot and cold foods cold). Understanding heat transfer saves energy, money, and lives.")
    ],
    "lever_L": "Students identify temperature difference, insulation level, container surface area, and air movement as the key components affecting heat loss.",
    "lever_E": "Students determine that insulation negatively affects heat loss (slows it down) while air movement and surface area positively affect heat loss (speed it up).",
    "lever_V": "Students build a model showing how these four factors interact to determine how quickly a hot drink cools.",
    "lever_Ev": "Students run open mug vs. travel mug vs. windy day scenarios to quantify the impact of each variable.",
    "lever_R": "Students add radiation rate or container material to make the model more comprehensive.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with steaming hot cocoa imagery", "say": "Has this ever happened to you? You make the perfect hot cocoa and then... it gets cold.", "do": "Bring in a real hot drink and a thermometer. Show the temperature dropping in real time.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're going to find out WHERE the heat goes — and how to stop it.", "do": "Have students read objectives. Pre-teach 'conduction,' 'convection,' and 'insulation.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does the heat go?", "say": "Your cocoa starts at 85°C and ends at room temperature. That heat energy didn't disappear — so where did it go?", "do": "Think-pair-share: Where do students think the heat goes? Capture predictions.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to understand exactly how heat escapes — and then stop it.", "do": "Preview LEVER steps. Explain that the STEM challenge will use model evidence.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for thermal model", "say": "What factors affect how fast your cocoa cools? Some we can control, some we can't.", "do": "Guide sorting. Discuss why temperature difference and air movement are external inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More insulation means LESS heat loss — that's a negative relationship. But more air movement means MORE heat loss.", "do": "Use hand gestures: positive = both go up together; negative = one up, other down.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's compare an open mug, a travel mug, and a mug in the wind!", "do": "Students predict cooling curves first. Then run simulations and compare to predictions.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So heat flows from hot to cold — ALWAYS. We can slow it down but never stop it completely.", "do": "Discuss the Second Law of Thermodynamics in kid-friendly terms.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Design the ultimate hot cocoa keeper", "say": "Now you're engineers. Design a container that keeps cocoa hot for 2 hours!", "do": "Provide materials. Groups design, build, and test insulated containers.", "time": "12 min"}
    ],
    "sort_reasoning": "Temperature Difference and Air Movement are external because they come from the environment — the room temperature and wind are outside factors the drink can't control. Insulation Level and Container Surface Area are internal design features of the container that can be engineered to control heat loss.",
    "relationships": [
        ("Temperature Difference to Heat Loss Rate", "POSITIVE (+)", "The bigger the gap between hot cocoa and room temperature, the faster heat flows out. As the drink cools and the gap shrinks, heat loss slows down naturally."),
        ("Insulation Level to Heat Loss Rate", "NEGATIVE (-)", "Better insulation slows thermal energy transfer by trapping air and blocking conduction. A well-insulated container dramatically reduces cooling rate."),
        ("Air Movement to Heat Loss Rate", "POSITIVE (+)", "Moving air carries away warm air molecules and replaces them with cool ones (convection). Wind or a fan dramatically increases the rate of heat loss.")
    ],
    "sim_answers": [
        ("Open Mug vs. Travel Mug", "The open mug loses heat rapidly — temperature drops quickly in the first 15-20 minutes then slows as it approaches room temperature. The travel mug (80% insulation) loses heat much more slowly, maintaining a drinkable temperature 3-4 times longer. The model shows insulation's dramatic effect."),
        ("Windy Day Scenario", "With maximum air movement, the open mug cools even faster than in still air. Wind accelerates convection, the most significant heat loss mechanism for a hot liquid. The model shows that convection can double or triple the cooling rate compared to still air.")
    ],
    "reflection_exemplars": [
        ("Why does blowing on soup cool it down?", "Blowing on soup accelerates convection. Your breath pushes away the layer of warm air sitting above the soup and replaces it with cooler air. This increases the temperature difference at the surface and speeds up heat transfer. You're essentially creating artificial wind that strips away the warm air boundary layer."),
        ("How does a coat keep you warm if it doesn't create heat?", "Your body generates heat through metabolism. A coat traps air between its fibers, creating insulation layers. These trapped air pockets slow the conduction of your body heat to the cold outside air. The coat doesn't warm you — it prevents your own heat from escaping. That's why a coat in a closet isn't warm but a coat on your body is.")
    ],
    "stem_intro": "Present the design challenge: A beverage company needs a travel mug that keeps drinks above 50°C for 2 hours. Your team must design, prototype, and test a solution using evidence from your thermal model.",
    "stem_concepts": [
        ("R-Value (Insulation Rating)", "A measure of how well a material resists heat flow. Higher R-value = better insulation. Materials like foam and fiberglass have high R-values."),
        ("Thermal Equilibrium", "The state when two objects reach the same temperature and heat transfer stops. Your goal is to delay reaching equilibrium as long as possible."),
        ("Vacuum Insulation", "Removing air entirely (creating a vacuum) eliminates convection and conduction, leaving only radiation. This is how thermos bottles work.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses all three heat transfer methods, uses model evidence, includes test data, and demonstrates understanding of thermal equilibrium"),
        ("Proficient (3)", "Design addresses at least two heat transfer methods with model evidence and testing plan"),
        ("Developing (2)", "Design mentions insulation but doesn't connect specific features to heat transfer types"),
        ("Beginning (1)", "Design is incomplete or doesn't demonstrate understanding of thermal energy transfer")
    ],
    "support": [
        "Provide a graphic organizer comparing conduction, convection, and radiation with everyday examples",
        "Let students feel different materials (metal, wood, foam, fabric) at the same temperature to experience conduction differences",
        "Sentence frames: 'When air movement increases, heat loss __ because __'"
    ],
    "extensions": [
        "Research how thermos bottles use vacuum insulation and explain why a vacuum stops conduction and convection",
        "Design an experiment to measure which material is the best insulator (foam, wool, bubble wrap, aluminum foil)",
        "Investigate how thermal energy transfer applies to building design — why are some houses colder than others?"
    ],
    "cross_curr": [
        ("Math", "Graph cooling curves for different containers and calculate the rate of temperature change per minute"),
        ("ELA", "Write product marketing copy for your insulated container design, explaining the science to consumers"),
        ("Social Studies", "Research how different cultures developed insulation solutions for extreme climates (igloos, adobe, yurts)")
    ],
    "misconceptions": [
        ("Cold flows into warm objects", "Cold is not a substance that flows. Only thermal energy (heat) flows — always from hot to cold. When your cocoa cools, heat is leaving the drink, not cold entering it. 'Feeling cold' means your body is losing heat to the environment.", "Ask: When you open a freezer, does cold come out or does heat go in? Feel the air — it's your body heat leaving!"),
        ("Insulation creates heat", "Insulation doesn't generate any energy. It simply slows down the rate of heat transfer. A jacket keeps you warm by trapping your body's heat, not by creating warmth. If you put a coat on a snowman, it would actually melt SLOWER.", "Demo: Put a thermometer inside a jacket with no heat source — the temperature doesn't rise."),
        ("Metal objects are colder than wooden objects", "At room temperature, metal and wood are the SAME temperature. Metal just FEELS colder because it conducts heat away from your hand much faster than wood does. Your brain interprets rapid heat loss as 'cold.'", "Measure both with a thermometer — they're identical! But your hand says otherwise because of conduction speed.")
    ]
}

L04 = {
    "id": "G06-L04",
    "title": "The Rock That Remembers Everything",
    "subtitle": "How Earth's Rocks Tell the Story of Millions of Years",
    "ngss": "MS-ESS2-1, MS-ESS2-3",
    "ngss_desc": "Develop a model to describe the cycling of Earth's materials and the flow of energy that drives this process. Analyze and interpret data on the distribution of fossils and rocks, continental shapes, and seafloor structures to provide evidence of the past plate motions.",
    "big_question": "How can a rock on top of a mountain contain seashells from the bottom of an ancient ocean?",
    "objectives": [
        "Explain how heat, pressure, weathering, and time transform one rock type into another",
        "Model how the rock cycle connects igneous, sedimentary, and metamorphic rocks",
        "Interpret fossil evidence in sedimentary rock to reconstruct past environments",
        "Connect the rock cycle to plate tectonics and large-scale Earth processes"
    ],
    "vocabulary": [
        ("Rock Cycle", "The continuous process by which rocks are created, broken down, and reformed into different types"),
        ("Sedimentary Rock", "Rock formed from layers of compressed sediment, often containing fossils"),
        ("Metamorphic Rock", "Rock that has been transformed by extreme heat and pressure without melting"),
        ("Fossil", "Preserved remains or traces of ancient organisms found in sedimentary rock layers")
    ],
    "components": [
        ("Heat & Pressure", "The thermal energy and compression forces from Earth's interior that transform rocks", True),
        ("Weathering Rate", "How quickly wind, water, ice, and chemicals break rocks into smaller pieces", True),
        ("Sediment Layers", "The accumulation of broken rock particles, minerals, and organic material over time", False),
        ("Time", "The immense timescale over which geological processes operate — millions to billions of years", True)
    ],
    "think_about_it": "When heat and pressure increase, what type of rock forms? When weathering rate increases, what happens to sediment layers?",
    "scenarios": [
        ("Mountain Builder", "Set Heat & Pressure to maximum and observe rock transformation over millions of years"),
        ("Erosion Machine", "Lock Weathering Rate to maximum and watch sediment layers build up"),
        ("Deep Time", "Set all processes to moderate and observe the full rock cycle over 500 million years")
    ],
    "sim_scenarios": [
        ("Mountain Builder", "Maximum heat and pressure, low weathering", "What type of rock do you predict will form under extreme heat and pressure?"),
        ("Erosion Machine", "Maximum weathering, moderate other factors", "What happens to sediment layers when weathering is extremely high?"),
        ("Deep Time", "All moderate, 500 million year timeframe", "Can a single rock go through the entire rock cycle? What would that look like?")
    ],
    "discoveries": [
        "The same atoms that make up a rock today have been recycled through the rock cycle for billions of years",
        "Extreme heat and pressure transform sedimentary rock into metamorphic rock without melting it",
        "Fossils are only preserved in sedimentary rock because igneous and metamorphic processes destroy them",
        "The rock cycle is powered by TWO energy sources: Earth's internal heat and the Sun's energy (driving weathering)"
    ],
    "answer": "Seashells end up on mountaintops because sedimentary rock forms on ocean floors where shells accumulate in layers. Over millions of years, tectonic forces push that seafloor upward, and heat and pressure can transform it. The rock 'remembers' its ocean origins through the fossils trapped inside — a record of millions of years of Earth's history!",
    "stem_title": "Design a Geological Time Capsule",
    "stem_mission": "Design a system to preserve a message for 1 million years using your understanding of how rocks form, weather, and preserve materials.",
    "stem_scenario": "A science foundation wants to create a time capsule that will survive for 1 million years. Your geology team must use evidence from the rock cycle model to recommend the best materials, location, and protection strategy.",
    "stem_questions": [
        "Which rock type is most likely to preserve your message for a million years?",
        "What location would protect your time capsule from weathering and tectonic destruction?",
        "How does understanding the rock cycle help you predict what might happen to your capsule?"
    ],
    "stem_design_qs": [
        "What material will you encase your message in — and what rock properties make it durable?",
        "Where on Earth would you place your time capsule to minimize weathering and tectonic activity?",
        "How will you protect against heat, pressure, water, and biological degradation?",
        "How will future discoverers know what they've found and how to read your message?"
    ],
    "career": "Geologists and Paleontologists study rocks, fossils, and Earth's history to find natural resources, predict hazards, and understand our planet's past. They earn $60,000–$115,000/year.",
    "images": {
        "cover": ("cover-rocks.png", "A stunning close-up photograph of sedimentary rock layers showing visible fossil shells embedded in limestone, warm golden light highlighting the textures and layers"),
        "landscape": ("landscape-rocks.png", "6th grade students examining rock samples with hand lenses and magnifying glasses outdoors, collecting specimens, sunny day in a rocky natural area"),
        "modeling": ("modeling-rocks.png", "A diverse group of 6th grade students working on laptops building a rock cycle model, classroom with rock specimens and geology posters on walls"),
        "discussion": ("discussion-rocks.png", "A teacher showing fossil specimens to fascinated 6th grade students, students touching and examining rocks, bright classroom with rock collection displayed"),
        "stem": ("stem-time-capsule.png", "6th grade students designing and building geological time capsules using various materials at their desks, creative engineering project, collaborative group work")
    },
    "pre_assessment": [
        "Where do you think rocks come from? Have they always existed?",
        "How do you think a seashell could end up inside a rock on a mountain?",
        "Do you think a rock can change into a different kind of rock? How?",
        "Draw what you think happens to a rock over millions of years."
    ],
    "extend_components": [
        ("Volcanic Activity", "Eruptions produce new igneous rock from cooled magma and lava"),
        ("Water Erosion", "Moving water is the most powerful weathering agent, carving canyons and transporting sediment"),
        ("Biological Weathering", "Plant roots, burrowing animals, and microorganisms break down rock chemically and physically")
    ],
    "reflections": [
        "Why are fossils only found in sedimentary rock and not in igneous or metamorphic rock?",
        "If the atoms in a rock have been recycled for billions of years, what were they part of before?",
        "How is the rock cycle connected to plate tectonics?",
        "Why is the rock cycle called a 'cycle' if it doesn't always happen in the same order?",
        "How does studying rocks help us understand what Earth looked like millions of years ago?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how heat, pressure, weathering, and time interact to cycle Earth's materials through different rock types."),
        ("Disciplinary Core Idea", "ESS2.A Earth Materials and Systems", "All Earth processes are the result of energy flowing and matter cycling within and among the planet's systems, including the rock cycle."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how rocks appear stable but are constantly being transformed by slow processes that operate over immense timescales.")
    ],
    "cast_items": [
        "Describe how energy and matter cycle through the rock cycle",
        "Use fossil evidence to reconstruct past environments",
        "Explain how different rock types form through specific processes"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A geologist finds a metamorphic rock that contains distorted fossil shells. Which sequence of events best explains how this rock formed?"),
        ("Constructed Response:", "Explain how a grain of sand on a beach could eventually become part of a metamorphic rock on a mountain. Describe each step of the journey using rock cycle processes.")
    ],
    "background_intro": "The rock cycle is one of Earth's most fundamental processes, recycling materials over billions of years. Every rock on Earth has a story to tell about the conditions under which it formed.",
    "background_sections": [
        ("Three Rock Types", "Igneous rocks form when magma or lava cools and solidifies (granite, basalt, obsidian). Sedimentary rocks form when layers of sediment are compressed and cemented together (limestone, sandstone, shale). Metamorphic rocks form when existing rocks are transformed by heat and pressure without melting (marble from limestone, slate from shale)."),
        ("The Rock Cycle Process", "Rocks continuously transform from one type to another. Igneous rock weathers into sediment, which becomes sedimentary rock. Heat and pressure transform sedimentary rock into metamorphic rock. Melting creates magma that cools into new igneous rock. Any rock type can become any other type — the cycle doesn't follow a fixed order."),
        ("Fossils as Evidence", "Fossils form when organisms die and are quickly buried by sediment before they decompose. Over time, minerals replace the organic material, preserving the shape. Fossils are only found in sedimentary rock because the heat and pressure that create metamorphic and igneous rocks would destroy them. Fossil distribution provides evidence for continental drift and past environments."),
        ("Deep Time", "The rock cycle operates on timescales that are difficult to comprehend. The oldest rocks on Earth are about 4 billion years old. A single grain of sand might have been part of a mountain, a beach, a seafloor, and a mountain again over hundreds of millions of years. Understanding deep time is essential for understanding geological processes.")
    ],
    "lever_L": "Students identify heat & pressure, weathering rate, sediment layers, and time as the key drivers of the rock cycle.",
    "lever_E": "Students determine that heat & pressure positively drive metamorphism, weathering positively increases sediment production, and time is essential for all transformations.",
    "lever_V": "Students build a model showing how energy inputs and surface processes cycle materials through igneous, sedimentary, and metamorphic stages.",
    "lever_Ev": "Students run mountain-building and erosion scenarios to observe how different processes dominate at different stages of the cycle.",
    "lever_R": "Students add volcanic activity or biological weathering to explore additional pathways in the rock cycle.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with fossil-embedded rock imagery", "say": "I'm holding a rock that's older than the dinosaurs. And it has a story to tell.", "do": "Pass around fossil specimens or high-quality images. Let students examine them.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're reading the autobiography that rocks write — over millions of years.", "do": "Have students read objectives. Pre-teach 'sedimentary,' 'metamorphic,' and 'fossil.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Seashells on a mountaintop?", "say": "How did ocean creatures end up trapped in rocks on the top of Mount Everest?", "do": "Show image of marine fossils found at high elevations. Capture student hypotheses.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the forces that recycle every rock on Earth — over and over for billions of years.", "do": "Preview LEVER steps. Connect to prior plate tectonics knowledge from L02.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for rock cycle model", "say": "What forces shape rocks? Which come from inside Earth and which from the surface?", "do": "Guide sorting. Discuss how heat comes from inside Earth while weathering comes from the surface.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More heat and pressure creates metamorphic rock. More weathering creates more sediment.", "do": "Help students trace the cycle: weathering → sediment → compression → metamorphism → melting → igneous.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's build a mountain and then weather it away — over a few hundred million years!", "do": "Students predict outcomes before running. Compare mountain-building vs. erosion scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Every rock has been recycled for billions of years. The atoms in that rock might have been in a dinosaur!", "do": "Connect to the concept of deep time. Discuss why fossils only survive in sedimentary rock.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Geological time capsule design", "say": "Can you design something that lasts a MILLION years? Use your rock cycle knowledge!", "do": "Distribute materials. Groups design time capsules using geological principles.", "time": "12 min"}
    ],
    "sort_reasoning": "Heat & Pressure, Weathering Rate, and Time are external because they are environmental forces acting ON the rock system — heat comes from Earth's interior, weathering comes from surface conditions, and time is an independent variable. Sediment Layers are internal because they accumulate as a RESULT of weathering and represent the system's response to external forces.",
    "relationships": [
        ("Heat & Pressure to Rock Transformation", "POSITIVE (+)", "More heat and pressure drives rock transformation — turning sedimentary into metamorphic rock, or melting rock entirely into magma that becomes igneous rock."),
        ("Weathering Rate to Sediment Layers", "POSITIVE (+)", "Faster weathering breaks more rock into smaller pieces, producing more sediment that accumulates in layers over time."),
        ("Sediment Layers to Fossil Preservation", "POSITIVE (+)", "Thicker, faster-accumulating sediment layers bury organisms more quickly, increasing the chance of fossil preservation before decomposition.")
    ],
    "sim_answers": [
        ("Mountain Builder Scenario", "With maximum Heat & Pressure, existing rocks are rapidly transformed into metamorphic rock. If heat is high enough, rocks melt into magma and become igneous rock when they cool. The model shows that Earth's internal energy drives the 'deep' part of the rock cycle."),
        ("Erosion Machine Scenario", "With maximum Weathering Rate, existing rocks break down quickly into sediment. Sediment Layers build up rapidly, compressing lower layers into sedimentary rock. The model shows that surface processes (powered by the Sun) drive the 'surface' part of the rock cycle.")
    ],
    "reflection_exemplars": [
        ("Why are fossils only in sedimentary rock?", "Fossils form when organisms are buried by sediment before they decompose. The gentle process of sediment compression preserves their shapes. Igneous rock forms from molten magma (1000°C+), which would vaporize any organism. Metamorphic rock forms under extreme heat and pressure that crushes and distorts any fossils present. Only sedimentary rock's gentle formation process can preserve biological evidence."),
        ("How can the same atoms be in different rocks?", "The atoms in a rock are not permanently locked in. When a rock weathers, its atoms scatter as sediment. When sediment is compressed, those atoms become part of a new sedimentary rock. If that rock is heated, it transforms into metamorphic rock — same atoms, new arrangement. If melted and cooled, they become igneous rock. The atoms cycle endlessly through different rock types over billions of years.")
    ],
    "stem_intro": "Present the challenge: The Long Now Foundation wants to preserve a message for 1 million years. Your geological engineering team must recommend materials, locations, and protection strategies based on your understanding of how rocks form and weather.",
    "stem_concepts": [
        ("Mineral Stability", "Some minerals are extremely stable and resist weathering for millions of years. Quartz, for example, barely weathers, which is why sand (mostly quartz) accumulates on beaches."),
        ("Erosion Rates", "Different environments weather rocks at vastly different rates. Desert environments with little water weather rock very slowly, while coastal environments can wear away cliffs in decades."),
        ("Geological Stability Zones", "Some areas on Earth (cratons) have been geologically stable for billions of years. These ancient continental cores experience minimal tectonic activity and are ideal for long-term preservation.")
    ],
    "stem_eval": [
        ("Expert (4)", "Time capsule design uses rock cycle evidence, selects appropriate materials based on mineral stability, and considers multiple weathering threats"),
        ("Proficient (3)", "Design references rock cycle concepts and addresses at least two weathering threats"),
        ("Developing (2)", "Design mentions durability but doesn't connect to rock cycle processes"),
        ("Beginning (1)", "Design is incomplete or doesn't demonstrate understanding of geological preservation")
    ],
    "support": [
        "Provide a labeled rock cycle diagram with arrows showing all possible pathways between rock types",
        "Use candy or crayon shavings to physically demonstrate sedimentary layering, compression, and metamorphism",
        "Sentence frames: 'When weathering rate increases, sediment layers __ because __'"
    ],
    "extensions": [
        "Research how scientists date rocks using radioactive isotopes and explain the concept of half-life",
        "Investigate a local geological formation and explain its history using rock cycle concepts",
        "Compare the rock cycle to the water cycle — what similarities and differences exist?"
    ],
    "cross_curr": [
        ("Math", "Calculate how long it would take a mountain to erode completely given a specific weathering rate in mm/year"),
        ("ELA", "Write a first-person narrative from the perspective of an atom traveling through the entire rock cycle"),
        ("History", "Research how ancient civilizations used different rock types for construction and why some buildings survived millennia")
    ],
    "misconceptions": [
        ("Rocks don't change", "Rocks are constantly changing, just extremely slowly. Over millions of years, mountains erode to plains, seafloors rise to mountaintops, and rocks transform from one type to another. The rock you hold today was once something completely different.", "Compare time-lapse erosion images. Show before/after photos of geological formations."),
        ("The rock cycle goes in one direction", "Unlike a simple circle, rocks can transform from any type to any other type. Sedimentary rock doesn't HAVE to become metamorphic before becoming igneous — it can melt directly. The 'cycle' is more like a web of possible pathways.", "Draw the rock cycle as a triangle with arrows going in every direction, not just around the outside."),
        ("Fossils are just rocks shaped like animals", "Fossils are actual preserved remains where mineral replacement has occurred atom by atom, preserving original structures at microscopic detail. Some fossils even preserve cellular structures, original proteins, and in rare cases, soft tissues.", "Show microscope images of fossil bone with preserved cell structures visible.")
    ]
}

L05 = {
    "id": "G06-L05",
    "title": "Slime Is Serious Science",
    "subtitle": "How Molecules Determine the Properties of Everything You Touch",
    "ngss": "MS-PS1-1, MS-PS1-2",
    "ngss_desc": "Develop models to describe the atomic composition of simple molecules and extended structures. Analyze and interpret data on the properties of substances before and after the substances interact to determine if a chemical reaction has occurred.",
    "big_question": "Why does slime act like both a liquid AND a solid at the same time?",
    "objectives": [
        "Explain how the size and arrangement of molecules determine a substance's physical properties",
        "Model how molecule size, bond strength, temperature, and concentration affect material behavior",
        "Distinguish between physical and chemical changes using molecular-level evidence",
        "Connect molecular structure to the properties of everyday materials"
    ],
    "vocabulary": [
        ("Molecule", "Two or more atoms bonded together — the smallest unit of a chemical compound"),
        ("Polymer", "A long chain molecule made of repeating smaller units linked together, like a molecular train"),
        ("Viscosity", "A measure of how thick or resistant to flow a fluid is — honey has high viscosity"),
        ("Non-Newtonian Fluid", "A substance whose viscosity changes when force is applied — slime, ketchup, quicksand")
    ],
    "components": [
        ("Molecule Size", "The length and mass of the polymer chains that make up the substance", False),
        ("Bond Strength", "How strongly the molecules are connected to each other through chemical bonds", False),
        ("Temperature", "The thermal energy affecting how fast molecules vibrate and move", True),
        ("Concentration", "The ratio of polymer molecules to solvent (water) in the mixture", False)
    ],
    "think_about_it": "When you increase concentration (add more glue to the slime), what happens to the viscosity? What about when you increase temperature?",
    "scenarios": [
        ("Liquid Slime", "Set Concentration to 20% and Bond Strength to low — observe how it flows"),
        ("Perfect Slime", "Set Concentration to 60% and Bond Strength to moderate — observe the non-Newtonian behavior"),
        ("Solid Slime", "Lock Concentration to 90% and Bond Strength to maximum — can it still flow?")
    ],
    "sim_scenarios": [
        ("Liquid Slime", "Low concentration, weak bonds", "What do you predict the slime will act like — more liquid or more solid?"),
        ("Perfect Slime", "Moderate concentration and bond strength", "Why do you think 'perfect' slime can be both liquid and solid?"),
        ("Solid Slime", "Maximum concentration and bond strength", "At what point does slime stop behaving like a fluid entirely?")
    ],
    "discoveries": [
        "Longer polymer chains get tangled together, making the substance thicker and more viscous",
        "Stronger bonds between molecules mean the substance resists flowing — it acts more solid",
        "Temperature increases molecular movement, loosening bonds and making substances flow more easily",
        "Slime is non-Newtonian because its polymer chains tangle when squeezed but slide apart when relaxed"
    ],
    "answer": "Slime acts like both a liquid and solid because it's made of long polymer chains that can slide past each other slowly (liquid behavior) but tangle and lock up when force is applied quickly (solid behavior). The molecule size, bond strength, and concentration determine exactly where the substance falls on the liquid-to-solid spectrum!",
    "stem_title": "Design the Perfect Slime Formula",
    "stem_mission": "Engineer a slime with specific target properties (stretch distance, bounce height, flow rate) by adjusting your molecular recipe based on model evidence.",
    "stem_scenario": "A toy company needs a new slime product. They want three versions: 'Super Stretch' (maximum elongation), 'Bouncy Blob' (maximum bounce), and 'Slow Flow' (slowest pour). Your chemistry team must design formulas for all three using your molecular model.",
    "stem_questions": [
        "How does changing polymer chain length affect stretchiness vs. bounciness?",
        "What concentration and bond strength produces the slowest flow rate?",
        "How will you test and measure each property to prove your formula works?"
    ],
    "stem_design_qs": [
        "What ratio of glue to activator will you use for each slime type?",
        "How will you measure stretch distance, bounce height, and flow rate consistently?",
        "What happens if you change the temperature of your slime? Does it help or hurt?",
        "How will you record and compare your results for the three formulas?"
    ],
    "career": "Materials Scientists and Polymer Chemists design new materials with specific properties for products like sneakers, phone cases, medical devices, and more. They earn $70,000–$130,000/year.",
    "images": {
        "cover": ("cover-slime.png", "A dramatic close-up of colorful stretchy slime being pulled and stretched by hands, showing its unique non-Newtonian fluid properties, vibrant colors, studio lighting"),
        "landscape": ("landscape-slime.png", "6th grade students making slime at lab tables in a science classroom, measuring ingredients carefully, colorful materials, excited expressions"),
        "modeling": ("modeling-molecules.png", "A diverse group of 6th grade students working on laptops building a molecular model, classroom with chemistry posters and molecular model kits on shelves"),
        "discussion": ("discussion-slime.png", "A teacher demonstrating non-Newtonian fluid properties to amazed 6th grade students, dropping a ball onto a tray of cornstarch mixture"),
        "stem": ("stem-slime-lab.png", "6th grade students testing different slime formulas, measuring stretch and bounce, recording data on clipboards, organized lab setup")
    },
    "pre_assessment": [
        "Is slime a solid, liquid, or gas? Explain your reasoning.",
        "What do you think molecules look like inside slime compared to inside water?",
        "Why do you think some liquids (like honey) are thick while others (like water) are thin?",
        "Draw what you think is happening at the molecular level when you stretch slime."
    ],
    "extend_components": [
        ("Cross-Linking Density", "The number of chemical bridges between polymer chains — more cross-links make the substance stiffer"),
        ("Solvent Type", "Water vs. other liquids — different solvents interact differently with polymer chains"),
        ("Additive Particles", "Small particles added to the mixture can change its texture, color, and flow properties")
    ],
    "reflections": [
        "Why does slime stretch slowly but break when you pull it quickly?",
        "How is making slime a chemical change, not just a physical change?",
        "If you could design a molecule for the perfect bouncy ball, what would it look like?",
        "Why does warming up slime make it runnier? What's happening to the molecules?",
        "How does understanding molecular structure help engineers design new materials?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how molecular size, bond strength, temperature, and concentration determine the physical properties of a substance."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Substances are made from different types of atoms, which combine with one another in various ways. Atoms form molecules that range in size from simple to complex."),
        ("Crosscutting Concept", "Structure and Function", "Students discover that the STRUCTURE of molecules (their size, arrangement, and bonds) directly determines the FUNCTION (physical properties) of the substance.")
    ],
    "cast_items": [
        "Describe how the arrangement of molecules determines a substance's properties",
        "Distinguish between physical and chemical changes based on molecular-level evidence",
        "Model how changing molecular structure changes material behavior"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two liquids look identical but one is water (viscosity: 1 cP) and one is glycerol (viscosity: 1500 cP). What molecular difference best explains why glycerol is much thicker?"),
        ("Constructed Response:", "Explain why slime can act like a solid when you hit it quickly but flows like a liquid when you let it sit. Use the concepts of polymer chains and molecular interaction in your answer.")
    ],
    "background_intro": "The study of how molecular structure determines material properties is at the heart of chemistry and materials science. Slime is the perfect entry point because it demonstrates that 'solid' and 'liquid' aren't always clear-cut categories.",
    "background_sections": [
        ("Polymers Everywhere", "Polymers are long chain molecules made of repeating units (monomers). Natural polymers include DNA, proteins, cellulose (wood), and silk. Synthetic polymers include plastics, nylon, rubber, and silicone. The properties of a polymer depend on chain length, branching, and how chains interact with each other."),
        ("Non-Newtonian Fluids", "Most fluids (water, oil) have constant viscosity regardless of applied force. Non-Newtonian fluids change viscosity under stress. Slime is 'shear-thickening' — it gets MORE viscous under force. Ketchup is 'shear-thinning' — it gets LESS viscous under force (that's why you shake the bottle). These behaviors are determined by molecular structure."),
        ("Chemical vs. Physical Changes", "Making slime is a CHEMICAL change — the borax creates chemical cross-links between PVA (glue) polymer chains, forming a new substance with different properties. This is different from a physical change (like melting ice) where the molecular structure stays the same but the arrangement changes."),
        ("Real-World Applications", "Understanding polymer chemistry enables engineers to design bulletproof vests (Kevlar — aligned polymer chains), memory foam (temperature-responsive polymers), biodegradable plastics (polymers that bacteria can break down), and self-healing materials (polymers that can reconnect broken bonds).")
    ],
    "lever_L": "Students identify molecule size, bond strength, temperature, and concentration as the key components determining material properties.",
    "lever_E": "Students determine that larger molecules and stronger bonds increase viscosity (positive), while higher temperature decreases viscosity (negative).",
    "lever_V": "Students build a model showing how molecular-level interactions produce observable material properties like viscosity and elasticity.",
    "lever_Ev": "Students run liquid vs. perfect vs. solid slime scenarios to observe how changing molecular variables affects physical behavior.",
    "lever_R": "Students add cross-linking density or solvent type to explore more complex material behaviors.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic slime imagery", "say": "Is slime a solid or a liquid? Trick question — it's actually BOTH.", "do": "Pull out a container of slime and demonstrate: it pours (liquid!) but bounces when dropped (solid!).", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're going to figure out WHY slime breaks the rules of matter.", "do": "Have students read objectives. Pre-teach 'polymer,' 'viscosity,' and 'non-Newtonian fluid.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How can something be liquid AND solid?", "say": "Everything you learned about the three states of matter? Slime doesn't care about those rules.", "do": "Quick demo: Slowly pour slime (liquid behavior), then punch it (solid behavior). Capture reactions.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a molecular model to crack the slime mystery.", "do": "Preview LEVER steps. Emphasize that the answer is at the MOLECULAR level.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for molecular model", "say": "What variables at the molecular level affect how slime behaves?", "do": "Guide sorting. Explain that temperature is external while molecule properties are internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Bigger molecules = thicker substance. But higher temperature = more flow. These work against each other.", "do": "Demonstrate with cooked spaghetti (tangles = polymers) — short noodles slide easily, long ones tangle.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's dial in the perfect slime — and then make it too thick and too thin!", "do": "Students predict then run three scenarios. Graph and compare viscosity results.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "The secret is polymer chains! They tangle when hit, but slide when relaxed.", "do": "Connect to real-world non-Newtonian fluids: ketchup, quicksand, body armor.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Slime formula engineering challenge", "say": "You're now materials scientists. Engineer three different slimes with specific properties!", "do": "Distribute materials. Groups design formulas, test, and measure stretch/bounce/flow.", "time": "12 min"}
    ],
    "sort_reasoning": "Temperature is external because it comes from the environment and affects the substance from outside. Molecule Size, Bond Strength, and Concentration are internal because they are properties of the substance itself that can be engineered during creation.",
    "relationships": [
        ("Molecule Size to Viscosity", "POSITIVE (+)", "Larger, longer polymer chains get tangled together more easily, making the substance thicker and more resistant to flow."),
        ("Bond Strength to Viscosity", "POSITIVE (+)", "Stronger bonds between molecules hold them together more tightly, resisting flow and making the substance behave more like a solid."),
        ("Temperature to Viscosity", "NEGATIVE (-)", "Higher temperature gives molecules more kinetic energy, causing them to vibrate and move faster. This loosens bonds and reduces tangling, making the substance flow more easily.")
    ],
    "sim_answers": [
        ("Liquid vs. Perfect Slime", "At 20% concentration with weak bonds, the substance flows freely like a liquid — polymer chains are sparse and barely interact. At 60% concentration with moderate bonds, the substance shows non-Newtonian behavior — it flows slowly but resists sudden force. The model shows how concentration and bond strength create the sweet spot."),
        ("Temperature Effect", "When temperature increases on perfect slime, viscosity drops noticeably. The polymer chains gain kinetic energy and slide past each other more easily. This is why warm slime is runnier than cold slime — and why warming honey makes it flow faster.")
    ],
    "reflection_exemplars": [
        ("Why does slime stretch slowly but break when pulled fast?", "When pulled slowly, the polymer chains have time to untangle and slide past each other, allowing the slime to stretch. When pulled fast, the chains can't rearrange quickly enough — they lock up and snap rather than slide. It's like slowly pulling tangled headphones apart vs. yanking them — slow works, fast breaks."),
        ("How is making slime a chemical change?", "When borax is added to glue, it creates chemical cross-links between the PVA polymer chains. These are new chemical bonds that didn't exist before — creating an entirely new substance with different properties. The cross-links are what make slime stretchy instead of just liquid glue. You can't reverse the process by just stirring — that's the signature of a chemical change.")
    ],
    "stem_intro": "Present the toy company scenario: They need three slime products with specific measurable properties. Your team must design formulas using evidence from the molecular model.",
    "stem_concepts": [
        ("Cross-Linking", "Chemical bridges between polymer chains that determine flexibility. Few cross-links = stretchy. Many cross-links = stiff. This is how rubber bands and bowling balls can both be made from polymers."),
        ("Viscoelasticity", "Materials that show both viscous (liquid) and elastic (solid) behavior. Slime is viscoelastic — it flows like a liquid over time but bounces like a solid when hit quickly."),
        ("Thixotropy", "Some non-Newtonian fluids become more liquid when stirred and more solid when still. Ketchup is thixotropic — that's why shaking the bottle helps it flow.")
    ],
    "stem_eval": [
        ("Expert (4)", "Three distinct formulas with measurable targets, uses model evidence to justify ratios, includes test data and comparisons"),
        ("Proficient (3)", "At least two formulas with model evidence, includes testing plan and measurements"),
        ("Developing (2)", "Formulas created but not clearly connected to molecular model evidence"),
        ("Beginning (1)", "Single formula without clear connection to molecular structure concepts")
    ],
    "support": [
        "Provide molecular model kits or drawings showing short vs. long polymer chains to visualize size differences",
        "Use spaghetti noodles of different lengths as a physical analogy for polymer chains tangling",
        "Sentence frames: 'When bond strength increases, the substance becomes more __ because the molecules __'"
    ],
    "extensions": [
        "Research how Kevlar's molecular structure makes it strong enough to stop bullets",
        "Investigate shape-memory polymers that can return to a preset shape when heated",
        "Design an experiment comparing the viscosity of different household fluids and explaining the molecular reasons"
    ],
    "cross_curr": [
        ("Math", "Graph the relationship between concentration and viscosity — is it linear, exponential, or something else?"),
        ("ELA", "Write a scientific procedure for making slime that someone else could follow to get the exact same results"),
        ("Art", "Design product packaging for your three slime formulas, including scientific explanations for consumers")
    ],
    "misconceptions": [
        ("Matter is always clearly solid, liquid, or gas", "Many real materials don't fit neatly into the three states. Non-Newtonian fluids, gels, plasmas, and amorphous solids (glass) blur the boundaries. The states of matter are useful categories but nature is more complex.", "Demo: Show slime behaving as solid AND liquid. Ask: Which state is it? The answer: it depends on how you interact with it."),
        ("Molecules don't move in solids", "Molecules are ALWAYS moving — in all states of matter. In solids, they vibrate in place. In liquids, they slide past each other. In gases, they fly freely. Temperature determines how much they move. Even at absolute zero, there is still some quantum vibration.", "Connect to temperature: Warming slime makes molecules move MORE, which is why it gets runnier."),
        ("Chemical changes can be easily reversed", "Chemical changes create new substances with new properties. Making slime creates chemical cross-links that can't be undone by stirring or cooling. This is different from physical changes (like ice melting) which are easily reversed. The key test: is a new substance formed?", "Compare: Can you un-bake a cake? Can you un-make slime? These are chemical changes. Can you re-freeze water? That's a physical change — easily reversed.")
    ]
}

L06 = {
    "id": "G06-L06",
    "title": "Your Body Is a City of Trillions",
    "subtitle": "How Your Organ Systems Work Together to Keep You Alive",
    "ngss": "MS-LS1-3",
    "ngss_desc": "Use argument supported by evidence for how the body is a system of interacting subsystems composed of groups of cells.",
    "big_question": "How does your body run a city more complex than any humans have ever built — 24/7, without you even thinking about it?",
    "objectives": [
        "Explain how organ systems are made of organs, which are made of tissues, which are made of cells",
        "Model how heart rate, blood oxygen, nutrient intake, and physical activity interact in the body system",
        "Describe how the circulatory, respiratory, digestive, and muscular systems depend on each other",
        "Use evidence to argue that the body is a system of interacting subsystems"
    ],
    "vocabulary": [
        ("Organ System", "A group of organs that work together to perform a major body function"),
        ("Homeostasis", "The body's ability to maintain stable internal conditions even when the outside environment changes"),
        ("Circulatory System", "The heart, blood vessels, and blood that transport oxygen, nutrients, and waste throughout the body"),
        ("Cellular Respiration", "The process cells use to convert glucose and oxygen into energy (ATP), carbon dioxide, and water")
    ],
    "components": [
        ("Heart Rate", "How many times the heart beats per minute, controlling blood flow speed throughout the body", False),
        ("Blood Oxygen Level", "The percentage of hemoglobin in red blood cells carrying oxygen to tissues", False),
        ("Nutrient Intake", "The amount of glucose and other fuel molecules available from digested food", True),
        ("Physical Activity", "The intensity of muscular work being performed, increasing energy demand", True)
    ],
    "think_about_it": "When physical activity increases, what has to happen to heart rate and blood oxygen? Can your body keep exercising if nutrient intake is zero?",
    "scenarios": [
        ("Resting State", "Set Physical Activity to low and observe how all systems maintain homeostasis"),
        ("Sprint Mode", "Lock Physical Activity to maximum and observe how the body responds"),
        ("Skipping Lunch", "Set Nutrient Intake to 10% during moderate activity — what fails first?")
    ],
    "sim_scenarios": [
        ("Resting State", "Low physical activity, normal nutrients and oxygen", "What do you predict heart rate will be during rest? Why?"),
        ("Sprint Mode", "Maximum physical activity", "What do you predict happens to blood oxygen when you sprint? Why does heart rate increase?"),
        ("Skipping Lunch", "Low nutrients, moderate activity", "What happens to your body's performance when fuel runs low?")
    ],
    "discoveries": [
        "Heart rate increases during exercise to deliver more oxygen and nutrients to working muscles",
        "Blood oxygen drops during intense activity because muscles consume oxygen faster than lungs can replace it",
        "Without adequate nutrients, the body can't produce enough energy for sustained physical activity",
        "All organ systems are interconnected — when one system is stressed, others must compensate"
    ],
    "answer": "Your body works like a city because every organ system has a specialized job, and they ALL depend on each other. Your digestive system provides fuel, your respiratory system provides oxygen, your circulatory system delivers both to every cell, and your muscular system creates movement. Remove any one system and the whole city shuts down — just like a real city without power, water, or roads!",
    "stem_title": "Design an Athletic Performance Plan",
    "stem_mission": "Design an evidence-based training and nutrition plan for a student athlete that optimizes how their body systems work together during competition.",
    "stem_scenario": "A middle school track team needs help. Their coach wants your biomedical team to design a plan that helps runners perform their best in the 400-meter race. Use your body systems model to explain your recommendations.",
    "stem_questions": [
        "Based on your model, what happens to body systems during a 60-second sprint?",
        "What nutrients should the athlete eat before a race, and when should they eat them?",
        "How should training prepare the body's systems to handle the stress of competition?"
    ],
    "stem_design_qs": [
        "What foods will provide the right type and amount of energy for a sprint?",
        "How should the athlete warm up to prepare their circulatory and respiratory systems?",
        "What is the ideal heart rate zone for peak performance vs. risk of exhaustion?",
        "How will you measure whether your plan actually improves performance?"
    ],
    "career": "Exercise Physiologists and Sports Medicine Specialists study how the body responds to physical activity and design training programs for athletes and patients. They earn $55,000–$100,000/year.",
    "images": {
        "cover": ("cover-body-systems.png", "A dramatic artistic visualization of the human body showing the circulatory system with glowing blood vessels, organs visible, scientific medical illustration style, dark background with luminous anatomy"),
        "landscape": ("landscape-body.png", "6th grade students checking their pulse rates after exercise in a gym or science classroom, using fitness trackers and stopwatches, active and engaged"),
        "modeling": ("modeling-body.png", "A diverse group of 6th grade students working on laptops building a body systems model, classroom with human anatomy posters and a skeleton model"),
        "discussion": ("discussion-body.png", "A teacher using an anatomical model torso to show organ systems to engaged 6th grade students, students pointing and asking questions"),
        "stem": ("stem-fitness-plan.png", "6th grade students creating athletic performance plans on poster boards, analyzing heart rate data, charts and graphs visible, collaborative team work")
    },
    "pre_assessment": [
        "What happens to your breathing and heartbeat when you run?",
        "Why do you need to eat food? What does your body do with it?",
        "How does the oxygen you breathe get to your muscles?",
        "Draw the path food takes through your body from mouth to muscle."
    ],
    "extend_components": [
        ("Body Temperature", "Internal temperature rises during exercise; the body must cool itself through sweating and blood flow to skin"),
        ("Lactic Acid Buildup", "During intense activity, muscles produce lactic acid faster than the body can clear it, causing fatigue and burning"),
        ("Hydration Level", "Water is essential for blood volume, sweating, and chemical reactions — dehydration degrades all body systems")
    ],
    "reflections": [
        "Why does your heart beat faster when you exercise? What problem is it solving?",
        "What would happen to your muscles if your circulatory system stopped working?",
        "How is your body like a city? Give at least three specific comparisons.",
        "Why do athletes need to eat differently than people who sit at desks all day?",
        "How does homeostasis keep your body working even when conditions change?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how heart rate, blood oxygen, nutrient intake, and physical activity interact as interacting body subsystems."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "In multicellular organisms, the body is a system of multiple interacting subsystems. These subsystems are groups of cells that work together to form tissues and organs."),
        ("Crosscutting Concept", "Systems and System Models", "Students use the concept of interacting systems to understand how changes in one body system (e.g., increased physical activity) cascade through other systems (increased heart rate, breathing rate, energy demand).")
    ],
    "cast_items": [
        "Argue that the body is a system of interacting subsystems using evidence",
        "Explain how organ systems work together to maintain homeostasis",
        "Describe the hierarchical organization from cells to tissues to organs to organ systems"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During intense exercise, a student's heart rate increases from 70 bpm to 160 bpm. Which best explains WHY the circulatory system responds this way?"),
        ("Constructed Response:", "A student eats a banana before running a race. Trace the journey of the banana's energy from digestion to muscle contraction, identifying at least three organ systems involved and how they interact.")
    ],
    "background_intro": "The human body is an extraordinary system of interacting subsystems — approximately 11 organ systems working in concert to maintain life. Understanding these interactions is fundamental to health science and medicine.",
    "background_sections": [
        ("Levels of Organization", "The body is organized hierarchically: atoms → molecules → cells → tissues → organs → organ systems → organism. Each level has emergent properties that arise from the interactions of its components. A heart cell can beat on its own, but only the whole heart can pump blood effectively."),
        ("The Big Four Systems", "The four systems most relevant to exercise physiology are: Circulatory (heart, blood, vessels — transports everything), Respiratory (lungs, airways — gas exchange), Digestive (stomach, intestines — nutrient extraction), and Muscular (muscles — movement and heat production). During exercise, all four must increase their output simultaneously."),
        ("Exercise Response", "During exercise, muscles demand up to 20x more oxygen and glucose than at rest. The heart rate increases from ~70 to 180+ bpm. Breathing rate jumps from 12 to 40+ breaths/minute. Blood flow is redirected from digestive organs to muscles. These coordinated responses demonstrate how body systems communicate and cooperate."),
        ("Homeostasis", "Homeostasis is the body's ability to maintain stable internal conditions (temperature, blood sugar, pH, oxygen levels) despite changing external conditions. When you exercise in the heat, your body simultaneously increases heart rate (to feed muscles), produces sweat (to cool down), and adjusts breathing (to maintain oxygen). This multi-system coordination is homeostasis in action.")
    ],
    "lever_L": "Students identify heart rate, blood oxygen level, nutrient intake, and physical activity as the key interacting components of the body system.",
    "lever_E": "Students determine that physical activity positively drives heart rate (compensation response) while negatively affecting blood oxygen (increased consumption), and that nutrient intake positively supports all body functions.",
    "lever_V": "Students build a model showing how the body's subsystems interact to maintain function during different activity levels.",
    "lever_Ev": "Students run resting, sprinting, and low-fuel scenarios to observe how the body compensates — and what happens when it can't.",
    "lever_R": "Students add body temperature, lactic acid, or hydration to explore more complex physiological responses.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with glowing body systems imagery", "say": "Right now, your body is running a city of 37 trillion workers — and you're not even thinking about it.", "do": "Have students feel their pulse. Count heartbeats for 15 seconds and multiply by 4.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're going inside your body to see how four major systems keep you alive.", "do": "Have students read objectives. Pre-teach 'homeostasis' and 'organ system.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does your body run itself?", "say": "Your body runs 24/7 for your entire life — no breaks, no software updates, no off switch.", "do": "Think-pair-share: What happens if your heart takes a 5-minute break? What about your lungs?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how your body systems talk to each other — especially during exercise.", "do": "Preview LEVER steps. Tell students they'll be testing their OWN heart rate data.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for body systems model", "say": "What variables does your body need to track? Which can you control and which does your body control automatically?", "do": "Guide sorting. Explain that nutrient intake and activity level are external choices, while heart rate and blood oxygen are internal responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "When you sprint, your heart goes UP and your blood oxygen goes DOWN. These are connected!", "do": "Have students do 30 seconds of jumping jacks and immediately retake pulse. Compare to resting rate.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's see what happens when you sprint vs. rest vs. skip lunch!", "do": "Students predict, then run simulations. Compare to their own heart rate data from earlier.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Your body is the most sophisticated system on Earth — every part depends on every other part.", "do": "Lead discussion: What would happen to muscles if the circulatory system failed? What about if lungs failed?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Athletic performance plan design", "say": "You're now sports scientists. Design a plan to help a runner perform their best!", "do": "Distribute materials. Groups create evidence-based training and nutrition plans.", "time": "12 min"}
    ],
    "sort_reasoning": "Nutrient Intake and Physical Activity are external because they are controlled by the person's choices — what they eat and how hard they exercise. Heart Rate and Blood Oxygen Level are internal because they are automatic responses that the body adjusts in reaction to those external inputs.",
    "relationships": [
        ("Physical Activity to Heart Rate", "POSITIVE (+)", "Increased physical activity demands more oxygen and nutrients at muscle cells. The heart responds by beating faster to increase blood flow and delivery."),
        ("Physical Activity to Blood Oxygen", "NEGATIVE (-)", "Intense activity consumes oxygen faster than the lungs can replace it, causing blood oxygen levels to temporarily drop during vigorous exercise."),
        ("Nutrient Intake to Physical Performance", "POSITIVE (+)", "More available nutrients (especially glucose) provide more fuel for cellular respiration in muscle cells, supporting sustained physical activity.")
    ],
    "sim_answers": [
        ("Sprint Mode Scenario", "When Physical Activity is locked at maximum, Heart Rate spikes dramatically (70 → 170+ bpm) as the circulatory system compensates. Blood Oxygen drops because muscles consume oxygen faster than lungs can resupply. The model shows how the body's systems work together under stress — and that there's a limit to compensation."),
        ("Skipping Lunch Scenario", "At 10% Nutrient Intake during moderate activity, performance degrades within minutes. Without glucose fuel, muscles can't sustain contraction. Heart rate may initially compensate but the body quickly runs out of stored energy. This models why athletes 'hit the wall' — their fuel supply is depleted.")
    ],
    "reflection_exemplars": [
        ("Why does heart rate increase during exercise?", "Muscles need oxygen and glucose to produce ATP (energy) through cellular respiration. When you exercise, muscles need up to 20x more fuel and oxygen than at rest. The heart beats faster to push more blood through the system, delivering more oxygen and nutrients per minute. It's like a city increasing bus service during rush hour — more demand requires more deliveries."),
        ("How is the body like a city?", "The circulatory system is like roads and delivery trucks (transporting supplies everywhere). The respiratory system is like air filtration (bringing in clean air, removing CO₂). The digestive system is like food processing plants (converting raw food into usable fuel). The muscular system is like the workforce (doing the physical jobs). The nervous system is like the communications network (coordinating everything). Remove any one system and the city collapses.")
    ],
    "stem_intro": "Present the athletic performance scenario: A middle school track team's coach needs science-based recommendations for nutrition, warm-up, and training strategies for the 400-meter race.",
    "stem_concepts": [
        ("VO₂ Max", "The maximum rate at which the body can consume oxygen during exercise. Higher VO₂ max = better endurance performance. Training increases VO₂ max by strengthening the heart and increasing blood vessel density in muscles."),
        ("Glycogen Loading", "The strategy of eating carbohydrate-rich meals before competition to maximize glycogen (stored glucose) in muscles and liver. This provides more fuel for intense activity."),
        ("Active Recovery", "Light movement after intense exercise helps clear lactic acid faster than complete rest. Walking after a sprint helps the circulatory system flush waste from muscles.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses nutrition, warm-up, and training with model evidence, explains multiple system interactions, includes measurable performance goals"),
        ("Proficient (3)", "Plan addresses at least two factors with model evidence and explains system interactions"),
        ("Developing (2)", "Plan mentions exercise and nutrition but doesn't connect recommendations to body systems model"),
        ("Beginning (1)", "Plan is incomplete or doesn't demonstrate understanding of body system interactions")
    ],
    "support": [
        "Provide a body systems diagram showing connections between circulatory, respiratory, digestive, and muscular systems",
        "Use the 'City Analogy' chart: organ system → city equivalent (heart=water pump, lungs=air system, etc.)",
        "Sentence frames: 'When physical activity increases, heart rate __ because muscles need __'"
    ],
    "extensions": [
        "Research how altitude training affects the circulatory system and blood oxygen capacity",
        "Investigate what happens to body systems during sleep — does the 'city' ever fully shut down?",
        "Compare the body systems of an elite athlete vs. an average person — what adaptations occur with training?"
    ],
    "cross_curr": [
        ("Math", "Graph heart rate data over time during rest, exercise, and recovery — calculate the rate of increase and decrease"),
        ("ELA", "Write a persuasive essay arguing that the digestive system is the MOST important body system, using evidence"),
        ("PE/Health", "Design a fitness assessment that tests circulatory, respiratory, and muscular system function")
    ],
    "misconceptions": [
        ("The heart creates blood", "The heart is a PUMP, not a factory. It pumps blood through blood vessels but doesn't create blood. New blood cells are made in bone marrow. The heart's job is transportation — moving blood where it needs to go, about 2,000 gallons per day.", "Ask: Does a water pump create water? No — it moves water. The heart moves blood the same way."),
        ("You breathe in oxygen and breathe out carbon dioxide", "Air is about 78% nitrogen, 21% oxygen, and 0.04% CO₂. When you exhale, the air is still 78% nitrogen and about 16% oxygen — you only absorb a fraction of the oxygen. You exhale more CO₂ (4%) than you inhale, but the change is smaller than most people think.", "Have students look at the actual composition of inhaled vs. exhaled air — the numbers are surprising."),
        ("Organs work independently", "No organ system works alone. The heart needs signals from the nervous system, oxygen from the respiratory system, and nutrients from the digestive system. Every organ depends on every other organ through the circulatory system's delivery network. Disease in one system cascades to others.", "Ask: What happens to muscles if the heart stops? What happens to the brain? Everything is connected.")
    ]
}

L07 = {
    "id": "G06-L07",
    "title": "The Invisible Plant Factory",
    "subtitle": "How Plants Build Themselves from Thin Air and Sunlight",
    "ngss": "MS-LS1-6",
    "ngss_desc": "Construct a scientific explanation based on evidence for the role of photosynthesis in the cycling of matter and flow of energy into and out of organisms.",
    "big_question": "If plants make their own food from sunlight and air, where does the MASS of a giant tree actually come from?",
    "objectives": [
        "Explain how plants convert light energy, water, and carbon dioxide into glucose and oxygen",
        "Model how sunlight intensity, water availability, CO₂ concentration, and chlorophyll affect photosynthesis rates",
        "Describe photosynthesis as a chemical reaction that transforms energy and matter",
        "Connect photosynthesis to the global carbon cycle and energy flow in ecosystems"
    ],
    "vocabulary": [
        ("Photosynthesis", "The process plants use to convert light energy, CO₂, and water into glucose (food) and oxygen"),
        ("Chlorophyll", "The green pigment in plant cells that captures light energy to power photosynthesis"),
        ("Glucose", "A sugar molecule (C₆H₁₂O₆) that stores chemical energy — the product of photosynthesis"),
        ("Carbon Dioxide (CO₂)", "A gas in the atmosphere that plants absorb and use as a carbon source for building molecules")
    ],
    "components": [
        ("Sunlight Intensity", "The amount of light energy reaching the plant's leaves from the Sun", True),
        ("Water Availability", "The amount of water accessible to the plant through its root system", True),
        ("CO₂ Concentration", "The amount of carbon dioxide in the air around the plant's leaves", True),
        ("Chlorophyll Amount", "The quantity of light-capturing pigment in the plant's leaves", False)
    ],
    "think_about_it": "When sunlight intensity increases, what happens to the rate of photosynthesis? What happens when CO₂ runs low — can the plant still make food?",
    "scenarios": [
        ("Perfect Day", "Set all inputs to moderate-high levels and observe glucose production"),
        ("Cloudy Week", "Lock Sunlight Intensity to 20% and observe how it affects the plant"),
        ("Drought Stress", "Set Water Availability to 10% while keeping other inputs normal")
    ],
    "sim_scenarios": [
        ("Perfect Day", "High sunlight, adequate water and CO₂", "How much glucose do you predict a plant can make in ideal conditions?"),
        ("Cloudy Week", "Lock Sunlight to 20%", "What do you predict happens to glucose production when sunlight is limited?"),
        ("Drought Stress", "Water at 10%, other inputs normal", "Why can't the plant keep making food even though it has sunlight and CO₂?")
    ],
    "discoveries": [
        "Plants need ALL THREE inputs (sunlight, water, CO₂) — removing any one stops photosynthesis completely",
        "Most of a tree's mass comes from CARBON DIOXIDE in the air, not from the soil",
        "Photosynthesis is the reverse of cellular respiration — they're balanced opposite reactions",
        "More chlorophyll allows a plant to capture more light energy, increasing photosynthesis rate up to a saturation point"
    ],
    "answer": "A giant tree's mass comes mostly from carbon dioxide in the AIR! During photosynthesis, plants pull CO₂ from the atmosphere and use light energy to rearrange the carbon atoms into glucose molecules. Those carbon atoms become the wood, bark, and leaves. A tree is literally built from air and sunlight — the soil mainly provides water and minerals!",
    "stem_title": "Design a Space Greenhouse",
    "stem_mission": "Design a greenhouse for a Mars colony that provides maximum food production by optimizing photosynthesis conditions in an environment with limited resources.",
    "stem_scenario": "NASA is planning a Mars colony and needs a self-sustaining greenhouse. Mars has 95% CO₂ atmosphere but only 43% of Earth's sunlight, limited water, and no soil. Your agricultural engineering team must design a greenhouse using your photosynthesis model evidence.",
    "stem_questions": [
        "How will you provide enough light for photosynthesis on Mars where sunlight is weaker?",
        "With 95% CO₂ on Mars, is carbon dioxide still a limiting factor? What IS the limiting factor?",
        "How will you recycle water and nutrients in a closed system?"
    ],
    "stem_design_qs": [
        "What artificial lighting system will supplement the weaker Martian sunlight?",
        "How will you supply and recycle water in a closed greenhouse system?",
        "Which crops will you grow to maximize calories per square meter?",
        "How does your greenhouse design address temperature, pressure, and radiation on Mars?"
    ],
    "career": "Botanists and Agricultural Engineers develop new crop varieties, design sustainable farming systems, and study how to grow food in extreme environments — including space. They earn $55,000–$110,000/year.",
    "images": {
        "cover": ("cover-photosynthesis.png", "A stunning macro photograph of sunlight streaming through green leaves, showing the detailed vein structure and cells, light creating a beautiful glowing effect, nature photography"),
        "landscape": ("landscape-plants.png", "6th grade students planting seeds and examining growing plants in a school greenhouse or classroom garden, measuring and recording data, green and bright"),
        "modeling": ("modeling-photosynthesis.png", "A diverse group of 6th grade students working on laptops building a photosynthesis model, classroom with potted plants, grow lights, and biology posters"),
        "discussion": ("discussion-plants.png", "A teacher leading a discussion about photosynthesis with 6th grade students, using a real plant and a diagram showing the photosynthesis equation on a smartboard"),
        "stem": ("stem-greenhouse.png", "6th grade students designing and building miniature greenhouse models with clear plastic, small plants, and LED grow lights, engineering project at lab tables")
    },
    "pre_assessment": [
        "Where do you think plants get their food? Do they eat like we do?",
        "If a tree weighs 10,000 pounds, where did all that weight come from?",
        "Why are most plants green? Does the color matter?",
        "Draw what you think happens inside a leaf when sunlight hits it."
    ],
    "extend_components": [
        ("Temperature", "Enzymes that drive photosynthesis work best at specific temperatures — too hot or cold and they stop functioning"),
        ("Soil Nutrients", "Minerals like nitrogen, phosphorus, and potassium from soil are needed for building proteins and DNA, not for photosynthesis directly"),
        ("Leaf Surface Area", "More leaf surface area captures more sunlight, but also loses more water through stomata")
    ],
    "reflections": [
        "Why is it surprising that most of a tree's mass comes from air instead of soil?",
        "How are photosynthesis and cellular respiration opposite processes?",
        "What would happen to Earth's oxygen supply if all plants died?",
        "Why do plants grow toward light? What advantage does this give them?",
        "How is a plant's leaf like a solar panel? How is it even better than a solar panel?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how sunlight, water, CO₂, and chlorophyll interact to drive photosynthesis and produce glucose."),
        ("Disciplinary Core Idea", "LS1.C Organization for Matter and Energy Flow in Organisms", "Plants use the energy from light to make sugars from carbon dioxide and water through photosynthesis, which releases oxygen. This is the entry point for energy and carbon into living systems."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students trace the flow of energy (sunlight → chemical energy in glucose) and matter (CO₂ + H₂O → C₆H₁₂O₆ + O₂) through the photosynthesis process.")
    ],
    "cast_items": [
        "Explain how photosynthesis converts light energy into chemical energy stored in glucose",
        "Describe the role of photosynthesis in the cycling of carbon through ecosystems",
        "Use evidence to explain where the mass of a growing plant comes from"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student grows two identical plants — one in sunlight and one in complete darkness. After 4 weeks, the plant in sunlight is thriving but the one in darkness has wilted. Which best explains this result?"),
        ("Constructed Response:", "A scientist weighs a potted tree seedling and its soil. After 5 years, the tree has gained 50 kg but the soil has only lost 0.5 kg. Explain where the other 49.5 kg of mass came from, using the process of photosynthesis.")
    ],
    "background_intro": "Photosynthesis is the most important chemical reaction on Earth. It converts solar energy into food energy, produces the oxygen we breathe, and is the foundation of almost every food chain on the planet.",
    "background_sections": [
        ("The Photosynthesis Equation", "6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂. In words: six molecules of carbon dioxide plus six molecules of water, powered by light energy, produce one molecule of glucose and six molecules of oxygen. This seemingly simple reaction involves hundreds of molecular steps and is the basis of almost all life on Earth."),
        ("Where Does the Mass Come From?", "This is the most counterintuitive fact in plant biology: most of a tree's mass comes from CO₂ in the air, NOT from the soil. The famous Van Helmont experiment (1648) showed that a willow tree gained 75 kg while its soil lost only a few ounces. The carbon in CO₂ is rearranged into organic molecules that build wood, bark, leaves, and roots."),
        ("Limiting Factors", "Photosynthesis rate is limited by whichever input is in shortest supply — the 'law of the minimum.' On a sunny day with plenty of water, CO₂ is usually the limiting factor. On a cloudy day, light is limiting. During drought, water is limiting. This concept is critical for agriculture — farmers must provide ALL needed inputs for maximum crop yield."),
        ("Global Importance", "Plants and algae perform photosynthesis, producing about 300 billion tons of oxygen per year. Photosynthesis is also Earth's main carbon sink — removing CO₂ from the atmosphere. Deforestation reduces this capacity, contributing to climate change. Understanding photosynthesis is essential for addressing food security and climate challenges.")
    ],
    "lever_L": "Students identify sunlight intensity, water availability, CO₂ concentration, and chlorophyll amount as the key inputs to photosynthesis.",
    "lever_E": "Students determine that all three external inputs positively affect photosynthesis rate (more input = more glucose), and that chlorophyll amount determines how much light the plant can capture.",
    "lever_V": "Students build a model showing how limiting factors control glucose production and how removing any single input stops the entire process.",
    "lever_Ev": "Students run perfect day, cloudy, and drought scenarios to identify which factor limits photosynthesis under different conditions.",
    "lever_R": "Students add temperature or leaf surface area to explore how additional factors affect photosynthesis in real plants.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with glowing leaf imagery", "say": "A tree weighing 10,000 pounds grows from a tiny seed. Where does all that STUFF come from?", "do": "Hold up a small seed and a photo of a giant tree. Ask: Where did the mass come from?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're cracking the mystery of how plants build themselves from thin air.", "do": "Have students read objectives. Pre-teach 'photosynthesis,' 'chlorophyll,' and 'glucose.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does a tree's mass come from?", "say": "Here's a mind-blowing fact: most of this tree is made from AIR. Not soil. Not water. Air.", "do": "Poll the class: Soil, water, air, or sunlight? Most students will say soil — they're wrong!", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model of the invisible factory inside every leaf.", "do": "Preview LEVER steps. Connect to prior knowledge — what do students know about how plants grow?", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for photosynthesis model", "say": "What does a plant need to make food? Which inputs come from the environment?", "do": "Guide sorting. Emphasize that THREE inputs are all external — plants depend entirely on their environment.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Every input is positive — more sunlight, more water, more CO₂ all mean more food. But remove ANY one and it all stops.", "do": "Demonstrate with a recipe analogy: you can't make a cake without flour, even if you have eggs and sugar.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "What happens to a plant on a cloudy week? What about during a drought?", "do": "Students predict, then run scenarios. Compare which limiting factor has the biggest impact.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Trees are made from AIR. Your desk was once CO₂ floating around in the atmosphere.", "do": "Reveal the Van Helmont experiment result. Connect to carbon cycle — where does the carbon go?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Mars greenhouse design challenge", "say": "NASA needs your help. Design a greenhouse that works on MARS!", "do": "Distribute Mars environment fact sheets. Groups design greenhouses optimized for Martian conditions.", "time": "12 min"}
    ],
    "sort_reasoning": "Sunlight Intensity, Water Availability, and CO₂ Concentration are all external because they come from the environment and the plant cannot create them internally. Chlorophyll Amount is internal because it is a property of the plant itself that the plant produces in its leaf cells.",
    "relationships": [
        ("Sunlight Intensity to Glucose Production", "POSITIVE (+)", "More sunlight provides more energy to drive the photosynthesis reaction. Up to a saturation point, increased light directly increases glucose production."),
        ("Water Availability to Glucose Production", "POSITIVE (+)", "Water is a direct reactant in photosynthesis (6H₂O needed per glucose molecule). Without water, the reaction cannot proceed regardless of other inputs."),
        ("CO₂ Concentration to Glucose Production", "POSITIVE (+)", "CO₂ provides the carbon atoms that become glucose. More CO₂ allows the plant to build more sugar molecules, up to the point where another factor becomes limiting.")
    ],
    "sim_answers": [
        ("Cloudy Week Scenario", "At 20% Sunlight Intensity, glucose production drops dramatically even though water and CO₂ are normal. Light is the energy source — without enough energy, the plant can't drive the chemical reaction fast enough. This demonstrates that sunlight is the limiting factor on cloudy days."),
        ("Drought Stress Scenario", "At 10% Water Availability, glucose production nearly stops despite adequate sunlight and CO₂. Water is both a reactant AND essential for keeping stomata open (pores that let CO₂ in). Without water, stomata close to prevent water loss, which also blocks CO₂ entry — a double hit to photosynthesis.")
    ],
    "reflection_exemplars": [
        ("Where does tree mass come from?", "It's incredibly counterintuitive, but most of a tree's mass comes from carbon dioxide gas in the atmosphere. During photosynthesis, plants take in CO₂ and use light energy to rearrange carbon atoms into glucose molecules. Those glucose molecules are then used to build cellulose (wood), lignin (bark), and other structural molecules. The tree is literally assembling itself from air molecules, one carbon atom at a time."),
        ("How are photosynthesis and respiration opposite?", "Photosynthesis: CO₂ + H₂O + light → glucose + O₂ (builds sugar, releases oxygen). Cellular respiration: glucose + O₂ → CO₂ + H₂O + energy (breaks sugar, releases CO₂). They're mirror images! Plants do BOTH — photosynthesis during the day and respiration 24/7. Animals only do respiration. Together, these two reactions cycle carbon and oxygen through the biosphere.")
    ],
    "stem_intro": "Present the NASA Mars greenhouse scenario: Mars has 95% CO₂ but only 43% of Earth's sunlight, very limited water (ice at the poles), no soil, and extreme temperature swings. Your team must design a self-sustaining food production system.",
    "stem_concepts": [
        ("Limiting Factors in Agriculture", "Crop yield is determined by whichever essential input is in shortest supply. Even if a greenhouse has perfect lighting, without enough water, plants can't photosynthesize. Farmers must optimize ALL inputs simultaneously."),
        ("Hydroponics", "Growing plants without soil by dissolving nutrients directly in water. This is ideal for space greenhouses because it uses less water, grows faster, and eliminates the need to transport heavy soil."),
        ("Bioregenerative Life Support", "A system where plants provide food and oxygen while recycling CO₂ and water from human waste. This creates a closed-loop ecosystem essential for long-term space missions.")
    ],
    "stem_eval": [
        ("Expert (4)", "Greenhouse design addresses all limiting factors on Mars, uses model evidence, includes specific crop recommendations, and explains water/air recycling"),
        ("Proficient (3)", "Design addresses at least two limiting factors with model evidence and includes a specific growing strategy"),
        ("Developing (2)", "Design mentions plants on Mars but doesn't address specific photosynthesis challenges"),
        ("Beginning (1)", "Design is incomplete or doesn't connect greenhouse features to photosynthesis requirements")
    ],
    "support": [
        "Provide a simple diagram of the photosynthesis equation with molecule counts labeled: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
        "Use LEGO bricks to physically model how carbon atoms from CO₂ are rearranged into glucose molecules",
        "Sentence frames: 'When sunlight intensity decreases, glucose production __ because __'"
    ],
    "extensions": [
        "Research how ocean phytoplankton perform photosynthesis and produce more than half of Earth's oxygen",
        "Investigate how greenhouses increase CO₂ levels to boost crop growth — and the math behind it",
        "Design an experiment to test whether the color of light affects photosynthesis rate"
    ],
    "cross_curr": [
        ("Math", "Balance the photosynthesis equation by counting atoms on each side: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂"),
        ("ELA", "Write an explanatory article for a younger student about where trees get their mass, debunking the common myth"),
        ("Social Studies", "Research the Green Revolution — how understanding photosynthesis led to agricultural changes that feed billions")
    ],
    "misconceptions": [
        ("Plants get their food from soil", "Plants get WATER and MINERALS from soil, but their actual food (glucose) is made through photosynthesis using CO₂ from air and light energy. Soil provides micronutrients but is NOT the main source of plant mass. Van Helmont proved this in 1648.", "Classic demo: Grow a plant hydroponically (no soil) — it still thrives because it gets CO₂, water, and light."),
        ("Plants only do photosynthesis, not respiration", "Plants do BOTH. During the day, photosynthesis produces more oxygen than respiration consumes, so the net effect is oxygen release. At night, plants only respire (consuming oxygen, releasing CO₂) just like animals. Plants are full-time respirers and part-time photosynthesizers.", "Place a plant in a dark sealed container and test the air after 24 hours — CO₂ increases, oxygen decreases."),
        ("Photosynthesis is the reverse of breathing", "While the equations are reverse, the processes are completely different. Photosynthesis uses light energy to BUILD glucose molecules (energy storage). Respiration BREAKS glucose to release energy (energy use). They happen in different organelles (chloroplasts vs. mitochondria) using different enzymes.", "Compare: Building a house takes energy and materials. Demolishing a house releases materials. Both involve a house, but they're completely different processes.")
    ]
}

L08 = {
    "id": "G06-L08",
    "title": "Can You Outsmart a Disaster?",
    "subtitle": "How Science Helps Communities Survive Natural Hazards",
    "ngss": "MS-ESS3-2",
    "ngss_desc": "Analyze and interpret data on natural hazards to forecast future catastrophic events and inform the development of technologies to mitigate their effects.",
    "big_question": "Why do some communities survive natural disasters better than others — what makes the difference between tragedy and resilience?",
    "objectives": [
        "Analyze data patterns to predict where natural hazards are most likely to occur",
        "Model how hazard intensity, population density, warning time, and building design interact to determine disaster outcomes",
        "Evaluate engineering solutions that reduce the impact of natural hazards on communities",
        "Use model evidence to design a disaster-resilient community plan"
    ],
    "vocabulary": [
        ("Natural Hazard", "A natural event (earthquake, flood, hurricane, wildfire) that threatens human life and property"),
        ("Resilience", "A community's ability to prepare for, withstand, and recover from natural hazards"),
        ("Mitigation", "Actions taken BEFORE a disaster to reduce its impact — building codes, levees, firebreaks"),
        ("Early Warning System", "Technology that detects hazards in advance, giving people time to prepare or evacuate")
    ],
    "components": [
        ("Hazard Intensity", "The strength or magnitude of the natural event — earthquake magnitude, hurricane category, flood depth", True),
        ("Population Density", "The number of people living per square kilometer in the affected area", False),
        ("Warning Time", "How much advance notice a community receives before the hazard strikes", True),
        ("Building Design", "How well structures are engineered to withstand the specific hazard type", False)
    ],
    "think_about_it": "When warning time increases, what happens to the number of casualties? Does better building design help more against earthquakes or floods?",
    "scenarios": [
        ("Unprepared City", "Set Building Design to 10% and Warning Time to zero — observe the outcome"),
        ("Prepared Community", "Set Building Design to 80% and Warning Time to 48 hours — compare to unprepared"),
        ("Monster Storm", "Lock Hazard Intensity to maximum — can ANY preparation save everyone?")
    ],
    "sim_scenarios": [
        ("Unprepared City", "Poor buildings, no warning", "What do you predict happens to casualties when there's no warning and weak buildings?"),
        ("Prepared Community", "Strong buildings, 48-hour warning", "How much difference do you predict preparation makes compared to the unprepared scenario?"),
        ("Monster Storm", "Maximum hazard intensity", "Is there a hazard level that overwhelms even the best preparation?")
    ],
    "discoveries": [
        "Warning time dramatically reduces casualties but NOT property damage — you can evacuate people but not buildings",
        "Building design is the most effective factor for reducing BOTH casualties and property damage",
        "Population density multiplies the impact — the same earthquake in a rural area vs. a dense city produces vastly different outcomes",
        "No amount of preparation can eliminate all risk from extreme natural hazards — but it can reduce impact by 80-90%"
    ],
    "answer": "The difference between communities that survive disasters and those that don't comes down to three things: early warning systems (to evacuate), building codes (to withstand the hazard), and planning (to reduce population in high-risk zones). Japan and Haiti both get earthquakes, but Japan's preparation results in far fewer deaths because of decades of investment in resilient engineering and warning systems.",
    "stem_title": "Design a Disaster-Resilient Community",
    "stem_mission": "Design a community plan for a region that faces multiple natural hazards (earthquakes AND flooding) that minimizes casualties and property damage within a limited budget.",
    "stem_scenario": "A coastal city near a fault line needs a comprehensive disaster resilience plan. Your urban planning team has a $10 million budget and must decide how to allocate resources among warning systems, building upgrades, evacuation routes, and emergency shelters. Use your model evidence to justify every budget decision.",
    "stem_questions": [
        "Based on your model, which investment saves the most lives: warning systems, building codes, or evacuation routes?",
        "How do you prioritize when the city faces BOTH earthquake and flood risk?",
        "What compromises must you make with a limited budget?"
    ],
    "stem_design_qs": [
        "How will you divide the $10 million budget among different resilience strategies?",
        "Which areas of the city should be restricted from residential development?",
        "What building codes will you require for new construction?",
        "How will you ensure that warning systems reach every resident, including those without smartphones?"
    ],
    "career": "Emergency Management Specialists and Civil Engineers design systems that protect communities from natural hazards. They plan evacuations, design resilient infrastructure, and save lives. They earn $60,000–$120,000/year.",
    "images": {
        "cover": ("cover-disasters.png", "A powerful dramatic photo of a large storm system approaching a city skyline from above, dark clouds contrasting with the lit city below, cinematic weather photography"),
        "landscape": ("landscape-hazards.png", "6th grade students studying maps of natural hazard zones in a modern classroom, analyzing data charts and maps on tables, engaged in research"),
        "modeling": ("modeling-disasters.png", "A diverse group of 6th grade students working on laptops building a natural hazards model, classroom with maps and emergency preparedness posters"),
        "discussion": ("discussion-hazards.png", "A teacher leading a discussion about disaster preparedness with 6th grade students, showing before-and-after photos of natural disasters on a screen"),
        "stem": ("stem-resilient-city.png", "6th grade students building a model resilient city layout on poster boards, showing flood barriers and evacuation routes, collaborative design work")
    },
    "pre_assessment": [
        "What natural disasters have you heard about or experienced? What happened?",
        "Why do you think some buildings collapse in earthquakes while others don't?",
        "If you knew a hurricane was coming in 48 hours, what would you do?",
        "Draw a community plan that would be safe from flooding."
    ],
    "extend_components": [
        ("Emergency Response Time", "How quickly first responders can reach affected areas after a disaster strikes"),
        ("Community Education", "How well-informed residents are about hazard risks and evacuation procedures"),
        ("Infrastructure Age", "Older buildings and infrastructure are more vulnerable; newer construction follows stricter codes")
    ],
    "reflections": [
        "Why did the 2010 Haiti earthquake kill 230,000 people while a stronger earthquake in Japan killed far fewer?",
        "Is it possible to make a community completely disaster-proof? Why or why not?",
        "How does population density change the impact of a natural hazard?",
        "Should governments force people to move away from high-risk areas? What are the ethical considerations?",
        "How does your model help decision-makers spend limited money on the most effective protections?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how hazard intensity, population density, warning time, and building design interact to determine disaster outcomes."),
        ("Disciplinary Core Idea", "ESS3.B Natural Hazards", "Mapping the history of natural hazards in a region, combined with an understanding of related geologic forces, can help forecast the locations and likelihoods of future events."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships between preparation levels and disaster outcomes — more warning time CAUSES fewer casualties, better building design CAUSES less structural damage.")
    ],
    "cast_items": [
        "Analyze data on natural hazard patterns to forecast future events",
        "Evaluate technologies designed to mitigate the effects of natural hazards",
        "Use evidence to compare disaster outcomes between prepared and unprepared communities"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two cities of equal population both experience a magnitude 7.0 earthquake. City A has modern building codes while City B has older construction. City A suffers 50 casualties while City B suffers 5,000. Which factor best explains this 100x difference?"),
        ("Constructed Response:", "A city is located on a river floodplain and also near a fault line. The city council has $5 million for disaster preparation. Using evidence from natural hazard data, explain how you would recommend they spend the money and why.")
    ],
    "background_intro": "Natural hazards have shaped human civilization throughout history. Modern science and engineering allow us to predict, prepare for, and mitigate the impacts of natural disasters — saving millions of lives each year.",
    "background_sections": [
        ("Types of Natural Hazards", "Major categories include: geologic hazards (earthquakes, volcanic eruptions, tsunamis, landslides), meteorological hazards (hurricanes, tornadoes, floods, droughts), and wildfires. Each type has specific patterns, warning signs, and mitigation strategies. Understanding these patterns is the first step in disaster preparedness."),
        ("The Role of Data", "Scientists use historical data, geological surveys, weather monitoring, and satellite imagery to forecast natural hazards. Earthquake recurrence intervals help predict when and where quakes will strike. Hurricane models track storms days in advance. Flood maps identify vulnerable areas. This data drives preparation decisions that save lives."),
        ("Engineering for Resilience", "Modern engineering provides powerful tools against natural hazards. Earthquake-resistant buildings use base isolation (floating foundations) and flexible materials. Levees and flood walls protect against flooding. Storm shelters withstand tornado-force winds. Fire-resistant materials and defensible space reduce wildfire risk. Each solution addresses a specific hazard."),
        ("Japan vs. Haiti: A Case Study", "The 2010 Haiti earthquake (M7.0) killed approximately 230,000 people. The 2011 Japan earthquake (M9.0 — 1000x stronger) killed approximately 20,000, mostly from the tsunami. The difference: Japan has strict building codes, tsunami warning systems, regular earthquake drills, and massive infrastructure investment. Haiti had none of these. Preparation is the difference between tragedy and resilience.")
    ],
    "lever_L": "Students identify hazard intensity, population density, warning time, and building design as the key components determining disaster outcomes.",
    "lever_E": "Students determine that warning time negatively affects casualties (more warning = fewer deaths), building design negatively affects property damage (better design = less damage), and population density positively amplifies all impacts.",
    "lever_V": "Students build a model showing how preparation factors interact with hazard severity to determine overall disaster impact.",
    "lever_Ev": "Students run prepared vs. unprepared vs. extreme scenarios to quantify how much difference preparation makes.",
    "lever_R": "Students add emergency response time or community education to explore additional factors in disaster resilience.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic storm imagery", "say": "Natural disasters happen everywhere. But they don't affect everywhere equally. Why?", "do": "Show side-by-side images of earthquake damage in Haiti vs. Japan. Ask: Why the difference?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're figuring out how science and engineering can outsmart disasters.", "do": "Have students read objectives. Pre-teach 'resilience,' 'mitigation,' and 'early warning system.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do some communities survive better?", "say": "Same size earthquake. One city loses 200 people. Another loses 200,000. What explains the difference?", "do": "Quick write: Students list factors they think make a community more disaster-resilient.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model what factors matter most — and which investments save the most lives.", "do": "Preview LEVER steps. Connect to real disaster data they'll analyze.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for disaster model", "say": "What factors determine whether a community survives a natural disaster?", "do": "Guide sorting. Discuss why hazard intensity and warning time are external (nature and technology), while population density and building design are community choices.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More warning time saves lives. Better buildings save BOTH lives and property. But more people in harm's way multiplies everything.", "do": "Discuss the multiplier effect of population density. Use concrete numbers to illustrate.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's test: Does a prepared community survive a disaster that destroys an unprepared one?", "do": "Students predict then run all three scenarios. Compare outcomes quantitatively.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "You can't stop a hurricane. But you CAN decide how much damage it does.", "do": "Show Haiti vs. Japan data. Connect model results to real-world outcomes.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Resilient community design", "say": "You're now urban planners. You have $10 million and two hazards to prepare for. Go!", "do": "Distribute budget sheets and hazard data. Groups must justify every spending decision with model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Hazard Intensity and Warning Time are external because they come from nature and technology systems outside the community's permanent control. Population Density and Building Design are internal because they are characteristics of the community itself that can be engineered and planned.",
    "relationships": [
        ("Warning Time to Casualties", "NEGATIVE (-)", "More warning time allows evacuation, reducing the number of people in harm's way. However, warning time doesn't protect buildings or infrastructure."),
        ("Building Design to Property Damage", "NEGATIVE (-)", "Better-engineered buildings withstand more force before failing. Modern earthquake-resistant buildings can survive events that would destroy older construction."),
        ("Population Density to Total Impact", "POSITIVE (+)", "Higher population density means more people and structures exposed to the hazard. The same disaster in a dense city affects far more people than in a rural area.")
    ],
    "sim_answers": [
        ("Unprepared vs. Prepared", "With no warning and weak buildings (10% design quality), a moderate hazard produces devastating casualties and property loss. With 48-hour warning and strong buildings (80% design), the same hazard produces 70-90% fewer casualties and 50-70% less property damage. The model proves that preparation is the single most important variable."),
        ("Monster Storm Scenario", "Even with excellent preparation, a maximum-intensity hazard still causes significant damage. No building can withstand every possible event. However, the DIFFERENCE between prepared and unprepared communities remains enormous — preparation reduces the catastrophe from existential to manageable. The model shows that preparation has diminishing returns at extreme intensities.")
    ],
    "reflection_exemplars": [
        ("Why the Haiti vs. Japan difference?", "Haiti had: no earthquake building codes, no early warning system, no earthquake drills, and extremely dense population in poorly constructed concrete buildings. Japan had: strict building codes requiring earthquake resistance, sophisticated tsunami warning systems, regular disaster drills starting in kindergarten, and massive infrastructure investment over decades. Japan's 2011 earthquake was 1000x stronger than Haiti's, yet killed 90% fewer people. The difference is entirely due to preparation."),
        ("Can a community be completely disaster-proof?", "No — but they can be disaster-resilient. There is no building that can survive every possible earthquake, and no warning system that works 100% of the time. However, data shows that even modest preparation can reduce casualties by 70-90%. The goal isn't to eliminate risk (impossible) but to reduce it to manageable levels. This is why risk assessment and model evidence are so important — they help communities invest limited resources where they'll save the most lives.")
    ],
    "stem_intro": "Present the budget challenge: A coastal city on a fault line receives $10 million for disaster resilience. They face BOTH earthquake and flood risk. Your team must present a budget allocation with scientific justification for every dollar spent.",
    "stem_concepts": [
        ("Risk Assessment Matrix", "A tool that evaluates hazards by multiplying probability × impact. High-probability, high-impact risks (like flooding in a floodplain) get the most attention and budget."),
        ("Cost-Benefit Analysis", "Comparing the cost of mitigation measures against the expected losses they prevent. If a $2M seawall prevents $50M in flood damage, the return on investment is 25:1."),
        ("Multi-Hazard Planning", "Communities often face multiple hazard types. Some investments (like warning systems) help against multiple hazards. Multi-hazard planning seeks solutions that address multiple risks simultaneously.")
    ],
    "stem_eval": [
        ("Expert (4)", "Budget allocation addresses both hazards, uses model evidence, includes cost-benefit reasoning, and demonstrates understanding of trade-offs"),
        ("Proficient (3)", "Budget addresses both hazards with model evidence and at least two mitigation strategies"),
        ("Developing (2)", "Budget mentions disaster preparation but doesn't justify allocations with model evidence"),
        ("Beginning (1)", "Budget is incomplete or doesn't connect spending decisions to natural hazard concepts")
    ],
    "support": [
        "Provide a simplified risk matrix template with hazard types and probability/impact ratings",
        "Use case study cards (Japan, Haiti, New Orleans) for students to analyze real examples",
        "Sentence frames: 'When warning time increases, casualties __ because people can __'"
    ],
    "extensions": [
        "Research how FEMA flood maps are created and how they determine insurance rates",
        "Investigate how climate change is increasing the frequency and intensity of certain natural hazards",
        "Design an early warning system for your school that addresses the most likely local natural hazard"
    ],
    "cross_curr": [
        ("Math", "Calculate cost-benefit ratios: If a $3M levee prevents $90M in flood damage, what is the return on investment?"),
        ("ELA", "Write a persuasive budget proposal to a city council arguing for specific disaster preparation investments"),
        ("Social Studies", "Research how socioeconomic factors affect which communities are most vulnerable to natural disasters")
    ],
    "misconceptions": [
        ("Natural disasters are unpredictable and random", "While we can't predict the exact time of an earthquake, we CAN identify high-risk zones using historical data and geological mapping. Hurricane tracks are forecast days in advance. Flood zones are well-mapped. Most natural hazard risk is predictable and plannable.", "Show USGS earthquake hazard maps — the patterns are clear and consistent, not random."),
        ("Technology can prevent natural disasters", "Technology can't PREVENT earthquakes, hurricanes, or floods — these are natural Earth processes. But technology can predict them (seismographs, weather satellites), warn about them (alert systems), and reduce their impact (resilient engineering). Mitigation, not prevention, is the goal.", "Ask: Can we stop an earthquake? No. Can we build a building that survives one? Yes! That's the difference."),
        ("All disasters affect everyone equally", "Disasters disproportionately affect vulnerable populations — those in poverty, elderly, disabled, and communities with poor infrastructure. A hurricane causes vastly different impacts in a wealthy neighborhood vs. a low-income area. Social and economic factors multiply natural hazard impacts.", "Compare outcomes of Hurricane Katrina across different New Orleans neighborhoods — the differences are striking.")
    ]
}

L09 = {
    "id": "G06-L09",
    "title": "Your Sneakers Are Made of Dinosaurs",
    "subtitle": "How Scientists Engineer Materials That Don't Exist in Nature",
    "ngss": "MS-PS1-3, MS-PS1-6",
    "ngss_desc": "Gather and make sense of information to describe that synthetic materials come from natural resources and impact society. Undertake a design project to construct, test, and modify a device that either releases or absorbs thermal energy by chemical processes.",
    "big_question": "If most of the stuff you wear, carry, and use every day doesn't exist in nature, where does it come from and what is it made of?",
    "objectives": [
        "Explain how synthetic materials are engineered from natural resources through chemical processes",
        "Model how polymer chain length, heat treatment, chemical additives, and raw material quality affect material properties",
        "Evaluate the benefits and environmental trade-offs of synthetic vs. natural materials",
        "Design a synthetic material for a specific purpose using molecular-level understanding"
    ],
    "vocabulary": [
        ("Synthetic Material", "A material made by humans through chemical processes that doesn't occur naturally — plastics, nylon, polyester"),
        ("Natural Resource", "A raw material from Earth (petroleum, minerals, plants) used to create synthetic materials"),
        ("Polymerization", "The chemical process of joining small molecules (monomers) into long chains (polymers)"),
        ("Material Properties", "The physical characteristics of a material — strength, flexibility, heat resistance, durability")
    ],
    "components": [
        ("Polymer Chain Length", "The number of monomer units linked together in each chain — longer chains generally mean stronger materials", False),
        ("Heat Treatment", "The temperature and duration of heating during manufacturing, which affects how polymer chains arrange themselves", True),
        ("Chemical Additives", "Substances mixed in to modify properties — plasticizers for flexibility, colorants, UV stabilizers", False),
        ("Raw Material Quality", "The purity and type of starting materials, typically derived from petroleum or plant-based sources", True)
    ],
    "think_about_it": "When polymer chain length increases, how does it affect material strength? What happens when you add plasticizer additives — does the material get stiffer or more flexible?",
    "scenarios": [
        ("Weak Plastic", "Set Polymer Chain Length to short and Heat Treatment to low — observe material properties"),
        ("Super Strong", "Lock Polymer Chain Length to maximum and Heat Treatment to optimal — what material results?"),
        ("Flexible Film", "Maximize Chemical Additives (plasticizers) and observe how the same polymer becomes flexible")
    ],
    "sim_scenarios": [
        ("Weak Plastic", "Short chains, minimal treatment", "What do you predict this material will be like — strong or brittle?"),
        ("Super Strong", "Maximum chain length, optimal heat treatment", "How will this material compare to the weak plastic?"),
        ("Flexible Film", "Maximum plasticizer additives", "How do additives change a rigid plastic into a flexible film?")
    ],
    "discoveries": [
        "Longer polymer chains create stronger materials because chains tangle and hold together better",
        "Heat treatment allows polymer chains to organize into crystalline structures, dramatically increasing strength",
        "Additives can completely change a material's properties — the same base polymer can become rigid OR flexible",
        "Almost all synthetic materials trace back to petroleum (ancient organisms), making your sneakers literally made from transformed ancient life"
    ],
    "answer": "Your sneakers, phone case, and backpack are made from synthetic materials engineered from petroleum — which is the transformed remains of ancient organisms (including dinosaurs' contemporaries). Scientists take these natural resources and rearrange their molecules through polymerization, heat treatment, and additives to create materials with properties that don't exist in nature: lightweight, waterproof, flexible, and durable all at once!",
    "stem_title": "Design a Sustainable Material of the Future",
    "stem_mission": "Design a new material for a specific product that is both high-performance AND environmentally sustainable, replacing a petroleum-based plastic.",
    "stem_scenario": "A sportswear company wants to eliminate petroleum-based plastics from their products by 2030. Your materials engineering team must design a replacement material for running shoe soles that matches the performance of current materials while using sustainable raw materials.",
    "stem_questions": [
        "What properties must the replacement material have to work as a shoe sole?",
        "Which sustainable raw materials (plant-based, recycled) could replace petroleum?",
        "How will you test whether your material matches the performance of current shoe soles?"
    ],
    "stem_design_qs": [
        "What natural or recycled raw materials will you start with?",
        "What polymer chain length and heat treatment will give you the needed durability?",
        "What additives will provide the right combination of cushioning and grip?",
        "How will you measure performance: bounce, durability, water resistance, or something else?"
    ],
    "career": "Materials Engineers and Polymer Scientists develop new synthetic materials for products ranging from sneakers to spacecraft. They work on sustainability challenges and create materials that don't yet exist. They earn $70,000–$130,000/year.",
    "images": {
        "cover": ("cover-synthetics.png", "A dramatic close-up of a colorful modern sneaker being deconstructed showing all its synthetic material layers, mesh fabric, foam sole, rubber tread, product photography style"),
        "landscape": ("landscape-materials.png", "6th grade students examining different materials at lab stations, comparing natural vs synthetic fabrics, plastics, and rubber, using magnifying tools"),
        "modeling": ("modeling-materials.png", "A diverse group of 6th grade students working on laptops building a materials science model, classroom with material samples displayed on shelves"),
        "discussion": ("discussion-materials.png", "A teacher holding up different synthetic materials while explaining their properties to 6th grade students, some students touching and comparing material samples"),
        "stem": ("stem-sustainable.png", "6th grade students designing sustainable material alternatives, testing samples for strength and flexibility, science fair project style with data charts visible")
    },
    "pre_assessment": [
        "Look at your clothes and belongings. Which items exist in nature and which were made by humans?",
        "Where do you think plastic comes from originally?",
        "Why might scientists create materials that don't exist in nature?",
        "What makes a good material for a shoe sole? List the properties it needs."
    ],
    "extend_components": [
        ("Cross-Linking Density", "Chemical bonds between polymer chains that create a network — more cross-links mean stiffer, more heat-resistant material"),
        ("Recycled Content", "The percentage of material made from recycled sources rather than virgin petroleum — affects both properties and sustainability"),
        ("Biodegradability", "How quickly the material breaks down in the environment — a critical property for environmental sustainability")
    ],
    "reflections": [
        "Why can the same base polymer become a rigid water bottle OR a flexible plastic bag?",
        "What are the environmental trade-offs of synthetic materials — benefits vs. costs?",
        "How is making a polymer similar to building with LEGO bricks?",
        "Why is it important to develop plant-based alternatives to petroleum plastics?",
        "How does understanding molecular structure help engineers design better materials?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how polymer chain length, heat treatment, additives, and raw materials determine synthetic material properties."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter / PS1.B Chemical Reactions", "Each pure substance has characteristic physical and chemical properties that can be used to identify it. Substances react chemically in characteristic ways, and chemical processes can be designed to produce desired materials."),
        ("Crosscutting Concept", "Structure and Function", "Students discover that the molecular STRUCTURE of synthetic materials (chain length, arrangement, additives) directly determines their FUNCTION (strength, flexibility, durability).")
    ],
    "cast_items": [
        "Explain how synthetic materials are derived from natural resources through chemical processes",
        "Describe how molecular structure determines material properties",
        "Evaluate the societal impacts of synthetic materials — both benefits and environmental costs"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two plastic samples are made from the same polymer. Sample A is rigid and Sample B is flexible. What molecular-level difference most likely explains this?"),
        ("Constructed Response:", "Explain why petroleum (crude oil) can be transformed into thousands of different synthetic materials with different properties. Use the concepts of polymerization, chain length, and additives in your answer.")
    ],
    "background_intro": "Synthetic materials have transformed modern life. From the clothes on your back to the phone in your pocket, most everyday objects contain materials that don't exist in nature — materials engineered by chemists and materials scientists.",
    "background_sections": [
        ("From Petroleum to Plastic", "Crude oil (petroleum) is a mixture of hydrocarbon molecules formed from ancient marine organisms over millions of years. Refineries separate these molecules by size (distillation). Chemical plants then link small hydrocarbon molecules (monomers) into long chains (polymers) through polymerization. Different monomers and processes create different plastics with vastly different properties."),
        ("How Properties Are Controlled", "Materials scientists control properties by adjusting: chain length (longer = stronger), branching (more branches = less dense), cross-linking (more = stiffer), crystallinity (more = harder), and additives (plasticizers for flexibility, fillers for strength, pigments for color). The same base polymer — polyethylene — becomes grocery bags (low density, branched) OR bulletproof plates (ultra-high molecular weight, aligned chains)."),
        ("Environmental Impact", "Synthetic materials provide enormous benefits: medical devices, safety equipment, lightweight transportation, and food preservation. However, petroleum-based plastics don't biodegrade easily, creating pollution that persists for hundreds of years. Only 9% of all plastic ever made has been recycled. Scientists are now developing biodegradable polymers from plant-based sources as alternatives."),
        ("The Future of Materials", "Cutting-edge materials science is producing: self-healing polymers that repair their own damage, shape-memory materials that return to preset shapes, biodegradable plastics from corn and sugarcane, graphene (one atom thick but 200x stronger than steel), and programmable materials that change properties on demand. Understanding molecular structure is the key to all of these innovations.")
    ],
    "lever_L": "Students identify polymer chain length, heat treatment, chemical additives, and raw material quality as the key variables determining synthetic material properties.",
    "lever_E": "Students determine that longer chains and optimal heat treatment increase strength (positive), while plasticizer additives decrease rigidity (negative relationship with stiffness but positive with flexibility).",
    "lever_V": "Students build a model showing how molecular-level decisions during manufacturing determine the final material's macroscopic properties.",
    "lever_Ev": "Students run weak plastic, super strong, and flexible film scenarios to see how the same base chemistry produces radically different materials.",
    "lever_R": "Students add cross-linking density or recycled content to explore additional factors in material design.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with sneaker material imagery", "say": "Look at your shoes. Almost nothing in them exists in nature. So where did it all come from?", "do": "Have students look at their shoes and list the materials they can identify. Most are synthetic.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're learning how scientists create materials that nature never imagined.", "do": "Have students read objectives. Pre-teach 'synthetic,' 'polymer,' and 'polymerization.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does your stuff come from?", "say": "Your shoes, phone case, backpack, and jacket — made from ancient organisms, transformed by chemistry.", "do": "Show the journey: oil well → refinery → chemical plant → product. Trace the molecular path.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how scientists dial in exactly the right properties for any material.", "do": "Preview LEVER steps. Explain that materials scientists are molecular-level engineers.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for materials model", "say": "What molecular-level variables determine whether a material is strong, flexible, or brittle?", "do": "Guide sorting. Show real material samples (rigid bottle vs. flexible bag vs. stretchy rubber) — all polymers!", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Longer chains = stronger material. More plasticizer = more flexible. You can dial in ANY combination.", "do": "Use LEGO chain analogy: short chains pull apart easily, long chains tangle and hold.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's engineer three materials: weak, super strong, and ultra flexible — from the same starting chemistry!", "do": "Students predict, then run scenarios. Show how dramatically properties change with molecular adjustments.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "The same molecules that make a flimsy grocery bag can make a bulletproof vest. It's all about structure.", "do": "Discuss environmental impact. Ask: What's the trade-off of materials that last forever?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sustainable material design challenge", "say": "Can you engineer a shoe sole that's strong, flexible, AND sustainable? The planet is counting on you.", "do": "Distribute material property targets. Groups design sustainable replacements with scientific justification.", "time": "12 min"}
    ],
    "sort_reasoning": "Heat Treatment and Raw Material Quality are external because they are manufacturing inputs that come from outside the material itself — factory conditions and supply chain choices. Polymer Chain Length and Chemical Additives are internal because they are properties of the material itself that determine its final characteristics.",
    "relationships": [
        ("Polymer Chain Length to Material Strength", "POSITIVE (+)", "Longer polymer chains tangle and interlock more effectively, creating stronger intermolecular forces. Ultra-high molecular weight polyethylene has chains so long it can stop bullets."),
        ("Heat Treatment to Crystallinity", "POSITIVE (+)", "Controlled heating allows polymer chains to organize into ordered crystalline regions. More crystallinity means harder, stiffer, more heat-resistant material."),
        ("Chemical Additives (Plasticizers) to Flexibility", "POSITIVE (+)", "Plasticizer molecules insert between polymer chains, pushing them apart and allowing them to slide more easily. This converts rigid PVC pipe into flexible PVC cling wrap — same polymer, different properties.")
    ],
    "sim_answers": [
        ("Weak vs. Super Strong", "Short polymer chains with minimal heat treatment produce a brittle, weak material that breaks easily. Maximum chain length with optimal heat treatment produces a material that is dramatically stronger, harder, and more durable. The model shows that chain length and processing are the primary drivers of strength."),
        ("Flexible Film Scenario", "Adding maximum plasticizer additives to the same base polymer completely transforms it from rigid to flexible. The plasticizer molecules act as molecular lubricant, allowing chains to slide past each other. This demonstrates that a material's properties aren't fixed — they're engineered.")
    ],
    "reflection_exemplars": [
        ("Why can the same polymer be rigid or flexible?", "A polymer's properties depend not just on what molecules it contains but how they're arranged. Without plasticizers, PVC polymer chains are packed tightly and locked together by intermolecular forces — resulting in rigid pipe. Add plasticizer molecules and they wedge between chains, pushing them apart and allowing them to slide — resulting in flexible cling wrap. Same molecule, completely different behavior, controlled by additives."),
        ("What are the trade-offs of synthetic materials?", "Benefits: synthetic materials are lightweight, durable, waterproof, cheap to produce, and can be engineered for specific purposes. No natural material matches the versatility of plastics. Costs: petroleum extraction has environmental impacts, plastics persist in the environment for centuries, only 9% is recycled, and microplastics are now found in every ecosystem on Earth including human blood. The challenge is keeping the benefits while eliminating the environmental costs.")
    ],
    "stem_intro": "Present the sportswear company challenge: They need a petroleum-free shoe sole material that matches current performance. Your team must design a sustainable alternative using molecular engineering principles.",
    "stem_concepts": [
        ("Bio-Based Polymers", "Polymers made from renewable biological sources like corn starch (PLA), sugarcane (bio-PE), or castor oil (bio-nylon). These replace petroleum with plant-based carbon while maintaining similar material properties."),
        ("Lifecycle Analysis", "Evaluating a material's total environmental impact from raw material extraction through manufacturing, use, and disposal. A truly sustainable material must be better at EVERY stage, not just one."),
        ("Circular Economy", "Designing materials that can be recycled, composted, or safely returned to the environment after use. This eliminates the concept of 'waste' — every material becomes a resource for the next product.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design specifies sustainable raw materials, molecular properties (chain length, additives), performance testing plan, and lifecycle analysis"),
        ("Proficient (3)", "Design addresses sustainability and performance with model evidence and at least two property targets"),
        ("Developing (2)", "Design mentions sustainable materials but doesn't connect molecular structure to performance"),
        ("Beginning (1)", "Design is incomplete or doesn't demonstrate understanding of how molecular structure determines material properties")
    ],
    "support": [
        "Provide a chart comparing natural vs. synthetic materials with their properties listed side by side",
        "Use physical LEGO chains of different lengths to demonstrate how chain length affects tangle/strength",
        "Sentence frames: 'When polymer chain length increases, the material becomes __ because the molecules __'"
    ],
    "extensions": [
        "Research how Adidas is making shoes from recycled ocean plastic — what molecular processes are involved?",
        "Investigate graphene — a one-atom-thick material 200x stronger than steel — and explain its properties from molecular structure",
        "Design an experiment to compare the strength and flexibility of different plastic types using a standardized test"
    ],
    "cross_curr": [
        ("Math", "Calculate the percentage of everyday objects that contain synthetic materials — survey 20 items and categorize"),
        ("ELA", "Write an argumentative essay: Should single-use plastics be banned? Use evidence from materials science"),
        ("Social Studies", "Research how the invention of synthetic materials (nylon, polyester, plastic) transformed the economy in the 20th century")
    ],
    "misconceptions": [
        ("Plastic comes from chemicals, not nature", "ALL synthetic materials start as natural resources — primarily petroleum (ancient organisms) or sometimes plants. 'Chemical' processes rearrange natural molecules into new structures. Nothing in plastic was created from nothing — it's all rearranged atoms from Earth's resources.", "Show the chain: prehistoric organisms → petroleum → refinery → monomers → polymer → product. It all starts in nature."),
        ("All plastics are the same", "There are thousands of different plastics with vastly different properties. Polyethylene (PE) is in grocery bags. Polystyrene (PS) is in foam cups. Polycarbonate (PC) is in bulletproof glass. They're all polymers but with different monomers, chain lengths, and structures — like how different LEGO sets use the same basic bricks but create completely different things.", "Show students 5 different plastic products and have them feel the differences — all 'plastic' but completely different materials."),
        ("Recycling solves the plastic problem", "Only about 9% of all plastic ever made has been recycled. Many plastics degrade in quality when recycled (downcycling) and can only be recycled 1-2 times. True solutions require reducing plastic use, designing for recyclability from the start, and developing biodegradable alternatives.", "Ask: If recycling solved everything, why is there plastic in the ocean? The answer reveals the gap between recycling's promise and reality.")
    ]
}

L10 = {
    "id": "G06-L10",
    "title": "The Secret War in Your Backyard",
    "subtitle": "How Ecosystems Balance Competition, Cooperation, and Survival",
    "ngss": "MS-LS2-2, MS-LS2-3, MS-LS2-5",
    "ngss_desc": "Construct an explanation that predicts patterns of interactions among organisms across multiple ecosystems. Develop a model to describe the cycling of matter and flow of energy among living and nonliving parts of an ecosystem. Evaluate competing design solutions for maintaining biodiversity and ecosystem services.",
    "big_question": "Even a tiny backyard is a hidden battlefield — how do organisms compete, cooperate, and survive in a complex ecosystem?",
    "objectives": [
        "Explain how predator-prey relationships create population cycles in ecosystems",
        "Model how predator population, prey population, habitat size, and resource availability interact",
        "Predict what happens to an ecosystem when one population is removed or dramatically changed",
        "Evaluate strategies for maintaining biodiversity in threatened ecosystems"
    ],
    "vocabulary": [
        ("Ecosystem", "A community of living organisms interacting with each other and their nonliving environment"),
        ("Biodiversity", "The variety of different species in an ecosystem — more biodiversity generally means a healthier ecosystem"),
        ("Carrying Capacity", "The maximum population size an environment can sustain given available food, water, and space"),
        ("Trophic Level", "An organism's position in a food chain — producers, primary consumers, secondary consumers, decomposers")
    ],
    "components": [
        ("Predator Population", "The number of organisms that hunt and eat other organisms in the ecosystem", False),
        ("Prey Population", "The number of organisms that are hunted by predators — typically herbivores eating plants", False),
        ("Habitat Size", "The total area of suitable living space available to organisms in the ecosystem", True),
        ("Resource Availability", "The amount of food, water, shelter, and other necessities available in the environment", True)
    ],
    "think_about_it": "When prey population increases, what happens to predator population? And when predator population increases, what happens to prey? Do these relationships create a cycle?",
    "scenarios": [
        ("Balanced Ecosystem", "Set all components to moderate levels and observe population cycles over time"),
        ("Predator Removal", "Lock Predator Population to zero and observe what happens to prey and resources"),
        ("Habitat Loss", "Cut Habitat Size to 25% and observe how both populations respond")
    ],
    "sim_scenarios": [
        ("Balanced Ecosystem", "Moderate predators, prey, habitat, and resources", "What pattern do you predict predator and prey populations will follow over time?"),
        ("Predator Removal", "Predator Population locked at zero", "What do you predict happens to prey population when predators are removed?"),
        ("Habitat Loss", "Habitat Size reduced to 25%", "How does shrinking habitat affect BOTH predator and prey populations?")
    ],
    "discoveries": [
        "Predator and prey populations naturally cycle — when prey increases, predators follow, then prey crashes, then predators crash",
        "Removing predators causes prey to overshoot carrying capacity, depleting resources and causing a population crash",
        "Habitat loss reduces carrying capacity for ALL species, often pushing the smallest populations to extinction first",
        "Biodiversity makes ecosystems more resilient — diverse ecosystems recover from disturbances faster than simple ones"
    ],
    "answer": "Your backyard is a battlefield of constant competition and cooperation. Predators control prey populations, prey control plant populations, and decomposers recycle everything. These interactions create a dynamic balance. When humans disrupt that balance — by removing predators, shrinking habitat, or introducing invasive species — the entire ecosystem can collapse like a chain of dominoes.",
    "stem_title": "Design a Biodiversity Rescue Plan",
    "stem_mission": "Design an evidence-based plan to restore biodiversity in a degraded ecosystem, using your model to predict which interventions will be most effective.",
    "stem_scenario": "A local nature preserve has lost 60% of its habitat to development. Deer populations have exploded without wolves, overgrazing vegetation. Bird species are declining, and the stream ecosystem is degrading. Your ecology team must design a restoration plan using model evidence.",
    "stem_questions": [
        "Based on your model, which single intervention would have the greatest positive impact on biodiversity?",
        "Should predators be reintroduced? What does your model predict will happen?",
        "How much habitat must be restored to support a balanced ecosystem?"
    ],
    "stem_design_qs": [
        "Which species will you prioritize for protection or reintroduction?",
        "How much habitat needs to be restored and what type?",
        "What timeline do you predict for ecosystem recovery based on your model?",
        "How will you measure whether your plan is working?"
    ],
    "career": "Conservation Biologists and Ecologists study ecosystems to protect biodiversity and restore degraded habitats. They develop strategies that balance human needs with environmental health. They earn $55,000–$110,000/year.",
    "images": {
        "cover": ("cover-ecosystem.png", "A stunning macro photograph of a diverse backyard ecosystem showing insects, a spider web, flowers, and a small bird, vivid colors, shallow depth of field, nature photography"),
        "landscape": ("landscape-ecosystem.png", "6th grade students conducting a field study outdoors, examining plants and insects with magnifying glasses and collection jars, sunny natural setting"),
        "modeling": ("modeling-ecosystem.png", "A diverse group of 6th grade students working on laptops building an ecosystem population model, classroom with nature posters and aquarium visible"),
        "discussion": ("discussion-ecosystem.png", "A teacher leading a discussion about food webs with 6th grade students, drawing connections on a whiteboard showing predator-prey relationships"),
        "stem": ("stem-biodiversity.png", "6th grade students creating a biodiversity rescue plan on large paper, drawing habitat maps and listing species, colored markers and nature field guides on table")
    },
    "pre_assessment": [
        "What living things can you find in a typical backyard? List as many as you can.",
        "What do you think would happen if all the birds in an area suddenly disappeared?",
        "Why do you think some species go extinct while others thrive?",
        "Draw a food chain that might exist in your backyard."
    ],
    "extend_components": [
        ("Invasive Species", "Non-native organisms that outcompete local species for resources, often with no natural predators"),
        ("Decomposer Activity", "The rate at which dead organisms are broken down and nutrients recycled back into the soil"),
        ("Climate Conditions", "Temperature and rainfall patterns that determine which organisms can survive in an area")
    ],
    "reflections": [
        "Why do predator and prey populations rise and fall in cycles instead of staying constant?",
        "What happened when wolves were removed from Yellowstone — and what happened when they were brought back?",
        "Why does losing biodiversity make an ecosystem more vulnerable to collapse?",
        "Is it possible for an ecosystem to survive without decomposers? Why or why not?",
        "How does your backyard ecosystem connect to ecosystems around the world?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how predator and prey populations interact with habitat size and resource availability to create ecosystem dynamics."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems / LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Organisms and populations of organisms are dependent on their environmental interactions both with other living things and with nonliving factors. Ecosystems are dynamic and can respond to disruptions."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how ecosystems maintain dynamic stability through population cycles, and how disruptions (habitat loss, species removal) can push systems past tipping points into instability.")
    ],
    "cast_items": [
        "Predict patterns of interaction among organisms in ecosystems",
        "Describe how matter and energy flow through ecosystems",
        "Evaluate design solutions for maintaining biodiversity"
    ],
    "cast_questions": [
        ("Multiple Choice:", "In a grassland ecosystem, a disease kills 80% of the rabbit population. Which of the following is the most likely short-term effect on other species in the ecosystem?"),
        ("Constructed Response:", "A state park manager is considering reintroducing wolves to control an overpopulated deer herd. Using ecosystem concepts, predict what would happen to the deer population, vegetation, and overall biodiversity if wolves were reintroduced.")
    ],
    "background_intro": "Ecology is the study of how organisms interact with each other and their environment. Every ecosystem — from your backyard to the Amazon — operates on the same fundamental principles of competition, predation, cooperation, and energy flow.",
    "background_sections": [
        ("Predator-Prey Dynamics", "Predator and prey populations naturally cycle in a predictable pattern: when prey is abundant, predators thrive and increase. More predators reduce prey numbers. Fewer prey causes predators to decline. Fewer predators allows prey to recover. This Lotka-Volterra cycle repeats indefinitely in a healthy ecosystem. The famous example is the lynx and snowshoe hare cycle in Canada, documented over 100+ years."),
        ("Trophic Cascades", "When a top predator is removed, the effects cascade through the entire food web. In Yellowstone, removing wolves caused elk to overgraze riverbanks, which caused erosion, which degraded streams, which reduced fish populations, which affected bears and eagles. When wolves were reintroduced in 1995, the entire ecosystem recovered — even the rivers changed course. This is called a trophic cascade."),
        ("Carrying Capacity", "Every environment has a maximum population it can support — its carrying capacity. This limit is determined by available food, water, space, and shelter. When a population exceeds carrying capacity, individuals compete for scarce resources, death rates increase, and the population crashes. Habitat loss reduces carrying capacity, making population crashes more likely."),
        ("Biodiversity and Resilience", "Ecosystems with more species are more resilient to disturbance. If one species is lost in a diverse ecosystem, others can fill its ecological role. In a simple ecosystem with few species, losing one can collapse the whole system. This is why biodiversity conservation is critical — it's not just about saving individual species, it's about maintaining ecosystem function for all life, including humans.")
    ],
    "lever_L": "Students identify predator population, prey population, habitat size, and resource availability as the key components driving ecosystem dynamics.",
    "lever_E": "Students discover the cyclical relationships: prey positively affects predators (more food), predators negatively affect prey (consumption), and both depend positively on habitat and resources.",
    "lever_V": "Students build a model showing how predator-prey cycles emerge from simple component interactions and how external changes disrupt these cycles.",
    "lever_Ev": "Students run balanced, predator-removal, and habitat-loss scenarios to observe how ecosystems respond to different types of disruption.",
    "lever_R": "Students add invasive species or decomposer activity to explore more complex ecosystem interactions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with vibrant ecosystem imagery", "say": "Right now, in every yard and park and forest, there's a war happening that you can't see.", "do": "Show a time-lapse video of a backyard ecosystem or a nature documentary clip.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're going to model the invisible battles that keep ecosystems alive.", "do": "Have students read objectives. Pre-teach 'biodiversity,' 'carrying capacity,' and 'trophic level.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do ecosystems stay balanced?", "say": "What would happen if all the predators in your backyard disappeared? It seems like prey animals would be happy — but would they?", "do": "Quick write: Students predict what happens if all predators are removed. Most will be wrong!", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model a real ecosystem and then BREAK it to see what happens.", "do": "Preview LEVER steps. Tell students they'll be ecosystem managers making life-or-death decisions.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for ecosystem model", "say": "What factors determine whether an ecosystem stays balanced or collapses?", "do": "Guide sorting. Discuss why habitat size and resources are external (environment), while populations are internal (they change in response).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Here's the mind-bending part: more predators is actually GOOD for the ecosystem, not bad.", "do": "Draw the cycle on the board: prey up → predators up → prey down → predators down → repeat.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's see what happens when we remove all predators. Paradise for prey — or disaster?", "do": "Students predict, then run all three scenarios. The predator-removal result is counterintuitive and powerful.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Predators don't just kill prey — they SAVE ecosystems. That's why losing wolves was a catastrophe for Yellowstone.", "do": "Share the Yellowstone wolf reintroduction story. Connect to model results.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Biodiversity rescue plan", "say": "A nature preserve is collapsing. You're the ecologists. Use your model to design a rescue plan.", "do": "Distribute ecosystem data sheets. Groups design restoration plans with model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Habitat Size and Resource Availability are external because they represent environmental conditions that exist independent of the organisms — they set the stage for the ecosystem. Predator Population and Prey Population are internal because they are the living components of the ecosystem that change dynamically in response to each other and to environmental conditions.",
    "relationships": [
        ("Prey Population to Predator Population", "POSITIVE (+)", "More prey means more food available for predators, allowing predator populations to grow. When prey is abundant, predators reproduce more and survive longer."),
        ("Predator Population to Prey Population", "NEGATIVE (-)", "More predators consume more prey, reducing the prey population. This creates the classic predator-prey cycle where both populations oscillate."),
        ("Habitat Size to Carrying Capacity", "POSITIVE (+)", "Larger habitat provides more resources, shelter, and territory, increasing the maximum population the environment can support for both predators and prey.")
    ],
    "sim_answers": [
        ("Predator Removal Scenario", "When predators are removed, prey populations initially skyrocket — but then crash dramatically. Without predators controlling their numbers, prey overshoot the carrying capacity, deplete their food resources, and suffer a massive population crash. The model shows that predators STABILIZE prey populations by preventing overshoot — removing them is actually bad for prey in the long run."),
        ("Habitat Loss Scenario", "At 25% habitat, carrying capacity drops for both species. Prey populations shrink to fit the smaller habitat, and predator populations shrink even more because there are fewer prey. If habitat shrinks enough, predator populations may drop below the minimum viable population and go extinct — triggering the same cascade as predator removal.")
    ],
    "reflection_exemplars": [
        ("Why do populations cycle instead of staying constant?", "Populations cycle because of TIME DELAYS in the system. When prey increases, predators don't increase instantly — it takes time to reproduce. During that delay, prey keeps growing. When predators finally catch up, they overshoot and eat too many prey. Then predators decline because food is scarce, giving prey time to recover. The cycle repeats because each population's response is always slightly delayed behind the other's."),
        ("What happened with Yellowstone wolves?", "When wolves were removed from Yellowstone in the 1920s, elk populations exploded. Without fear of wolves, elk overgrazed riverbanks, destroying willow and aspen trees. Without trees, riverbanks eroded, streams widened, water warmed, and fish declined. Beavers disappeared because they need willows. When wolves were reintroduced in 1995, elk moved away from rivers (fear effect). Trees regrew, beavers returned, streams narrowed, and the entire ecosystem recovered. Wolves literally changed the rivers.")
    ],
    "stem_intro": "Present the degraded nature preserve scenario: 60% habitat loss, no wolves, deer explosion, vegetation overgrazing, declining bird species, degrading streams. Your team must prioritize interventions using model evidence.",
    "stem_concepts": [
        ("Trophic Cascade", "When changes at the top of a food web cascade down through every level. Removing a top predator doesn't just help prey — it can transform the entire ecosystem, even affecting rivers and landscapes."),
        ("Minimum Viable Population", "The smallest population size that can survive long-term. Below this number, inbreeding, random events, and inability to find mates lead to extinction. For large predators, this is typically 50-500 individuals."),
        ("Wildlife Corridors", "Strips of habitat connecting isolated nature preserves. These allow animals to move between areas, maintaining genetic diversity and allowing populations to respond to environmental changes.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan identifies key species, uses model evidence for all interventions, includes timeline and monitoring strategy, addresses multiple trophic levels"),
        ("Proficient (3)", "Plan addresses at least two interventions with model evidence and explains expected ecosystem effects"),
        ("Developing (2)", "Plan mentions conservation but doesn't justify interventions with ecosystem model evidence"),
        ("Beginning (1)", "Plan is incomplete or doesn't demonstrate understanding of ecosystem interactions")
    ],
    "support": [
        "Provide a simple food web diagram for the preserve showing connections between species",
        "Use physical tokens (colored chips) to simulate predator-prey interactions on a tabletop 'habitat'",
        "Sentence frames: 'When predator population increases, prey population __ because __'"
    ],
    "extensions": [
        "Research the Yellowstone wolf reintroduction and create a timeline of ecosystem changes",
        "Investigate how invasive species like zebra mussels or Asian carp disrupt ecosystem balance",
        "Design a biodiversity survey protocol for your school grounds — how many species can you identify?"
    ],
    "cross_curr": [
        ("Math", "Graph predator-prey population data from the Lotka-Volterra model and calculate the cycle period"),
        ("ELA", "Write a persuasive letter to a senator arguing for increased funding for wildlife corridors, using ecosystem evidence"),
        ("Social Studies", "Research how indigenous communities managed ecosystems sustainably for thousands of years before European colonization")
    ],
    "misconceptions": [
        ("Predators are bad for ecosystems", "Predators are ESSENTIAL for ecosystem health. They prevent prey from overshooting carrying capacity, keep ecosystems balanced, and maintain biodiversity. Removing top predators consistently leads to ecosystem degradation. The Yellowstone wolf story is the most famous demonstration of this principle.", "Ask: If predators are bad, why did Yellowstone get WORSE without wolves and BETTER when wolves returned?"),
        ("Ecosystems will balance themselves no matter what", "While ecosystems are resilient to small disturbances, they have tipping points beyond which they cannot recover. If habitat loss, pollution, or species removal pushes an ecosystem past its tipping point, it can collapse to a fundamentally different state that may take centuries to recover — if it can recover at all.", "Show examples of ecosystem collapse: deforested Amazon turning to grassland, coral reefs dying to algae fields. Some changes are not easily reversible."),
        ("Only large animals matter in ecosystems", "Every species plays a role, and some of the most important are the smallest. Insects pollinate plants, decomposers recycle nutrients, bacteria fix nitrogen, and plankton produce half the world's oxygen. Losing a 'small' species can have cascading effects just as dramatic as losing a large predator.", "Ask: What happens if all the bees disappear? 35% of food crops depend on bee pollination. Small organisms, massive impact.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
