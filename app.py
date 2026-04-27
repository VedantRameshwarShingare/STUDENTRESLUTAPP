from flask import Flask, request, render_template_string

app = Flask(__name__)

page = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Result App</title>
    <style>
        body{
            font-family: Arial;
            text-align:center;
            margin-top:50px;
            background:#f2f2f2;
        }
        .box{
            background:white;
            width:400px;
            margin:auto;
            padding:30px;
            border-radius:10px;
            box-shadow:0 0 10px gray;
        }
        input{
            padding:10px;
            width:80%;
            margin:10px;
        }
        button{
            padding:10px 20px;
            background:green;
            color:white;
            border:none;
        }
    </style>
</head>
<body>

<div class="box">
<h2>Student Result System</h2>

<form method="POST">
<input type="text" name="name" placeholder="Enter Name" required><br>
<input type="number" name="marks" placeholder="Enter Marks" required><br>
<button type="submit">Check Result</button>
</form>

{% if result %}
<h3>{{ result }}</h3>
{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    result = ""

    if request.method == "POST":
        name = request.form["name"]
        marks = int(request.form["marks"])

        if marks >= 40:
            result = f"{name} is PASS "
        else:
            result = f"{name} is FAIL "

    return render_template_string(page, result=result)

if __name__ == "__main__":
    app.run(debug=True)