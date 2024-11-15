from flask import Flask, request, jsonify,render_template
app = Flask(__name__, template_folder='C:\VScode\Test')
Food = {'Roti': 120,'Naan': 270,'Paratha': 500,'Puri': 130,'Idli': 70,'Dosa':350,'Uttapam':420,'Upma':290,'Khichdi':420,'Biryani':900,
        'pBM':300 ,'palakPaneer':220,'alooGobi':150,'Bharta':150,'Chole':250,'Rajma':270,'Bhindi':140,'malaiKofta':350,'Sambar':150,'Dosa':200,
        'butterChicken':350,'cTM':300,'fishCurry':220,'mRJ':400,'Keema':300,'tandooriChicken':250,'Prawn':200,'eggCurry':180,'chickenBiryani':300,'Korma':350,
        'Samosa':150,'Pakora':100,'bhelPuri':200,'paniPuri':50,'vadaPav':300,'Dhokla':80,'alooTikki':180,'pavBhaji':350,'Kachori':200,'Chaat':250,'Chips':170,
        'gulabJamun':180,'Rasgulla':120,'Jalebi':150,'Laddu':200,'Kheer':250,'Barfi':180,'Rasmalai':220,'Halwa':250,'Payasam':230,'mysorePak':220}
@app.route('/')
def index():
    return render_template('diets.html')
@app.route('/calculate_calories', methods=['POST'])
def calculateCalories():
    data = request.json
    total_calories=0
    count=0 
    for food_item,count in data.items():
        if food_item in Food:
           total_calories += Food[food_item] * count
           return jsonify({'total_calories':total_calories})
        else:
             return jsonify({'Error':'Food item not found'}),400
if __name__ == '__main__':
    app.run(debug=True)
