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
