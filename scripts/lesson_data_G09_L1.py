#!/usr/bin/env python3
"""Complete lesson data for G09L1-L01 through G09L1-L10 (Grade 9 Level 1: Foundations of Computational Modeling)"""

L01 = {
    "id": "G09L1-L01",
    "title": "Why Do Athletes Collapse in the Heat?",
    "subtitle": "Modeling Homeostasis and the Body's Breaking Point",
    "ngss": "HS-LS1-3",
    "ngss_desc": "Plan and conduct an investigation to provide evidence that feedback mechanisms maintain homeostasis.",
    "big_question": "Why do some athletes collapse during games while others playing the same sport are fine?",
    "objectives": [
        "Model how the body uses feedback mechanisms to regulate core temperature during physical activity",
        "Explain how sweat rate, hydration, and exertion interact to maintain or disrupt homeostasis",
        "Predict the conditions under which an athlete's thermoregulation system will fail",
        "Analyze how external factors like hydration can shift the tipping point of heat-related illness"
    ],
    "vocabulary": [
        ("Homeostasis", "The body's ability to maintain stable internal conditions — like temperature, blood sugar, and pH — even when the external environment changes"),
        ("Thermoregulation", "The biological process by which the body maintains its core temperature within a safe range, primarily through sweating and blood vessel dilation"),
        ("Feedback Mechanism", "A biological loop where the output of a system influences its own input — negative feedback stabilizes, positive feedback amplifies"),
        ("Heat Exhaustion", "A dangerous condition caused by the body's inability to cool itself, marked by heavy sweating, rapid pulse, dizziness, and potential organ damage")
    ],
    "components": [
        ("Core Temperature", "The internal temperature of the body, normally maintained around 37°C (98.6°F); rises with exertion and falls with cooling", False),
        ("Sweat Rate", "The volume of sweat produced per hour by the body to cool itself through evaporative cooling", False),
        ("Hydration Level", "The amount of available water in the body, which decreases as sweat is produced and must be replenished by drinking fluids", True),
        ("Physical Exertion", "The intensity of physical activity, which generates metabolic heat and increases the body's demand for cooling", True)
    ],
    "think_about_it": "When Physical Exertion is high and Hydration Level drops, what happens to the body's ability to produce sweat and regulate Core Temperature? Where does the feedback loop break?",
    "scenarios": [
        ("Moderate Exercise, Well Hydrated", "Set Physical Exertion to moderate and Hydration Level to high — observe how the body maintains homeostasis"),
        ("Intense Exercise, Dehydrated", "Set Physical Exertion to maximum and Hydration Level to low — observe the cascade to heat exhaustion"),
        ("Gradual Dehydration", "Start Hydration Level high and gradually reduce it while keeping exertion steady — find the tipping point")
    ],
    "sim_scenarios": [
        ("Moderate & Hydrated", "Moderate exertion, high hydration", "What do you predict will happen to Core Temperature when the athlete is well-hydrated during moderate exercise?"),
        ("Intense & Dehydrated", "Maximum exertion, low hydration", "What do you predict happens to Sweat Rate when the body runs out of water during intense exercise?"),
        ("Gradual Dehydration", "Steady exertion, declining hydration", "At what point do you predict the body's cooling system will fail?")
    ],
    "discoveries": [
        "The body's thermoregulation is a negative feedback loop — rising temperature triggers sweating, which cools the body back down",
        "Dehydration breaks the feedback loop because the body can't produce sweat without water, causing temperature to spike",
        "There's a critical tipping point where the cooling system fails — core temperature rises uncontrollably, leading to heat stroke",
        "Individual differences in fitness, acclimatization, and hydration habits explain why some athletes collapse while others don't"
    ],
    "answer": "Athletes collapse when their body's negative feedback loop for temperature regulation breaks down. High exertion generates enormous heat, which normally triggers sweating to cool the body. But when hydration drops too low, the body can't produce enough sweat. Core temperature spirals upward past the tipping point, and the athlete's organs start shutting down — that's heat stroke.",
    "stem_title": "Design a Heat Safety Alert System",
    "stem_mission": "Design a wearable or sideline monitoring system that tracks athlete biometrics and alerts coaches before heat-related illness occurs.",
    "stem_scenario": "A high school athletic department has had three heat-related incidents in two years. The principal has hired your team to design a monitoring system that can predict when an athlete is approaching dangerous territory and alert the coaching staff before collapse occurs.",
    "stem_questions": [
        "What biometric indicators would your system monitor in real time?",
        "How would you determine the threshold for triggering an alert?",
        "What role does individual variation play in setting safety limits?"
    ],
    "stem_design_qs": [
        "What sensors would you need and where would they be placed on the athlete?",
        "How would the system communicate alerts to coaches during a game?",
        "How would you account for differences in body size, fitness level, and acclimatization?",
        "What data would you display on the coach's dashboard?"
    ],
    "career": "Sports Physiologists study how the body responds to physical activity and environmental stress. They work with professional sports teams, military programs, and research institutions, earning $60,000–$120,000/year.",
    "images": {
        "cover": ("G09L1-L01-cover.png", "A photorealistic, cinematic image of diverse high school athletes on a football field in intense summer heat, heat waves visible rising from the turf, one athlete bent over with hands on knees showing exhaustion while athletic trainers rush over with water, dramatic lighting"),
        "landscape": ("G09L1-L01-landscape.png", "A diverse group of 14-15 year old students in a modern science lab examining thermal imaging displays showing body heat maps during exercise, engaged and curious expressions, natural classroom lighting"),
        "modeling": ("G09L1-L01-modeling.png", "A diverse group of 14-15 year old students working on laptops building computational models of body temperature regulation, modern classroom with anatomy posters, collaborative atmosphere"),
        "discussion": ("G09L1-L01-discussion.png", "A teacher leading an animated discussion with diverse 14-15 year old students about homeostasis, a diagram of the thermoregulation feedback loop displayed on a smartboard, students raising hands"),
        "stem": ("G09L1-L01-stem.png", "Diverse 14-15 year old students designing a wearable heat monitoring prototype using sensors and microcontrollers, collaborative group work at lab tables with electronics components")
    },
    "pre_assessment": [
        "Why do you think some athletes collapse from the heat while others on the same team are fine?",
        "What happens inside your body when you get too hot during exercise?",
        "Draw a diagram showing how you think the body cools itself during intense physical activity.",
        "What is homeostasis and why is it important for survival?"
    ],
    "extend_components": [
        ("Ambient Temperature", "The external air temperature and humidity, which affects how efficiently sweat can evaporate and cool the body"),
        ("Blood Volume", "The total volume of blood circulating in the body, which decreases with dehydration and reduces the body's ability to transport heat"),
        ("Acclimatization Level", "How adapted an athlete's body is to exercising in heat, which improves sweating efficiency and reduces strain")
    ],
    "reflections": [
        "How does your model demonstrate that homeostasis depends on negative feedback loops?",
        "What happens in your model when the feedback loop is broken by dehydration?",
        "Why might two athletes of the same fitness level respond differently to the same heat conditions?",
        "How could coaches use your model to design safer practice schedules?",
        "What are the limitations of modeling a complex biological system with only four components?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan investigations using their model to test how different combinations of exertion and hydration affect thermoregulation outcomes."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "Feedback mechanisms maintain the body's internal conditions within a range that supports life, including thermoregulation through sweating and blood vessel dilation."),
        ("Crosscutting Concept", "Stability and Change", "Students model how negative feedback maintains homeostatic stability and identify the conditions that push the system past its tipping point.")
    ],
    "cast_items": [
        "Model how negative feedback mechanisms maintain body temperature during exercise",
        "Investigate the relationship between hydration, sweat rate, and thermoregulation failure",
        "Predict conditions under which homeostasis breaks down using computational models"
    ],
    "cast_questions": [
        ("Multiple Choice:", "An athlete's core temperature rises during a game but returns to normal during halftime. Which feedback mechanism best explains this observation?"),
        ("Constructed Response:", "Using your model, explain why an athlete who is dehydrated is more likely to experience heat stroke than one who is well-hydrated, even if they are performing at the same intensity level.")
    ],
    "background_intro": "The human body is a remarkable self-regulating machine. Every second, billions of biochemical reactions generate heat as a byproduct. The thermoregulatory system must continuously dissipate this heat to keep core temperature within a narrow safe range — typically 36.5–37.5°C. When this system fails, the consequences can be life-threatening.",
    "background_sections": [
        ("Thermoregulation Basics", "The hypothalamus acts as the body's thermostat, detecting blood temperature and triggering cooling responses. When core temperature rises, the hypothalamus signals sweat glands to produce sweat and blood vessels near the skin to dilate, increasing heat loss through evaporation and radiation. This is a classic negative feedback loop."),
        ("The Role of Hydration", "Sweat is about 99% water. An athlete can lose 1-2 liters of sweat per hour during intense exercise. When fluid loss exceeds intake, blood volume drops, making it harder for the cardiovascular system to transport heat from muscles to the skin surface. The body's cooling capacity diminishes rapidly with dehydration."),
        ("Heat-Related Illness Spectrum", "Heat illness exists on a continuum: heat cramps (muscle spasms from electrolyte loss), heat exhaustion (heavy sweating, weakness, nausea — body still attempting to cool), and heat stroke (core temp above 40°C, sweating stops, organ damage begins). Heat stroke is a medical emergency with a mortality rate of 10-50% if untreated."),
        ("Individual Variation", "Not all athletes respond to heat the same way. Factors include body composition, cardiovascular fitness, heat acclimatization (which takes 10-14 days of gradual exposure), hydration habits, medication use, sleep quality, and genetics. This explains why one player collapses while teammates seem fine.")
    ],
    "lever_L": "Students identify core temperature, sweat rate, hydration level, and physical exertion as the key components of the body's thermoregulation system.",
    "lever_E": "Students determine that physical exertion increases core temperature, which increases sweat rate, which decreases hydration level — and that low hydration breaks the cooling loop.",
    "lever_V": "Students build a computational model showing the negative feedback loop of thermoregulation and the conditions under which it fails.",
    "lever_Ev": "Students run moderate/hydrated, intense/dehydrated, and gradual dehydration scenarios to test their model and identify the tipping point.",
    "lever_R": "Students add ambient temperature, blood volume, or acclimatization level to explore more realistic thermoregulation dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic image of athletes in extreme heat", "say": "In 2022, over 9,000 high school athletes were treated for heat-related illness. Some of them died. Why?", "do": "Show a brief news clip or headline about a student athlete heat collapse. Let the room react.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling something your body does every second of every day — regulate its own temperature.", "do": "Have students read objectives. Pre-teach 'homeostasis' and 'feedback mechanism.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do some athletes collapse while others are fine?", "say": "Same team, same field, same temperature. So why does one player go down while another is fine?", "do": "Quick-write: Students list 3 factors they think determine who collapses. Share out.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to build a model that can actually predict when an athlete is in danger.", "do": "Preview each LEVER step. Emphasize that feedback loops are the key to understanding this.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for thermoregulation model", "say": "What are the key players in the body's cooling system? Which ones can you control?", "do": "Guide sorting of external vs. internal components. Discuss why hydration is external (you can control it).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When you sprint in 100-degree heat, what chain reaction happens inside your body?", "do": "Help students trace the feedback loop. Identify where the loop breaks.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results", "say": "Let's find the exact point where the body's cooling system fails.", "do": "Students predict tipping points first, then run simulations. Compare results.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model exploration", "say": "So what's the difference between heat exhaustion and heat stroke? Your model just showed you.", "do": "Lead discussion connecting model findings to real athletic scenarios. Discuss prevention.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Heat safety alert system design challenge", "say": "Your school just hired you to make sure no athlete ever collapses on this field again.", "do": "Groups design monitoring systems using model insights. Present prototypes.", "time": "12 min"}
    ],
    "sort_reasoning": "Physical Exertion and Hydration Level are external components because they represent inputs that can be controlled or adjusted — an athlete chooses how hard to work and how much to drink. Core Temperature and Sweat Rate are internal because they are outputs of the body's thermoregulatory system that change in response to the external inputs.",
    "relationships": [
        ("Physical Exertion to Core Temperature", "POSITIVE (+)", "Higher physical exertion generates more metabolic heat, directly raising core temperature. Muscle contractions convert chemical energy to kinetic energy and heat."),
        ("Core Temperature to Sweat Rate", "POSITIVE (+)", "As core temperature rises, the hypothalamus triggers increased sweat production to cool the body through evaporative cooling."),
        ("Sweat Rate to Hydration Level", "NEGATIVE (-)", "Higher sweat rate depletes the body's water reserves faster, decreasing hydration level. Without fluid replacement, the body loses its ability to cool itself.")
    ],
    "sim_answers": [
        ("Moderate & Hydrated Scenario", "When Physical Exertion is moderate and Hydration Level is high, Core Temperature rises slightly but the feedback loop works effectively. Sweat Rate increases to match heat production, Hydration Level decreases slowly, and Core Temperature stabilizes within the safe range. The system maintains homeostasis."),
        ("Intense & Dehydrated Scenario", "When Physical Exertion is at maximum and Hydration Level is low, the feedback loop breaks down. Core Temperature rises rapidly, Sweat Rate initially increases but then drops as the body runs out of water. With no evaporative cooling, Core Temperature spirals upward uncontrollably — this is the onset of heat stroke.")
    ],
    "reflection_exemplars": [
        ("How does the feedback loop break?", "The thermoregulation feedback loop breaks when hydration drops too low. Normally, rising core temperature triggers more sweating, which cools the body. But sweating requires water. When the body is dehydrated, it can't produce enough sweat, so temperature keeps rising with nothing to bring it back down. The negative feedback loop becomes a positive one — heat generates more heat."),
        ("Why do some athletes collapse while others don't?", "Individual variation in hydration habits, fitness level, heat acclimatization, and body composition means each athlete's tipping point is different. A well-hydrated, heat-acclimatized athlete can maintain homeostasis much longer than a dehydrated, unacclimatized one — even in identical conditions. The model shows that the threshold isn't the same for everyone.")
    ],
    "stem_intro": "Present the challenge: Your school's athletic department needs a system that prevents heat-related illness. Your team will design a monitoring solution that tracks key biometrics and alerts coaching staff before an athlete reaches dangerous territory.",
    "stem_concepts": [
        ("Biometric Monitoring", "Wearable sensors can track heart rate, skin temperature, sweat rate, and motion in real time. These data streams can be combined with environmental data to estimate heat stress risk."),
        ("Threshold Detection", "Alert systems need carefully calibrated thresholds — too sensitive and coaches ignore constant false alarms, too lenient and athletes collapse before warnings trigger."),
        ("Individual Baselines", "Effective monitoring requires knowing each athlete's baseline values. A resting heart rate of 80 might be normal for one athlete but a sign of stress for another.")
    ],
    "stem_eval": [
        ("Expert (4)", "System monitors multiple biometrics, uses individualized thresholds, provides graduated alerts, and includes evidence-based justification from model data"),
        ("Proficient (3)", "System monitors key biometrics and alerts coaches with reasonable thresholds based on model findings"),
        ("Developing (2)", "System monitors some indicators but thresholds are not well justified or alerts lack graduation"),
        ("Beginning (1)", "System is incomplete or does not connect monitoring to the thermoregulation model")
    ],
    "support": [
        "Provide a simplified diagram of the thermoregulation feedback loop for reference",
        "Use colored arrows (red = positive, blue = negative) to help visualize feedback relationships",
        "Sentence frames: 'When __ increases, __ responds by __ because __'"
    ],
    "extensions": [
        "Research how military training programs prevent heat casualties and compare their protocols to your model",
        "Investigate how humidity affects evaporative cooling and add an environmental factor to your model",
        "Compare thermoregulation strategies in different organisms — how do dogs, elephants, and desert lizards cool themselves?"
    ],
    "cross_curr": [
        ("Math", "Calculate fluid loss rates and determine optimal hydration schedules for different exercise intensities"),
        ("ELA", "Research and write a persuasive essay arguing for mandatory hydration protocols in high school athletics"),
        ("Health/PE", "Design a pre-season heat acclimatization protocol based on sports physiology research")
    ],
    "misconceptions": [
        ("Sweating means you're out of shape", "Sweating is actually a sign of an efficient cooling system. Well-trained athletes often sweat MORE than untrained people because their bodies have adapted to dissipate heat more effectively. Less sweating during intense exercise can actually be a danger sign.", "Compare: Who sweats more during the same workout — the marathoner or the couch potato? The marathoner, because their cooling system is better trained."),
        ("Drinking water when thirsty is enough", "By the time you feel thirsty, you're already 1-2% dehydrated, which is enough to impair performance and thermoregulation. Thirst is a lagging indicator — the body needs water before the brain signals the sensation of thirst.", "Try this thought experiment: If your car's temperature gauge only turned on after the engine was already overheating, would that be a good warning system?"),
        ("Heat stroke only happens in extreme heat", "Heat stroke can occur at surprisingly moderate temperatures when humidity is high, exertion is intense, or the athlete is dehydrated. Multiple cases have occurred at temperatures below 80°F. It's the combination of factors, not just air temperature, that matters.", "Show cases of heat illness at 75°F with high humidity — ask students why temperature alone isn't a reliable predictor.")
    ]
}

L02 = {
    "id": "G09L1-L02",
    "title": "The Vaping Crisis: What's Really Happening to Your Lungs?",
    "subtitle": "Modeling Chemical Damage to the Respiratory System",
    "ngss": "HS-LS1-2",
    "ngss_desc": "Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms.",
    "big_question": "If vaping is \"just water vapor,\" why are teenagers ending up in the hospital?",
    "objectives": [
        "Model how chemical exposure from vaping damages lung cells over time",
        "Explain the relationship between nicotine concentration, inflammation, and lung cell health",
        "Predict how chronic vaping leads to progressive respiratory system damage",
        "Analyze why short-term effects may not reflect long-term consequences of vaping"
    ],
    "vocabulary": [
        ("Inflammation Response", "The body's immune reaction to injury or irritation — sending white blood cells and fluids to the damaged area, causing swelling, redness, and reduced function"),
        ("Epithelial Cells", "The thin layer of cells lining the lungs' airways and alveoli that facilitate gas exchange and protect against pathogens"),
        ("Chronic Exposure", "Repeated contact with a harmful substance over weeks, months, or years — causing cumulative damage that may not be immediately apparent"),
        ("Alveolar Damage", "Destruction or impairment of the tiny air sacs in the lungs where oxygen and carbon dioxide are exchanged with the bloodstream")
    ],
    "components": [
        ("Nicotine Concentration", "The amount of nicotine and associated chemicals delivered to the lungs with each vaping session", True),
        ("Chemical Exposure Duration", "The total time the lung tissue has been exposed to vaping chemicals — from days to years of use", True),
        ("Lung Cell Health", "The structural integrity and function of epithelial cells lining the airways and alveoli", False),
        ("Inflammation Response", "The intensity of the immune system's reaction to chemical irritation in the lungs", False)
    ],
    "think_about_it": "If Nicotine Concentration is high and Chemical Exposure Duration increases over months, what happens to the cycle between Inflammation Response and Lung Cell Health? Can the lungs recover?",
    "scenarios": [
        ("Occasional Use", "Set Nicotine Concentration low and Chemical Exposure Duration short — observe Lung Cell Health"),
        ("Daily Heavy Use", "Set Nicotine Concentration high and Chemical Exposure Duration long — observe the damage cascade"),
        ("Quit After 6 Months", "Set high exposure for a period, then reduce Nicotine Concentration to zero — can the lungs recover?")
    ],
    "sim_scenarios": [
        ("Occasional Use", "Low nicotine, short duration", "What do you predict happens to Lung Cell Health with occasional, low-level vaping?"),
        ("Daily Heavy Use", "High nicotine, long duration", "What do you predict happens to the Inflammation Response with chronic, heavy vaping?"),
        ("Quit After 6 Months", "High exposure followed by cessation", "Do you predict Lung Cell Health will fully recover after quitting? Why or why not?")
    ],
    "discoveries": [
        "Nicotine and vaping chemicals directly damage epithelial cells, reducing their ability to protect the lungs and facilitate gas exchange",
        "Chronic inflammation creates a destructive cycle — the immune response meant to heal actually causes additional tissue damage over time",
        "The damage is cumulative and not always reversible — some lung cell damage becomes permanent after prolonged exposure",
        "Short-term effects are mild enough to ignore, which is why many vapers don't realize the damage until it's significant"
    ],
    "answer": "Vaping is NOT just water vapor — it delivers nicotine, heavy metals, and volatile organic compounds directly into the lungs. These chemicals damage the epithelial cells lining the airways and trigger chronic inflammation. The inflammation meant to protect the lungs actually accelerates tissue destruction in a vicious cycle. Over time, this cascade reduces lung function, and some damage becomes permanent.",
    "stem_title": "Design a Vaping Impact Public Health Campaign",
    "stem_mission": "Create a science-based public health campaign that uses data from your model to show teens the real biological impact of vaping on lung tissue.",
    "stem_scenario": "The local health department has noticed a 40% increase in teen vaping and wants to launch a campaign that goes beyond 'just say no.' They need scientifically accurate materials that show WHAT actually happens inside the lungs. Your team has been hired to create the campaign using your model data.",
    "stem_questions": [
        "What biological evidence from your model is most compelling for convincing teens?",
        "How can you present cumulative damage data in a way that resonates with 14-15 year olds?",
        "What makes science-based messaging more effective than fear-based messaging?"
    ],
    "stem_design_qs": [
        "What format will your campaign take — social media, poster, video, interactive website?",
        "How will you visualize the damage cascade from your model in an engaging way?",
        "What data from your simulations will you use as evidence?",
        "How will you address the misconception that vaping is harmless?"
    ],
    "career": "Pulmonologists are physicians who specialize in respiratory diseases and lung health. They diagnose and treat conditions from asthma to EVALI (E-cigarette/Vaping-Associated Lung Injury), earning $300,000–$500,000/year. Respiratory therapists who work directly with patients earn $55,000–$75,000/year.",
    "images": {
        "cover": ("G09L1-L02-cover.png", "A photorealistic, cinematic close-up of a healthy pink human lung next to a damaged, inflamed lung tissue comparison, medical imaging style with dramatic lighting, educational medical photography"),
        "landscape": ("G09L1-L02-landscape.png", "A diverse group of 14-15 year old students in a modern biology lab examining lung tissue models and microscope slides, focused and engaged expressions, bright lab lighting"),
        "modeling": ("G09L1-L02-modeling.png", "A diverse group of 14-15 year old students working on laptops building computational models of lung cell damage, modern classroom with respiratory system diagrams on the walls"),
        "discussion": ("G09L1-L02-discussion.png", "A teacher leading a discussion with diverse 14-15 year old students about respiratory health, a diagram of alveoli and inflammation displayed on a smartboard, students actively participating"),
        "stem": ("G09L1-L02-stem.png", "Diverse 14-15 year old students creating public health campaign materials with laptops and art supplies, infographics and posters about lung health visible on their screens and tables")
    },
    "pre_assessment": [
        "What do you think is actually inside vape aerosol — is it just water vapor?",
        "Why do you think vaping-related lung injuries have become so common in teens?",
        "Draw what you think happens to lung cells when exposed to vaping chemicals.",
        "How do you think the body responds to foreign chemicals entering the lungs?"
    ],
    "extend_components": [
        ("Oxygen Exchange Rate", "The efficiency of gas exchange in the alveoli, which decreases as cells are damaged and airways become inflamed"),
        ("Mucociliary Clearance", "The lung's self-cleaning mechanism using mucus and tiny hair-like cilia to sweep out particles and pathogens"),
        ("Immune Cell Activity", "The concentration and behavior of white blood cells in lung tissue, which increases with chronic chemical exposure")
    ],
    "reflections": [
        "How does your model show the difference between short-term and long-term effects of vaping?",
        "Why does the inflammation response — which is meant to protect you — end up causing more damage?",
        "What does your model predict about lung recovery if someone quits vaping after one year versus five years?",
        "How might your model change if you added oxygen exchange rate as a component?",
        "What are the limitations of modeling complex biological damage with only four components?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model to illustrate how chemical exposure progressively damages the hierarchical organization of lung tissue."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "Multicellular organisms have hierarchical structural organization, in which any one system is made up of numerous parts that interact to carry out life functions."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from chemical exposure to cellular damage to systemic inflammation and reduced lung function.")
    ],
    "cast_items": [
        "Model how chemical exposure damages the hierarchical structure of the respiratory system",
        "Explain the feedback loop between inflammation and cell damage in chronically exposed lungs",
        "Predict long-term health outcomes based on vaping frequency and duration"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student has been vaping daily for one year. Which model prediction best explains why their lung function test shows a 15% decrease even though they feel fine?"),
        ("Constructed Response:", "Using your model, explain the biological mechanism by which chronic vaping leads to progressive lung damage. Include the roles of inflammation and epithelial cell health in your explanation.")
    ],
    "background_intro": "The human respiratory system is a marvel of biological engineering — 300 million alveoli provide a gas exchange surface area the size of a tennis court. But this delicate tissue was never designed to handle the chemical cocktail delivered by e-cigarettes. Understanding the hierarchical organization of the lungs is essential for understanding how vaping causes damage at every level.",
    "background_sections": [
        ("Respiratory System Organization", "The respiratory system follows a hierarchical structure: the trachea branches into bronchi, which branch into bronchioles, which terminate in alveoli. Each level is lined with specialized epithelial cells. Alveoli are surrounded by capillaries where oxygen enters the blood and CO2 is removed. This organization maximizes surface area for gas exchange."),
        ("What's Actually in Vape Aerosol", "E-cigarette aerosol is not water vapor. It contains nicotine, propylene glycol, vegetable glycerin, formaldehyde, acrolein, heavy metals (lead, nickel, chromium), and ultrafine particles. When heated, these chemicals undergo pyrolysis, creating new toxic compounds. The ultrafine particles penetrate deep into the alveoli where there is no mucociliary clearance."),
        ("Inflammation as a Double-Edged Sword", "When chemicals damage lung cells, the immune system responds with inflammation — sending white blood cells, releasing cytokines, and increasing blood flow to the area. Short-term, this helps clear damage. But chronic inflammation causes collateral damage: healthy cells are destroyed, scar tissue forms, and the inflammatory molecules themselves damage surrounding tissue. This creates a self-reinforcing cycle of damage."),
        ("EVALI and Youth Vaping", "In 2019, EVALI (E-cigarette or Vaping Product Use-Associated Lung Injury) hospitalized over 2,800 people and killed 68 in the US. Most were under 35. Even without acute EVALI, chronic vaping causes measurable reductions in lung function, increased respiratory symptoms, and cellular changes that may increase cancer risk. Adolescent lungs are especially vulnerable because they're still developing.")
    ],
    "lever_L": "Students identify nicotine concentration, chemical exposure duration, lung cell health, and inflammation response as the key components of the vaping damage system.",
    "lever_E": "Students determine that nicotine concentration decreases lung cell health, exposure duration increases inflammation, and inflammation further decreases cell health — creating a destructive feedback loop.",
    "lever_V": "Students build a computational model showing how chemical exposure leads to progressive lung damage through the inflammation-damage cycle.",
    "lever_Ev": "Students run occasional use, daily heavy use, and cessation scenarios to compare short-term versus long-term outcomes and recovery potential.",
    "lever_R": "Students add oxygen exchange rate, mucociliary clearance, or immune cell activity to model more complete respiratory system dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with healthy vs. damaged lung comparison", "say": "In 2019, a healthy 17-year-old ended up on life support. The cause? Vaping. And he's not the only one.", "do": "Share a brief EVALI case study. Ask: How can something that seems harmless cause this much damage?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're modeling what actually happens inside your lungs when vape chemicals hit them.", "do": "Have students read objectives. Pre-teach 'inflammation response' and 'epithelial cells.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "If it's just water vapor, why are teens in the hospital?", "say": "Companies say it's harmless. Hospitals say otherwise. Let's find out who's right.", "do": "Anonymous poll: What do you think is in vape aerosol? Compare guesses to the actual chemical list.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a model of your actual lung cells being exposed to these chemicals.", "do": "Preview LEVER steps. Emphasize this is about biological mechanisms, not moral judgments.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for vaping damage model", "say": "What are the key biological players when chemicals enter your lungs?", "do": "Guide sorting. Discuss why nicotine concentration and duration are external (user-controlled).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "Here's where it gets scary — the body's own defense system starts causing MORE damage.", "do": "Help students identify the destructive feedback loop. Use red arrows for damage pathways.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results", "say": "Let's see what happens to lung cells after one month, six months, and two years.", "do": "Students predict damage curves first. Run simulations. Discuss the recovery scenario.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Why didn't the occasional user's lungs recover completely? What does that tell us?", "do": "Connect model findings to real clinical data. Discuss cumulative vs. reversible damage.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Public health campaign design challenge", "say": "The health department needs YOUR data to convince teens. Make it scientifically accurate AND compelling.", "do": "Groups design science-based campaigns using model evidence. Peer review for accuracy.", "time": "12 min"}
    ],
    "sort_reasoning": "Nicotine Concentration and Chemical Exposure Duration are external components because they are determined by the user's vaping behavior — how much they vape and for how long. Lung Cell Health and Inflammation Response are internal because they are biological responses that the body produces in reaction to the external chemical exposure.",
    "relationships": [
        ("Nicotine Concentration to Lung Cell Health", "NEGATIVE (-)", "Higher nicotine and chemical concentrations directly damage epithelial cells lining the airways. The chemicals cause oxidative stress, DNA damage, and cell death in the delicate lung tissue."),
        ("Chemical Exposure Duration to Inflammation Response", "POSITIVE (+)", "Longer exposure duration means the immune system remains activated for extended periods. Chronic exposure leads to persistent, escalating inflammation that never fully resolves."),
        ("Inflammation Response to Lung Cell Health", "NEGATIVE (-)", "Chronic inflammation damages healthy lung cells through collateral damage from immune molecules. The immune response meant to protect the lungs ends up accelerating tissue destruction.")
    ],
    "sim_answers": [
        ("Occasional Use Scenario", "With low Nicotine Concentration and short Chemical Exposure Duration, Lung Cell Health decreases slightly and Inflammation Response is mild. The lungs' repair mechanisms can mostly keep up with the damage, and recovery is possible if exposure stops. However, even low-level exposure causes measurable cellular changes."),
        ("Daily Heavy Use Scenario", "With high Nicotine Concentration over long duration, the model shows a devastating cascade. Lung Cell Health drops dramatically as both direct chemical damage and chronic inflammation compound. The inflammation-damage feedback loop accelerates tissue destruction, and some damage becomes irreversible as scar tissue replaces functional lung tissue.")
    ],
    "reflection_exemplars": [
        ("Why does inflammation make things worse?", "Inflammation is designed for short-term injury repair — white blood cells arrive, clean up damage, and leave. But chronic chemical exposure means inflammation never turns off. The immune molecules (reactive oxygen species, cytokines) that kill damaged cells also destroy healthy neighboring cells. It's like using a flamethrower to put out a candle — the cure becomes worse than the disease."),
        ("Can lungs fully recover after quitting?", "It depends on duration and severity. The model shows that short-term users can recover most lung cell health because the damage hasn't reached the point of permanent scarring. But long-term heavy users sustain irreversible damage — scar tissue (fibrosis) replaces functional lung tissue and cannot regenerate. The earlier someone quits, the more recovery is possible.")
    ],
    "stem_intro": "Present the challenge: A health department needs a science-based campaign showing teens what vaping actually does to lung tissue. Your team will create campaign materials using data from your computational model to replace myths with biological evidence.",
    "stem_concepts": [
        ("Dose-Response Relationships", "The severity of biological damage is related to both the concentration of a substance and the duration of exposure. Higher doses and longer exposure produce more severe effects — but even low doses cause measurable changes."),
        ("Cumulative Damage", "Some biological damage accumulates over time and isn't immediately noticeable. Like sun damage to skin, the effects of vaping on lung cells build up silently until clinical symptoms appear."),
        ("Science Communication", "Effective health campaigns translate complex biological mechanisms into clear, compelling messages. The best campaigns use data visualization, relatable comparisons, and evidence-based claims rather than fear tactics.")
    ],
    "stem_eval": [
        ("Expert (4)", "Campaign uses model data accurately, presents biological mechanisms clearly, addresses common misconceptions, and uses effective science communication techniques"),
        ("Proficient (3)", "Campaign presents accurate scientific information and uses some model data to support claims"),
        ("Developing (2)", "Campaign contains scientific information but lacks clear connection to model evidence or contains minor inaccuracies"),
        ("Beginning (1)", "Campaign is incomplete, scientifically inaccurate, or relies on fear tactics without evidence")
    ],
    "support": [
        "Provide a labeled diagram of lung anatomy showing alveoli, bronchioles, and epithelial cell layers",
        "Use a timeline graphic to help visualize cumulative damage over weeks, months, and years",
        "Sentence frames: 'When __ enters the lungs, the body responds by __, which causes __ over time'"
    ],
    "extensions": [
        "Research the chemical composition of five popular vape brands and compare their potential for lung damage",
        "Investigate how the developing adolescent lung responds differently to chemical exposure compared to adult lungs",
        "Compare the biological mechanisms of vaping damage to those of traditional cigarette smoking"
    ],
    "cross_curr": [
        ("Math", "Analyze dose-response data and create graphs showing the relationship between vaping frequency and measured lung function decline"),
        ("ELA", "Analyze the marketing language used by e-cigarette companies and write a critical response using scientific evidence"),
        ("Health", "Research the addictive properties of nicotine and create an infographic showing the neurological pathway of addiction")
    ],
    "misconceptions": [
        ("Vaping is just water vapor", "E-cigarette aerosol contains nicotine, heavy metals, volatile organic compounds, and ultrafine particles — not water vapor. The base liquids (propylene glycol and vegetable glycerin) break down into formaldehyde and acrolein when heated. These chemicals cause direct cellular damage.", "Show the chemical analysis of vape aerosol side by side with actual water vapor. Ask: Would you inhale formaldehyde if it wasn't hidden in a flavored cloud?"),
        ("If I don't feel sick, it's not hurting me", "Cumulative damage often has no symptoms until it's significant. Like high blood pressure or UV skin damage, vaping causes progressive cellular changes that aren't felt day-to-day but show up on medical tests and eventually as symptoms.", "Analogy: You don't feel a sunburn forming while you're getting it — you feel it hours later. Lung damage works similarly, but over months and years instead of hours."),
        ("Vaping is safe because it's FDA-regulated", "E-cigarettes are regulated as tobacco products, not as safe products. The FDA has authorized very few e-cigarettes and only for adults already addicted to cigarettes as a harm-reduction tool — not as a safe alternative for non-smokers. No e-cigarettes have been approved as safe for youth.", "Compare: Cars are regulated, but they're not safe to drive at 150 mph. Regulation doesn't mean safe — it means there are rules about how dangerous something is allowed to be.")
    ]
}

L03 = {
    "id": "G09L1-L03",
    "title": "Can We Actually Live on Mars?",
    "subtitle": "Modeling Survival in the Most Hostile Environment Humans Have Ever Faced",
    "ngss": "HS-ESS1-2, HS-ETS1-2",
    "ngss_desc": "Construct an explanation of the Big Bang theory based on astronomical evidence including light spectra, motion of distant galaxies, and composition of matter in the universe. Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.",
    "big_question": "What would it actually take to keep humans alive on Mars — and is it even possible?",
    "objectives": [
        "Model the key environmental factors that determine human survival on Mars",
        "Analyze how atmospheric pressure, radiation, water, and temperature interact to affect crop viability",
        "Evaluate the engineering challenges of creating a self-sustaining habitat on Mars",
        "Predict the minimum conditions required for sustained human presence on Mars"
    ],
    "vocabulary": [
        ("Atmospheric Pressure", "The force exerted by gas molecules pressing on a surface — Mars has less than 1% of Earth's atmospheric pressure, making liquid water and unprotected human survival impossible"),
        ("Ionizing Radiation", "High-energy particles from the Sun and cosmic rays that damage DNA and living tissue — Mars lacks the magnetic field and thick atmosphere that protect Earth"),
        ("Regolith", "The layer of loose rock and dust covering Mars' surface, which contains toxic perchlorates and lacks the organic matter and microorganisms found in Earth's soil"),
        ("Bioregenerative Life Support", "A system that uses living organisms — primarily plants — to recycle air, water, and waste in a closed habitat, reducing dependence on resupply from Earth")
    ],
    "components": [
        ("Atmospheric Pressure", "The air pressure inside the habitat, which must be maintained above 6.1 kPa to allow liquid water and above 47.3 kPa for human breathing", True),
        ("Radiation Exposure", "The amount of ionizing radiation reaching the habitat interior, which must be shielded to prevent DNA damage and cancer", True),
        ("Water Availability", "The amount of extractable water from Martian ice deposits and recycled wastewater for drinking, agriculture, and industrial use", True),
        ("Temperature", "The internal habitat temperature, which must be maintained between 18-26°C despite Mars surface temps ranging from -125°C to 20°C", True),
        ("Crop Viability", "The ability of food crops to grow, survive, and produce nutritional yields inside the habitat under controlled conditions", False)
    ],
    "think_about_it": "If any ONE of the external factors — pressure, radiation, water, or temperature — fails, what happens to Crop Viability and the entire colony's food supply? What makes this system so fragile?",
    "scenarios": [
        ("Optimal Habitat", "Set all external factors to ideal levels — observe Crop Viability at peak performance"),
        ("Pressure Breach", "Drop Atmospheric Pressure to Mars surface levels — observe the cascade failure"),
        ("Water Crisis", "Reduce Water Availability to minimal levels — observe how the colony prioritizes survival over growth")
    ],
    "sim_scenarios": [
        ("Optimal Habitat", "All systems functioning at ideal levels", "What do you predict Crop Viability will be when all environmental controls are working perfectly?"),
        ("Pressure Breach", "Atmospheric Pressure drops to near-Mars surface levels", "What do you predict happens to Crop Viability and human survival if the habitat loses pressure?"),
        ("Water Crisis", "Water Availability drops to critical levels", "How do you predict the colony will respond when water becomes scarce?")
    ],
    "discoveries": [
        "Human survival on Mars requires simultaneously solving pressure, radiation, water, temperature, and food challenges — failure of any one system is catastrophic",
        "Crop viability depends on ALL four external factors being within acceptable ranges — it's the weakest link in the survival chain",
        "The system has almost no margin for error — a small change in any variable can cascade into colony-wide failure",
        "Mars colonization is fundamentally an engineering problem, not a discovery problem — we know what needs to happen, we just can't do it all yet"
    ],
    "answer": "Living on Mars is theoretically possible but extraordinarily difficult. The planet offers almost nothing humans need: no breathable air, almost no atmospheric pressure, lethal radiation, temperatures averaging -60°C, and no liquid water on the surface. Every survival requirement must be engineered from scratch inside a sealed habitat. The biggest challenge isn't any single factor — it's that ALL of them must work simultaneously with no room for failure.",
    "stem_title": "Design a Mars Habitat Module",
    "stem_mission": "Design a habitat module that addresses the five critical survival factors and can sustain a crew of six for one year using available Martian resources.",
    "stem_scenario": "NASA has announced the Mars Colony Design Challenge for high school students. Your team must design a habitat module that solves pressure, radiation, water, temperature, and food production simultaneously. The module must use in-situ Martian resources wherever possible and include failure contingency plans.",
    "stem_questions": [
        "How will you maintain atmospheric pressure and what happens if there's a breach?",
        "What materials and methods will you use for radiation shielding?",
        "How will you source and recycle water on Mars?"
    ],
    "stem_design_qs": [
        "What shape and materials will provide the best pressure containment and radiation shielding?",
        "How will you extract water from Martian ice and recycle wastewater?",
        "What crops are best suited for Mars habitat agriculture and how much growing space do six people need?",
        "What backup systems will you include for each critical failure mode?"
    ],
    "career": "Aerospace Engineers design spacecraft, habitats, and life support systems for space missions. They work at NASA, SpaceX, Blue Origin, and defense contractors, earning $80,000–$160,000/year. Astrobiologists who study the potential for life on other planets earn $60,000–$130,000/year.",
    "images": {
        "cover": ("G09L1-L03-cover.png", "A photorealistic, cinematic image of a futuristic Mars habitat dome on the red Martian surface with Earth visible in the dark sky, warm interior lights glowing through the dome showing plants growing inside, dramatic Martian landscape"),
        "landscape": ("G09L1-L03-landscape.png", "A diverse group of 14-15 year old students examining Mars surface samples and terrain models in a modern science lab, Mars posters and NASA imagery on the walls, excited expressions"),
        "modeling": ("G09L1-L03-modeling.png", "A diverse group of 14-15 year old students working on laptops building computational models of Mars habitat conditions, classroom with space exploration imagery and Mars data displays"),
        "discussion": ("G09L1-L03-discussion.png", "A teacher leading a discussion with diverse 14-15 year old students about Mars colonization challenges, a comparison chart of Earth vs. Mars conditions displayed on a smartboard"),
        "stem": ("G09L1-L03-stem.png", "Diverse 14-15 year old students building scale model Mars habitats using craft materials and 3D-printed components, collaborative engineering challenge atmosphere")
    },
    "pre_assessment": [
        "What do you think are the biggest challenges to keeping humans alive on Mars?",
        "How is Mars different from Earth in terms of what humans need to survive?",
        "Draw what you think a Mars habitat would need to include to keep six people alive for a year.",
        "Could we grow food on Mars? What would that require?"
    ],
    "extend_components": [
        ("Energy Production", "The power generation capacity of the habitat using solar panels or nuclear reactors to run life support, heating, and agricultural systems"),
        ("Oxygen Generation", "The production of breathable oxygen through electrolysis of water or CO2 processing from the Martian atmosphere"),
        ("Waste Recycling Efficiency", "How effectively the habitat converts human waste, CO2, and wastewater back into usable resources in a closed-loop system")
    ],
    "reflections": [
        "Why is Mars colonization often described as 'the hardest engineering problem in human history'?",
        "What does your model reveal about the difference between surviving on Mars and thriving on Mars?",
        "Which of the five components is the most critical — and what happens if it fails?",
        "How does your model change when you add energy production or oxygen generation?",
        "What assumptions does your model make that might not hold true on the actual Martian surface?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students construct explanations of Mars survival challenges and design habitat solutions based on computational model evidence."),
        ("Disciplinary Core Idea", "ESS1.B Earth and the Solar System / ETS1.C Optimizing the Design Solution", "Students analyze the conditions on Mars that differ from Earth and engineer solutions to sustain human life."),
        ("Crosscutting Concept", "Systems and System Models", "Students model Mars habitat as a system where multiple interacting components must simultaneously maintain conditions for human survival.")
    ],
    "cast_items": [
        "Model the interdependent environmental factors required for human survival on Mars",
        "Analyze how failure of a single system cascades through the entire habitat",
        "Design engineering solutions based on computational model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A Mars habitat experiences a slow leak that reduces atmospheric pressure by 20% over three days. According to your model, which component would be affected FIRST?"),
        ("Constructed Response:", "Using your model, explain why Mars colonization requires solving all five survival factors simultaneously. What happens when even one factor drops below the critical threshold?")
    ],
    "background_intro": "Mars is the most Earth-like planet in our solar system — and it's still incredibly hostile to human life. With less than 1% of Earth's atmospheric pressure, average temperatures of -60°C, no breathable oxygen, lethal radiation, and no liquid surface water, Mars represents the ultimate engineering challenge: can humans recreate the conditions for life on a world that has none?",
    "background_sections": [
        ("Mars vs. Earth", "Mars has 38% of Earth's gravity, a thin CO2 atmosphere (95.3% CO2) at 0.6% of Earth's pressure, no global magnetic field, and surface temperatures from -125°C to 20°C. A human standing unprotected on Mars would simultaneously suffocate, freeze, be irradiated, and have their blood boil due to low pressure — all within about 15 seconds."),
        ("Atmospheric Pressure Challenge", "Earth's atmospheric pressure is 101.3 kPa. Mars surface pressure is 0.6 kPa. Liquid water requires at least 6.1 kPa; human breathing requires about 47.3 kPa of pressure with appropriate oxygen concentration. Any habitat must maintain this pressure differential against the near-vacuum of Mars — and a breach could be catastrophic."),
        ("Radiation on Mars", "Without Earth's protective magnetic field and thick atmosphere, Mars receives about 2.5 times the radiation astronauts experience on the ISS. Over a two-year stay, colonists would receive enough radiation to significantly increase cancer risk. Shielding options include burying habitats under regolith, using water walls, or developing advanced materials."),
        ("Water and Food Production", "Mars has significant water ice at its poles and underground. Extracting and purifying this water is essential for drinking, agriculture, and producing oxygen through electrolysis. Growing food on Mars requires controlled environments with artificial lighting, recycled water, and processed regolith — a system that must be virtually 100% efficient since resupply from Earth takes 6-9 months.")
    ],
    "lever_L": "Students identify atmospheric pressure, radiation exposure, water availability, temperature, and crop viability as the critical components of the Mars survival system.",
    "lever_E": "Students determine that all four external factors must be within acceptable ranges simultaneously for crop viability to be maintained — and that any single failure cascades through the system.",
    "lever_V": "Students build a computational model showing how Mars habitat conditions interact to determine the feasibility of sustained human presence.",
    "lever_Ev": "Students run optimal, pressure breach, and water crisis scenarios to test their model and identify critical failure thresholds.",
    "lever_R": "Students add energy production, oxygen generation, or waste recycling to model more realistic habitat dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with Mars habitat concept art", "say": "Elon Musk says we'll have people on Mars by 2030. But here's what he doesn't talk about: how do you keep them alive?", "do": "Show a brief video of Mars surface conditions. Let students react to the -60°C average temperature.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today you're engineering a solution to the hardest survival problem in human history.", "do": "Have students read objectives. Pre-teach 'atmospheric pressure' and 'bioregenerative life support.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What would it take to keep humans alive on Mars?", "say": "Forget the movies. On real Mars, you'd be dead in 15 seconds without protection. How do we fix that?", "do": "Earth vs. Mars comparison chart. Students identify what's missing on Mars for human survival.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a model of a Mars habitat to figure out what actually keeps people alive — and what kills them.", "do": "Preview LEVER steps. Emphasize that this is a SYSTEM problem — everything is connected.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for Mars survival model", "say": "What are the non-negotiable requirements for human survival? Which ones does Mars provide?", "do": "Guide sorting. All four environmental factors are external — Mars controls them, not us.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "If pressure drops, what happens to water? To crops? To the people inside?", "do": "Help students trace cascade failures. Emphasize that all paths lead to crop viability.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's break our habitat and see what fails first — and fastest.", "do": "Students predict failure cascades, then run scenarios. Compare pressure breach vs. water crisis.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So is Mars colonization actually possible? What does your model say about the engineering challenges?", "do": "Facilitate evidence-based debate. Which challenge is hardest? What would you solve first?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Mars habitat design challenge", "say": "NASA wants your design. Build a habitat that solves ALL five problems for six people for one year.", "do": "Groups design habitat modules. Must address all five factors with failure contingencies.", "time": "12 min"}
    ],
    "sort_reasoning": "Atmospheric Pressure, Radiation Exposure, Water Availability, and Temperature are all external because they represent Mars environmental conditions that exist independently of the habitat and must be actively countered through engineering. Crop Viability is the sole internal component because it is the biological outcome that depends on all four external factors being maintained within acceptable ranges.",
    "relationships": [
        ("Atmospheric Pressure to Crop Viability", "POSITIVE (+)", "Higher atmospheric pressure inside the habitat allows liquid water to exist and plants to photosynthesize. Below the critical threshold, water boils at room temperature and plants cannot survive."),
        ("Radiation Exposure to Crop Viability", "NEGATIVE (-)", "Higher radiation damages plant DNA, reduces photosynthetic efficiency, and can kill crops. Effective shielding is essential for agricultural viability."),
        ("Water Availability to Crop Viability", "POSITIVE (+)", "More available water directly supports plant growth, transpiration, and nutrient transport. Water scarcity is the most immediate threat to food production."),
        ("Temperature to Crop Viability", "POSITIVE (+) within range", "Crop viability increases as temperature approaches the optimal growth range (18-26°C). Both extreme cold and extreme heat reduce or eliminate crop yields.")
    ],
    "sim_answers": [
        ("Optimal Habitat Scenario", "When all external factors are at ideal levels — pressure at 101 kPa, radiation shielded, water abundant, temperature at 22°C — Crop Viability is at maximum. The system mirrors Earth-like growing conditions inside the sealed habitat, allowing food production sufficient for the crew."),
        ("Pressure Breach Scenario", "When Atmospheric Pressure drops toward Mars surface levels, the cascade is catastrophic. Water begins to boil at low temperatures, making irrigation impossible. Plants lose turgor pressure and wilt rapidly. Without pressurized atmosphere, both crops and humans are at immediate risk. This scenario demonstrates that pressure is the most time-critical failure mode.")
    ],
    "reflection_exemplars": [
        ("Why is Mars colonization the hardest engineering problem?", "Because it requires solving multiple interdependent problems simultaneously with zero margin for error. On Earth, if one system fails, we have backup from the natural environment — breathable air, drinkable water, moderate temperatures. On Mars, every single survival requirement must be artificially maintained. The model shows that failure in any single component can cascade into total system collapse within hours or days."),
        ("Which factor is most critical?", "Atmospheric pressure is the most time-critical — a breach can kill within minutes. But water availability is the most strategically critical for long-term survival because it limits food production, oxygen generation, and crew health. The model reveals that 'most critical' depends on timescale: pressure for minutes, water for months, radiation for years.")
    ],
    "stem_intro": "Present the challenge: NASA is soliciting Mars habitat designs from student teams. Your module must sustain a crew of six for one year, addressing all five survival factors using Martian resources wherever possible. Include contingency plans for the failure modes your model identified.",
    "stem_concepts": [
        ("In-Situ Resource Utilization (ISRU)", "Using materials found on Mars — ice for water, regolith for shielding, CO2 atmosphere for fuel production — instead of transporting everything from Earth. This is the key to making Mars colonization economically possible."),
        ("Closed-Loop Life Support", "A system where waste products become inputs: CO2 from breathing feeds plants, plant waste becomes compost, wastewater is purified and reused. Perfect efficiency is the goal — every molecule must be recycled."),
        ("Redundancy Engineering", "Building backup systems for every critical function. In aerospace engineering, this means multiple independent systems that can maintain operations if the primary system fails — because on Mars, there's no rescue.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses all five survival factors with detailed engineering solutions, uses ISRU where possible, includes redundancy for critical systems, and justifies design choices with model evidence"),
        ("Proficient (3)", "Design addresses most survival factors with reasonable engineering solutions and includes some failure contingencies"),
        ("Developing (2)", "Design addresses some survival factors but lacks detail, redundancy, or connection to model evidence"),
        ("Beginning (1)", "Design is incomplete or doesn't realistically address Mars survival challenges")
    ],
    "support": [
        "Provide a Mars fact sheet comparing conditions to Earth for quick reference",
        "Use a survival priority matrix to help students identify which factors to address first",
        "Sentence frames: 'Our habitat addresses __ by __, which ensures that __ remains within safe limits'"
    ],
    "extensions": [
        "Research the actual Mars habitat designs being developed by NASA and SpaceX and compare them to your model",
        "Calculate the amount of water, food, and oxygen needed per person per day and design a recycling system to meet those needs",
        "Investigate how the ISS currently handles life support and identify what would need to change for Mars"
    ],
    "cross_curr": [
        ("Math", "Calculate the volume of pressurized habitat space needed per person and the energy required to maintain temperature and pressure"),
        ("ELA", "Write a mission proposal to NASA arguing for your habitat design, using evidence from your model simulations"),
        ("Social Studies", "Research the ethics and governance challenges of establishing a permanent Mars colony — who makes the rules?")
    ],
    "misconceptions": [
        ("Mars is basically like a cold desert on Earth", "Mars is nothing like any place on Earth. Its atmosphere is 100 times thinner, there's no breathable oxygen, radiation is lethal, and the average temperature is -60°C. Even the driest, coldest desert on Earth has thousands of times more air pressure and infinitely more water than Mars.", "Compare: The highest point on Earth (Everest summit) has 33% of sea-level pressure. Mars has 0.6%. It's not even close."),
        ("We just need space suits to walk around on Mars", "Space suits are emergency survival equipment, not a long-term solution. They're heavy, restrict movement, require constant maintenance, and have limited life support duration. A suit breach on Mars means death in seconds. Sustainable Mars living requires permanent pressurized structures.", "Ask: Could you live your entire life in a scuba suit underwater? That's easier than what Mars demands."),
        ("We can terraform Mars to be like Earth", "Terraforming Mars — making it Earth-like — would take centuries to millennia if it's even possible. Mars has lost most of its atmosphere to space because it lacks a global magnetic field. Even if we could warm it, the atmosphere would slowly escape. Realistic Mars habitation means sealed habitats, not open-air living.", "Calculate: Earth's atmosphere took billions of years to develop. How long would it take to rebuild one on Mars from almost nothing?")
    ]
}

# ── L04 ───────────────────────────────────────────────────────────
L04 = {
    "id": "G09L1-L04",
    "title": "Why Your Phone Battery Dies So Fast",
    "subtitle": "Energy Conversion, Efficiency, and the Heat Tax",
    "ngss": "HS-PS3-1, HS-PS3-3",
    "ngss_desc": "Create a computational model to calculate the change in the energy of one component in a system when the change in energy of the other component(s) and energy flows in and out of the system are known. Design, build, and refine a device that works within given constraints to convert one form of energy into another form of energy.",
    "big_question": "Why does your phone die in 3 hours of gaming but lasts all day on standby?",
    "objectives": [
        "Identify the components that consume energy in a mobile device",
        "Model how energy converts from chemical to electrical to heat",
        "Explain why energy conversion is never 100% efficient",
        "Predict battery life under different usage scenarios"
    ],
    "vocabulary": [
        ("Energy Conversion", "The process of changing energy from one form to another — e.g., chemical energy in a battery to electrical energy to light from the screen"),
        ("Thermal Dissipation", "Energy lost as heat during any energy conversion process — this is the 'heat tax' you pay every time energy changes form"),
        ("Power Draw", "The rate at which a device consumes energy, measured in watts — higher power draw means faster battery drain"),
        ("Efficiency", "The ratio of useful energy output to total energy input — no device is 100% efficient because some energy always becomes heat")
    ],
    "components": [
        ("Screen Brightness", "How much power the display consumes. Higher brightness requires more energy to produce light.", True),
        ("Processing Load", "How hard the CPU/GPU works. Games and video demand maximum processing; texting uses minimal.", True),
        ("Battery Capacity", "Total stored chemical energy available. Degrades over charge cycles as battery chemistry breaks down.", False),
        ("Heat Generation", "Wasted energy converted to thermal energy. More processing and brightness means more heat.", False),
        ("Battery Life", "How long the device operates before running out. Determined by capacity minus all energy drains.", False)
    ],
    "think_about_it": "Your phone gets hot when you game. Where is that heat energy coming from — and where was it supposed to go instead?",
    "scenarios": [
        ("Heavy Gaming", "Set Screen Brightness to HIGH and Processing Load to HIGH. Observe Battery Life and Heat Generation."),
        ("Standby Mode", "Set Screen Brightness to LOW and Processing Load to LOW. Compare battery drain to gaming mode."),
        ("Brightness Test", "Keep Processing Load at MEDIUM but change Screen Brightness from LOW to HIGH. What drains more — screen or processor?")
    ],
    "sim_scenarios": [
        ("Heavy Gaming", "Screen Brightness: HIGH | Processing Load: HIGH", "Predict: How long will the battery last? How much heat will be generated?"),
        ("Standby Mode", "Screen Brightness: LOW | Processing Load: LOW", "Predict: How much longer does the battery last compared to gaming?"),
        ("Brightness Test", "Processing Load: MEDIUM | Screen Brightness: LOW → HIGH", "Which factor drains battery faster — screen brightness or processing load?")
    ],
    "discoveries": [
        "Energy conversion from battery chemical energy to screen light and computation is never 100% efficient",
        "Heat generation is wasted energy — every watt of heat is a watt NOT powering your screen or apps",
        "Screen brightness and processing load have a multiplicative effect on battery drain",
        "Battery capacity degrades over time, meaning the same usage pattern drains faster on an old phone"
    ],
    "answer": "Your phone battery dies fast during gaming because both the screen and processor are drawing maximum power simultaneously. Energy converts from chemical (battery) to electrical to light (screen) and computation (CPU), but at every step some energy is lost as heat. Gaming might use 5-8 watts while standby uses 0.1-0.3 watts — a 20-50x difference. That's why 3 hours of gaming equals 24+ hours of standby.",
    "stem_title": "The Battery Optimization Challenge",
    "stem_mission": "Design a power management system that maximizes battery life for a student who needs their phone to last a full school day (8 hours) with moderate use.",
    "stem_scenario": "A student's phone has a 4,000 mAh battery. They need to text, check social media during breaks, watch a 30-minute video at lunch, and use GPS to get home. Design power settings that keep the phone alive all day without carrying a charger.",
    "stem_questions": [
        "Which energy-consuming components can you reduce without ruining the experience?",
        "When during the day should you allow high-power activities vs. conserve?",
        "What's the minimum acceptable brightness and processing for each activity?"
    ],
    "stem_design_qs": [
        "What are the highest-priority functions the phone must perform?",
        "How will you schedule high-power and low-power activities across the day?",
        "What trade-offs are you making between experience quality and battery life?",
        "How would you test whether your power plan actually works for 8 hours?"
    ],
    "career": "Electrical Engineers design the power management systems in every device you own. They optimize energy conversion efficiency, design battery charging circuits, and create the algorithms that decide when to throttle performance to save power.",
    "images": {
        "cover": ("G09L1-L04-cover.png", "close-up of a smartphone with a critically low battery warning, dramatic red glow on screen, thermal camera overlay showing heat spots on the processor, dark modern background"),
        "landscape": ("G09L1-L04-landscape.png", "diverse group of 9th graders in a modern physics lab testing battery drain on different devices with multimeters and thermal cameras, engaged expressions"),
        "modeling": ("G09L1-L04-modeling.png", "diverse 9th grade students at computers building energy flow models, screens showing battery discharge curves and heat maps"),
        "discussion": ("G09L1-L04-discussion.png", "Black teacher leading classroom discussion about energy conversion with diagrams of battery chemistry on smartboard, students with phones out comparing battery stats"),
        "stem": ("G09L1-L04-stem.png", "diverse group of 9th graders designing power management schedules on whiteboards, phones and battery packs on desks, engineering design process visible")
    },
    "pre_assessment": [
        "What type of energy is stored in a phone battery? What does it convert into?",
        "Why does your phone get hot when you play games or watch videos?",
        "What does 'efficiency' mean in the context of energy conversion?",
        "List three things that drain your phone battery the fastest."
    ],
    "extend_components": [
        ("Battery Age", "How old the battery is measured in charge cycles. Lithium-ion batteries lose about 20% capacity after 500 full cycles."),
        ("Ambient Temperature", "Environmental temperature affects battery chemistry. Extreme cold reduces available capacity; extreme heat accelerates degradation."),
        ("Background Apps", "Programs running behind the scenes that consume power even when you're not using them — GPS, notifications, data syncing.")
    ],
    "reflections": [
        "Why is it impossible to build a device with 100% energy efficiency?",
        "How does the second law of thermodynamics relate to your phone getting hot?",
        "What trade-offs do engineers make when designing phone power systems?",
        "Why do older phones have worse battery life even with the same usage patterns?",
        "How could understanding energy conversion help you design better technology?"
    ],
    "dimensions": [
        ("SEP", "Using Mathematics and Computational Thinking", "Students create computational models to calculate energy changes and predict battery life under different usage scenarios."),
        ("DCI", "PS3.A: Definitions of Energy / PS3.D: Energy in Chemical Processes", "Energy is stored in batteries as chemical energy and converted through multiple steps. At each conversion, some energy is dissipated as thermal energy, reducing efficiency."),
        ("CCC", "Energy and Matter: Flows, Cycles, and Conservation", "Energy is conserved but degrades in quality — chemical energy converts to electrical to light/computation plus waste heat. Tracking energy flows reveals why systems are never perfectly efficient.")
    ],
    "cast_items": [
        "Calculate energy conversion efficiency from battery chemical energy to useful device output",
        "Model and predict battery life under varying usage conditions",
        "Explain energy dissipation and the second law of thermodynamics in consumer electronics"
    ],
    "cast_questions": [
        ("Calculate:", "A phone battery stores 15.4 Wh of energy. The screen uses 2.5 W, the processor uses 3.0 W during gaming, and 0.8 W of heat is generated. How long can the phone game before dying? What's the energy efficiency?"),
        ("Explain:", "Two identical phones with identical batteries are used for 4 hours — one for texting, one for gaming. The gaming phone is nearly dead while the texting phone has 70% battery. Use your energy model to explain why.")
    ],
    "background_intro": "Every device you own is a chain of energy conversions, and every link in that chain leaks energy as heat. Understanding why requires grasping the fundamental physics of energy transformation and the inescapable reality of the second law of thermodynamics.",
    "background_sections": [
        ("How Batteries Store Energy", "Lithium-ion batteries store energy in chemical bonds. During discharge, lithium ions flow from the anode to the cathode through an electrolyte, releasing electrons that travel through the external circuit (your phone's components) as electrical current. A typical smartphone battery stores about 15 Watt-hours of energy — equivalent to lifting a 1-kg weight about 5,500 meters."),
        ("The Energy Conversion Chain", "Battery chemical energy → electrical current → multiple endpoints: screen (electrical → light), processor (electrical → computation + heat), speakers (electrical → sound), radios (electrical → electromagnetic waves). At every conversion step, the second law of thermodynamics demands that some energy degrades to thermal energy. No conversion is 100% efficient."),
        ("Why Phones Get Hot", "Heat generation in phones comes from electrical resistance in circuits (Joule heating), transistor switching in processors, and LED/OLED inefficiency in screens. A phone running a demanding game might generate 3-5 watts of heat — equivalent to a small nightlight. This is energy your battery paid for but that did nothing useful. Modern phones use thermal throttling to reduce performance when temperatures get dangerous."),
        ("Battery Degradation", "Lithium-ion batteries degrade with every charge cycle. Repeated expansion and contraction of electrode materials causes microscopic cracks, and a thin layer of lithium compounds (SEI layer) gradually grows thicker, trapping lithium ions permanently. After 500 full cycles, most batteries retain only 80% of original capacity. Fast charging and extreme temperatures accelerate degradation.")
    ],
    "lever_L": "Students identify screen brightness, processing load, battery capacity, heat generation, and battery life as components of the phone energy system.",
    "lever_E": "Students discover that brightness and processing load both drain battery (+heat, -life) while heat represents wasted energy.",
    "lever_V": "Students build a model showing energy flowing from battery through components with heat as a loss pathway.",
    "lever_Ev": "Students run gaming, standby, and brightness test scenarios to compare energy drain rates.",
    "lever_R": "Students add battery age, ambient temperature, or background apps to create a more realistic energy model.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with phone battery image", "say": "Raise your hand if your phone has ever died at the worst possible moment. Why does this happen?", "do": "Quick poll: What drains your battery fastest? Games? TikTok? YouTube?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're investigating the physics of why your phone battery can't keep up with your life.", "do": "Have students read objectives. Pre-teach 'energy conversion' with a simple example.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Gaming vs standby comparison", "say": "3 hours gaming vs 24 hours standby — same battery. Why the 8x difference?", "do": "Show actual battery drain curves. Ask students to hypothesize.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model where your battery energy actually goes — and how much is wasted.", "do": "Preview LEVER steps. Emphasize we're tracking energy FLOWS.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for energy model", "say": "What can YOU control about your phone's energy use? What happens as a RESULT?", "do": "Guide sorting. Discuss why brightness is external (you choose) but heat is internal (you can't avoid it).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More brightness means more battery drain. But where does that extra energy actually GO?", "do": "Reveal that heat is the hidden energy thief. Draw the energy flow diagram.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Battery drain graphs", "say": "Let's race: gaming mode vs standby vs brightness-only. Which kills your battery fastest?", "do": "Students predict battery life for each scenario. Compare predictions to simulation.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "So every time your phone gets hot, that's YOUR battery energy being wasted as heat. The second law of thermodynamics strikes again.", "do": "Connect heat to wasted energy. Discuss why 100% efficiency is impossible.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Battery optimization plan", "say": "Design a power plan that keeps your phone alive for a full 8-hour school day. Every watt counts.", "do": "Groups plan schedules balancing usage needs with power conservation.", "time": "12 min"}
    ],
    "sort_reasoning": "Screen Brightness and Processing Load are external because YOU control them — you choose how bright your screen is and what apps you run. Battery Capacity, Heat Generation, and Battery Life are internal because they are consequences of those choices and the physics of energy conversion.",
    "relationships": [
        ("Screen Brightness to Battery Life", "NEGATIVE (-)", "Higher screen brightness draws more power from the battery, converting more chemical energy to light (plus wasted heat), reducing the time the battery can last."),
        ("Processing Load to Heat Generation", "POSITIVE (+)", "More intensive processing means more electrical energy flowing through transistors, and more energy lost as heat through electrical resistance. Gaming generates several watts of heat."),
        ("Heat Generation to Battery Life", "NEGATIVE (-)", "Heat represents wasted energy — every watt of heat is a watt that didn't go to useful function. More heat means faster energy depletion and shorter battery life.")
    ],
    "sim_answers": [
        ("Heavy Gaming Scenario", "With both Screen Brightness and Processing Load at HIGH, Battery Life drops dramatically — the phone might last only 2-3 hours. Heat Generation spikes as both the screen and processor draw maximum power. The battery is draining through both high-power pathways simultaneously, plus paying the 'heat tax' on both."),
        ("Brightness Test Scenario", "Increasing Screen Brightness from LOW to HIGH while keeping Processing Load at MEDIUM shows that the screen is a major battery drain — often the single biggest power consumer. However, the processor during gaming typically generates MORE heat because transistor switching is less efficient than LED/OLED light production.")
    ],
    "reflection_exemplars": [
        ("Why is 100% energy efficiency impossible?", "The second law of thermodynamics states that whenever energy converts from one form to another, some energy always degrades to thermal energy (heat). In a phone, chemical energy → electrical energy → light/computation, and each arrow represents a conversion where some energy is lost as heat. Even the best processors lose 30-40% of their energy as heat. This is a fundamental law of physics, not an engineering failure."),
        ("How does battery age affect your model?", "As a battery ages through charge cycles, its internal chemistry degrades — the SEI layer thickens, trapping lithium ions permanently. This means Battery Capacity decreases over time even though Screen Brightness and Processing Load stay the same. Our model predicts that the same usage pattern will drain an old battery much faster because there's simply less stored energy to begin with.")
    ],
    "stem_intro": "Challenge students to think like power management engineers. Real phone companies employ hundreds of engineers whose entire job is optimizing energy flows to maximize battery life without sacrificing user experience.",
    "stem_concepts": [
        ("Power Budget", "The total energy available divided among all consuming components. Engineers must 'budget' watts the way you budget money — spending more on one thing means less for everything else."),
        ("Adaptive Brightness", "Technology that automatically adjusts screen brightness based on ambient light. This saves significant battery by avoiding unnecessarily high brightness in dim environments."),
        ("Thermal Throttling", "When a phone gets too hot, it automatically reduces processor speed to prevent damage. This is why games sometimes lag after 30 minutes — the phone is protecting itself by sacrificing performance.")
    ],
    "stem_eval": [
        ("Expert (4)", "Power plan accounts for all major energy consumers, includes time-based scheduling, references model data, and addresses realistic daily activities"),
        ("Proficient (3)", "Power plan identifies key energy drains with reasonable settings, supported by simulation evidence"),
        ("Developing (2)", "Power plan addresses some energy factors but lacks scheduling detail or evidence"),
        ("Beginning (1)", "Power plan is incomplete or doesn't connect to energy conversion concepts")
    ],
    "support": [
        "Provide a visual energy flow diagram showing battery → components → heat as a pre-made reference",
        "Use a water tank analogy: battery = full tank, usage = drain valves, heat = leaks in the pipes",
        "Sentence frames: 'When screen brightness increases, battery life __ because more energy is converted to __'"
    ],
    "extensions": [
        "Research wireless charging efficiency — how much energy is lost converting wall AC → charger DC → wireless → phone battery?",
        "Compare the energy density of lithium-ion batteries to gasoline. Why can't phone batteries match the energy of fuel?",
        "Investigate solid-state batteries: How would they change the energy conversion efficiency model?"
    ],
    "cross_curr": [
        ("Math", "Calculate: A 4,000 mAh, 3.8V battery stores 15.2 Wh. If gaming draws 5.5W and standby draws 0.2W, calculate battery life for each and the ratio."),
        ("ELA", "Write a consumer guide explaining to non-technical users WHY their phone battery dies fast and what they can actually do about it."),
        ("Social Studies", "Research the environmental impact of lithium mining for phone batteries. What are the human and ecological costs of our energy-hungry devices?")
    ],
    "misconceptions": [
        ("Closing apps saves battery", "On modern phones, background apps are 'frozen' and use almost zero power. Force-closing them actually WASTES energy because reopening them requires more processing than leaving them suspended. The real battery drains are screen brightness, cellular/GPS radios, and active processing.", "Show battery usage stats on a phone. The screen is almost always #1, not background apps."),
        ("Charging overnight damages the battery", "Modern phones have smart charging circuits that stop charging at 100% and maintain the battery. However, keeping a lithium-ion battery at 100% charge does cause slightly faster degradation over months. The bigger damage comes from extreme heat and fast-charging frequently.", "Explain that 'damage' is about chemistry: keeping lithium ions at maximum voltage causes slightly faster SEI growth. It's real but very slow."),
        ("Bigger battery always means longer life", "Battery size (mAh) is only half the equation. A phone with a 5,000 mAh battery but a power-hungry screen and processor might last shorter than a 3,000 mAh phone with efficient components. Total battery life = capacity ÷ average power draw. Efficiency matters as much as size.", "Analogy: A bigger gas tank doesn't help if your car's engine is inefficient. A Prius with 11 gallons outlasts a truck with 30 gallons.")
    ]
}

# ── L05 ───────────────────────────────────────────────────────────
L05 = {
    "id": "G09L1-L05",
    "title": "The Ocean Is Turning to Acid",
    "subtitle": "How CO2 Emissions Are Dissolving Marine Life",
    "ngss": "HS-ESS3-6, HS-PS1-7",
    "ngss_desc": "Use a computational representation to illustrate the relationships among Earth systems and how those relationships are being modified due to human activity. Use mathematical representations to support the claim that atoms, and therefore mass, are conserved during a chemical reaction.",
    "big_question": "How is the CO2 from your car slowly dissolving the shells of sea creatures thousands of miles away?",
    "objectives": [
        "Trace the path of CO2 from emission to ocean absorption",
        "Model how dissolved CO2 changes ocean pH through chemical reactions",
        "Explain the relationship between ocean acidification and coral/shell health",
        "Predict the impact of different emission scenarios on marine ecosystems"
    ],
    "vocabulary": [
        ("Ocean Acidification", "The ongoing decrease in ocean pH caused by absorption of atmospheric CO2 — the ocean has become 30% more acidic since the Industrial Revolution"),
        ("pH Scale", "A measure of how acidic or basic a solution is, from 0 (extremely acidic) to 14 (extremely basic). Seawater has dropped from pH 8.2 to 8.1 — sounds small but it's a 30% increase in acidity"),
        ("Carbonic Acid", "The weak acid (H2CO3) formed when CO2 dissolves in water — this is the chemical mechanism driving ocean acidification"),
        ("Calcification", "The biological process marine organisms use to build shells and coral skeletons from calcium carbonate — acidification dissolves these structures")
    ],
    "components": [
        ("CO2 Emissions", "The rate at which humans release carbon dioxide into the atmosphere from burning fossil fuels, deforestation, and industry.", True),
        ("Ocean CO2 Absorption", "How much atmospheric CO2 dissolves into seawater. The ocean absorbs about 30% of human CO2 emissions.", False),
        ("Ocean pH", "The acidity level of seawater. As more CO2 dissolves, pH decreases (becomes more acidic).", False),
        ("Coral Health", "The ability of coral reefs and shell-building organisms to survive. Lower pH dissolves their calcium carbonate structures.", False)
    ],
    "think_about_it": "The ocean absorbs 30% of our CO2 emissions. Is the ocean helping us or hurting itself — or both?",
    "scenarios": [
        ("Current Trajectory", "Set CO2 Emissions to HIGH (current global rate). Observe how Ocean pH and Coral Health change over decades."),
        ("Paris Agreement", "Set CO2 Emissions to MEDIUM (reduced per Paris targets). Compare pH decline to current trajectory."),
        ("Zero Emissions", "Set CO2 Emissions to LOW. Does the ocean recover? How quickly?")
    ],
    "sim_scenarios": [
        ("Current Trajectory", "CO2 Emissions: HIGH (current rate)", "Predict: What happens to ocean pH and coral health over 50 years at current emission rates?"),
        ("Paris Agreement", "CO2 Emissions: MEDIUM (reduced)", "Predict: Does reducing emissions stop acidification or just slow it?"),
        ("Zero Emissions", "CO2 Emissions: LOW (near zero)", "Predict: If we stopped all emissions today, how long would the ocean take to recover?")
    ],
    "discoveries": [
        "The ocean acts as a massive CO2 sink — absorbing billions of tons yearly — but this absorption comes at the cost of increasing acidity",
        "Ocean pH has dropped 0.1 units since pre-industrial times — a 30% increase in hydrogen ion concentration",
        "Even under the Paris Agreement, ocean acidification continues for decades because CO2 already in the atmosphere keeps dissolving",
        "Coral reefs and shellfish are the first casualties because their calcium carbonate structures literally dissolve in more acidic water"
    ],
    "answer": "CO2 from your car enters the atmosphere, and about 30% dissolves into the ocean. When CO2 meets seawater, it forms carbonic acid (H2CO3), which releases hydrogen ions that lower pH. This more acidic water dissolves the calcium carbonate that corals and shellfish need to build their structures. The chemistry is simple and inescapable: more CO2 in = more acid = less coral. The ocean has been absorbing our CO2 for decades — it's helped slow atmospheric warming but is paying with its own chemistry.",
    "stem_title": "The Coral Reef Rescue Plan",
    "stem_mission": "Design an intervention strategy that protects a coral reef from acidification while addressing the root cause of CO2 emissions.",
    "stem_scenario": "A Caribbean coral reef that supports local fishing and tourism is showing signs of bleaching and dissolution. Your team must propose a multi-pronged strategy: immediate reef protection, medium-term emission reduction, and long-term ocean chemistry restoration.",
    "stem_questions": [
        "Can we protect reefs locally while the global ocean continues to acidify?",
        "What's more effective: reducing emissions or directly treating ocean chemistry?",
        "How do you balance economic needs (fishing, tourism) with environmental protection?"
    ],
    "stem_design_qs": [
        "What are the most urgent threats to the reef right now?",
        "How will your plan address both symptoms (acidification) and causes (emissions)?",
        "What trade-offs exist between immediate protection and long-term solutions?",
        "How would you measure whether your intervention is actually working?"
    ],
    "career": "Marine Chemists and Oceanographers study the chemical composition of seawater and how it's changing. They deploy sensors across the ocean, model chemical reactions at global scale, and advise governments on climate policy. This field combines chemistry, biology, and environmental science.",
    "images": {
        "cover": ("G09L1-L05-cover.png", "dramatic underwater photograph of a coral reef showing half healthy vibrant coral and half bleached white dissolving coral, split composition, deep blue water, cinematic lighting"),
        "landscape": ("G09L1-L05-landscape.png", "diverse group of 9th graders in a marine science lab testing pH of water samples with indicators, colorful pH strips and beakers on lab benches"),
        "modeling": ("G09L1-L05-modeling.png", "diverse 9th grade students at computers building ocean acidification models, screens showing pH curves and CO2 absorption graphs"),
        "discussion": ("G09L1-L05-discussion.png", "Black teacher leading classroom discussion about ocean chemistry with pH scale diagram on smartboard, holding up a coral specimen, students engaged"),
        "stem": ("G09L1-L05-stem.png", "diverse group of 9th graders designing coral reef protection plans on large poster boards, ocean maps and data charts visible, collaborative energy")
    },
    "pre_assessment": [
        "What is the pH scale and what does it measure?",
        "Where does the CO2 from burning fossil fuels go after it enters the atmosphere?",
        "What are coral reefs made of and why are they important?",
        "How could a gas in the atmosphere affect creatures living deep in the ocean?"
    ],
    "extend_components": [
        ("Water Temperature", "Warmer water holds less dissolved CO2 but accelerates chemical reactions. Rising ocean temperatures interact with acidification in complex ways."),
        ("Biological Buffering", "Healthy marine ecosystems can partially buffer pH changes through photosynthesis (which consumes CO2). Losing marine plants reduces this natural buffer."),
        ("Deep Ocean Circulation", "Ocean currents carry acidified surface water to the deep ocean. This means acidification impacts spread globally, even to remote areas far from emission sources.")
    ],
    "reflections": [
        "Why is a 0.1 pH change considered significant when the scale goes from 0 to 14?",
        "How does the law of conservation of mass explain where atmospheric CO2 ends up in the ocean?",
        "Why can't marine organisms simply adapt to more acidic water?",
        "What makes ocean acidification an especially difficult problem to reverse?",
        "How does this model connect local actions (driving a car) to global impacts (coral death)?"
    ],
    "dimensions": [
        ("SEP", "Using Mathematics and Computational Thinking", "Students use computational models to represent the quantitative relationships between CO2 emissions, ocean absorption, pH changes, and biological impacts."),
        ("DCI", "ESS3.C: Human Impacts on Earth Systems / PS1.B: Chemical Reactions", "Human CO2 emissions are absorbed by the ocean, driving chemical reactions that produce carbonic acid and lower pH. Atoms are conserved — the carbon in your exhaust becomes the acid dissolving coral."),
        ("CCC", "Stability and Change", "The ocean's pH has been stable for millions of years. Human CO2 emissions have disrupted this stability faster than marine organisms can adapt, pushing the system toward a new — and potentially catastrophic — equilibrium.")
    ],
    "cast_items": [
        "Model the quantitative relationship between atmospheric CO2 and ocean pH",
        "Trace the conservation of carbon atoms from fossil fuel combustion through atmospheric CO2 to dissolved carbonic acid",
        "Predict biological impacts of continued acidification using computational evidence"
    ],
    "cast_questions": [
        ("Trace:", "Follow a carbon atom from gasoline in a car engine, through the atmosphere, into the ocean, and into a chemical reaction with seawater. Write the chemical equations and explain each step."),
        ("Evaluate:", "A policy advisor claims that 'the ocean is cleaning up our CO2 for free.' Using your model, explain why this statement is dangerously misleading.")
    ],
    "background_intro": "Ocean acidification is often called 'the other CO2 problem' — less famous than global warming but potentially just as devastating. The chemistry is straightforward, the evidence is irrefutable, and the consequences for marine life are already visible.",
    "background_sections": [
        ("The Chemistry of Ocean Acidification", "When CO2 dissolves in seawater, it reacts with water to form carbonic acid: CO2 + H2O → H2CO3. This carbonic acid then dissociates, releasing hydrogen ions (H+) that lower pH: H2CO3 → H+ + HCO3-. The excess hydrogen ions also react with carbonate ions (CO3²-) that marine organisms need for building shells: H+ + CO3²- → HCO3-. This is why acidification is a double hit — it increases acidity AND removes the building blocks organisms need."),
        ("The Scale of the Problem", "The ocean has absorbed approximately 525 billion tons of CO2 from the atmosphere since the Industrial Revolution — about 30% of all human emissions. Surface ocean pH has dropped from 8.2 to 8.1. While 0.1 sounds tiny, pH is logarithmic: this represents a 30% increase in hydrogen ion concentration. Current projections show pH could drop to 7.8 by 2100 — a 150% increase in acidity from pre-industrial levels."),
        ("Biological Impacts", "Organisms that build calcium carbonate structures — corals, oysters, clams, sea urchins, and many plankton species — are most vulnerable. Below a pH threshold, their shells and skeletons literally dissolve faster than they can build them. Coral reefs, which support 25% of all marine species despite covering less than 1% of the ocean floor, are facing dissolution. Pteropods (sea butterflies) at the base of many food chains are already showing shell thinning."),
        ("The Recovery Problem", "Even if CO2 emissions stopped completely today, ocean acidification would continue for decades as existing atmospheric CO2 continues dissolving. Full recovery of ocean pH would take tens of thousands of years because the deep ocean circulation that mixes surface and deep water operates on millennial timescales. This makes prevention far more effective than cure.")
    ],
    "lever_L": "Students identify CO2 emissions, ocean CO2 absorption, ocean pH, and coral health as components of the ocean acidification system.",
    "lever_E": "Students discover that emissions drive absorption (+), absorption drives pH down (-), and lower pH destroys coral health (-).",
    "lever_V": "Students build a model showing the causal chain from human emissions to marine ecosystem destruction.",
    "lever_Ev": "Students run current trajectory, Paris Agreement, and zero emission scenarios to compare outcomes.",
    "lever_R": "Students add water temperature, biological buffering, or deep ocean circulation to explore more complex dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with split coral image", "say": "This coral reef is dissolving. Not from pollution you can see — from an invisible gas. How?", "do": "Show before/after images of coral bleaching. Ask: What could cause solid rock to dissolve?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're tracing an invisible path: from your car's tailpipe to a coral reef 10,000 miles away.", "do": "Have students read objectives. Pre-teach pH with a visual scale.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Car exhaust to ocean connection", "say": "How does burning gasoline in your city dissolve a shell on the ocean floor?", "do": "Show the chemical pathway. Ask: Where does exhaust CO2 go?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how CO2 travels from atmosphere to ocean and what it does when it arrives.", "do": "Preview LEVER steps. Emphasize we're tracking a MOLECULE's journey.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "What can humans control? What's a consequence of our choices?", "do": "Guide sorting. CO2 Emissions is the only truly external component — everything else is a downstream effect.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with chemistry", "say": "More CO2 absorbed means lower pH. But what does lower pH mean for living things?", "do": "Show the chemical equation. Demonstrate with vinegar on chalk (calcium carbonate).", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "pH projection graphs", "say": "Let's test three futures: do nothing, follow Paris, or go to zero. Can the ocean recover?", "do": "Students predict pH for each scenario. The zero-emission recovery delay is the key insight.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Even if we stopped ALL emissions today, the ocean keeps acidifying for decades. Why?", "do": "Discuss the lag effect. Existing atmospheric CO2 keeps dissolving.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Coral rescue plan", "say": "A Caribbean reef is dying. Design a rescue plan that addresses both symptoms AND causes.", "do": "Groups design multi-pronged strategies: immediate protection + long-term emission reduction.", "time": "12 min"}
    ],
    "sort_reasoning": "CO2 Emissions is external because it's driven by human activity — we choose how much fossil fuel to burn. Ocean CO2 Absorption, Ocean pH, and Coral Health are all internal because they are consequences of CO2 levels — the ocean chemistry responds automatically to atmospheric CO2 concentration.",
    "relationships": [
        ("CO2 Emissions to Ocean CO2 Absorption", "POSITIVE (+)", "More atmospheric CO2 means more dissolves into the ocean. The ocean absorbs roughly 30% of our emissions — more emissions means more absorption."),
        ("Ocean CO2 Absorption to Ocean pH", "NEGATIVE (-)", "More dissolved CO2 creates more carbonic acid, releasing hydrogen ions that lower pH. Every additional ton of CO2 absorbed makes the ocean measurably more acidic."),
        ("Ocean pH to Coral Health", "POSITIVE (+)", "Higher pH (less acidic) supports healthy coral growth. As pH drops, coral's calcium carbonate structures dissolve faster than organisms can build them, leading to reef death.")
    ],
    "sim_answers": [
        ("Current Trajectory", "With CO2 Emissions at HIGH, ocean pH drops steadily from 8.1 toward 7.8 by 2100. Coral Health declines catastrophically as acidification crosses biological thresholds. Ocean CO2 Absorption actually increases initially (more atmospheric CO2 to absorb) but this 'service' destroys marine chemistry."),
        ("Zero Emissions", "Even at zero emissions, Ocean pH continues dropping for decades because the existing 420+ ppm atmospheric CO2 keeps dissolving. Recovery takes thousands of years because deep ocean circulation is extremely slow. This lag effect is the most important insight: prevention is far more effective than cure.")
    ],
    "reflection_exemplars": [
        ("Why is a 0.1 pH change significant?", "The pH scale is logarithmic — each whole number represents a 10x change in hydrogen ion concentration. A drop from 8.2 to 8.1 means a 26% increase in H+ ions. Projected drops to 7.8 would mean a 150% increase. For organisms that evolved over millions of years in stable pH conditions, these changes happen thousands of times faster than natural variation, giving them no time to adapt."),
        ("Why can't the ocean just recover?", "Recovery requires removing excess CO2 from the entire ocean volume — about 1.335 billion cubic kilometers of water. The deep ocean, which contains 90% of ocean water, mixes with the surface only through slow thermohaline circulation that takes 500-1,000 years per cycle. Even if we stopped adding CO2 today, it would take 10,000-50,000 years for ocean chemistry to return to pre-industrial levels.")
    ],
    "stem_intro": "Frame this as a real-world policy challenge: students are marine conservation consultants advising a Caribbean nation whose economy depends on coral reef tourism and fishing.",
    "stem_concepts": [
        ("Ocean Alkalinity Enhancement", "Proposed geoengineering technique that adds alkaline minerals to seawater to neutralize acidity. Like adding antacid to the ocean. Currently experimental and the scale required is enormous."),
        ("Marine Protected Areas", "Designated ocean regions where human activities are restricted. MPAs can reduce LOCAL stresses (pollution, overfishing) to help reefs survive acidification, but they can't change ocean chemistry."),
        ("Blue Carbon", "Carbon captured and stored by coastal ecosystems like mangroves, seagrasses, and salt marshes. Protecting and restoring these ecosystems removes CO2 from the water AND provides habitat.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses immediate reef protection, medium-term emission reduction, and long-term chemistry restoration with evidence from model simulations"),
        ("Proficient (3)", "Plan includes multiple intervention strategies with some model evidence"),
        ("Developing (2)", "Plan addresses either symptoms or causes but not both"),
        ("Beginning (1)", "Plan is incomplete or doesn't connect to ocean acidification model")
    ],
    "support": [
        "Provide a pre-drawn CO2 pathway diagram: tailpipe → atmosphere → ocean surface → chemical reaction → coral",
        "Use a hands-on demo: put chalk (CaCO3) in vinegar (acid) to show dissolution — same chemistry, faster timescale",
        "Sentence frames: 'When CO2 emissions increase, ocean pH __ because __, which causes coral health to __'"
    ],
    "extensions": [
        "Research ocean alkalinity enhancement — calculate how many tons of limestone you'd need to neutralize one year of CO2 absorption",
        "Compare ocean acidification rates to the Permian-Triassic extinction (the Great Dying) — how do current rates compare?",
        "Investigate how shellfish farming industries in the Pacific Northwest are already adapting to acidification"
    ],
    "cross_curr": [
        ("Math", "Calculate: If the ocean absorbs 9.3 billion tons of CO2 per year and current atmospheric CO2 is 420 ppm, model pH change over 10-year intervals using the carbonate chemistry equations."),
        ("ELA", "Write a policy brief for a coastal senator explaining ocean acidification, its economic impacts on fishing communities, and recommended legislative action."),
        ("Social Studies", "Research environmental justice: Which coastal communities and nations are most vulnerable to ocean acidification impacts, and which nations emit the most CO2?")
    ],
    "misconceptions": [
        ("The ocean is basic so it can handle some acid", "While seawater is indeed slightly basic (pH 8.1), marine life evolved over millions of years in this exact pH range. A shift of 0.1 pH units represents a 30% change in acidity — equivalent to changing the oxygen concentration in air by 30%. Organisms can't just 'handle' that.", "Analogy: Human blood pH is 7.4. A change of just 0.2 pH units (to 7.2) causes acidosis and can be fatal. Small pH changes matter enormously to biology."),
        ("CO2 is natural so it can't be harmful", "CO2 is natural and essential for photosynthesis. The problem isn't CO2 existing — it's the RATE of increase. Natural CO2 cycles take thousands of years; we've increased atmospheric CO2 by 50% in 150 years. The ocean can absorb CO2 gradually, but not at this pace. It's like the difference between rain (natural) and a flood (too much, too fast).", "Show the Keeling Curve: atmospheric CO2 was 280 ppm for 10,000 years, then shot to 420 ppm in 150 years. That rate is unprecedented."),
        ("We can just add chemicals to fix the ocean", "The ocean contains 1.335 billion cubic kilometers of water. To raise its pH by 0.1 units would require billions of tons of alkaline minerals. We'd need to mine, transport, and distribute more material than the entire global mining industry produces. And we'd need to keep doing it every year. Prevention (cutting emissions) is millions of times more practical than cure.", "Calculate: The ocean volume is 1.335 × 10^18 cubic meters. How many tons of limestone would you need per cubic meter? Multiply out to see the absurdity.")
    ]
}

# ── L06 ───────────────────────────────────────────────────────────
L06 = {
    "id": "G09L1-L06",
    "title": "Why Some People Can't Drink Milk",
    "subtitle": "Gene Expression, Enzymes, and the Lactose Puzzle",
    "ngss": "HS-LS3-1",
    "ngss_desc": "Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring.",
    "big_question": "Why can some people drink a milkshake with no problem while others suffer for hours?",
    "objectives": [
        "Explain how genes code for enzyme production",
        "Model the relationship between lactase gene activity and lactose digestion",
        "Predict digestive outcomes based on gene expression levels",
        "Analyze why lactose tolerance varies across human populations"
    ],
    "vocabulary": [
        ("Gene Expression", "The process by which information from a gene is used to make a functional protein — when a gene is 'expressed,' it's actively being read and translated"),
        ("Lactase", "The enzyme that breaks down lactose (milk sugar) into glucose and galactose — without enough lactase, lactose passes undigested into the large intestine"),
        ("Enzyme", "A protein that speeds up a specific chemical reaction — lactase specifically catalyzes the breakdown of the lactose molecule"),
        ("Epigenetics", "Changes in gene expression that don't alter the DNA sequence itself — the lactase gene gets 'turned down' after weaning in most humans")
    ],
    "components": [
        ("Lactase Gene Activity", "How actively the LCT gene is being expressed (read and translated into protein). In most humans, this decreases after childhood.", True),
        ("Lactase Enzyme Production", "The amount of functional lactase enzyme present in the small intestine lining. Directly determined by gene expression level.", False),
        ("Lactose Breakdown", "How effectively milk sugar (lactose) is split into absorbable sugars (glucose + galactose). Depends on available lactase enzyme.", False),
        ("Gut Bacteria Response", "When undigested lactose reaches the large intestine, bacteria ferment it, producing gas (bloating, cramps) and drawing in water (diarrhea).", False)
    ],
    "think_about_it": "Every human baby can digest milk. Why would evolution 'turn off' this ability in most adults — and why did some populations keep it?",
    "scenarios": [
        ("Lactose Tolerant", "Set Lactase Gene Activity to HIGH. Observe Lactose Breakdown and Gut Bacteria Response after drinking milk."),
        ("Lactose Intolerant", "Set Lactase Gene Activity to LOW. What happens to undigested lactose in the gut?"),
        ("Partial Tolerance", "Set Lactase Gene Activity to MEDIUM. Is there a threshold where symptoms appear?")
    ],
    "sim_scenarios": [
        ("Lactose Tolerant", "Lactase Gene Activity: HIGH", "Predict: What happens to lactose breakdown and gut bacteria response when the gene is fully active?"),
        ("Lactose Intolerant", "Lactase Gene Activity: LOW", "Predict: What happens to the undigested lactose, and why does it cause symptoms?"),
        ("Partial Tolerance", "Lactase Gene Activity: MEDIUM", "Predict: Is there a threshold level of enzyme needed to avoid symptoms, or is it gradual?")
    ],
    "discoveries": [
        "Lactase gene activity directly controls enzyme production, which determines whether lactose gets digested or fermented",
        "Most humans naturally reduce lactase production after weaning — lactose TOLERANCE is actually the mutation, not intolerance",
        "There's a threshold effect: some lactase is enough to digest small amounts of dairy, but large amounts overwhelm limited enzyme",
        "Gut bacteria fermentation of undigested lactose produces gas and osmotic effects — this is what causes the symptoms"
    ],
    "answer": "The difference comes down to a single gene. The LCT gene codes for lactase enzyme. In about 65% of humans worldwide, this gene gets 'turned down' after childhood (a process called lactase non-persistence). Without enough lactase, milk sugar passes undigested to the large intestine where bacteria ferment it, producing gas, bloating, cramps, and diarrhea. The ~35% who can drink milk as adults carry a mutation that keeps the LCT gene active — this mutation spread in populations that domesticated dairy animals about 7,500 years ago.",
    "stem_title": "The Dairy Product Design Challenge",
    "stem_mission": "Design a dairy product line that people with lactose intolerance can enjoy without symptoms, using your understanding of enzyme science.",
    "stem_scenario": "A food company wants to create a line of dairy products for the 65% of the world's population that is lactose intolerant. Using your model of lactase-lactose interactions, design products that solve the digestion problem through different scientific approaches.",
    "stem_questions": [
        "Can you add lactase enzyme to the product? How much and when?",
        "Could you pre-ferment the lactose using bacteria (like in yogurt)?",
        "What's the maximum amount of lactose an intolerant person can typically handle?"
    ],
    "stem_design_qs": [
        "What scientific approach will your product use to solve the lactose problem?",
        "How will you ensure the product still tastes and feels like dairy?",
        "What testing would you need to verify your product works for intolerant consumers?",
        "How does your solution compare to existing products like Lactaid?"
    ],
    "career": "Genetic Counselors help people understand how their genes affect their health, from lactose intolerance to disease risk. Food Scientists apply enzyme chemistry to create products like lactose-free milk, yogurt, and cheese — a market worth over $15 billion globally.",
    "images": {
        "cover": ("G09L1-L06-cover.png", "dramatic split image of a glass of milk with DNA double helix visible inside the milk, one half shows happy digestion symbols and the other shows distress, modern scientific aesthetic"),
        "landscape": ("G09L1-L06-landscape.png", "diverse group of 9th graders in a biology lab examining enzyme reaction tubes with different milk samples, using pH indicators and timers"),
        "modeling": ("G09L1-L06-modeling.png", "diverse 9th grade students at computers building gene expression models, screens showing lactase enzyme diagrams and digestion pathways"),
        "discussion": ("G09L1-L06-discussion.png", "Black teacher leading classroom discussion about genetics and lactose intolerance with world map showing lactose tolerance distribution on smartboard"),
        "stem": ("G09L1-L06-stem.png", "diverse group of 9th graders designing dairy products with enzyme solutions, lab coats and food science equipment visible, product mockups on tables")
    },
    "pre_assessment": [
        "What is an enzyme and what does it do?",
        "What does it mean when a gene is 'expressed' or 'active'?",
        "Why do some people get stomach problems from drinking milk?",
        "How do genes determine physical traits like enzyme production?"
    ],
    "extend_components": [
        ("Dairy Amount", "The volume of lactose-containing food consumed. Small amounts may be tolerated even with low lactase, but large amounts overwhelm the system."),
        ("Gut Microbiome Composition", "The specific bacteria species in your large intestine determine how aggressively undigested lactose is fermented and how severe symptoms are."),
        ("Epigenetic Regulation", "Chemical modifications to DNA (methylation) that silence the lactase gene after weaning. This is the mechanism that 'turns off' lactase in most adults.")
    ],
    "reflections": [
        "Why is lactose TOLERANCE the mutation, not lactose intolerance?",
        "How does this example demonstrate the connection between DNA, proteins, and physical traits?",
        "Why did the lactase persistence mutation spread in some populations but not others?",
        "How does the threshold effect in your model relate to real-world dairy tolerance?",
        "What does this tell us about human evolution being driven by cultural practices (dairy farming)?"
    ],
    "dimensions": [
        ("SEP", "Asking Questions and Defining Problems", "Students ask questions about how DNA sequence variations lead to different enzyme production levels and downstream phenotypic differences across populations."),
        ("DCI", "LS3.A: Inheritance of Traits", "DNA codes for proteins (enzymes). Variations in gene regulation determine how much lactase enzyme is produced, directly causing the observable trait of lactose tolerance or intolerance. This is gene expression controlling phenotype."),
        ("CCC", "Cause and Effect", "A clear causal chain connects gene activity → enzyme production → substrate breakdown → symptom presence. Changing the initial cause (gene expression level) predictably changes the final effect (digestive outcome).")
    ],
    "cast_items": [
        "Model the causal relationship between gene expression and enzyme-mediated digestion",
        "Explain how DNA variations lead to observable phenotypic differences across populations",
        "Predict digestive outcomes based on genetic and environmental inputs"
    ],
    "cast_questions": [
        ("Explain:", "Two siblings eat identical ice cream sundaes. One feels fine; the other has severe stomach cramps an hour later. Using your model, trace the causal chain from their LCT gene activity to their different outcomes."),
        ("Analyze:", "About 90% of East Asian populations are lactose intolerant while 90% of Northern Europeans are tolerant. Using your understanding of gene expression and natural selection, explain this difference.")
    ],
    "background_intro": "Lactose intolerance is one of the most elegant examples of how a single gene controls a physical trait through enzyme production — and how human culture (dairy farming) drove genetic evolution in real time.",
    "background_sections": [
        ("The Lactase Gene (LCT)", "The LCT gene on chromosome 2 encodes the enzyme lactase-phlorizin hydrolase, which sits on the brush border of small intestine epithelial cells. In all mammals, this gene is active during infancy (when the sole food is mother's milk) and naturally decreases in expression after weaning. This 'lactase non-persistence' is the ancestral, default human condition — NOT a disorder."),
        ("The Lactase Persistence Mutation", "About 7,500 years ago, a mutation arose upstream of the LCT gene that prevents the normal age-related decrease in expression. This mutation (specifically, a C-to-T change at position -13910) doesn't change the enzyme itself — it changes REGULATION, keeping the gene 'turned on' into adulthood. This mutation spread rapidly in populations that domesticated dairy cattle, providing a powerful selective advantage: access to a rich, reliable food source."),
        ("Why Symptoms Occur", "When lactose reaches the large intestine undigested, resident bacteria eagerly ferment it through anaerobic metabolism. This produces hydrogen gas, methane, and short-chain fatty acids. The gas causes bloating and cramps. Additionally, the undigested lactose is osmotically active — it draws water into the intestinal lumen through osmosis, causing diarrhea. The severity depends on how much lactose reaches the colon, which depends on how much lactase enzyme was available."),
        ("Global Distribution", "Lactase persistence follows dairy farming history almost perfectly. Northern European populations (90%+ tolerant), East African pastoralist groups like the Maasai and Tutsi (50-90% tolerant), and some Middle Eastern populations show high tolerance — all cultures with thousands of years of dairy tradition. East Asian, West African, Native American, and Aboriginal Australian populations show 70-100% intolerance — cultures without historical dairy farming. This is one of the clearest examples of gene-culture co-evolution.")
    ],
    "lever_L": "Students identify lactase gene activity, enzyme production, lactose breakdown, and gut bacteria response as components.",
    "lever_E": "Students discover the causal chain: gene activity (+) enzyme → enzyme (+) breakdown → undigested lactose (+) bacteria response.",
    "lever_V": "Students build a model showing how gene expression level determines digestive outcomes.",
    "lever_Ev": "Students run tolerant, intolerant, and partial scenarios to discover threshold effects.",
    "lever_R": "Students add dairy amount, microbiome composition, or epigenetic regulation for more realistic modeling.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with milk and DNA", "say": "Raise your hand if ice cream has ever made you feel terrible. Now raise your hand if it never has. Why the difference?", "do": "Quick informal poll. Don't ask students to self-identify — just note the split exists.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're solving a genetics mystery: why your DNA decides whether you can drink milk.", "do": "Have students read objectives. Pre-teach 'gene expression' as 'reading a recipe from the cookbook.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Milkshake comparison", "say": "Same milkshake, two people, completely different outcomes. One gene makes the difference.", "do": "Show the global map of lactose tolerance. Ask: Why the geographic pattern?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how ONE gene controls whether you can enjoy pizza or suffer after it.", "do": "Preview LEVER steps. Emphasize the causal chain: gene → enzyme → digestion → symptoms.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "Which part of this system is the 'input' and which parts are 'outputs'?", "do": "Guide sorting. Gene activity is the key external driver — everything else cascades from it.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More gene activity means more enzyme. More enzyme means more breakdown. But what happens when there's NOT enough enzyme?", "do": "Draw the complete causal chain. Show how it branches at 'undigested lactose → bacteria.'", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Digestion outcome graphs", "say": "Let's test three genetic scenarios: fully tolerant, fully intolerant, and somewhere in between.", "do": "Students predict outcomes. The partial tolerance threshold is the key discovery.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Here's the twist: lactose INTOLERANCE is the default. Tolerance is the mutation. We evolved to stop drinking milk.", "do": "Show the evolutionary timeline: mutation arose 7,500 years ago with dairy farming.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Dairy product design", "say": "65% of the world can't drink milk. Design a product that solves this problem using enzyme science.", "do": "Groups design solutions: pre-added lactase, bacterial fermentation, or dosing strategies.", "time": "12 min"}
    ],
    "sort_reasoning": "Lactase Gene Activity is external because it's determined by your genetics — you don't control which version of the gene you inherited. Lactase Enzyme Production, Lactose Breakdown, and Gut Bacteria Response are internal because they are all downstream consequences of gene expression level.",
    "relationships": [
        ("Lactase Gene Activity to Lactase Enzyme Production", "POSITIVE (+)", "Higher gene expression means more mRNA is transcribed and translated into functional lactase protein. The gene is the blueprint; more reading = more enzyme."),
        ("Lactase Enzyme Production to Lactose Breakdown", "POSITIVE (+)", "More enzyme molecules in the small intestine means more lactose molecules get broken down into absorbable glucose and galactose before reaching the large intestine."),
        ("Lactose Breakdown to Gut Bacteria Response", "NEGATIVE (-)", "When more lactose is broken down in the small intestine, less undigested lactose reaches the large intestine bacteria. Higher breakdown means less fermentation and fewer symptoms.")
    ],
    "sim_answers": [
        ("Lactose Tolerant Scenario", "With HIGH Lactase Gene Activity, Enzyme Production is high, Lactose Breakdown is nearly complete, and Gut Bacteria Response is minimal — almost no undigested lactose reaches the colon. The person drinks milk with no symptoms because the causal chain handles the lactose before bacteria ever encounter it."),
        ("Lactose Intolerant Scenario", "With LOW Lactase Gene Activity, Enzyme Production drops to near zero, Lactose Breakdown is minimal, and most lactose passes intact to the large intestine where bacteria ferment it aggressively. Gut Bacteria Response is high — producing gas (bloating/cramps), drawing in water (diarrhea), and causing discomfort 30-120 minutes after dairy consumption.")
    ],
    "reflection_exemplars": [
        ("Why is tolerance the mutation?", "All mammals stop producing lactase after weaning — it's an unnecessary energy expenditure once you stop nursing. The 'normal' state is lactase non-persistence. About 7,500 years ago, humans who domesticated cattle gained a massive survival advantage if they could digest milk as adults — a rich, reliable food source. A mutation that kept the lactase gene active was so advantageous that it spread through dairy-farming populations in just a few thousand years. Lactose tolerance is one of the fastest examples of natural selection in humans."),
        ("What does the threshold effect mean in real life?", "Our model shows that at MEDIUM gene activity, there's enough enzyme to handle small amounts of lactose but not large amounts. This matches reality: many lactose-intolerant people can eat a slice of cheese (low lactose) or a cup of yogurt (bacteria pre-digested the lactose) but can't drink a glass of milk. The threshold effect means intolerance isn't binary — it's about the RATIO of available enzyme to consumed lactose.")
    ],
    "stem_intro": "Frame this as a food science entrepreneurship challenge. The lactose-free market is worth over $15 billion globally and growing. Students are food scientists designing products for a massive underserved market.",
    "stem_concepts": [
        ("Enzymatic Pre-treatment", "Adding microbial lactase enzyme directly to milk before packaging. The enzyme breaks down 99%+ of lactose during cold storage, producing sweeter-tasting milk (glucose and galactose taste sweeter than lactose)."),
        ("Bacterial Fermentation", "Using Lactobacillus bacteria to ferment lactose in dairy products like yogurt and aged cheese. The bacteria consume lactose and produce lactic acid, naturally reducing lactose content by 20-80%."),
        ("Enzyme Supplements", "Lactase pills taken before dairy consumption. The challenge is timing — the enzyme needs to reach the small intestine simultaneously with the lactose, and stomach acid partially deactivates it.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design uses correct enzyme science, addresses specific lactose threshold levels, includes testing plan, and considers taste/texture/cost trade-offs"),
        ("Proficient (3)", "Design applies enzyme or fermentation principles correctly with reasonable product specifications"),
        ("Developing (2)", "Design addresses lactose removal but lacks scientific detail or testing plan"),
        ("Beginning (1)", "Design is incomplete or doesn't connect to gene expression / enzyme concepts")
    ],
    "support": [
        "Provide a pre-drawn diagram showing: Gene → mRNA → Protein (enzyme) → Chemical reaction → Products",
        "Use a lock-and-key analogy for enzyme specificity: lactase is the ONLY key that opens the lactose lock",
        "Sentence frames: 'When lactase gene activity is low, enzyme production __ which means lactose breakdown __ causing gut bacteria to __'"
    ],
    "extensions": [
        "Research CRISPR possibilities: Could we theoretically 'turn on' the lactase gene in adults? What are the ethical implications?",
        "Investigate the parallel evolution of lactase persistence: It evolved independently at least 5 times in different dairy cultures with different mutations",
        "Compare the speed of lactase persistence evolution (7,500 years) to other human adaptations — why was this so fast?"
    ],
    "cross_curr": [
        ("Math", "Calculate: If 65% of 8 billion people are lactose intolerant, and the average person would spend $50/year on lactose-free products, what's the total market size?"),
        ("ELA", "Write a persuasive product pitch for a lactose-free dairy company targeting an Asian market where 90% of the population is intolerant."),
        ("Social Studies", "Research how dairy farming spread across Europe and Africa and how this cultural practice drove genetic change — a case study in gene-culture co-evolution.")
    ],
    "misconceptions": [
        ("Lactose intolerance is an allergy", "Lactose intolerance is NOT an allergy. Allergies involve the immune system attacking a protein (like milk protein allergy, which is different and rarer). Lactose intolerance is a deficiency — not enough enzyme to break down a sugar. No immune response is involved. The distinction matters because allergies can be life-threatening (anaphylaxis) while lactose intolerance is uncomfortable but not dangerous.", "Ask: What's the difference between being allergic to peanuts and being unable to digest beans? One involves your immune system; the other involves missing an enzyme."),
        ("Lactose intolerant people can't eat ANY dairy", "Most lactose-intolerant people can handle some dairy. Aged cheeses (cheddar, parmesan) contain almost no lactose because bacteria consumed it during aging. Yogurt has 20-50% less lactose than milk for the same reason. Many intolerant people can tolerate a splash of milk in coffee. The threshold varies by individual.", "Try the threshold experiment: Our model shows MEDIUM gene activity can handle small amounts. Most 'intolerant' people actually have SOME lactase — just not enough for a glass of milk."),
        ("Lactose intolerance is a modern disease", "Lactose intolerance is the ancestral human condition — every human before 7,500 years ago was lactose intolerant as an adult. Tolerance is the modern mutation. We've medicalized the DEFAULT state and treated the mutation as normal, probably because medical science was developed primarily in Northern European populations where tolerance is common.", "Show the evolutionary timeline: 200,000 years of human existence with intolerance; only 7,500 years with the tolerance mutation. Which is 'normal'?")
    ]
}

L07 = {
    "id": "G09L1-L07",
    "title": "How Social Media Hacks Your Brain",
    "subtitle": "Modeling Dopamine, Feedback Loops, and Digital Addiction",
    "ngss": "HS-LS1-2",
    "ngss_desc": "Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms.",
    "big_question": "Why can't you put your phone down — even when you know you should?",
    "objectives": [
        "Model how social media platforms exploit the brain's dopamine reward system to sustain engagement",
        "Explain the feedback loop between notifications, dopamine release, and compulsive phone checking",
        "Predict how increased screen time degrades self-esteem through social comparison mechanisms",
        "Analyze how design features of social media apps are engineered to create habit-forming behavior"
    ],
    "vocabulary": [
        ("Dopamine", "A neurotransmitter that acts as the brain's reward chemical — released during pleasurable activities like eating, socializing, and receiving likes on social media, reinforcing behaviors that triggered its release"),
        ("Variable Reward Schedule", "A pattern where rewards (likes, comments, notifications) arrive at unpredictable intervals — the same mechanism used in slot machines — which is far more addictive than predictable rewards"),
        ("Social Comparison", "The psychological process of evaluating your own worth, appearance, or success by comparing yourself to others — amplified by curated social media feeds showing highlight reels of other people's lives"),
        ("Neuroplasticity", "The brain's ability to physically rewire itself based on repeated experiences — meaning habitual phone use literally reshapes neural pathways to crave more screen time")
    ],
    "components": [
        ("Notification Frequency", "The rate at which a social media platform sends push notifications, alerts, and badges designed to pull users back into the app", True),
        ("Screen Time", "The total number of hours per day spent actively using social media platforms on phones, tablets, and computers", False),
        ("Dopamine Release", "The amount of dopamine neurotransmitter released in the brain's reward circuit in response to social media interactions like likes, comments, and new followers", False),
        ("Social Comparison", "The intensity of comparing oneself to others based on curated images, achievements, and lifestyles displayed on social media feeds", False),
        ("Self-Esteem Level", "An individual's overall sense of self-worth, confidence, and personal value — which can be eroded by chronic social comparison and validation-seeking online", False)
    ],
    "think_about_it": "When Notification Frequency is high, what chain reaction does it trigger through Dopamine Release, Screen Time, Social Comparison, and ultimately Self-Esteem Level? Where does the feedback loop trap you?",
    "scenarios": [
        ("Moderate Use, Notifications Off", "Set Notification Frequency to low — observe how Dopamine Release, Screen Time, and Self-Esteem respond when the platform can't pull you back in"),
        ("Heavy Use, All Notifications On", "Set Notification Frequency to maximum — observe the dopamine-driven loop that increases Screen Time and escalates Social Comparison"),
        ("Gradual Escalation", "Start with low Notification Frequency and slowly increase it over time — find the tipping point where healthy use becomes compulsive")
    ],
    "sim_scenarios": [
        ("Low Notifications", "Notification Frequency set to low, simulating intentional phone use", "What do you predict will happen to Screen Time and Self-Esteem when the app can't constantly pull you back in?"),
        ("High Notifications", "Notification Frequency at maximum, simulating default app settings", "What do you predict happens to the dopamine-screen time loop when notifications bombard you every few minutes?"),
        ("Gradual Escalation", "Notification Frequency slowly increasing over weeks", "At what point do you predict casual social media use crosses into compulsive, addictive behavior?")
    ],
    "discoveries": [
        "Social media platforms exploit the brain's dopamine reward system using the same variable reward schedule as slot machines — unpredictable likes and notifications are more addictive than predictable ones",
        "A positive feedback loop forms: notifications trigger dopamine, dopamine drives more screen time, more screen time means more social comparison, and lower self-esteem drives users to seek more online validation",
        "The tipping point from healthy to compulsive use is driven by notification frequency — once the brain is conditioned to expect constant rewards, it becomes difficult to disengage",
        "Self-esteem erosion is gradual and often invisible to the user, making the damage harder to recognize until it's deeply established in neural pathways"
    ],
    "answer": "You can't put your phone down because social media platforms are engineered to exploit your brain's dopamine reward system. Every notification triggers a small dopamine hit, reinforcing the behavior of checking your phone. The variable timing of likes and comments creates an unpredictable reward schedule — the exact mechanism that makes slot machines addictive. As screen time increases, social comparison intensifies, slowly eroding self-esteem. Lower self-esteem drives you to seek MORE validation online, creating a self-reinforcing loop that literally rewires your brain to crave the next notification.",
    "stem_title": "Design a Digital Wellness App",
    "stem_mission": "Design an app or system that helps teenagers recognize and break the dopamine-driven feedback loop by providing real-time awareness of their usage patterns and emotional state.",
    "stem_scenario": "A school district has reported that 73% of its students spend more than 4 hours daily on social media, with school counselors seeing a 40% increase in anxiety and depression referrals. The superintendent has hired your team to design a digital wellness tool that doesn't just limit screen time, but helps students understand WHY they keep going back and gives them strategies to break the cycle.",
    "stem_questions": [
        "What behavioral indicators would your system monitor to detect when a user is in a compulsive usage loop?",
        "How would you design interventions that are helpful without being annoying or patronizing?",
        "What role should peer support or social features play in a digital wellness app?"
    ],
    "stem_design_qs": [
        "How would your app detect the difference between intentional use (texting a friend) and compulsive scrolling?",
        "What data visualizations would help users see their own dopamine-driven patterns?",
        "How would you incorporate the neuroscience of habit-breaking into your app's intervention strategies?",
        "How would you test whether your app actually improves self-esteem and reduces compulsive use?"
    ],
    "career": "Behavioral Neuroscientists study how the brain drives behavior, including addiction and habit formation. They work in research labs, pharmaceutical companies, and tech ethics departments, earning $70,000–$140,000/year. UX Ethics Designers at companies like Apple and Google earn $90,000–$170,000/year designing technology that respects human well-being.",
    "images": {
        "cover": ("G09L1-L07-cover.png", "A photorealistic, cinematic image of a diverse group of 14-15 year old students in a dimly lit room all staring down at their glowing phone screens with notification badges visible, their faces illuminated by blue light, one student in the center looking up with a thoughtful expression while the others remain absorbed, dramatic lighting contrast"),
        "landscape": ("G09L1-L07-landscape.png", "A diverse group of 14-15 year old students in a modern neuroscience classroom examining large brain diagrams on screens showing the dopamine reward pathway lit up, one student pointing to the nucleus accumbens region, engaged and curious expressions, natural lighting"),
        "modeling": ("G09L1-L07-modeling.png", "A diverse group of 14-15 year old students at laptops building computational models of the brain's reward system, colorful feedback loop diagrams visible on their screens, modern classroom with neuroscience posters"),
        "discussion": ("G09L1-L07-discussion.png", "A Black teacher leading an animated discussion with diverse 14-15 year old students about social media and the brain, a diagram comparing slot machine reward schedules to notification patterns displayed on a smartboard, students engaged with hands raised"),
        "stem": ("G09L1-L07-stem.png", "Diverse 14-15 year old students designing digital wellness app prototypes on whiteboards and tablets, wireframes and user flow diagrams visible, collaborative design thinking environment with sticky notes and sketches")
    },
    "pre_assessment": [
        "How many hours per day do you spend on social media, and how does it make you feel after using it?",
        "Why do you think it's so hard to stop scrolling even when you know you should do something else?",
        "What do you think happens in your brain when you get a like or comment on your post?",
        "Do you think social media affects your mood or how you feel about yourself? Explain your reasoning."
    ],
    "extend_components": [
        ("Sleep Quality", "The number of hours and depth of restorative sleep, which is severely disrupted by blue light exposure and dopamine-driven late-night scrolling, creating a secondary health cascade"),
        ("Anxiety Level", "The chronic state of worry and unease amplified by constant social comparison, fear of missing out (FOMO), and the pressure to maintain an online persona"),
        ("Algorithm Intensity", "The aggressiveness of the platform's recommendation algorithm, which learns what triggers dopamine release in each individual user and serves increasingly targeted content")
    ],
    "reflections": [
        "How does your model explain why social media companies design their apps with variable notification schedules rather than predictable ones?",
        "What does the positive feedback loop in your model reveal about why quitting social media feels so difficult?",
        "How does the relationship between social comparison and self-esteem create a trap that keeps users engaged?",
        "If you could redesign one feature of social media based on your model, what would you change and why?",
        "What are the ethical implications of companies knowingly engineering products that exploit the brain's reward system?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model of the brain's dopamine reward system to illustrate how hierarchical biological systems — from neurotransmitters to behavior to mental health — interact across scales."),
        ("Disciplinary Core Idea", "LS1.A: Structure and Function", "The nervous system's hierarchical organization — from neurotransmitter molecules to neural circuits to behavioral patterns — demonstrates how disruption at the molecular level (dopamine dysregulation) cascades to affect the whole organism's functioning and well-being."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from external stimulus (notification) to molecular response (dopamine release) to behavioral change (increased screen time) to psychological outcome (self-esteem change), demonstrating multi-level cause and effect.")
    ],
    "cast_items": [
        "Model how the brain's dopamine reward system creates a positive feedback loop with social media notifications",
        "Analyze the hierarchical relationship between neurotransmitter activity, behavioral patterns, and psychological well-being",
        "Predict how changes to notification design could disrupt or reinforce the addictive feedback loop"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student turns off all push notifications on their social media apps but still checks them manually every 15 minutes. According to your model, which component is most responsible for maintaining the compulsive behavior?"),
        ("Constructed Response:", "Using your model, explain the complete causal chain from a single Instagram notification to a measurable decrease in self-esteem. Identify every component involved and whether each relationship is positive or negative.")
    ],
    "background_intro": "Your brain evolved over millions of years to seek rewards that helped your ancestors survive — food, social bonding, mating opportunities. Every time you found something rewarding, your brain released dopamine to say 'do that again.' Social media has hijacked this ancient system, delivering hyper-concentrated social rewards at a speed and frequency your brain was never designed to handle.",
    "background_sections": [
        ("The Dopamine Reward Pathway", "Dopamine is released by neurons in the ventral tegmental area (VTA) and projects to the nucleus accumbens and prefrontal cortex. When you receive a like, comment, or new follower, this pathway activates — the same circuit triggered by food, sex, and drugs. The key insight is that dopamine doesn't just signal pleasure; it signals ANTICIPATION of reward. The buzz of a notification is often more powerful than the actual content, because your brain is responding to the POSSIBILITY of a reward."),
        ("Variable Reward Schedules", "B.F. Skinner discovered in the 1950s that the most addictive reward pattern is variable ratio reinforcement — rewards that come at unpredictable intervals. Slot machines use this principle: you never know when the next win is coming, so you keep pulling. Social media does the same thing. You don't know which refresh will bring a flood of likes or a disappointing nothing. This unpredictability keeps you checking, because the next time MIGHT be the big payoff."),
        ("Social Comparison Theory", "Psychologist Leon Festinger proposed in 1954 that humans have a fundamental drive to evaluate themselves by comparing to others. On social media, you're comparing your unfiltered daily life to everyone else's curated highlight reel — their best photos, achievements, and moments. Research shows this 'upward social comparison' consistently decreases self-esteem and life satisfaction, particularly in adolescents whose identity is still forming."),
        ("Neuroplasticity and Digital Habits", "The brain physically changes in response to repeated experiences — neurons that fire together wire together. Heavy social media use strengthens the neural pathways associated with phone-checking behavior while weakening pathways for sustained attention, delayed gratification, and real-world social skills. Brain imaging studies show that adolescents who use social media heavily have measurable differences in their prefrontal cortex (decision-making) and amygdala (emotion processing) compared to light users.")
    ],
    "lever_L": "Students identify notification frequency, screen time, dopamine release, social comparison, and self-esteem level as the key components of the social media–brain interaction system.",
    "lever_E": "Students determine that notifications trigger dopamine release, dopamine drives screen time, screen time enables social comparison, and social comparison erodes self-esteem — forming a self-reinforcing positive feedback loop.",
    "lever_V": "Students build a computational model showing the positive feedback loop between social media design features and the brain's reward system, and the downstream effects on self-esteem.",
    "lever_Ev": "Students run low-notification, high-notification, and gradual escalation scenarios to test their model and identify the tipping point where use becomes compulsive.",
    "lever_R": "Students add sleep quality, anxiety level, or algorithm intensity to explore more realistic models of social media's impact on adolescent well-being.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic image of teens glowing in phone light", "say": "The average American teen spends 4.8 hours a day on social media. That's more time than sleeping, doing homework, or being with family. Why?", "do": "Show the statistic on screen. Let it sink in. Ask: Does that number sound right for you? Higher? Lower?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today we're reverse-engineering the technology that's designed to hack your brain. Once you see the code, you can't unsee it.", "do": "Have students read objectives. Pre-teach 'dopamine' and 'variable reward schedule.' Ask who knows how slot machines work.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why can't you put your phone down?", "say": "You've told yourself a hundred times: 'five more minutes.' An hour later, you're still scrolling. That's not weakness — that's engineering.", "do": "Quick-write: Students describe a time they couldn't stop scrolling even though they wanted to. Pair-share.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to build a model of what's happening inside your skull every time your phone buzzes.", "do": "Preview LEVER steps. Emphasize this is about understanding the SYSTEM, not shaming anyone's phone use.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for social media brain model", "say": "What's the one thing the app CONTROLS that starts the whole chain? And what are the things that happen inside your brain and mind?", "do": "Guide sorting: notification frequency is external (the platform controls it). Everything else is internal to the user. Discuss why this matters.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "Trace the chain: notification hits your phone. Then what? What fires in your brain? What do you DO? And how do you FEEL after?", "do": "Help students build the complete causal loop. Identify the positive feedback loop and explain why it escalates.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs showing notification-driven behavior and self-esteem curves", "say": "Let's find out: what happens if you turn notifications OFF? And what happens if they're on all the time?", "do": "Students predict outcomes, then run all three scenarios. Key discovery: the tipping point from casual to compulsive use.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings: dopamine loop, variable rewards, comparison trap", "say": "Social media isn't a product. YOU are the product. The app is the machine designed to harvest your attention.", "do": "Discuss the ethics of addictive design. Compare to tobacco industry knowingly designing addictive products. Is this different?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Digital wellness app design challenge", "say": "Now that you've seen the code, write the antidote. Design an app that helps people break the loop.", "do": "Groups design digital wellness tools using model insights. Must address the dopamine loop AND social comparison. Present prototypes.", "time": "12 min"}
    ],
    "sort_reasoning": "Notification Frequency is the external component because it is controlled by the social media platform's design team, not by the user's biology. Screen Time, Dopamine Release, Social Comparison, and Self-Esteem Level are all internal because they represent the user's neurological responses, behavioral patterns, and psychological states that change as a consequence of the external stimulus.",
    "relationships": [
        ("Notification Frequency to Dopamine Release", "POSITIVE (+)", "More frequent notifications create more opportunities for the brain's reward system to activate. Each buzz or badge triggers an anticipatory dopamine response, even before the user sees the content."),
        ("Dopamine Release to Screen Time", "POSITIVE (+)", "Higher dopamine release reinforces phone-checking behavior. The brain learns that opening the app produces a reward, driving increased screen time as the user seeks to replicate the pleasurable feeling."),
        ("Screen Time to Social Comparison", "POSITIVE (+)", "More time spent scrolling through feeds means more exposure to curated images of other people's lives, achievements, and appearances, intensifying the social comparison process."),
        ("Social Comparison to Self-Esteem Level", "NEGATIVE (-)", "Increased social comparison — especially upward comparison to idealized, filtered content — erodes self-esteem as individuals perceive themselves as less attractive, successful, or popular than their peers appear online.")
    ],
    "sim_answers": [
        ("Low Notifications Scenario", "When Notification Frequency is low, the dopamine reward cycle activates less often. Screen Time decreases because the brain isn't being constantly pulled back to the app. With less scrolling, Social Comparison diminishes, and Self-Esteem Level remains relatively stable. The model shows that controlling the entry point — notifications — can disrupt the entire addictive loop."),
        ("High Notifications Scenario", "When Notification Frequency is at maximum, Dopamine Release spikes repeatedly throughout the day. Screen Time escalates dramatically as the brain's reward pathway is continuously reinforced. Social Comparison intensifies with more feed exposure, and Self-Esteem Level drops progressively. The positive feedback loop becomes self-sustaining — even without notifications, the brain starts checking the app in anticipation of rewards.")
    ],
    "reflection_exemplars": [
        ("Why is the positive feedback loop so hard to break?", "The loop is self-reinforcing at every stage. Lower self-esteem from social comparison drives you to seek validation online (more likes = temporary self-esteem boost), which increases screen time, which exposes you to more comparison content, which further lowers self-esteem. Additionally, neuroplasticity means the brain has physically rewired itself to make phone-checking automatic — it becomes a reflex, not a conscious choice. Breaking the loop requires disrupting it at the entry point (notifications) because once the dopamine cycle starts, the biological drive to continue is extremely powerful."),
        ("What makes variable rewards more addictive than predictable ones?", "Predictable rewards — like getting exactly 10 likes on every post — allow the brain to habituate and lose interest. Variable rewards keep the brain in a state of constant anticipation because you never know if the next check will bring 0 likes or 200. This uncertainty is neurologically more stimulating than certainty. The brain releases more dopamine in ANTICIPATION of a possible reward than during the reward itself. This is exactly why slot machines are more addictive than vending machines — both give you something, but only one keeps you guessing.")
    ],
    "stem_intro": "Present the challenge: A school district is seeing measurable increases in student anxiety and depression linked to social media use. Your team has been hired to design a digital wellness tool that helps students understand the neuroscience behind their phone habits and provides science-based strategies for healthier use patterns.",
    "stem_concepts": [
        ("Behavioral Nudges", "Small design interventions that gently redirect behavior without removing choice. Examples include usage timers that show accumulated daily screen time, grayscale mode that removes the visual dopamine trigger of colorful feeds, and 'take a breath' prompts before opening an app."),
        ("Biofeedback Integration", "Using physiological data — heart rate variability, screen distance, typing speed — to detect when a user is in a compulsive scrolling state versus intentional use. The system could intervene only when stress indicators suggest harmful patterns."),
        ("Habit Replacement Theory", "Neuroscience shows that habits can't simply be eliminated — they must be replaced with alternative behaviors that satisfy the same need. A wellness app might redirect the social connection need from scrolling feeds to messaging a real friend or joining an in-person activity.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design addresses the dopamine loop at multiple points, uses neuroscience evidence from the model, includes personalized detection of compulsive patterns, and provides adaptive interventions that users would actually use"),
        ("Proficient (3)", "Design targets the dopamine loop with reasonable interventions and includes some basis in neuroscience from the model"),
        ("Developing (2)", "Design addresses screen time reduction but doesn't connect strategies to the underlying neuroscience or reward system"),
        ("Beginning (1)", "Design is incomplete or simply locks the phone without addressing the behavioral and neurological mechanisms")
    ],
    "support": [
        "Provide a simplified diagram of the dopamine reward pathway (VTA → nucleus accumbens → prefrontal cortex) for reference",
        "Use real-world analogies: notification bell = slot machine lever, likes = variable jackpot, infinite scroll = no exit sign",
        "Sentence frames: 'When notification frequency increases, dopamine release __ because __, which causes screen time to __ because __'"
    ],
    "extensions": [
        "Research the internal documents leaked by Facebook whistleblower Frances Haugen showing the company knew Instagram harmed teen mental health — analyze the ethical implications",
        "Investigate how different social media platforms (TikTok, Instagram, Snapchat) use different variable reward mechanisms and compare their addictive potential",
        "Design an experiment to test whether turning off notifications for one week measurably affects mood and screen time — then actually run it"
    ],
    "cross_curr": [
        ("Math", "Analyze screen time data: Calculate the percentage of waking hours spent on social media and create statistical models predicting screen time based on notification frequency"),
        ("ELA", "Write a persuasive argument for or against government regulation of addictive design features in social media platforms targeting minors"),
        ("Social Studies", "Research the history of addictive product design — from cigarettes to slot machines to social media — and analyze how societies have responded to protect consumers")
    ],
    "misconceptions": [
        ("Social media addiction isn't real — it's just a lack of willpower", "Social media platforms are engineered by teams of behavioral psychologists and neuroscientists to be as habit-forming as possible. The same brain circuits activated by social media are activated by gambling and substance use. Brain imaging studies show measurable changes in the prefrontal cortex and reward pathways of heavy social media users. Calling it 'willpower' ignores the neuroscience.", "Ask: If a casino designed a slot machine to be maximally addictive and someone couldn't stop playing, would you blame the player or the machine designer?"),
        ("I use social media because I want to — it's my choice", "While the initial download is a choice, the continued use is heavily influenced by design features specifically created to bypass conscious decision-making. Variable reward schedules, autoplay, infinite scroll, and notification timing are all optimized through A/B testing to maximize engagement. Your 'choice' is being made in an environment engineered to produce a specific outcome.", "Thought experiment: If the grocery store rearranged itself every visit to maximize the time you spend inside, and you always ended up buying more than you planned, is that really free choice?"),
        ("Only weak or lonely people get addicted to social media", "Research shows that social media's addictive mechanisms work on ALL brains — the dopamine reward system is universal. In fact, highly social people may be MORE susceptible because they have a stronger need for social feedback. Adolescent brains are particularly vulnerable because the prefrontal cortex (impulse control) isn't fully developed until age 25.", "Show the data: 95% of teens use social media. If 'only weak people' were affected, the usage rate would be much lower. The design works on everyone.")
    ]
}

L08 = {
    "id": "G09L1-L08",
    "title": "Fast Fashion Is Killing the Planet",
    "subtitle": "Modeling the Environmental Cost of Cheap Clothing",
    "ngss": "HS-ESS3-4, HS-ETS1-3",
    "ngss_desc": "Evaluate or refine a technological solution that reduces impacts of human activities on natural systems. Evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs that account for a range of constraints.",
    "big_question": "How does a $5 T-shirt end up costing the planet so much?",
    "objectives": [
        "Model how consumer demand for cheap clothing drives a cycle of overproduction, waste, and environmental destruction",
        "Explain the relationships between production rate, textile waste, water consumption, and carbon emissions in the fashion industry",
        "Predict the environmental consequences of current fast fashion trends continuing over the next decade",
        "Evaluate technological and behavioral solutions that could reduce the fashion industry's environmental footprint"
    ],
    "vocabulary": [
        ("Fast Fashion", "A business model based on rapidly producing large volumes of trendy clothing at low cost, encouraging consumers to buy frequently and discard quickly — brands like Shein, H&M, and Zara release thousands of new styles weekly"),
        ("Textile Waste", "Discarded clothing and fabric that ends up in landfills or incinerators — the average American throws away 81.5 pounds of clothing per year, and globally 92 million tons of textile waste is generated annually"),
        ("Water Footprint", "The total volume of fresh water used in the production of goods — a single cotton T-shirt requires approximately 2,700 liters of water to produce, equivalent to one person's drinking water for 2.5 years"),
        ("Carbon Footprint", "The total greenhouse gas emissions caused by manufacturing, transporting, and disposing of a product — the fashion industry produces 10% of global carbon emissions, more than international flights and maritime shipping combined")
    ],
    "components": [
        ("Consumer Demand", "The volume and frequency of clothing purchases driven by trends, low prices, social media marketing, and the perceived need for new outfits — the average consumer buys 68 garments per year", True),
        ("Production Rate", "The speed and volume at which clothing manufacturers produce garments, driven by consumer demand and the pressure to deliver new styles weekly at the lowest possible cost", False),
        ("Textile Waste", "The amount of discarded clothing, fabric scraps from manufacturing, and unsold inventory that ends up in landfills, is incinerated, or is exported to developing nations", False),
        ("Water Consumption", "The total freshwater used in growing cotton, dyeing fabric, washing textiles, and finishing garments throughout the supply chain", False),
        ("Carbon Emissions", "The total greenhouse gases released from manufacturing processes, global shipping, synthetic fiber production from petroleum, and decomposition of textile waste in landfills", False)
    ],
    "think_about_it": "When Consumer Demand increases because of a new social media trend, what chain reaction does it trigger through Production Rate, and how does that amplify Textile Waste, Water Consumption, and Carbon Emissions simultaneously?",
    "scenarios": [
        ("Current Trends Continue", "Set Consumer Demand to high (current levels) — observe the environmental outputs of the fast fashion system"),
        ("Conscious Consumer Shift", "Reduce Consumer Demand by 50% simulating a buy-less movement — observe how environmental outputs respond"),
        ("Circular Fashion Model", "Maintain Consumer Demand but add recycling and extend garment lifespan — observe whether technological solutions can offset high demand")
    ],
    "sim_scenarios": [
        ("Business as Usual", "Consumer Demand at current high levels", "What do you predict will happen to textile waste and carbon emissions if shopping habits stay exactly the same for the next 10 years?"),
        ("Buy Less Movement", "Consumer Demand reduced by 50%", "What do you predict happens to the entire supply chain when people buy half as many clothes?"),
        ("Circular Fashion", "High demand but with recycling and reuse systems", "Can technology and recycling offset the environmental impact of high consumer demand?")
    ],
    "discoveries": [
        "Consumer demand is the primary driver — every additional garment purchased triggers water consumption, carbon emissions, and eventual textile waste in a one-directional cascade",
        "The fast fashion system produces environmental damage at every stage: growing raw materials (water), manufacturing (carbon), shipping (carbon), wearing (microplastics), and disposal (landfill waste)",
        "Reducing demand has a larger environmental impact than improving recycling, because most environmental damage occurs during production, not disposal",
        "The fashion industry's environmental impact is hidden from consumers — the true cost of a $5 T-shirt includes 2,700 liters of water, 7 kg of CO2, and eventual landfill space for 200+ years"
    ],
    "answer": "A $5 T-shirt costs the planet enormously because the price tag hides the true environmental cost. Consumer demand for cheap, trendy clothing drives manufacturers to produce at breakneck speed using enormous quantities of water (2,700 liters per shirt), generating massive carbon emissions (10% of global total), and creating 92 million tons of textile waste annually. The model reveals a one-directional cascade: consumer demand drives production rate, which simultaneously increases water consumption, carbon emissions, and textile waste. The system is designed to be disposable — and the planet pays the hidden price.",
    "stem_title": "Design a Sustainable Fashion Solution",
    "stem_mission": "Design a business model, technology, or system that reduces the environmental footprint of the clothing industry while remaining economically viable and appealing to teenage consumers.",
    "stem_scenario": "A major clothing retailer wants to become more sustainable but can't afford to lose teenage customers. They've hired your team to design a solution — whether it's a new material, a recycling system, a rental service, or a completely new business model — that dramatically reduces water, carbon, and waste while keeping clothes affordable and trendy.",
    "stem_questions": [
        "What stage of the fashion supply chain causes the most environmental damage, and how would your solution target it?",
        "How would you make sustainable fashion cool enough that teenagers actually choose it over fast fashion?",
        "What trade-offs would your solution require, and are they acceptable?"
    ],
    "stem_design_qs": [
        "Would your solution focus on the production side (materials, manufacturing), the consumer side (behavior change, rental models), or the disposal side (recycling, upcycling)?",
        "How would you measure whether your solution actually reduces environmental impact?",
        "What would your sustainable clothing cost, and would your target market pay that price?",
        "How would you scale your solution to make a measurable impact on the industry's 92 million tons of annual textile waste?"
    ],
    "career": "Environmental Engineers design systems to reduce industrial pollution and waste, earning $65,000–$130,000/year. Sustainable Fashion Designers create clothing using eco-friendly materials and ethical production methods, working at brands like Patagonia, Eileen Fisher, and Stella McCartney, earning $50,000–$120,000/year.",
    "images": {
        "cover": ("G09L1-L08-cover.png", "A photorealistic, cinematic split image showing a glamorous fast fashion store on one side with colorful cheap clothing racks and shoppers, and on the other side a massive mountain of discarded textile waste in a developing country landfill, dramatic contrast lighting emphasizing the hidden cost"),
        "landscape": ("G09L1-L08-landscape.png", "A diverse group of 14-15 year old students in an environmental science lab examining fabric samples under magnification while graphs of water consumption and carbon emissions from the textile industry display on screens behind them"),
        "modeling": ("G09L1-L08-modeling.png", "A diverse group of 14-15 year old students at laptops building supply chain models, screens showing flow diagrams of the fashion production cycle with environmental impact data at each stage, collaborative atmosphere"),
        "discussion": ("G09L1-L08-discussion.png", "A teacher leading an animated discussion with diverse 14-15 year old students about fast fashion environmental impact, infographic comparing water usage per garment displayed on a smartboard, students examining clothing labels"),
        "stem": ("G09L1-L08-stem.png", "Diverse 14-15 year old students designing sustainable fashion prototypes using recycled fabric samples and natural dye materials, sketching designs on paper while referencing environmental impact data on tablets")
    },
    "pre_assessment": [
        "How many new clothing items do you think you buy in a typical month? Where do your old clothes end up?",
        "What do you think happens to clothes after you throw them in the donation bin?",
        "Why is fast fashion so cheap — what corners might companies be cutting to sell a T-shirt for $5?",
        "Do you think the clothing industry has a significant environmental impact? Why or why not?"
    ],
    "extend_components": [
        ("Microplastic Pollution", "Synthetic fabrics like polyester shed microscopic plastic fibers during washing — a single load of laundry releases up to 700,000 microplastic fibers into waterways, entering the food chain and accumulating in marine organisms and human tissue"),
        ("Labor Exploitation", "The social cost of fast fashion: garment workers in Bangladesh, Vietnam, and Cambodia earn as little as $2/day in unsafe conditions. The Rana Plaza collapse in 2013 killed 1,134 garment workers, exposing the human cost of cheap clothing."),
        ("Chemical Runoff", "Textile dyeing and finishing use over 8,000 synthetic chemicals, many of which are discharged untreated into rivers near factories. The fashion industry is the second-largest polluter of freshwater globally, after agriculture.")
    ],
    "reflections": [
        "How does your model reveal the hidden environmental cost behind a cheap price tag?",
        "Why does reducing consumer demand have a bigger environmental impact than improving recycling?",
        "What responsibility do consumers have versus manufacturers in reducing fashion's environmental footprint?",
        "How does social media's influence on fashion trends connect to the environmental cascade in your model?",
        "What would need to change about the economic system to make sustainable fashion the default?"
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze data on water usage, carbon emissions, and waste generation across the fashion supply chain to evaluate the environmental impact of consumer behavior and production practices."),
        ("Disciplinary Core Idea", "ESS3.C: Human Impacts on Earth Systems / ETS1.B: Developing Possible Solutions", "The fashion industry demonstrates how human industrial activity impacts multiple Earth systems — water, atmosphere, and land — simultaneously. Students evaluate technological and behavioral solutions to reduce these impacts."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from consumer purchasing decisions through industrial production to measurable environmental consequences, demonstrating how individual actions aggregate into global system-level effects.")
    ],
    "cast_items": [
        "Model the causal relationship between consumer demand, industrial production, and multi-system environmental impact",
        "Evaluate technological and behavioral solutions to reduce the fashion industry's environmental footprint",
        "Predict the long-term environmental consequences of current consumption trends using computational models"
    ],
    "cast_questions": [
        ("Analyze:", "A clothing company claims it has become 'carbon neutral' by offsetting its emissions. Using your model, explain why carbon offsets alone don't address the full environmental impact of fast fashion — what other components are still causing damage?"),
        ("Evaluate:", "Compare two solutions: (A) a new recycling technology that can process 50% of textile waste into new fabric, and (B) a cultural shift where consumers buy 50% fewer garments. Using evidence from your model, which solution would have a greater total environmental impact?")
    ],
    "background_intro": "The fashion industry has quietly become one of the most destructive industries on Earth. While we obsess over oil companies and car emissions, the clothes on your back account for 10% of global carbon emissions, consume 79 trillion liters of water annually, and generate 92 million tons of waste per year. And it's accelerating — clothing production has doubled since 2000.",
    "background_sections": [
        ("The Fast Fashion Business Model", "Fast fashion is built on speed, volume, and disposability. Traditional fashion had 2-4 seasons per year; Zara introduced 24 'micro-seasons.' Shein uploads 2,000-10,000 new styles DAILY. The model works by making clothes so cheap that consumers treat them as disposable — wearing garments an average of 7 times before discarding them. The average American buys 68 garments per year, up from 25 in 1960. Globally, 150 billion garments are produced annually for 8 billion people."),
        ("Water: The Hidden Cost", "Cotton is the most water-intensive crop used in fashion. Growing enough cotton for a single T-shirt requires 2,700 liters of water — equivalent to one person's drinking water for 2.5 years. Dyeing and finishing add more: textile dyeing is the second-largest polluter of clean water globally. The Aral Sea, once the world's fourth-largest lake, has virtually disappeared due in part to cotton irrigation for the textile industry. The fashion industry consumes 79 trillion liters of water annually."),
        ("Carbon Emissions: Fashion's Climate Impact", "The fashion industry produces approximately 1.2 billion tons of CO2 equivalent per year — 10% of global emissions. This exceeds international flights and maritime shipping combined. The carbon comes from every stage: petroleum-based synthetic fibers (polyester = plastic = oil), energy-intensive manufacturing, global shipping, and methane from decomposing textile waste in landfills. If the industry continues on its current trajectory, its emissions will increase by 50% by 2030."),
        ("Textile Waste: Mountains of Clothes", "Of the 150 billion garments produced annually, 87% end up in landfills or incinerators. Less than 1% of clothing is recycled into new clothing. Even donated clothes face grim fates — only 10-20% of donated items are sold domestically; the rest are exported to developing nations where they're often dumped in landfills, destroying local textile industries. In Ghana's Kantamanto market, 40% of imported secondhand clothes arrive in such poor condition they go directly to the dump.")
    ],
    "lever_L": "Students identify consumer demand, production rate, textile waste, water consumption, and carbon emissions as the key components of the fast fashion environmental impact system.",
    "lever_E": "Students determine that consumer demand drives production rate, which simultaneously increases textile waste, water consumption, and carbon emissions — a one-directional cascade with demand as the primary driver.",
    "lever_V": "Students build a computational model showing how purchasing decisions cascade through the supply chain to create measurable environmental damage across multiple Earth systems.",
    "lever_Ev": "Students run business-as-usual, buy-less, and circular fashion scenarios to compare the environmental impact of demand reduction versus technological solutions.",
    "lever_R": "Students add microplastic pollution, labor exploitation, or chemical runoff to model more complete environmental and social impacts of the fashion industry.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with split image: glamorous store vs. textile landfill", "say": "Look at your outfit right now. How much water did it take to make? How much CO2? Where will it end up when you're done with it? The answers might shock you.", "do": "Have students look at their clothing labels. Ask who knows where their clothes were made. Show map of global garment production.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today we're following your T-shirt from cotton field to landfill — and measuring the environmental destruction at every step.", "do": "Have students read objectives. Pre-teach 'water footprint' and 'carbon footprint.' Share the 2,700 liters per T-shirt fact.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does a $5 T-shirt cost the planet so much?", "say": "You paid five dollars. But the planet paid 2,700 liters of water, 7 kilograms of CO2, and a spot in a landfill for the next 200 years. That's the real price tag.", "do": "Show the true cost infographic. Quick-write: Why do you think the environmental cost isn't included in the price?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model the system that turns your shopping habit into an environmental disaster — and then figure out how to fix it.", "do": "Preview LEVER steps. Emphasize that this is a SYSTEM — changing one thing changes everything.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for fast fashion model", "say": "What's the one thing that drives this entire system? And what are the environmental consequences?", "do": "Guide sorting: consumer demand is external (it's the input WE control). Production rate, waste, water, and carbon are internal system responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Supply chain relationship arrows", "say": "When you click 'add to cart,' what happens next? Trace the impact from your phone to the cotton field to the landfill.", "do": "Help students map the complete supply chain. Identify how demand drives production, which drives ALL environmental outputs.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Environmental impact graphs for each scenario", "say": "Let's test three futures: keep shopping like we do, buy half as much, or recycle everything. Which one actually saves the planet?", "do": "Students predict outcomes. Key discovery: reducing demand beats recycling because most damage happens during production, not disposal.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings: demand is the driver, production is the damage", "say": "The most sustainable garment is the one you already own. Recycling helps — but buying less helps MORE.", "do": "Lead discussion on why demand reduction is more effective than recycling. Connect to social media's role in driving trend cycles.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sustainable fashion design challenge", "say": "A billion-dollar industry wants to go green without losing teenage customers. Design their solution.", "do": "Groups design sustainable fashion solutions. Must be appealing to teen market AND reduce environmental impact. Present business pitches.", "time": "12 min"}
    ],
    "sort_reasoning": "Consumer Demand is the external component because it represents the input that drives the entire system — purchasing decisions are made by consumers and can be consciously changed. Production Rate, Textile Waste, Water Consumption, and Carbon Emissions are internal because they are system responses that increase or decrease as a direct consequence of changes in consumer demand.",
    "relationships": [
        ("Consumer Demand to Production Rate", "POSITIVE (+)", "Higher consumer demand signals manufacturers to increase production speed and volume. Fast fashion brands use real-time sales data and social media trends to ramp up production of popular styles within days."),
        ("Production Rate to Textile Waste", "POSITIVE (+)", "Higher production rates generate more manufacturing waste (fabric scraps, defective items, overstock) and more consumer waste as garments are treated as disposable. Approximately 12% of fabric is wasted during cutting alone."),
        ("Production Rate to Water Consumption", "POSITIVE (+)", "More garments produced means more cotton grown (irrigated), more fabric dyed (water-intensive), and more textiles washed and finished. Water consumption scales almost linearly with production volume."),
        ("Production Rate to Carbon Emissions", "POSITIVE (+)", "Increased production requires more energy for manufacturing, more petroleum for synthetic fibers, more fuel for global shipping, and generates more landfill methane from unsold and discarded garments.")
    ],
    "sim_answers": [
        ("Business as Usual Scenario", "When Consumer Demand stays at current high levels, Production Rate continues at 150 billion garments annually. Textile Waste remains at 92 million tons/year, Water Consumption at 79 trillion liters/year, and Carbon Emissions at 1.2 billion tons CO2/year. The model shows all environmental indicators continuing to climb as fast fashion accelerates, with projections suggesting a 50% increase in emissions by 2030."),
        ("Buy Less Movement Scenario", "When Consumer Demand drops by 50%, Production Rate halves accordingly. Textile Waste, Water Consumption, and Carbon Emissions all decrease roughly proportionally — the model shows this demand reduction cuts environmental impact more effectively than any recycling technology because it prevents damage at the SOURCE (production stage) rather than trying to clean up at the END (disposal stage).")
    ],
    "reflection_exemplars": [
        ("Why does reducing demand beat recycling?", "The model reveals that the vast majority of environmental damage — water consumption, carbon emissions, chemical pollution — occurs during PRODUCTION, not disposal. Recycling only addresses the waste component, and current technology can only recycle less than 1% of clothing into new clothing anyway. When you reduce demand, you prevent production from happening in the first place, which means the water is never consumed, the carbon is never emitted, and the waste is never generated. It's the difference between cleaning up a mess and never making the mess."),
        ("What responsibility do consumers have?", "The model shows that consumer demand is the external driver of the entire system — it's literally the input that controls all outputs. This means individual purchasing decisions aggregate into massive environmental consequences. However, the system is DESIGNED to stimulate demand through aggressive marketing, artificially low prices, and social media trend cycles. Responsibility is shared: consumers can choose to buy less, but companies design the addictive cycle and governments fail to regulate the externalities. Systemic change requires action at all three levels.")
    ],
    "stem_intro": "Frame this as a design-for-sustainability challenge. Students are consultants hired by a major retailer that wants to reduce its environmental impact while remaining profitable and appealing to teenage consumers. The solution must address at least two of the three environmental outputs (waste, water, carbon).",
    "stem_concepts": [
        ("Circular Economy", "An economic model where products are designed to be reused, repaired, and recycled rather than discarded. In fashion, this means designing garments for disassembly, using mono-materials that can be recycled, and creating take-back programs where old clothes become raw material for new ones."),
        ("Life Cycle Assessment (LCA)", "A scientific method for measuring the total environmental impact of a product from raw material extraction ('cradle') through manufacturing, use, and disposal ('grave'). LCA reveals that a polyester shirt's biggest impact is manufacturing, while cotton's is water-intensive agriculture."),
        ("Sustainable Materials Innovation", "New technologies are creating fabrics from unexpected sources: mushroom leather (Mylo), orange peel fiber (Orange Fiber), recycled ocean plastic (Parley), and lab-grown spider silk (Bolt Threads). These materials can match conventional performance with a fraction of the environmental footprint.")
    ],
    "stem_eval": [
        ("Expert (4)", "Solution targets the highest-impact stage of the supply chain, addresses multiple environmental outputs, includes a viable business model, appeals to teen consumers, and uses evidence from the computational model"),
        ("Proficient (3)", "Solution addresses a real environmental impact with a reasonable approach and considers both sustainability and consumer appeal"),
        ("Developing (2)", "Solution addresses one environmental issue but lacks business viability, consumer appeal, or connection to model data"),
        ("Beginning (1)", "Solution is incomplete or doesn't realistically address fashion's environmental impact")
    ],
    "support": [
        "Provide a fashion supply chain diagram showing environmental impact at each stage for quick reference",
        "Use real product comparisons: $5 Shein shirt vs. $35 sustainably-made shirt — what accounts for the price difference?",
        "Sentence frames: 'When consumer demand increases, production rate __ which causes water consumption to __ and carbon emissions to __ because __'"
    ],
    "extensions": [
        "Research and calculate the total environmental footprint of your wardrobe — how much water, carbon, and waste does everything you own represent?",
        "Investigate how the secondhand clothing market (Depop, ThredUp, Goodwill) is disrupting fast fashion and analyze whether it truly reduces environmental impact or just delays disposal",
        "Compare the environmental impact per wearing of a $5 Shein shirt worn 5 times versus a $50 quality shirt worn 100 times — which is actually cheaper per use?"
    ],
    "cross_curr": [
        ("Math", "Calculate the per-garment environmental cost: If the fashion industry uses 79 trillion liters of water for 150 billion garments, what is the average water footprint per item? Compare to per-capita water access in water-scarce nations."),
        ("ELA", "Write an investigative journalism piece exposing the hidden environmental and social costs of a specific fast fashion brand, citing data from your model and external research"),
        ("Social Studies", "Research the global justice dimension: How does textile waste exported from wealthy nations to Ghana, Chile, and Kenya affect local economies, environments, and communities?")
    ],
    "misconceptions": [
        ("Donating old clothes is sustainable", "Only 10-20% of donated clothing is sold domestically. The rest is exported to developing nations, where up to 40% ends up in landfills — the same fate it would have had at home, just in a poorer country. Donation makes us FEEL sustainable without actually solving the waste problem. The most impactful action is buying less in the first place.", "Show the data: Follow a donated shirt's journey from the Goodwill bin to a landfill in Ghana. Ask: Is this what you imagined when you donated?"),
        ("Recycled clothing solves the waste problem", "Less than 1% of clothing is recycled into new clothing. Most 'recycled' textiles are downcycled into insulation, rags, or stuffing — and even that represents a tiny fraction of total waste. The technology to turn an old T-shirt into a new T-shirt at scale doesn't exist yet. Recycling is important but cannot offset the volume of waste created by current production levels.", "Math check: If we recycle 1% of 92 million tons of textile waste, that's 920,000 tons recycled — and 91 million tons still going to landfills. Can recycling alone solve this?"),
        ("Sustainable fashion is too expensive for normal people", "Fast fashion is artificially cheap because environmental costs are externalized — someone else pays for the water, carbon, and waste. A $5 shirt isn't actually cheap; the true cost is just hidden. Moreover, cost-per-wear analysis shows that a $50 quality garment worn 100 times ($0.50/wear) is cheaper than a $5 garment worn 5 times ($1.00/wear) before falling apart.", "Calculate: You buy twelve $5 shirts that each last 2 months, or two $30 shirts that each last a year. Same time period — which costs more? Which creates more waste?")
    ]
}

L09 = {
    "id": "G09L1-L09",
    "title": "Why Earthquakes Hit Some Cities Harder",
    "subtitle": "Modeling Seismic Energy, Ground Conditions, and Urban Vulnerability",
    "ngss": "HS-ESS2-1",
    "ngss_desc": "Develop a model to illustrate how Earth's internal and surface processes operate at different spatial and temporal scales to form continental and ocean-floor features.",
    "big_question": "Why do two cities the same distance from an earthquake experience completely different levels of destruction?",
    "objectives": [
        "Model how tectonic stress accumulates along fault lines and is released as seismic energy during an earthquake",
        "Explain how ground conditions amplify or dampen seismic waves, determining the severity of shaking at different locations",
        "Predict which urban areas are most vulnerable to earthquake damage based on geological and structural factors",
        "Analyze why building codes and soil conditions are as important as earthquake magnitude in determining destruction"
    ],
    "vocabulary": [
        ("Tectonic Stress", "The slow buildup of pressure along tectonic plate boundaries as plates push against, pull apart from, or slide past each other — this stress accumulates over decades to centuries before sudden release as an earthquake"),
        ("Seismic Waves", "Energy waves that radiate outward from an earthquake's focus through Earth's interior and along its surface — P-waves (compressional), S-waves (shear), and surface waves each cause different types of ground motion"),
        ("Ground Amplification", "The phenomenon where soft, loose sediments (like clay, sand, or landfill) amplify seismic waves far more than solid bedrock — causing dramatically worse shaking in some locations despite equal distance from the earthquake"),
        ("Liquefaction", "A process where water-saturated, loose soil temporarily behaves like a liquid during strong shaking, causing buildings to sink, tilt, or collapse as the ground loses its ability to support structures")
    ],
    "components": [
        ("Tectonic Stress", "The accumulated mechanical pressure along a fault zone caused by plate motion — measured in megapascals and building over years to centuries until it exceeds the fault's frictional strength", True),
        ("Fault Slip", "The sudden movement along a fault plane when accumulated tectonic stress exceeds friction — the rupture length and displacement determine the earthquake's magnitude", False),
        ("Seismic Wave Energy", "The total energy radiated as seismic waves during an earthquake, traveling through rock and soil at speeds of 3-8 km/s — the energy that shakes buildings and reshapes landscapes", False),
        ("Building Vulnerability", "The susceptibility of structures to seismic damage based on construction materials, design, age, height, and whether the building was engineered to withstand earthquake forces", False),
        ("Ground Amplification", "The degree to which local soil and geological conditions amplify or dampen incoming seismic waves — soft sediments can amplify shaking 2-10 times compared to solid bedrock", False)
    ],
    "think_about_it": "If Tectonic Stress has been building for 100 years and suddenly releases, how do Fault Slip, Seismic Wave Energy, Ground Amplification, and Building Vulnerability interact to determine whether a city survives or is devastated?",
    "scenarios": [
        ("Moderate Quake on Bedrock", "Set Tectonic Stress to moderate with buildings on solid bedrock — observe how low Ground Amplification protects the city"),
        ("Major Quake on Soft Soil", "Set Tectonic Stress to maximum with buildings on soft sediment — observe the amplification cascade that multiplies destruction"),
        ("Same Quake, Two Cities", "Same earthquake, but compare one city on bedrock with modern building codes versus another city on soft soil with older construction — observe why outcomes are so different")
    ],
    "sim_scenarios": [
        ("Bedrock City", "Moderate earthquake, city built on solid bedrock with modern codes", "What do you predict will happen to Building Vulnerability when seismic waves travel through solid bedrock?"),
        ("Soft Soil City", "Major earthquake, city built on soft sediment with older construction", "What do you predict happens when strong seismic waves encounter loose, water-saturated soil beneath a city?"),
        ("Two Cities Comparison", "Same earthquake affecting two cities with different ground and building conditions", "Why do you predict that two cities equidistant from the same earthquake will experience dramatically different levels of destruction?")
    ],
    "discoveries": [
        "Ground amplification is often more important than distance from the earthquake — soft soil can amplify shaking 2-10 times, meaning a city on clay can experience worse shaking than a closer city on bedrock",
        "Tectonic stress builds silently over decades to centuries, then releases in seconds — the longer the buildup, the more powerful the potential earthquake",
        "Building vulnerability varies enormously with construction quality — modern earthquake-resistant buildings can survive shaking that destroys unreinforced structures just blocks away",
        "The deadliest earthquakes aren't necessarily the strongest — a moderate earthquake in a vulnerable city can kill more people than a powerful earthquake in a prepared one"
    ],
    "answer": "Two cities the same distance from an earthquake experience vastly different destruction because of two critical local factors: ground conditions and building quality. When seismic waves travel through solid bedrock, they pass through efficiently with relatively little amplification. But when those same waves enter soft, loose sediments — especially water-saturated clay or artificial fill — the ground amplifies the shaking 2 to 10 times. Meanwhile, buildings engineered with earthquake-resistant design flex and absorb energy, while older unreinforced structures crack and collapse. The earthquake's magnitude is just the starting point — what happens to the seismic energy at each specific location determines who lives and who dies.",
    "stem_title": "Design an Earthquake Risk Assessment System",
    "stem_mission": "Design a risk assessment and early warning system that identifies the most vulnerable areas in a city and provides actionable information to emergency responders and residents before, during, and after an earthquake.",
    "stem_scenario": "Your city sits near an active fault zone that hasn't produced a major earthquake in 120 years — meaning enormous tectonic stress has accumulated. The city council has hired your team to create a seismic risk assessment that maps vulnerability across different neighborhoods based on soil type, building age, and proximity to the fault. Your system must identify which areas face the highest risk and recommend prioritized actions.",
    "stem_questions": [
        "How would you map the different soil and ground types across the city to identify amplification zones?",
        "What building characteristics would you survey to assess structural vulnerability?",
        "How would you communicate risk levels to residents without causing unnecessary panic?"
    ],
    "stem_design_qs": [
        "What data sources would you use to map soil conditions, fault proximity, and building types across the city?",
        "How would you create a risk scoring system that combines ground amplification potential with building vulnerability?",
        "What would your early warning system communicate, and how many seconds of warning would different zones receive?",
        "How would you prioritize which buildings or neighborhoods need retrofitting first?"
    ],
    "career": "Seismologists study earthquakes and seismic waves using networks of sensors around the world, earning $60,000–$130,000/year. Structural Engineers design buildings to withstand earthquake forces using specialized materials and damping systems, earning $70,000–$140,000/year. Emergency Management Directors coordinate disaster preparedness and response, earning $75,000–$150,000/year.",
    "images": {
        "cover": ("G09L1-L09-cover.png", "A photorealistic, cinematic aerial view of a city after an earthquake showing dramatic contrast — one neighborhood of modern buildings stands intact while an adjacent neighborhood of older structures is heavily damaged, cracked roads and emergency vehicles visible, dust in the air, dramatic lighting"),
        "landscape": ("G09L1-L09-landscape.png", "A diverse group of 14-15 year old students in a geology lab examining rock and soil samples in clear containers — solid granite next to loose sand and clay — while seismograph equipment runs on a nearby table, focused expressions, natural lighting"),
        "modeling": ("G09L1-L09-modeling.png", "A diverse group of 14-15 year old students at laptops building seismic wave propagation models, screens showing wave diagrams passing through different soil layers with amplification zones highlighted, modern science classroom"),
        "discussion": ("G09L1-L09-discussion.png", "A teacher leading a discussion with diverse 14-15 year old students using a cross-section diagram of city geology showing bedrock vs soft soil zones on a smartboard, students examining a seismic hazard map of their region"),
        "stem": ("G09L1-L09-stem.png", "Diverse 14-15 year old students building shake table models with different building designs and soil conditions, testing structural designs against simulated seismic waves, engineering equipment visible on lab tables")
    },
    "pre_assessment": [
        "Why do you think some buildings collapse in an earthquake while others right next to them are fine?",
        "What causes earthquakes, and why do they happen in some places but not others?",
        "If you were designing a building in an earthquake zone, what features would you include to keep it standing?",
        "Do you think the ground beneath a building matters during an earthquake? Why or why not?"
    ],
    "extend_components": [
        ("Aftershock Frequency", "The number and intensity of smaller earthquakes that follow a major event, which can collapse already-weakened structures and hamper rescue efforts for days to weeks after the mainshock"),
        ("Tsunami Potential", "The risk of ocean displacement when submarine earthquakes cause sudden vertical seafloor movement, generating tsunami waves that can travel across entire ocean basins at jet speed"),
        ("Infrastructure Interdependency", "The cascading failure of interconnected systems — a ruptured gas line causes fires, a broken water main prevents firefighting, downed power lines block roads — multiplying damage beyond direct seismic effects")
    ],
    "reflections": [
        "Why is ground amplification often a bigger factor in earthquake destruction than the earthquake's magnitude?",
        "What does your model reveal about why wealth and poverty determine earthquake survival as much as geology?",
        "How does the timescale difference between stress buildup (centuries) and stress release (seconds) affect earthquake preparedness?",
        "Why might a city that hasn't experienced an earthquake in a long time actually be at HIGHER risk?",
        "What are the limitations of modeling earthquake damage with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model to illustrate how tectonic processes at depth interact with surface conditions to produce variable earthquake impacts across spatial scales."),
        ("Disciplinary Core Idea", "ESS2.B: Plate Tectonics and Large-Scale System Interactions", "Earth's internal processes (tectonic stress, fault mechanics) operate at temporal scales of centuries and spatial scales of thousands of kilometers, while surface effects (ground amplification, building response) operate at human timescales and local spatial scales."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students analyze how earthquake phenomena span dramatically different scales: tectonic stress over centuries, fault slip in seconds, seismic waves over minutes, and ground amplification over meters — all interacting to determine outcomes.")
    ],
    "cast_items": [
        "Model how tectonic stress accumulation and release produces seismic energy that interacts with local ground conditions",
        "Analyze how ground amplification and building quality create dramatically different outcomes from the same seismic event",
        "Predict which urban areas face the greatest earthquake risk based on geological and structural vulnerability factors"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two neighborhoods are exactly 10 km from an earthquake epicenter. Neighborhood A is built on granite bedrock; Neighborhood B is built on water-saturated clay fill. According to your model, which will experience more intense shaking, and why?"),
        ("Constructed Response:", "The 2010 Haiti earthquake (magnitude 7.0) killed 230,000 people, while the 2010 Chile earthquake (magnitude 8.8 — nearly 500 times more energy) killed 525 people. Using your model, explain how two earthquakes of dramatically different power could produce such opposite death tolls.")
    ],
    "background_intro": "Earthquakes are among the most dramatic reminders that Earth's surface is not the stable, unchanging ground it appears to be. Beneath our feet, tectonic plates grind against each other at rates of centimeters per year, building enormous stress that is released in catastrophic bursts lasting seconds to minutes. But the earthquake itself is only half the story — what happens to seismic energy when it reaches the surface determines whether a city survives or collapses.",
    "background_sections": [
        ("Tectonic Stress and Fault Mechanics", "Earth's tectonic plates move at 1-15 cm per year, driven by mantle convection. Where plates meet, friction locks them together, and stress accumulates along the boundary. When stress exceeds the fault's frictional strength, the rocks suddenly snap past each other — releasing decades to centuries of stored energy in seconds. The San Andreas Fault, for example, has accumulated about 5 meters of 'slip deficit' since its last major rupture in 1906 — enough for a magnitude 7.8+ earthquake."),
        ("Seismic Wave Propagation", "An earthquake radiates three types of waves: P-waves (compressional, fastest, arrive first), S-waves (shear, slower, more damaging), and surface waves (slowest, most destructive). These waves travel through Earth's interior and along its surface at speeds of 3-8 km/s. As they encounter different rock and soil types, their behavior changes dramatically — they can be reflected, refracted, amplified, or dampened depending on the medium's density and elasticity."),
        ("Ground Amplification: The Site Effect", "This is the single most important factor in determining local earthquake damage. When seismic waves travel from dense bedrock into loose, soft sediments, conservation of energy forces the waves to slow down and increase in amplitude — like ocean waves growing taller as they approach the shore. Soft clay can amplify shaking 2-10 times compared to bedrock. The 1985 Mexico City earthquake killed 10,000 people largely because the city is built on an ancient lakebed that amplified seismic waves like a bowl of gelatin, even though the earthquake's epicenter was 350 km away."),
        ("Building Vulnerability and Engineering", "Modern earthquake engineering uses base isolation (buildings float on rubber bearings), moment-resisting frames (flexible steel that absorbs energy), shear walls (concrete cores that resist lateral forces), and tuned mass dampers (counterweights that reduce sway). The difference is stark: in the 2010 Chile earthquake, modern buildings designed to seismic codes suffered minimal damage while unreinforced masonry structures nearby were destroyed. Building codes save lives — but only if they exist, are enforced, and buildings are actually constructed to meet them.")
    ],
    "lever_L": "Students identify tectonic stress, fault slip, seismic wave energy, building vulnerability, and ground amplification as the key components that determine earthquake impact.",
    "lever_E": "Students determine that tectonic stress drives fault slip, which generates seismic wave energy, which is then modified by ground amplification and interacts with building vulnerability to determine destruction levels.",
    "lever_V": "Students build a computational model showing how geological processes at depth cascade through surface conditions to produce variable earthquake impacts across a city.",
    "lever_Ev": "Students run bedrock, soft soil, and two-city comparison scenarios to test their model and discover that local conditions often matter more than earthquake magnitude.",
    "lever_R": "Students add aftershock frequency, tsunami potential, or infrastructure interdependency to model more realistic post-earthquake cascading effects.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with aerial photo of contrasting earthquake damage", "say": "In 2010, Haiti had a magnitude 7.0 earthquake that killed 230,000 people. Two months later, Chile had a magnitude 8.8 — that's 500 times more energy — and 525 people died. How is that possible?", "do": "Show the comparison on screen. Let the numbers sink in. Ask students what could possibly explain this.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're learning why earthquakes are only half the story — the ground you're standing on and the building you're in determine whether you live or die.", "do": "Have students read objectives. Pre-teach 'ground amplification' and 'liquefaction.' Use the gelatin bowl analogy.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Two cities, same earthquake, different outcomes", "say": "Same earthquake, same distance. One city stands. One city falls. The earthquake didn't choose — the geology and engineering did.", "do": "Show a map with two cities equidistant from a fault. Ask students to predict which would fare worse and why.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a model that starts deep underground where stress is building and follows the energy all the way up to the buildings above.", "do": "Preview LEVER steps. Emphasize that this model spans scales from tectonic plates to individual buildings.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for earthquake model", "say": "Only one component is truly 'external' — the one we can't control. What is it, and why can't we control it?", "do": "Guide sorting: tectonic stress is external (geological force we can't influence). All other components are internal system responses. Discuss implications.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows from tectonic stress to building damage", "say": "Stress builds for 100 years. It releases in 10 seconds. Then what happens to the energy between the fault and your school?", "do": "Help students trace the energy path: stress → slip → waves → amplification → damage. Identify where intervention is possible.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Comparison graphs for bedrock vs. soft soil scenarios", "say": "Let's put two cities through the same earthquake and see which one survives. What's the difference?", "do": "Students predict outcomes. Run all three scenarios. Key discovery: ground amplification can matter more than earthquake magnitude.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings: amplification, vulnerability, preparedness", "say": "The deadliest earthquakes aren't the strongest. They're the ones that hit unprepared cities on bad soil. That's both terrifying and hopeful — because it means we CAN do something about it.", "do": "Lead discussion on Haiti vs. Chile. Connect preparedness to equity: who builds on the worst soil? Usually the poorest communities.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Earthquake risk assessment design challenge", "say": "Your city hasn't had a big earthquake in 120 years. That's not comforting — that means MORE stress has built up. Design a system that identifies who's most at risk.", "do": "Groups create risk assessment maps and early warning systems. Must consider soil type, building quality, and community communication.", "time": "12 min"}
    ],
    "sort_reasoning": "Tectonic Stress is the external component because it is a geological force driven by plate tectonics that humans cannot influence or control — it builds independently of anything happening at the surface. Fault Slip, Seismic Wave Energy, Ground Amplification, and Building Vulnerability are internal because they represent the system's response chain: stress triggers slip, which releases waves, which are modified by local ground conditions, which interact with building characteristics to determine outcomes.",
    "relationships": [
        ("Tectonic Stress to Fault Slip", "POSITIVE (+)", "Greater accumulated tectonic stress produces larger fault slip when the rocks finally break. More stored energy means a longer rupture, greater displacement, and a higher magnitude earthquake."),
        ("Fault Slip to Seismic Wave Energy", "POSITIVE (+)", "Larger fault slip releases more energy as seismic waves. A 1-meter slip produces moderate shaking; a 10-meter slip (like the 2011 Japan earthquake) releases catastrophic energy across vast distances."),
        ("Seismic Wave Energy to Ground Amplification", "POSITIVE (+)", "Stronger seismic waves traveling through soft sediments produce greater amplification effects. The interaction is multiplicative — double the wave energy in soil that amplifies 5x results in 10x the shaking compared to bedrock."),
        ("Ground Amplification to Building Vulnerability", "POSITIVE (+)", "Greater ground amplification increases the seismic forces that buildings must withstand. Buildings designed for moderate shaking may survive on bedrock but fail catastrophically when ground amplification doubles or triples the effective shaking intensity.")
    ],
    "sim_answers": [
        ("Bedrock City Scenario", "When the earthquake occurs beneath a city built on solid bedrock with modern seismic building codes, Seismic Wave Energy travels through dense rock with minimal Ground Amplification (factor of ~1x). Building Vulnerability is low because structures are designed to flex and absorb seismic forces. Result: moderate shaking, minimal structural damage, few casualties. The model shows that the combination of good geology and good engineering dramatically reduces earthquake impact."),
        ("Soft Soil City Scenario", "When the same earthquake reaches a city built on soft, water-saturated sediment with older, unreinforced construction, Ground Amplification magnifies shaking by 3-10x. Building Vulnerability is high because structures were not designed for these forces. Result: severe shaking, widespread structural failure, potential liquefaction causing buildings to sink and tilt. The model reveals that local conditions can transform a survivable earthquake into a catastrophe.")
    ],
    "reflection_exemplars": [
        ("Why does ground type matter more than magnitude?", "The model demonstrates that a magnitude 6.0 earthquake on soft clay can produce MORE actual shaking at the surface than a magnitude 7.0 earthquake on bedrock, because ground amplification multiplies the seismic energy by factors of 2-10x. Magnitude measures energy released at the SOURCE, but what matters for destruction is the shaking at the SURFACE. The ground acts as a filter that can either dampen or dramatically amplify the incoming waves. This is why seismic hazard maps focus on soil conditions, not just fault proximity."),
        ("Why does earthquake risk relate to poverty and equity?", "Historically, the cheapest land in earthquake-prone cities is on soft soil — former lakebeds, landfill, river deltas — because it's flat, easy to build on, and was considered less desirable. This means lower-income communities disproportionately occupy the most geologically vulnerable zones AND live in older, less earthquake-resistant buildings. The 2010 Haiti earthquake killed 230,000 people largely because Port-au-Prince was built on soft sediment with virtually no building codes, while wealthy nations facing similar seismic threats invest billions in retrofitting and engineering. Earthquake risk is a social justice issue as much as a geological one.")
    ],
    "stem_intro": "Present the challenge: Your city sits on an active fault zone that hasn't ruptured in 120 years — meaning enormous stress has accumulated. The city council needs a seismic risk assessment system that identifies the most vulnerable neighborhoods and recommends a prioritized action plan. Your team must combine geological, structural, and socioeconomic data to create an actionable risk map.",
    "stem_concepts": [
        ("Seismic Microzonation", "The process of dividing a city into zones based on expected ground response to earthquakes. Each zone is assigned an amplification factor based on soil type, depth to bedrock, and groundwater level. This determines building code requirements and informs land use planning."),
        ("Earthquake Early Warning (EEW)", "Systems like ShakeAlert detect the initial P-waves from an earthquake and broadcast warnings before the more destructive S-waves and surface waves arrive. This provides seconds to tens of seconds of warning — enough to stop trains, open fire station doors, and trigger automated shutdown of gas lines and industrial processes."),
        ("Seismic Retrofitting", "Strengthening existing buildings to resist earthquake forces through techniques like adding steel bracing, base isolation, shear walls, or fiber-reinforced polymer wrapping. Retrofitting is expensive but far cheaper than rebuilding after destruction — and saves lives.")
    ],
    "stem_eval": [
        ("Expert (4)", "Risk assessment integrates soil data, building inventory, and socioeconomic vulnerability to create a detailed neighborhood-level risk map with prioritized retrofitting recommendations and early warning system design justified by model evidence"),
        ("Proficient (3)", "Risk assessment identifies high-risk zones based on geological and structural factors with reasonable recommendations for risk reduction"),
        ("Developing (2)", "Risk assessment addresses some vulnerability factors but lacks integration of geological and structural data or actionable recommendations"),
        ("Beginning (1)", "Risk assessment is incomplete or doesn't connect geological and structural vulnerability to earthquake outcomes")
    ],
    "support": [
        "Provide a simplified cross-section diagram showing how seismic waves behave differently in bedrock versus soft soil",
        "Use a shake table demonstration or video: same structure on solid versus loose foundation shows amplification dramatically",
        "Sentence frames: 'When tectonic stress is released as fault slip, seismic wave energy __ and when those waves reach soft soil, ground amplification __ causing building vulnerability to __'"
    ],
    "extensions": [
        "Research the seismic risk assessment for your own city or region — what fault lines are nearby, what type of soil is your school built on, and what building codes are in effect?",
        "Investigate the 2011 Tohoku, Japan earthquake and tsunami: How did the seismic design of Japanese buildings perform, and why did the tsunami cause more damage than the shaking?",
        "Design a shake table experiment that demonstrates ground amplification using gelatin (soft soil) versus a rigid platform (bedrock) with identical building models"
    ],
    "cross_curr": [
        ("Math", "Calculate the energy difference between earthquake magnitudes using the logarithmic Richter scale: a magnitude 7.0 releases 31.6x more energy than a 6.0, and 1,000x more than a 5.0. Graph the exponential relationship."),
        ("ELA", "Write a disaster preparedness communication plan for a city on a seismic fault: How do you inform residents about risk without causing panic, distrust, or apathy?"),
        ("Social Studies", "Research how earthquake preparedness correlates with national wealth: Compare building codes, emergency response, and death tolls between earthquakes in wealthy versus low-income nations. What does this reveal about structural inequality?")
    ],
    "misconceptions": [
        ("Earthquakes kill people", "Earthquakes don't kill people — buildings kill people. The ground shaking itself is rarely directly lethal. Casualties result from collapsing structures, falling debris, fires from ruptured gas lines, and tsunamis. In well-engineered cities, even powerful earthquakes cause few deaths. The 2010 Chile magnitude 8.8 earthquake killed 525 people because of strict building codes; the 2010 Haiti magnitude 7.0 killed 230,000 because of absent building codes.", "Compare: Japan experiences thousands of earthquakes per year with very few casualties. What's different about their buildings?"),
        ("All earthquakes produce the same type of shaking", "Different earthquakes produce different frequency content depending on fault mechanics and depth. Smaller, shallow earthquakes produce high-frequency shaking that affects short, stiff buildings. Larger, deeper earthquakes produce low-frequency waves that cause tall buildings to sway dangerously. Ground conditions further modify the frequency content — soft soil amplifies low-frequency waves that are particularly damaging to mid-rise buildings.", "Analogy: Shaking a bowl of gelatin slowly makes it sway gently; shaking it quickly makes it jiggle on the surface. Different frequencies affect different structures."),
        ("We can predict when earthquakes will happen", "Despite decades of research, reliable short-term earthquake prediction remains impossible. We can identify WHERE earthquakes are likely (plate boundaries) and roughly HOW STRONG they might be (based on fault length and accumulated stress), but we cannot predict WHEN the fault will slip. The best approach is not prediction but preparation — building codes, early warning systems, and emergency plans that assume an earthquake can happen any time.", "Analogy: We know a dam is under stress, but we can't predict the exact second it will break. So we build the town downstream to survive the flood.")
    ]
}

L10 = {
    "id": "G09L1-L10",
    "title": "The Wildfire Feedback Loop",
    "subtitle": "Modeling How Fire, Climate, and Ecosystems Create a Self-Reinforcing Cycle",
    "ngss": "HS-ESS3-3, HS-LS2-6",
    "ngss_desc": "Create a computational simulation of a natural or designed system to test hypotheses about the functioning of natural systems. Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions.",
    "big_question": "Why are wildfires getting bigger, hotter, and harder to stop — and is the cycle feeding itself?",
    "objectives": [
        "Model the positive feedback loop where wildfire destroys vegetation, reduces soil moisture, and creates conditions for more intense future fires",
        "Explain how fuel load, fire intensity, soil moisture, wind speed, and vegetation recovery interact in wildfire dynamics",
        "Predict how climate change is accelerating the wildfire feedback cycle by lengthening fire seasons and increasing fuel dryness",
        "Analyze why fire suppression policies have paradoxically made wildfires more dangerous"
    ],
    "vocabulary": [
        ("Fuel Load", "The total amount of combustible material — dead leaves, fallen branches, dry grass, bark, and even living vegetation — available to burn in a given area, measured in tons per hectare"),
        ("Fire Intensity", "The rate of heat energy released by a wildfire, measured in kilowatts per meter of fire front — low-intensity fires clear underbrush, while high-intensity crown fires destroy entire ecosystems"),
        ("Soil Moisture", "The amount of water held in the soil, which affects both vegetation health and fire behavior — dry soil means stressed vegetation with higher fuel ignitability and faster fire spread"),
        ("Positive Feedback Loop", "A self-reinforcing cycle where the output of a system amplifies the input — in wildfire: fire reduces vegetation → less vegetation means drier soil → drier soil makes more fuel flammable → next fire is more intense")
    ],
    "components": [
        ("Wind Speed", "The velocity and consistency of air movement that delivers oxygen to the fire front, drives flame spread, carries embers to start spot fires ahead of the main front, and influences fire direction", True),
        ("Fuel Load", "The quantity and condition of combustible vegetation and debris in the fire's path — determined by decades of growth, drought conditions, and whether previous fires or management have reduced it", False),
        ("Fire Intensity", "The energy output and destructive power of the wildfire, determined by fuel availability, moisture content, wind, and topography — ranges from low-intensity surface fires to extreme crown fires that create their own weather", False),
        ("Soil Moisture", "The water content of the ground, which regulates vegetation health, fuel dryness, and the fire's ability to penetrate into the organic soil layer — low soil moisture creates conditions for extreme fire behavior", False),
        ("Vegetation Recovery", "The rate and extent to which plants regrow after a fire, restoring ground cover, stabilizing soil, and rebuilding the ecosystem — depends on fire intensity, soil condition, seed availability, and post-fire rainfall", False)
    ],
    "think_about_it": "After a major wildfire burns through a forest, how does the destruction affect Soil Moisture, Fuel Load for the next fire, and Vegetation Recovery? Where does the feedback loop either stabilize or spiral out of control?",
    "scenarios": [
        ("Low-Intensity Fire, Healthy Forest", "Set Wind Speed to low with moderate Fuel Load — observe how a mild fire clears underbrush without destroying the ecosystem"),
        ("Extreme Fire, Drought Conditions", "Set Wind Speed to high with maximum Fuel Load and low Soil Moisture — observe the catastrophic fire and its impact on future fire conditions"),
        ("Post-Fire Recovery", "After a major fire, track Vegetation Recovery and Soil Moisture over time — observe whether the ecosystem recovers or enters the destructive feedback loop")
    ],
    "sim_scenarios": [
        ("Healthy Fire Cycle", "Low wind, moderate fuel, adequate soil moisture", "What do you predict will happen when a low-intensity fire moves through a forest with moderate fuel load and healthy soil moisture?"),
        ("Catastrophic Fire", "High wind, maximum fuel, drought conditions", "What do you predict happens to fire intensity, soil moisture, and vegetation recovery when extreme conditions align?"),
        ("Feedback Loop Test", "Track system behavior over multiple fire cycles", "After a catastrophic fire, do you predict the ecosystem will recover to its previous state, or will conditions worsen for the next fire?")
    ],
    "discoveries": [
        "Low-intensity fires are natural and beneficial — they clear fuel buildup, recycle nutrients, and promote biodiversity, keeping forests healthy and reducing the risk of catastrophic fires",
        "A positive feedback loop exists: intense fire destroys vegetation → less vegetation means less water retention → drier soil creates drier fuel → next fire burns hotter → even more vegetation destroyed",
        "Decades of fire suppression have created unnaturally high fuel loads in many forests, turning what should be low-intensity surface fires into catastrophic crown fires that destroy entire ecosystems",
        "Climate change is accelerating the feedback loop by raising temperatures, extending drought seasons, and reducing soil moisture — creating fire conditions that exceed the ecosystem's ability to recover"
    ],
    "answer": "Wildfires are getting bigger, hotter, and harder to stop because of a self-reinforcing positive feedback loop accelerated by climate change and a century of fire suppression. When a catastrophic fire burns through a forest, it destroys the vegetation that holds soil moisture. Without vegetation, the soil dries out faster, which stresses any regrowing plants and makes dead material more flammable. The next fire encounters drier, more abundant fuel and burns even hotter. Meanwhile, decades of fire suppression have allowed fuel to accumulate to unnaturally high levels, and climate change has made droughts longer and more intense. The system is feeding itself — each fire creates the conditions for a worse one.",
    "stem_title": "Design a Community Wildfire Resilience Plan",
    "stem_mission": "Design a comprehensive wildfire management plan for a community in the wildland-urban interface that breaks the feedback loop through prevention, preparation, and ecosystem restoration.",
    "stem_scenario": "A mountain community of 15,000 people borders a national forest that hasn't experienced a major fire in 80 years. Fuel loads are at record levels, drought conditions are worsening, and the forest is surrounded by new housing developments. The community has hired your team to design a wildfire resilience plan that addresses both immediate safety and long-term ecosystem health. Your plan must balance fire prevention with the ecological need for fire.",
    "stem_questions": [
        "How would you use prescribed burns and fuel reduction to break the feedback loop before a catastrophic fire occurs?",
        "What design features would you recommend for homes and buildings in the wildland-urban interface?",
        "How do you balance the ecological benefits of natural fire with the need to protect human lives and property?"
    ],
    "stem_design_qs": [
        "What would your defensible space requirements look like for homes within 1 mile of the forest boundary?",
        "How would you design a prescribed burn program that reduces fuel loads without exceeding safe conditions?",
        "What early warning and evacuation systems would your plan include, and how would they account for wind speed and direction changes?",
        "How would you restore the natural fire cycle in the surrounding forest while protecting the community?"
    ],
    "career": "Wildfire Scientists study fire behavior, ecology, and management strategies using computational models and field research, earning $55,000–$110,000/year. Fire Ecologists study how fire shapes ecosystems and design prescribed burn programs, earning $50,000–$100,000/year. Urban Planners specializing in wildfire resilience design communities that can coexist with fire-prone landscapes, earning $60,000–$120,000/year.",
    "images": {
        "cover": ("G09L1-L10-cover.png", "A photorealistic, cinematic image of a massive wildfire burning on a forested hillside at dusk with enormous orange flames and a towering smoke column, embers carried by wind, a small town visible in the valley below with fire crews preparing defensive positions, dramatic and intense lighting"),
        "landscape": ("G09L1-L10-landscape.png", "A diverse group of 14-15 year old students on a field trip examining a recently burned forest area showing charred trees alongside green regrowth, one student collecting soil samples while others photograph the landscape, educational atmosphere"),
        "modeling": ("G09L1-L10-modeling.png", "A diverse group of 14-15 year old students at laptops building wildfire spread models with fire behavior simulations on their screens, color-coded maps showing fuel loads and wind patterns, modern science classroom with fire ecology posters"),
        "discussion": ("G09L1-L10-discussion.png", "A Black teacher leading a discussion with diverse 14-15 year old students about the wildfire feedback loop, a circular diagram showing the fire-vegetation-soil-fuel cycle displayed on a smartboard, students actively debating"),
        "stem": ("G09L1-L10-stem.png", "Diverse 14-15 year old students creating scale model communities in the wildland-urban interface, designing defensible spaces and fire-resistant building features, topographic maps and wind data charts spread across lab tables")
    },
    "pre_assessment": [
        "Why do you think wildfires in the western United States have been getting larger and more destructive in recent decades?",
        "Is fire always bad for a forest? Can you think of reasons fire might actually be necessary for a healthy ecosystem?",
        "What factors do you think determine how fast a wildfire spreads and how hot it burns?",
        "Draw a diagram showing what you think happens to a forest ecosystem after a major wildfire — include what changes over the next 5, 20, and 50 years."
    ],
    "extend_components": [
        ("Carbon Release", "The massive amount of CO2 released when vegetation burns — a single large wildfire can release more carbon in weeks than the surrounding forest absorbed in decades, contributing to climate change that makes future fires worse"),
        ("Fire Weather Index", "A composite measure of temperature, humidity, wind speed, and drought that predicts fire danger — climate change is increasing the number of high fire-weather days per year in fire-prone regions"),
        ("Pyrocumulonimbus Events", "Extreme wildfires that generate their own thunderstorms, producing lightning that starts new fires and erratic winds that make the original fire unpredictable — a feedback loop within the feedback loop, representing the most dangerous fire behavior on Earth")
    ],
    "reflections": [
        "How does the positive feedback loop in your model explain why wildfires are getting progressively worse over time?",
        "What does your model reveal about why a century of fire suppression has been counterproductive?",
        "How does climate change interact with the wildfire feedback loop to accelerate the cycle?",
        "If low-intensity fire is beneficial, how should forest management balance fire suppression with ecological fire needs?",
        "What are the limitations of modeling wildfire behavior with only five components when real fires involve hundreds of variables?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students create computational simulations that model fire behavior, track changes over multiple fire cycles, and test hypotheses about how feedback loops maintain or destabilize ecosystem conditions."),
        ("Disciplinary Core Idea", "ESS3.C: Human Impacts on Earth Systems / LS2.C: Ecosystem Dynamics, Functioning, and Resilience", "Students model how human activities (fire suppression, climate change, development) alter natural fire regimes, and how complex interactions in fire-adapted ecosystems are disrupted when the natural cycle is broken."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how fire-adapted ecosystems maintain stability through periodic low-intensity disturbance, and how disruption of this cycle — through suppression, climate change, or development — pushes the system toward catastrophic, self-reinforcing change.")
    ],
    "cast_items": [
        "Model the positive feedback loop between wildfire, vegetation loss, soil moisture, and fuel accumulation",
        "Analyze how human fire suppression policies and climate change have disrupted the natural fire cycle",
        "Create computational simulations to predict future fire behavior under different management and climate scenarios"
    ],
    "cast_questions": [
        ("Analyze:", "A national forest has not burned in 80 years due to aggressive fire suppression. Using your model, explain why this forest is now at HIGHER risk of catastrophic fire than one that experienced periodic low-intensity burns. Identify every component affected by the long suppression period."),
        ("Evaluate:", "A forest manager proposes two strategies: (A) Continue fire suppression and invest in firefighting technology, or (B) Implement a prescribed burn program that intentionally sets low-intensity fires. Using evidence from your model, evaluate which strategy is more likely to prevent catastrophic wildfire in the long term.")
    ],
    "background_intro": "Fire has been part of Earth's ecosystems for 400 million years — longer than flowering plants, longer than dinosaurs. Many ecosystems didn't just survive fire; they EVOLVED to need it. Pine cones that only open in extreme heat, grasses that regrow from underground roots, wildflowers that germinate in ash — fire is nature's reset button. But humans have disrupted this cycle in two devastating ways: a century of fire suppression that let fuel accumulate to explosive levels, and climate change that's drying out landscapes faster than they can recover.",
    "background_sections": [
        ("The Natural Fire Cycle", "In a healthy fire-adapted ecosystem, low-intensity surface fires sweep through every 5-30 years, burning dead leaves, fallen branches, and small shrubs while leaving mature trees largely unharmed. These fires recycle nutrients back to the soil, create openings for new growth, kill disease-causing organisms, and prevent fuel from accumulating to dangerous levels. Many species depend on fire: longleaf pine forests, tallgrass prairies, and Australian eucalyptus woodlands all evolved with regular burning. Without fire, these ecosystems slowly degrade."),
        ("Fire Suppression: A Century-Long Mistake", "After the Great Fires of 1910 burned 3 million acres and killed 85 firefighters in the American West, the U.S. adopted a policy of suppressing ALL wildfires as quickly as possible. For a century, this seemed to work — fire acreage dropped dramatically. But fuel loads skyrocketed. Forests that naturally burned every 10-15 years accumulated 50-100 years of dead wood, brush, and dense undergrowth. What would have been a mild surface fire in 1920 is now a catastrophic crown fire in 2025 because there's 10 times more fuel."),
        ("Climate Change: Adding Fuel to the Fire", "Climate change is supercharging the wildfire problem through multiple mechanisms: higher average temperatures dry out vegetation faster, snowpack melts earlier reducing summer soil moisture, drought periods are longer and more severe, and the fire season has extended by 80+ days in the western U.S. since 1970. The result: fire weather conditions that would have been extreme are now routine. The 2020 U.S. fire season burned 10.1 million acres. The 2023 Canadian wildfires burned 45 million acres — an area larger than Florida."),
        ("The Positive Feedback Loop", "Here's where the science gets frightening: wildfire itself creates conditions for worse future fires. A catastrophic fire destroys the tree canopy that shades the ground → without shade, soil temperatures rise and moisture evaporates → drier soil can't support rapid revegetation → the burned area accumulates dead, dry material as fuel → the next fire has abundant dry fuel and burns even hotter. Meanwhile, massive fires release stored carbon as CO2 → more CO2 accelerates climate change → climate change creates hotter, drier conditions → which make fires worse. The loop feeds itself at every level.")
    ],
    "lever_L": "Students identify wind speed, fuel load, fire intensity, soil moisture, and vegetation recovery as the key components that determine wildfire behavior and ecosystem recovery.",
    "lever_E": "Students determine that wind speed drives fire intensity when fuel is available, fire intensity reduces soil moisture and destroys vegetation, and slow vegetation recovery leaves fuel and dry conditions for the next fire — forming a positive feedback loop.",
    "lever_V": "Students build a computational model showing the positive feedback loop where each fire cycle creates conditions for more intense future fires, and where disruption points could break the cycle.",
    "lever_Ev": "Students run healthy fire, catastrophic fire, and post-fire recovery scenarios to test their model and discover whether the ecosystem recovers or enters a self-reinforcing destructive cycle.",
    "lever_R": "Students add carbon release, fire weather index, or pyrocumulonimbus events to model more realistic wildfire dynamics and climate feedback.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic wildfire image", "say": "In 2023, Canadian wildfires burned an area larger than Florida and turned New York City skies orange. In 2025, the LA fires destroyed over 12,000 structures. These aren't random events — they're part of a cycle that's feeding itself.", "do": "Show the iconic orange sky photos from NYC and satellite imagery of Canadian fires. Let the scale sink in.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today we're modeling why wildfires are getting worse — and discovering that the solution isn't fighting fire harder. It's understanding the loop.", "do": "Have students read objectives. Pre-teach 'fuel load' and 'positive feedback loop.' Ask who's been affected by wildfire smoke.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why are wildfires getting bigger and harder to stop?", "say": "Here's the paradox: we've spent a century putting out fires, and fires have gotten WORSE. How is that possible?", "do": "Quick-write: Students brainstorm why fighting fire might make fire worse. Pair-share. Introduce the concept of unintended consequences.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model the wildfire feedback loop and find out: is there a way to break the cycle, or is it already running away from us?", "do": "Preview LEVER steps. Emphasize that this model includes a FEEDBACK LOOP — the output becomes the next input.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for wildfire model", "say": "Wind is the one thing we absolutely cannot control in a wildfire. Everything else is part of the system that feeds or fights the fire. Sort them.", "do": "Guide sorting: wind speed is external. Fuel load, fire intensity, soil moisture, and vegetation recovery are internal system components. Discuss controllability.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Circular relationship arrows showing the feedback loop", "say": "Trace the loop: fire burns → vegetation gone → soil dries → more fuel for next fire → bigger fire. Where could we break this cycle?", "do": "Help students map the complete feedback loop. Critical moment: identify where the loop can be broken (fuel reduction, prescribed burns).", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Multi-cycle fire behavior graphs", "say": "Let's run three futures: a healthy forest with natural fire, a catastrophic fire, and the aftermath. Does the ecosystem bounce back or spiral down?", "do": "Students predict outcomes. Run scenarios over multiple fire cycles. Key discovery: the feedback loop — each fire makes the next one worse.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings: feedback loop, fire suppression backfire, climate acceleration", "say": "Fire isn't the enemy. The ABSENCE of fire — for a century — created an enemy we may not be able to stop. The solution isn't more firefighting. It's more FIRE — the right kind, at the right time.", "do": "Discuss the paradox: fighting fire made things worse. Indigenous fire management used controlled burns for thousands of years. Connect to climate change amplification.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Community wildfire resilience plan", "say": "A mountain town of 15,000 people borders a forest that hasn't burned in 80 years. The fuel is piled to the ceiling. Design a plan that saves the town AND the forest.", "do": "Groups design comprehensive wildfire resilience plans. Must include prescribed burns, defensible space, early warning, and ecological restoration. Present strategies.", "time": "12 min"}
    ],
    "sort_reasoning": "Wind Speed is the external component because it is a meteorological variable driven by atmospheric conditions that humans cannot control during a wildfire event — it is a given that the system must respond to. Fuel Load, Fire Intensity, Soil Moisture, and Vegetation Recovery are internal because they are interconnected ecological variables that influence each other in a feedback loop: fire intensity depends on fuel and wind, fire destroys vegetation and dries soil, and vegetation recovery depends on soil moisture and fire severity.",
    "relationships": [
        ("Wind Speed to Fire Intensity", "POSITIVE (+)", "Stronger winds deliver more oxygen to the fire front, increase flame length and spread rate, carry embers to start spot fires ahead of the main front, and can push a surface fire into tree crowns — transforming a manageable fire into an unstoppable inferno."),
        ("Fuel Load to Fire Intensity", "POSITIVE (+)", "More available fuel — dry wood, leaves, brush, and dead trees — provides more combustible material for the fire to consume, releasing more energy and sustaining higher temperatures and faster spread rates."),
        ("Fire Intensity to Soil Moisture", "NEGATIVE (-)", "Intense fires destroy the vegetation canopy that shades the ground, bake moisture out of the upper soil layers, and can create hydrophobic (water-repellent) compounds in the soil that prevent rainfall from absorbing, leading to rapid drying and erosion."),
        ("Soil Moisture to Vegetation Recovery", "POSITIVE (+)", "Higher soil moisture supports faster seed germination, root development, and plant growth after a fire. Without adequate moisture, regeneration stalls and the burned landscape remains barren, exposed to erosion and further drying.")
    ],
    "sim_answers": [
        ("Healthy Fire Scenario", "When Wind Speed is low and Fuel Load is moderate with adequate Soil Moisture, Fire Intensity remains low. The surface fire clears accumulated brush and dead material without killing mature trees. Soil Moisture is minimally affected because the canopy survives. Vegetation Recovery is rapid because root systems remain intact and soil conditions support regrowth. The model shows that low-intensity fire is a stabilizing force — it REDUCES fuel load, preventing the conditions for catastrophic fire."),
        ("Catastrophic Fire Scenario", "When Wind Speed is high, Fuel Load is at maximum (80 years of accumulation), and Soil Moisture is low from drought, Fire Intensity reaches extreme levels. Crown fire destroys the entire canopy and bakes the soil. Soil Moisture drops to near zero. Vegetation Recovery is extremely slow because root systems are killed, seed banks are destroyed, and the soil is hydrophobic. The model reveals the feedback loop: the burned landscape accumulates new fuel faster than it recovers canopy, making the next fire just as intense — or worse.")
    ],
    "reflection_exemplars": [
        ("Why did a century of fire suppression backfire?", "The model clearly shows why: by preventing low-intensity fires for 80-100 years, fire suppression allowed Fuel Load to accumulate to levels far beyond what would naturally exist. In a healthy fire regime, periodic burns keep fuel at moderate levels — like regularly emptying a trash can. Suppression is like never emptying the trash for a decade and then being surprised when it catches fire and burns down the house. The model demonstrates that removing periodic disturbance from a system that evolved with it doesn't create stability — it creates a bomb."),
        ("How does climate change accelerate the feedback loop?", "Climate change attacks the wildfire feedback loop at multiple points simultaneously. Higher temperatures reduce Soil Moisture, which stresses vegetation and makes Fuel Load drier and more ignitable. Extended drought periods prevent Vegetation Recovery between fires, leaving more bare ground that dries further. Warmer winters mean more insects that kill trees, adding to Fuel Load. And earlier snowmelt extends the fire season by 80+ days. The model shows that climate change doesn't just make individual fires worse — it accelerates the entire feedback cycle so that each successive fire occurs in progressively more extreme conditions.")
    ],
    "stem_intro": "Present the challenge: A mountain community of 15,000 residents borders a national forest with 80 years of accumulated fuel. Drought conditions are worsening, and development is expanding into the wildland-urban interface. The community council needs a comprehensive wildfire resilience plan that addresses immediate safety, long-term forest health, and the feedback loop that's making both worse.",
    "stem_concepts": [
        ("Prescribed Burns and Fuel Management", "Intentionally set, carefully controlled low-intensity fires that reduce accumulated fuel loads to historically natural levels. Prescribed burns mimic the natural fire cycle that maintained forest health for millennia. Indigenous peoples across the Americas, Australia, and Africa practiced cultural burning for thousands of years before European fire suppression policies disrupted these practices."),
        ("Defensible Space and Fire-Adapted Communities", "A zone around structures where vegetation is managed to reduce fire intensity and give firefighters a chance to defend the building. Zone 1 (0-5 feet): No combustible material. Zone 2 (5-30 feet): Low, well-spaced, fire-resistant plants. Zone 3 (30-100 feet): Reduced and spaced fuel. Combined with fire-resistant building materials (metal roofs, tempered glass, non-combustible siding), defensible space dramatically increases structure survival."),
        ("Post-Fire Ecosystem Restoration", "Active management to help fire-damaged ecosystems recover before the feedback loop takes hold. Strategies include erosion control (mulching, wattles), reseeding with native species, salvaging usable timber while leaving some dead wood for habitat, and controlling invasive species that colonize burned areas. The goal is to restore vegetation cover fast enough to stabilize soil moisture before the next fire season.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses the feedback loop at multiple intervention points, includes prescribed burn schedule, defensible space standards, early warning system, and post-fire restoration strategy, all justified with evidence from the computational model"),
        ("Proficient (3)", "Plan addresses wildfire prevention and community safety with reasonable strategies based on model findings"),
        ("Developing (2)", "Plan addresses some wildfire risks but doesn't connect strategies to the feedback loop or lacks comprehensive approach"),
        ("Beginning (1)", "Plan is incomplete or relies solely on traditional fire suppression without addressing the underlying feedback cycle")
    ],
    "support": [
        "Provide a diagram of the wildfire feedback loop with labeled intervention points where the cycle could be broken",
        "Use before/after images of prescribed burns: show how managed fire creates a park-like forest that resists catastrophic fire",
        "Sentence frames: 'When fire intensity is high, soil moisture __ because __, which means vegetation recovery __ because __, creating conditions where the next fire __'"
    ],
    "extensions": [
        "Research how Indigenous fire management practices (Aboriginal Australian fire-stick farming, Native American cultural burns) maintained healthy landscapes for thousands of years, and how these practices are being revived today",
        "Investigate pyrocumulonimbus events — fires so large they create their own thunderstorms — and model how this represents a feedback loop within the feedback loop",
        "Analyze satellite data showing how fire scars from major wildfires (Paradise, CA 2018; Black Summer Australia 2019-20) are recovering — is the vegetation returning, or is the feedback loop taking hold?"
    ],
    "cross_curr": [
        ("Math", "Calculate fuel accumulation rates: If a forest produces 2 tons/hectare/year of dead material and fire normally removes it every 15 years, how much fuel accumulates after 80 years of suppression? Graph the exponential risk increase."),
        ("ELA", "Write a policy brief for the state legislature arguing for increased funding for prescribed burns, using evidence from your model to demonstrate that fire prevention is more cost-effective than firefighting"),
        ("Social Studies", "Research how wildfire risk intersects with housing affordability: Why do people build in fire-prone areas, what role do insurance markets play, and who bears the cost when fires destroy communities?")
    ],
    "misconceptions": [
        ("All wildfire is destructive and should be prevented", "Many ecosystems REQUIRE fire to remain healthy. Longleaf pine forests, tallgrass prairies, chaparral, and Australian eucalyptus woodlands all evolved with regular fire and decline without it. Low-intensity surface fires recycle nutrients, reduce disease, promote biodiversity, and prevent catastrophic fuel accumulation. The problem isn't fire itself — it's the wrong KIND of fire at the wrong TIME, which results from decades of suppression.", "Show comparison: A longleaf pine forest burned every 3 years (open, park-like, diverse understory) versus one unburned for 30 years (choked with brush, diseased trees, catastrophic fire risk). Which is healthier?"),
        ("Climate change is the only reason wildfires are getting worse", "Climate change is a major accelerant, but it's not the whole story. A century of fire suppression has loaded forests with 5-10 times more fuel than they would naturally carry. Development in the wildland-urban interface has put millions of homes in fire's path. And the loss of Indigenous cultural burning practices removed a management tool that maintained healthy landscapes for millennia. The wildfire crisis is the result of MULTIPLE human decisions compounding over time.", "Thought experiment: If climate change magically reversed tomorrow, would forests with 80 years of accumulated fuel suddenly become safe? What else needs to change?"),
        ("Bigger firefighting budgets will solve the wildfire problem", "The U.S. spends over $3 billion per year on wildfire suppression, and fires are still getting worse. Suppression treats the symptom (active fire) without addressing the cause (excessive fuel, dry conditions, climate change). Worse, every dollar spent on suppression is a dollar NOT spent on prevention — prescribed burns, fuel reduction, and building codes. The model shows that breaking the feedback loop BEFORE a fire starts is exponentially more effective than fighting it once it's burning.", "Analogy: If your house flooded every year because of a broken pipe, would you buy bigger mops or fix the pipe? Fire suppression is the mop; prescribed burns and fuel management are the pipe fix.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
