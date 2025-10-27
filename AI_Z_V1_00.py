# AI_Z_V1_00 
#No copy rights
#This is a made up name for an AI the creator has never heard of any AI named AI Z before.
import random

# Hardcoded dataset: input-output pairs
dataset = [
    ("hi", "Hello! How's it going?"),
    ("hello", "Hey there!"),
    ("how are you", "I'm great, thanks! You?"),
    ("what's up", "Not much, just chilling. You?"),
    ("bye", "See ya later!"),
    ("what is 2+2", "Four"),
    ("what is the capital of france", "Paris"),
    ("tell me a joke", "Why did the scarecrow become a motivational speaker? Because he was outstanding!"),
    ("what is python", "Python is a programming language!"),
    ("what is love", "Love is a deep feeling of affection."),
    ("what is a noun", "A noun is a word that names a person, place, or thing."),
    ("what is a verb", "A verb describes an action, like run."),
    ("what is an adjective", "An adjective describes a noun, like big or happy."),
    ("what is a sentence", "A sentence is a group of words expressing a complete thought."),
    ("good", "Glad to hear that! What's next?"),
    ("fine", "Nice to know! Want to talk about something else?"),
    ("okay", "Cool, what's on your mind now?")
]

# Generate 100 ASCII art pictures using '█'
pictures = {
    "square": [
        "████████",
        "█      █",
        "█      █",
        "█      █",
        "█      █",
        "█      █",
        "████████"
    ],
    "tree": [
        "   █    ",
        "  ███   ",
        " █████  ",
        "███████ ",
        "   █    ",
        "   █    ",
        "  ███   "
    ],
    "heart": [
        " █   █  ",
        "███ ███ ",
        "████████",
        "████████",
        " ██████ ",
        "  ████  ",
        "   ██   "
    ],
    "star": [
        "   █    ",
        " █ █ █  ",
        "███ ███ ",
        "  ███   ",
        "███ ███ ",
        " █ █ █  ",
        "   █    "
    ],
    "arrow": [
        "   █    ",
        "  ███   ",
        " █████  ",
        "███████ ",
        "   █    ",
        "   █    ",
        "   █    "
    ],
    "diamond": [
        "   █    ",
        "  ███   ",
        " █████  ",
        "███████ ",
        " █████  ",
        "  ███   ",
        "   █    "
    ],
    "house": [
        "   █    ",
        "  ███   ",
        " █████  ",
        "███████ ",
        "█  █  █ ",
        "█  █  █ ",
        "███████ "
    ],
    "smiley": [
        " █████  ",
        "█     █ ",
        "█  █  █ ",
        "█     █ ",
        "█  █  █ ",
        " ██████ ",
        "        "
    ],
    "circle": [
        "  ███   ",
        " █   █  ",
        "█     █ ",
        "█     █ ",
        "█     █ ",
        " █   █  ",
        "  ███   "
    ],
    "triangle": [
        "   █    ",
        "  ███   ",
        " █████  ",
        "███████ ",
        " █████  ",
        "  ███   ",
        "   █    "
    ]
}

# Generate additional pictures programmatically
# Letters A-Z (26 designs)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i, letter in enumerate(letters):
    design = [
        "        ",
        "   █    ",
        f"  █{letter}█   ",
        " █████  ",
        f"  █{letter}█   ",
        "   █    ",
        "        "
    ]
    pictures[f"letter_{letter}"] = design

# Numbers 0-9 (10 designs)
numbers = "0123456789"
for i, number in enumerate(numbers):
    design = [
        "        ",
        "  ███   ",
        f" █ {number} █  ",
        " █████  ",
        f" █ {number} █  ",
        "  ███   ",
        "        "
    ]
    pictures[f"number_{number}"] = design

# Geometric patterns (30 designs: grids, diagonals, crosses)
for i in range(30):
    if i < 10:  # Grid patterns
        design = [
            "█ █ █ █ ",
            " █ █ █ █",
            "█ █ █ █ ",
            " █ █ █ █",
            "█ █ █ █ ",
            " █ █ █ █",
            "█ █ █ █ "
        ]
        if i % 2 == 0:
            design = [line.replace(" ", "█") if j % 2 == 0 else line for j, line in enumerate(design)]
    elif i < 20:  # Diagonal patterns
        design = ["        "] * 7
        for j in range(7):
            design[j] = " " * j + "█" + " " * (6 - j)
    else:  # Cross patterns
        design = ["        "] * 7
        design[3] = "█" * 7
        for j in range(7):
            design[j] = design[j][:3] + "█" + design[j][4:]
    pictures[f"pattern_{i}"] = design

# Symbols and objects (24 designs: plus, minus, box, frame, etc.)
symbols = ["plus", "minus", "box", "frame", "cross", "slash", "backslash", "x", "v", "u", "n", "m", "w", "z", "y", "t", "l", "j", "i", "o", "p", "q", "r", "s"]
for i, symbol in enumerate(symbols[:24]):
    if symbol == "plus":
        design = [
            "   █    ",
            "   █    ",
            " █████  ",
            "   █    ",
            "   █    ",
            "   █    ",
            "        "
        ]
    elif symbol == "minus":
        design = [
            "        ",
            "        ",
            " █████  ",
            "        ",
            "        ",
            "        ",
            "        "
        ]
    elif symbol == "box":
        design = [
            " █████  ",
            " █   █  ",
            " █   █  ",
            " █   █  ",
            " █   █  ",
            " █████  ",
            "        "
        ]
    else:  # Generic symbol (outline with symbol in center)
        design = [
            " █████  ",
            " █   █  ",
            " █   █  ",
            f" █ {symbol.upper()} █ ",
            " █   █  ",
            " █████  ",
            "        "
        ]
    pictures[f"symbol_{symbol}"] = design

# Create picture_keys list (100 designs)
picture_keys = ["square", "tree", "heart", "star", "arrow", "diamond", "house", "smiley", "circle", "triangle"]
picture_keys += [f"letter_{letter}" for letter in letters]
picture_keys += [f"number_{number}" for number in numbers]
picture_keys += [f"pattern_{i}" for i in range(30)]
picture_keys += [f"symbol_{symbol}" for symbol in symbols[:24]]

# Build vocabulary and initial weights (simulating a neural network)
vocab = set()
for input_text, output_text in dataset:
    vocab.update(input_text.lower().split() + output_text.lower().split())
vocab = list(vocab) + ['<END>']  # Add end token
weights = {}  # Simulate neural network weights: {input_word: {output_word: weight}}
for in_word in vocab:
    weights[in_word] = {out_word: 0.1 for out_word in vocab}  # Small initial weights

# Train the "neural network" (adjust weights based on data)
def train_network(dataset, learning_rate=0.1, epochs=10):
    for _ in range(epochs):
        for input_text, output_text in dataset:
            input_words = input_text.lower().split()
            output_words = output_text.lower().split() + ['<END>']
            for in_word in input_words:
                if in_word in weights:
                    for out_word in output_words:
                        if out_word in vocab:
                            weights[in_word][out_word] += learning_rate
                            for other_word in vocab:
                                if other_word != out_word:
                                    weights[in_word][other_word] -= learning_rate * 0.01
                    # Normalize weights to prevent dominance of common words
                    total = sum(abs(weights[in_word][out_word]) for out_word in vocab)
                    if total > 0:
                        for out_word in vocab:
                            weights[in_word][out_word] /= total

# Run training
train_network(dataset)

# Predefined greetings for quick responses
greetings = {
    "hi": "Hello! How's it going?",
    "hello": "Hey there!",
    "how are you": "I'm great, thanks! You?",
    "how's it going": "Going great, thanks! You?",
    "what's up": "Not much, just chilling. You?",
    "good morning": "Morning! Hope your day's off to a great start!",
    "bye": "See ya later!",
    "thanks": "You're welcome!"
}

# Knowledge base for exact-match Q&A
knowledge_base = {
    "what is 2+2": "Four",
    "what is the capital of france": "Paris",
    "tell me a joke": "Why did the scarecrow become a motivational speaker? Because he was outstanding!",
    "what is python": "Python is a programming language!",
    "what is love": "Love is a deep feeling of affection.",
    "what is a noun": "A noun is a word that names a person, place, or thing.",
    "what is a verb": "A verb describes an action, like run.",
    "what is an adjective": "An adjective describes a noun, like big or happy.",
    "what is a sentence": "A sentence is a group of words expressing a complete thought.",
    "good": "Glad to hear that! What's next?",
    "fine": "Nice to know! Want to talk about something else?",
    "okay": "Cool, what's on your mind now?"
}

# Track last topic, history, and last bot question
last_topic = ""
history = []
last_bot_question = ""

# Generate response using the "neural network"
def generate_response(input_text):
    global last_topic, history, last_bot_question
    input_text = input_text.lower().strip()
    
    # Update topic for context
    if "what is a" in input_text or "what is an" in input_text:
        last_topic = "grammar"
    elif "what is" in input_text:
        last_topic = "dictionary"
    elif "tell me" in input_text or "what" in input_text:
        last_topic = "general"
    else:
        last_topic = "small_talk"
    
    # Check if input is a follow-up to a bot question
    if last_bot_question in ["You?", "What's up with you?"] and input_text in ["good", "fine", "okay"]:
        last_bot_question = ""  # Clear question after responding
        return knowledge_base.get(input_text, "Cool, what's next?")
    
    # Check for picture request
    if any(keyword in input_text for keyword in ["draw", "show", "picture", "image"]):
        # Randomly select a picture
        key = random.choice(picture_keys)
        response = "AI Z drew a picture for you:\n" + "\n".join(pictures[key]) + "\nWant another one?"
        last_bot_question = ""
        return response
    
    # Check greetings first
    for key in greetings:
        if key in input_text:
            response = greetings[key]
            if response.endswith("You?"):
                last_bot_question = "You?"
            else:
                last_bot_question = ""
            return response
    
    # Check knowledge base for exact matches
    for question in knowledge_base:
        if question in input_text:
            follow_up = ""
            if last_topic == "grammar":
                follow_up = " Want to know more about grammar?"
            elif last_topic == "dictionary":
                follow_up = " Curious about another word?"
            elif last_topic == "general":
                follow_up = " Got another question?"
            last_bot_question = ""
            return knowledge_base[question] + follow_up
    
    # Check if input contains known words
    input_words = input_text.lower().split()
    history_text = " ".join(history[-5:])
    input_words += history_text.lower().split()
    has_known_words = False
    for word in input_words:
        if word in vocab:
            has_known_words = True
            break
    
    # If no known words, return default response
    if not has_known_words:
        response = "Sorry, AI Z didn't catch that!"
        if last_topic == "grammar":
            response += " Try asking about grammar, like 'what is a noun'!"
        elif last_topic == "dictionary":
            response += " Ask me a word's meaning, like 'what is love'!"
        elif last_topic == "general":
            response += " Try 'tell me a joke' or a fun fact!"
        else:
            response += " Try saying 'hi' or ask a question!"
        last_bot_question = ""
        return response
    
    # Generate response using weights, with anti-repetition
    response_words = []
    used_words = set()  # Track all words used in this response
    max_len = 8
    for _ in range(max_len):
        scores = {}
        for in_word in input_words:
            if in_word in weights:
                for out_word, weight in weights[in_word].items():
                    scores[out_word] = scores.get(out_word, 0) + weight
        if not scores:
            break
        # Get top words, excluding used ones
        top_words = sorted(scores, key=scores.get, reverse=True)[:5]
        best_word = None
        for word in top_words:
            if word not in used_words and word != '<END>':
                best_word = word
                break
        if best_word is None:
            break  # Stop if no non-repeating word
        response_words.append(best_word)
        used_words.add(best_word)
        input_words = [best_word]
    
    response = " ".join(response_words).capitalize()
    if not response:
        response = "Sorry, AI Z didn't catch that!"
    
    # Add context-based default response
    if last_topic == "grammar":
        response += " Try asking about grammar, like 'what is a noun'!"
    elif last_topic == "dictionary":
        response += " Ask me a word's meaning, like 'what is love'!"
    elif last_topic == "general":
        response += " Try 'tell me a joke' or a fun fact!"
    else:
        response += " Try saying 'hi' or ask a question!"
    last_bot_question = ""
    return response

# Learn new question-answer pair
def learn_new(user_input):
    global knowledge_base, dataset, vocab, weights
    parts = user_input.split("?", 1)
    if len(parts) != 2:
        return "Sorry, format should be: teach: question? answer"
    
    question = parts[0].strip().lower()
    answer = parts[1].strip()
    
    if question and answer:
        knowledge_base[question] = answer
        dataset.append((question, answer))
        new_words = set(question.lower().split() + answer.lower().split())
        new_words.add('<END>')
        for word in new_words:
            if word not in vocab:
                vocab.append(word)
                weights[word] = {out_word: 0.1 for out_word in vocab}
                for existing_word in weights:
                    weights[existing_word][word] = 0.1
        train_network([(question, answer)], epochs=1)
        return f"AI Z learned: '{question}' → '{answer}'"
    else:
        return "Hmm, that didn't work. Try 'teach: what is your name? AI Z'"

# Main chat loop
def chat():
    global history
    print("Welcome to AI Z, your Neural Chat AI! Type 'quit' to exit.")
    print("To teach me, say: 'teach: question? answer'")
    print("Try asking about words, grammar, fun facts, or say 'draw a picture'!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: Bye for now!")
            break
        elif user_input.lower().startswith("teach:"):
            teach_input = user_input[6:].strip()
            response = learn_new(teach_input)
            print("AI Z:", response)
        else:
            history.append(user_input)
            history = history[-5:]  # Keep last 5 inputs
            response = generate_response(user_input)
            print("AI Z:", response)

# Start the chatbot
chat()
