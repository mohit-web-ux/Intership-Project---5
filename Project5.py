import random
import time

outfits = {
    "happy": [
        "😊 Try a yellow t-shirt with blue jeans for positive vibes.",
        "😄 Wear white sneakers with a light-colored outfit to stay cheerful."
    ],
    "calm": [
        "😌 Go for a blue shirt with beige trousers.",
        "🌊 Soft green kurta or hoodie will keep you relaxed."
    ],
    "confident": [
        "🔥 A red shirt with black jeans will boost confidence.",
        "🖤 Black outfit with a bold watch looks powerful."
    ],
    "energetic": [
        "⚡ Yellow hoodie with joggers for active vibes.",
        "🏃 Sporty outfit with bright colors keeps energy high."
    ],
    "stressed": [
        "🧘 Green or pastel colors help calm the mind.",
        "💆 Loose white cotton clothes for comfort."
    ],
    "interview": [
        "👔 Blue formal shirt with black trousers shows trust & professionalism.",
        "🧑‍💼 Light grey suit with formal shoes is a safe choice."
    ],
    "date": [
        "❤️ Red or maroon shirt with fitted jeans looks attractive.",
        "🌹 Black t-shirt with jacket gives classy vibes."
    ],
    "party": [
        "🥳 Black outfit with shiny shoes for party mood.",
        "✨ Stylish dark jeans with printed shirt."
    ],
    "casual": [
        "👕 White t-shirt with denim jeans.",
        "😎 Hoodie with sneakers for relaxed style."
    ]
}

print("👗 Welcome to Outfit Recommendation Bot 👕")
time.sleep(1)

while True:
    user_input = input("\nTell your mood or event (or type 'exit'): ").lower().strip()

    if user_input == "exit":
        print("👋 Stay stylish! Goodbye!")
        break

    if user_input in outfits:
        suggestion = random.choice(outfits[user_input])
        print("\n🎯 Outfit Recommendation:")
        print(suggestion)
    else:
        print("❌ Sorry, I couldn't understand. Try moods like happy, calm, confident or events like interview, party.")
