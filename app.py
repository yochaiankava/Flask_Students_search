from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = [
    {"name": "John Doe", "phone": "1234567890"},
    {"name": "Jane Smith", "phone": "9876543210"},
    {"name": "Michael Johnson", "phone": "5555555555"}
]

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "yochai" and password == "123":
            return redirect("/students")
        else:
            error_message = "LOGIN ERROR. Please try again."
            return render_template('login.html', error_message=error_message)
    
    return render_template('login.html')

@app.route("/students", methods=['GET', 'POST'])
def view_students():
    if request.method == 'POST':
        search_name = request.form.get("search_name")
        results = [student for student in students if search_name.lower() in student["name"].lower()]
        return render_template('students.html', students=results, search_name=search_name)
    
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)


# check commit