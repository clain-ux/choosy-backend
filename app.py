from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

game_data = {
    "truth": {
        "easy": [
            "What's your favorite Ugandan song of all time?",
            "Who is the most likely to get married first in this room?",
            "What's the funniest nickname you had in school?",
            "Have you ever lied about your age to save money?",
            "If you could trade lives with one person here, who would it be?"
        ],
        "medium": [
            "RAGE BAIT: Is it okay to check your partner's phone if you have the password?",
            "Have you ever pretended to be sick to skip a family function?",
            "What is the most 'villager' thing you've ever done in Kampala?",
            "RAGE BAIT: Android vs iPhone—which one actually lasts longer in Uganda?",
            "Who here do you think is the 'fake-est' friend?"
        ],
        "hard": [
            "RAGE BAIT: If your partner and your mother were drowning, who do you save?",
            "What is the biggest secret you're hiding from everyone in this room?",
            "Have you ever ghosted someone because they were 'broke'?",
            "Who is the one person you regret meeting the most?",
            "What's the most illegal thing you've ever done?"
        ]
    },
    "dare": {
        "easy": [
            "Do 10 pushups while shouting 'For God and My Country!'",
            "Mime someone eating very hot roasted maize.",
            "Do your best impression of a Boda guy asking for 'Mafuta money'.",
            "Try to balance a phone on your head and walk across the room."
        ],
        "medium": [
            "Do the **Simanyi** dance challenge for 30 seconds.",
            "Call a random contact and ask 'Why did you do it?' then hang up.",
            "Do the **Kaba** dance challenge right now.",
            "Let the person to your left rewrite your WhatsApp bio for 1 hour."
        ],
        "hard": [
            "Do the **Zep** challenge—make sure the legwork is perfect!",
            "Do the **Zenzele** dance while someone pours a little water on you.",
            "Do the **Tobesa** challenge with full energy!",
            "Post 'I'm starting a poultry farm in the village, who's joining?' on your status."
        ]
    },
    "wololo": {
        "easy": [
            "GROUP CHALLENGE: Everyone must do the **Zep** legwork. The worst one owes everyone a soda.",
            "TOXIC CHOICE: Would you rather date your ex again or stay single for 5 years?",
            "DEBATE: Is Rolex a breakfast food or a dinner food? Fight it out!"
        ],
        "medium": [
            "PRANK: Send 'I need to tell you something...' to your crush and don't reply for 5 minutes.",
            "TOXIC CHOICE: Would you rather lose all your hair or lose your phone for a month?",
            "GROUP VOTE: Who in this room is most likely to become a 'Slay Queen/King'?"
        ],
        "hard": [
            "ULTIMATE DARE: Everyone in the room gets to scroll through your photo gallery for 20 seconds.",
            "TOXIC CHOICE: Would you rather your parents see your WhatsApp chats or your browser history?",
            "WILD: Call the 3rd person on your 'Recent Calls' and sing a song for them."
        ]
    }
}

history = {"truth": [], "dare": [], "wololo": []}

@app.route('/get-prompt/<category>')
def get_prompt(category):
    round_num = int(request.args.get('round', 1))
    level = "easy" if round_num <= 4 else "medium" if round_num <= 9 else "hard"

    if category in game_data:
        pool = game_data[category][level]
        available = [q for q in pool if q not in history[category]]
        
        if not available:
            history[category] = []
            available = pool
            
        selection = random.choice(available)
        history[category].append(selection)
        return jsonify({"result": selection, "level": level})
    
    return jsonify({"error": "Category not found"}), 404

if __name__ == '__main__':
    import os
    # This tells Python to use the port the cloud provider gives us
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)