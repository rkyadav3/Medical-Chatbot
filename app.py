from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Medical chatbot logic
class MedicalChatbot:
    def __init__(self):
        # Dictionary with multiple conditions, medications, precautions, and diet suggestions
        self.conditions = {

            'fever': {
                'medications': {'paracetamol': '500mg every 6 hours'},
                'precautions': 'Stay hydrated, take rest, avoid cold beverages.',
                'diet': 'Eat light food, drink plenty of fluids, avoid spicy and fried foods.'
            },
            'cold': {
                'medications': {'antihistamine': '10mg once daily', 'decongestant': 'as per need'},
                'precautions': 'Keep warm, avoid cold drinks, stay hydrated.',
                'diet': 'Drink warm fluids, eat light soups, avoid dairy products.'
            },
            'headache': {
                'medications': {'ibuprofen': '400mg every 8 hours'},
                'precautions': 'Avoid bright light, rest in a quiet environment.',
                'diet': 'Stay hydrated, avoid caffeine and processed foods.'
            },
            'stomach pain': {
                'medications': {'antacid': 'as per need'},
                'precautions': 'Avoid spicy, oily, and acidic foods, eat smaller meals.',
                'diet': 'Eat light and bland foods, avoid fried and fatty foods.'
            },
            'cough': {
                'medications': {'cough syrup': 'Take 5ml 2-3 times daily'},
                'precautions': 'Avoid cold air, drink warm fluids, avoid smoking.',
                'diet': 'Consume warm soups and teas, avoid cold beverages, stay hydrated.'
            },
            'diarrhea': {
                'medications': {'oral rehydration salts': 'as per need', 'loperamide': 'as directed'},
                'precautions': 'Stay hydrated, avoid dehydration, wash hands frequently.',
                'diet': 'Drink electrolyte solutions, eat bananas, rice, applesauce, and toast (BRAT diet). Avoid greasy and high-fiber foods.'
            },
            'constipation': {
                'medications': {'fiber supplements': 'as per need', 'laxative': 'as directed'},
                'precautions': 'Increase water intake, exercise regularly.',
                'diet': 'Eat high-fiber foods like fruits, vegetables, and whole grains. Avoid dairy and processed foods.'
            },
            'hypertension': {
                'medications': {'amlodipine': '5mg once daily', 'losartan': '50mg once daily'},
                'precautions': 'Monitor blood pressure regularly, reduce salt intake, avoid stress.',
                'diet': 'Eat potassium-rich foods (bananas, spinach), avoid salty and fatty foods, limit caffeine.'
            },
            'diabetes': {
                'medications': {'metformin': '500mg twice daily', 'insulin': 'as prescribed'},
                'precautions': 'Monitor blood sugar regularly, avoid sugary foods, exercise regularly.',
                'diet': 'Eat a balanced diet with whole grains, lean protein, and vegetables. Avoid processed sugars and carbs.'
            },
            'asthma': {
                'medications': {'inhaler': 'as directed', 'montelukast': '10mg once daily'},
                'precautions': 'Avoid allergens, use inhaler before exercise, avoid smoking.',
                'diet': 'Eat anti-inflammatory foods (e.g., ginger, turmeric), avoid processed and fried foods.'
            },
            'allergies': {
                'medications': {'antihistamine': '10mg once daily'},
                'precautions': 'Avoid known allergens, stay indoors during high pollen counts.',
                'diet': 'Eat foods rich in quercetin (e.g., apples, berries), avoid dairy and sugary foods during allergy season.'
            },
            'migraine': {
                'medications': {'sumatriptan': '50mg as needed', 'ibuprofen': '400mg every 6 hours'},
                'precautions': 'Rest in a dark, quiet room, avoid triggers such as bright light and loud noises.',
                'diet': 'Stay hydrated, eat magnesium-rich foods like spinach, avoid caffeine and processed foods.'
            },
            'acid reflux': {
                'medications': {'antacid': 'as needed', 'omeprazole': '20mg once daily'},
                'precautions': 'Avoid lying down immediately after eating, elevate your head while sleeping.',
                'diet': 'Eat smaller meals, avoid spicy and fatty foods, avoid citrus and tomato-based products.'
            },
            'anxiety': {
                'medications': {'benzodiazepine': 'as prescribed', 'SSRIs': 'as prescribed'},
                'precautions': 'Practice relaxation techniques like deep breathing and meditation, get regular exercise.',
                'diet': 'Eat magnesium-rich foods, avoid caffeine and alcohol.'
            },
            'depression': {
                'medications': {'SSRIs': 'as prescribed', 'SNRIs': 'as prescribed'},
                'precautions': 'Exercise regularly, maintain a healthy sleep schedule, avoid alcohol.',
                'diet': 'Eat omega-3 rich foods (e.g., salmon, walnuts), avoid processed and sugary foods.'
            },
            'back pain': {
                'medications': {'ibuprofen': '400mg every 8 hours', 'muscle relaxant': 'as prescribed'},
                'precautions': 'Avoid heavy lifting, practice proper posture, do gentle stretching exercises.',
                'diet': 'Eat anti-inflammatory foods like berries and leafy greens, avoid sugary and processed foods.'
            },
            'skin rash': {
                'medications': {'hydrocortisone cream': 'apply twice daily', 'antihistamine': 'as needed'},
                'precautions': 'Avoid scratching, use hypoallergenic soaps and moisturizers.',
                'diet': 'Eat foods rich in vitamin E (e.g., nuts, seeds), avoid spicy and hot foods.'
            },
            'high cholesterol': {
                'medications': {'statins': 'as prescribed'},
                'precautions': 'Exercise regularly, avoid trans fats, quit smoking if applicable.',
                'diet': 'Eat oats, nuts, and foods rich in omega-3 fatty acids. Avoid fried and fatty foods.'
            },
            'insomnia': {
                'medications': {'melatonin': '3mg before bedtime', 'zolpidem': 'as prescribed'},
                'precautions': 'Maintain a regular sleep schedule, avoid screen time before bed, create a calming bedtime routine.',
                'diet': 'Drink chamomile tea, eat magnesium-rich foods, avoid caffeine and alcohol in the evening.'
            },
            'arthritis': {
                'medications': {'ibuprofen': '400mg every 8 hours', 'glucosamine': 'as prescribed'},
                'precautions': 'Stay active with low-impact exercises, maintain a healthy weight.',
                'diet': 'Eat anti-inflammatory foods like fatty fish and berries, avoid processed foods and sugar.'
            },
            'gout': {
                'medications': {'allopurinol': 'as prescribed', 'NSAIDs': 'as needed for pain'},
                'precautions': 'Avoid foods high in purines (e.g., red meat, seafood), stay hydrated.',
                'diet': 'Eat cherries, low-fat dairy, and whole grains. Avoid alcohol and sugary beverages.'
            },
            'anemia': {
                'medications': {'iron supplements': 'as prescribed', 'vitamin B12': 'as prescribed'},
                'precautions': 'Avoid caffeine when taking iron supplements, get regular blood tests to monitor levels.',
                'diet': 'Eat iron-rich foods (e.g., spinach, red meat), consume vitamin C-rich foods to enhance iron absorption.'
            },
            'sinusitis': {
                'medications': {'decongestant': 'as needed', 'nasal spray': 'as prescribed'},
                'precautions': 'Avoid exposure to cold air, use a humidifier to keep air moist.',
                'diet': 'Drink warm liquids, eat anti-inflammatory foods like ginger and garlic, avoid dairy products.'
            }
        }
        # Medicines that prevent interactions or support overall health
        self.non_reactive_medications = {
            'multivitamin': 'Take once daily to prevent deficiencies.',
            'probiotic': 'Helps maintain gut health, especially with antibiotics.'
        }

    def get_medications(self, conditions):
        meds = {}
        precautions = []
        diet = []
        
        for condition in conditions:
            if condition in self.conditions:
                condition_info = self.conditions[condition]
                
                # Add medications (ensuring no conflict)
                for med, dose in condition_info['medications'].items():
                    if med not in meds:
                        meds[med] = dose
                
                # Add precautions and diet
                precautions.append(condition_info['precautions'])
                diet.append(condition_info['diet'])
        
        return meds, precautions, diet

    def suggest_medication(self, conditions):
        medications, precautions, diet = self.get_medications(conditions)
        
        # Preventative non-reactive medications
        prevent_reactions = self.non_reactive_medications

        # Formatting the response
        response = {
            'medications': medications,
            'precautions': precautions,
            'diet': diet,
            'prevent_reactions': prevent_reactions
        }
        
        return response

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    conditions_input = request.form.get('condition').lower()
    conditions = [condition.strip() for condition in conditions_input.split(',')]
    
    chatbot = MedicalChatbot()
    response = chatbot.suggest_medication(conditions)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
