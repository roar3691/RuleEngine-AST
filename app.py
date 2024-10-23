from flask import Flask, request, render_template_string
from rule_engine import ImprovedRuleEngine

app = Flask(__name__)
engine = ImprovedRuleEngine()

# HTML template for simple UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rule Engine</title>
</head>
<body>
    <h1>Rule Engine</h1>
    <form action="/" method="post">
        <label for="rule">Enter Rule:</label><br>
        <input type="text" id="rule" name="rule"><br><br>
        <input type="submit" value="Create Rule">
    </form>
    
    <form action="/" method="post">
        <label for="data">Enter Data (JSON):</label><br>
        <textarea id="data" name="data"></textarea><br><br>
        <input type="submit" value="Evaluate Rule">
    </form>

    {% if result is not none %}
        <h2>Evaluation Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if request.form.get('rule'):
            rule_string = request.form['rule']
            engine.create_rule(rule_string)
            result = f'Rule "{rule_string}" created.'
        
        if request.form.get('data'):
            data_str = request.form['data']
            try:
                data = eval(data_str)  # Use json.loads(data_str) in production for safety
                combined_rule = engine.combine_rules([rule.value for rule in engine.rules])
                result = engine.evaluate_rule(combined_rule, data)
            except Exception as e:
                result = f'Error evaluating rule: {e}'
    
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)