from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

def calculate_required_grades(prelim_grade):
    passing_grade = 75
    # Calculate the best possible overall grade with a given Prelim grade
    max_possible_grade = (0.20 * prelim_grade) + (0.30 * 100) + (0.50 * 100)
    
    if max_possible_grade < passing_grade:
        return False, None, None
    
    # Midterm and Final grades required to reach the passing grade
    midterm_required = ((passing_grade - (0.20 * prelim_grade)) / 0.80) * (0.30 / 0.80)
    final_required = ((passing_grade - (0.20 * prelim_grade)) / 0.80) * (0.50 / 0.80)
    
    return True, midterm_required, final_required

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle "Calculate Required Grades" button
        if 'calculate_required' in request.form:
            try:
                prelim_grade = float(request.form['prelim'])
            except ValueError:
                flash('Please enter a valid numerical value for the Prelim grade.')
                return redirect(url_for('index'))
            
            # Check if the prelim grade is valid
            if not (0 <= prelim_grade <= 100):
                flash('Prelim grade must be between 0 and 100.')
                return redirect(url_for('index'))
            
            # Calculate the required Midterm and Final grades
            can_pass, midterm_required, final_required = calculate_required_grades(prelim_grade)
            
            if not can_pass:
                message = 'It is impossible to pass with the given Prelim grade.'
            else:
                message = (f"To achieve an overall passing grade of 75, "
                           f"you need at least {midterm_required:.2f} in the Midterm "
                           f"and {final_required:.2f} in the Final.")
            
            return render_template('index.html', message=message)
        
        # Handle "Result Total" button
        elif 'result_total' in request.form:
            try:
                prelim_grade = float(request.form['prelim'])
                midterm_grade = float(request.form['midterm'])
                final_grade = float(request.form['final'])
            except ValueError:
                flash('Please enter valid numerical values for all grades.')
                return redirect(url_for('index'))
            
            # Check if the grades are valid
            if not (0 <= prelim_grade <= 100) or not (0 <= midterm_grade <= 100) or not (0 <= final_grade <= 100):
                flash('All grades must be between 0 and 100.')
                return redirect(url_for('index'))
            
            # Calculate the overall grade
            overall_grade = calculate_overall_grade(prelim_grade, midterm_grade, final_grade) # type: ignore
            message = f'Your overall grade is {overall_grade:.2f}.'
            
            return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grade Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        input, button {
            padding: 20px;
            margin-top: 20px;
            width: 100%;
        }
        .message {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Grade Calculator</h1>
    <form method="post">
        <label for="prelim">Enter your Prelim Grade:</label>
        <input type="text" id="prelim" name="prelim" required>
        
        <label for="midterm">Enter your Midterm Grade:</label>
        <input type="text" id="midterm" name="midterm">
        
        <label for="final">Enter your Final Grade:</label>
        <input type="text" id="final" name="final">
        
        <button type="submit" name="calculate_required">Calculate Required Grades</button>
        <button type="submit" name="result_total">Result Total</button>

        http://127.0.0.1:5500/
