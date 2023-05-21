from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"asdfsafsg346345F4Q8z\n\xec]/'

students = [
    {"name": "John Doe", "phone": "1234567890"},
    {"name": "Jane Smith", "phone": "9876543210"},
    {"name": "Michael Johnson", "phone": "5555555555"}
]


@app.route("/", methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        color = request.form.get("color")
        print(f"user:{username}, password:{password}. color:{color}")
        if username == "yochai" and password == "123":
            session["logged_in_user"] = username
            session["color"] = color
            return redirect("/students")
        else:
            message = "Error in login"              
    return render_template('login.html', error_message=message)

@app.route("/students", methods=['GET', 'POST'])
def view_students():
    if not session.get("logged_in_user"):
    # check if logged in. if not redirect("/")
        return redirect("/")
    return render_template("students.html", students = students, logged_in_user = session.get("logged_in_user"))

    # if request.method == 'POST':
    #     search_name = request.form.get("search_name")
    #     print({search_name})
    #     results = [student for student in students if search_name.lower() in student["name"].lower()]
    #     return render_template('students.html', students=results, search_name=search_name)
    
    # return render_template('students.html', students=students)
@app.route("/search")
def search():
    search = request.args.get("search")
    phone = request.args.get("phone")
    #color = request.args.get("color")
    new_list = []
    print(f"search-{search} phone-{phone}")
    
    for student in students:
        print(f"student-{student}")        
        if search in student["name"] and phone in student["phone"]:
            new_list.append(student)
    # new_list = [student for student in students(dic) if search in student]   
    print(f"new_list-{new_list}")
    return render_template("students.html", students = new_list, logged_in_user=session.get("logged_in_user"), color=session.get("color"))

@app.route("/logout")
def logout():
    session.clear()
    #session["logged_in_user"] = ""
    return redirect("/")
    
@app.errorhandler(404)
def page_not_found(error):
    # Custom logic for handling 404 errors
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)


# check