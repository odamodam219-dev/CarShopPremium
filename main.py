from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='templates')

products = [
    {
        "name": "Chevrolet Malibu 2023",
        "desc": "Avtomatik, 1.5 turbo, oq rang, 15,000 km yurgan",
        "price": "28,500",
        "image": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=400&h=250&fit=crop"
    },
    {
        "name": "BMW 5-Series 2022",
        "desc": "Qora rang, 2.0 dizel, panorama tom, 32,000 km",
        "price": "54,000",
        "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=400&h=250&fit=crop"
    },
    {
        "name": "Toyota Camry 2023",
        "desc": "Kumush rang, 2.5 benzin, to'liq komplektatsiya",
        "price": "38,900",
        "image": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=400&h=250&fit=crop"
    },
    {
        "name": "Mercedes C-Class 2021",
        "desc": "Qizil rang, 1.8 benzin, sport paket, 28,000 km",
        "price": "47,200",
        "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=400&h=250&fit=crop"
    },
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash("Xabaringiz muvaffaqiyatli yuborildi!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        flash("Tizimga muvaffaqiyatli kirdingiz!", "success")
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash("Ro'yxatdan muvaffaqiyatli o'tdingiz!", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)