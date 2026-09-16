import random

class AstroLLM:
    def __init__(self):
        self.predictions = [
            "The stars predict a 99% chance you will look at your phone in the next 5 minutes.",
            "Mercury is in retrograde, which fully excuses any bad decisions you make today.",
            "Your lucky number today is 404: Good fortune not found.",
            "Saturn says: Stop adding items to your online shopping cart.",
            "The cosmos suggest eating a snack. Not for spiritual alignment, just because you're hungry."
        ]
        
        self.zodiac_vibes = {
            "aries": "Your hotheaded energy today could power a small city.",
            "taurus": "The stars see a very long nap in your near future.",
            "gemini": "Both of your personalities should try agreeing on lunch today.",
            "cancer": "Cosmic advice: It is okay to leave the house today.",
            "leo": "The universe revolves around the sun, but today it revolves around you.",
            "virgo": "Your horoscope was delayed because you'd just critique the formatting anyway.",
            "libra": "The stars spent 3 hours trying to weigh your options and gave up.",
            "scorpio": "The cosmos know what you did. (Just kidding, or am I?)",
            "sagittarius": "You are about to book a flight to nowhere just to avoid responsibility.",
            "capricorn": "The planetary alignment strongly recommends taking a day off. You won't, but it recommends it.",
            "aquarius": "You are currently being judged by an alien civilization 40 light-years away.",
            "pisces": "Your head is so far in the clouds you just bumped into a satellite."
        }

    def predict(self, user_input):
        text = user_input.lower()
        
        # Check for specific zodiac signs
        for sign, vibe in self.zodiac_vibes.items():
            if sign in text:
                return f"✨ [{sign.upper()} HOROSCOPE] ✨\n{vibe}"
                
        # Generic astrological wisdom
        return f"🔮 [COSMIC READOUT] 🔮\n{random.choice(self.predictions)}"

# Run the AstroLLM
astrologer = AstroLLM()

print(astrologer.predict("I am a Leo, what is my alignment today?"))
print(astrologer.predict("Should I check my email?"))