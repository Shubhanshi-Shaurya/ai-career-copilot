from flask import Flask,render_template,redirect,request,session
from db import Base,engine,session_local
import models
import PyPDF2
import docx
import json
from ai import analyze_resume


app=Flask(__name__)

Base.metadata.create_all(bind=engine)

#HOME 
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# sign up 
@app.route("/signup",methods=['POST','GET'])
def signup():
    db=session_local()

    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        existing_user=db.query(models.User).filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        user=models.User(email=email,password=password)
        db.add(user)
        db.commit()

        return redirect("/login")

    return render_template("signup.html")

# login
@app.route("/login",methods=['POST','GET'])
def login():
    db=session_local()

    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        user=db.query(models.User).filter_by(email=email,password=password).first()

        if user :
            session["user"]=user.email
            return redirect("/dashboard")
        else :
            return "Invalid Credentials"

    return render_template("login.html")


# dashboard 
@app.route("/dashboard",methods=['POST','GET'])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    result=None

    if request.method=='POST':
        user_goal=request.form.get("role")
        resume_text=request.form.get("resume") 

        file=request.files.get("file")

        # file handling
        if file and file.name!="":
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader=PyPDF2.PdfReader(file)
                    text=""
                    for page in pdf_reader.pages:
                        text+=page.extract_text() or ""
                    resume_text=text
                except Exception as e:
                    result={"error ":f"{e}"}
            elif file.filename.endswith(".docx"):
                try:
                    doc=docx.Document(file)
                    text=""
                    for para in doc.paragraphs:
                        text+=para.text+"\n"
                    resume_text=text
                except Exception as e:
                    result={"error ":f"{e}"}

        if resume_text and user_goal and not result:
            try:
                result=analyze_resume(resume_text,user_goal)

                db=session_local()
                user=db.query(models.User).filter_by(email=session["user"]).first()

                report=models.Reports(
                    user_id=user.id,
                    resume_text=resume_text,
                    result=json.dumps(result)
                )

                db.add(report)
                db.commit()
            except Exception as e:
                result={"error":f"ai error : {e}"}

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=result
    )

 
# history
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    db=session_local()
    user=db.query(models.User).filter_by(email=session["user"]).first()

    reports=db.query(models.Reports).filter_by(user_id=user.id).all()

    past_report=[]
    for r in reports:
        try:
            past_result=json.loads(r.result)
        except Exception as e:
            past_result=[]

        past_report.append({
            "resume":r.resume_text,
            "result":past_result
        })

    return render_template("history.html",reports=past_report)

# logout 
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/login")

if __name__=="__main__":
    app.run(debug=True,port=5000)
