# chatbot.py
import random

class ChatBot:
    def __init__(self):
        self.conversation_history = []
        self.responses = {
            "greeting": [
                "Hello! Welcome to Africa International University. How can I assist you today?",
                "Hi there! I'm your AIU Assistant. What would you like to know?",
                "Welcome to Africa International University! Feel free to ask about our programs, campus, or admissions.",
            ],
            "course_ai": [
                "Our AI and Cybersecurity program is cutting-edge! We cover machine learning, data analysis, and cybersecurity fundamentals. Great for tech-focused careers!",
                "The AI and Cybersecurity program at AIU teaches advanced IT concepts, security protocols, and artificial intelligence. Perfect if you're interested in modern tech!",
            ],
            "course_it": [
                "Information Technology at AIU focuses on practical IT skills, networking, systems management, and cloud computing. Excellent career prospects!",
                "Our IT program covers everything from system administration to network security. You'll be job-ready upon graduation!",
            ],
            "course_accounting": [
                "The Accounting program prepares you for professional accounting careers with courses on financial management, auditing, and business analytics.",
                "AIU's Accounting program is accredited and comprehensive, covering accounting principles, taxation, and financial reporting.",
            ],
            "course_theology": [
                "Our Theology program offers deep theological education, biblical studies, and pastoral training for those called to ministry.",
                "The Theology program at AIU combines academic rigor with practical ministry preparation.",
            ],
            "course_general": [
                "We offer programs in AI and Cybersecurity, Information Technology, Accounting, and Theology. Which interests you?",
                "Africa International University offers diverse programs. Would you like to hear about a specific field?",
            ],
            "university_info": [
                "Africa International University is committed to academic excellence and holistic development of our students. We have facilities including a Library, Chapel, and Finance office.",
                "AIU provides a supportive campus community with key facilities: Library, Chapel, and Finance office. Is there a specific location you need?",
            ],
            "campus_location": [
                "Our main campus locations include the Library (study resources), Chapel (spiritual center), and Finance office (student services).",
                "You can find the Library for research, the Chapel for spiritual activities, and the Finance office for payment/billing inquiries.",
            ],
            "admission": [
                "To apply to Africa International University, visit the Registrar's office or check our admissions portal for application requirements.",
                "Admissions at AIU is straightforward! Contact the Registrar's office for application forms and info about enrollment.",
            ],
            "help": [
                "I can help with: AI & Cybersecurity, IT, Accounting, Theology programs, campus locations, and admissions. What would you like to know?",
                "Ask me about: Programs, Campus facilities, Admissions, or locations at Africa International University!",
            ],
            "farewell": [
                "Goodbye! Good luck with your studies at AIU!",
                "See you later! All the best at Africa International University!",
                "Take care! Welcome to the AIU family!",
            ],
            "unknown": [
                "I'm not sure I understand that. Try asking about our programs, campus, or admissions at AIU.",
                "That's outside my knowledge base. Ask me about AI & Cybersecurity, IT, Accounting, Theology, or campus info!",
                "Could you clarify? I'm here to help with Africa International University information.",
            ]
        }
        
        self.keywords = {
            "greeting": ["hello", "hi", "hey", "greetings", "what's up", "howdy", "welcome"],
            "course_ai": ["ai", "artificial intelligence", "cybersecurity", "machine learning", "security"],
            "course_it": ["information technology", "it", "tech", "computer", "networking", "systems"],
            "course_accounting": ["accounting", "finance", "accounting program", "auditing", "financial"],
            "course_theology": ["theology", "ministry", "biblical", "spiritual", "religious studies"],
            "course_general": ["course", "program", "subject", "class", "department", "major"],
            "university_info": ["africa international", "aiu", "university", "about", "institution"],
            "campus_location": ["library", "chapel", "finance office", "building", "campus", "where", "location"],
            "admission": ["admission", "register", "registration", "apply", "enroll", "sign up"],
            "help": ["help", "can you do", "what can", "capabilities", "assist"],
            "farewell": ["bye", "goodbye", "exit", "quit", "see you", "thanks"],
        }

    def get_intent(self, user_input):
        """Determine user intent based on keywords and context."""
        user_lower = user_input.lower()
        scores = {}
        
        # Check each intent for matching keywords
        for intent, keywords in self.keywords.items():
            score = sum(1 for keyword in keywords if keyword in user_lower)
            if score > 0:
                scores[intent] = score
        
        # Return the intent with highest score
        if scores:
            return max(scores, key=scores.get)
        return "unknown"

    def chatbot_response(self, user_input):
        """Generate response based on user input."""
        if not user_input.strip():
            return "You didn't say anything! What can I help you with?"
        
        intent = self.get_intent(user_input)
        self.conversation_history.append({"input": user_input, "intent": intent})
        
        # Select a random response from the intent category
        response_list = self.responses.get(intent, self.responses["unknown"])
        return random.choice(response_list)

    def main(self):
        print("=" * 50)
        print("Africa International University Assistant")
        print("Type 'exit' to quit or 'help' for available topics")
        print("=" * 50)
        
        bot = ChatBot()
        
        while True:
            try:
                user_query = input("\nYou: ").strip()
                
                if not user_query:
                    continue
                    
                if user_query.lower() in ["exit", "quit", "bye"]:
                    response = random.choice(self.responses["farewell"])
                    print(f"Chatbot: {response}")
                    break
                
                response = bot.chatbot_response(user_query)
                print(f"Chatbot: {response}")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"Chatbot: An error occurred. Please try again. ({str(e)})")

if __name__ == "__main__":
    bot = ChatBot()
    bot.main()

