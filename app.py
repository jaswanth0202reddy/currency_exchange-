from flask import Flask, render_template, request

app = Flask(__name__)

# A simple dictionary with some currency conversion rates (example rates)
currency_rates = {
    "USD": {
        "INR": 82.74,
        "EUR": 0.92,
        "GBP": 0.78,
        "AUD": 1.48
    },
    "INR": {
        "USD": 0.012,
        "EUR": 0.011,
        "GBP": 0.0094,
        "AUD": 0.018
    },
    "EUR": {
        "USD": 1.09,
        "INR": 89.48,
        "GBP": 0.85,
        "AUD": 1.61
    },
    "GBP": {
        "USD": 1.28,
        "INR": 110.57,
        "EUR": 1.17,
        "AUD": 1.89
    },
    "AUD": {
        "USD": 0.68,
        "INR": 55.77,
        "EUR": 0.62,
        "GBP": 0.53
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_amount = None
    error = None

    if request.method == 'POST':
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = request.form['amount']

        try:
            amount = float(amount)
            if from_currency in currency_rates and to_currency in currency_rates[from_currency]:
                conversion_rate = currency_rates[from_currency][to_currency]
                converted_amount = amount * conversion_rate
            else:
                error = "❌ Conversion not available for the selected currencies."
        except ValueError:
            error = "❌ Amount must be a number."
        except Exception as e:
            error = f"❌ Conversion failed: {e}"

    return render_template('index.html', converted_amount=converted_amount, error=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
