from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is fitbot and I'm a chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"(.*) (hungry|sleepy|bored|tired)",
        ["%1 %2? I feel you!",]
    ],
    [
        r"quit",
        ["Bye! Take care. :)", "Goodbye, have a great day!"]
    ],
    [
        r"(.*) start (fitness|workout)",
        [ "Start by setting specific goals, choosing activities you enjoy, and gradually increasing intensity and duration over time."]
    ],
    [
        r"(.*) exercise for weight loss",
        [ "A combination of cardiovascular exercise (like running or cycling) and strength training is most effective for weight loss."]
    ],
    [
        r"(.*) build muscle",
        [ "Focus on progressive overload through resistance training with weights or bodyweight exercises, ensuring adequate protein intake for muscle repair and growth."]
    ],
    [
        r"(.*)  cardio",
        [ "Either order is fine, but many prefer doing strength training before cardio to maximize energy and focus on lifting."]
    ],
    [
        r"(.*) (motivated|motivate)",
        [ "Set achievable goals, find activities you enjoy, vary your routine, enlist workout buddies, and track your progress."]
    ],
       [
        r"(.*) injuries(during workout|during exercise)",
        ["Warm up properly, use correct form, gradually increase intensity, listen to your body, and incorporate rest days into your routine."]
       
    ],
       [
        r"(.*) warmup",
        ["Warming up prepares your body for exercise, reducing injury risk"]
    ],
       [
        r"(.*) home workout",
        ["Bodyweight exercises, yoga, Pilates, and online workout videos can all be effective for home workouts."]
    ],
       [
        r"(.*) overtraining",
        ["Signs of overtraining include persistent fatigue, decreased performance, mood changes, and increased risk of injury."]
    ],
       [
        r"(.*) eat (before workout|after workout)",
        ["Opt for a balanced meal with carbohydrates and protein before exercise, and focus on protein and carbs for recovery after."]
        
    ],
     [
        r"(.*) get  (abs|six packs)",
        ["To get abs, focus on a combination of targeted abdominal exercises (like crunches, planks, and leg raises), a balanced diet to reduce body fat, and overall fitness training to strengthen your core muscles. Consistency is key!"],
],]

chatbot = Chat(pairs, reflections)
