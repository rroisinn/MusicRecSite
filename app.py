#admin log in to access /admin 
#user id = admin
#password = 1234
from flask import Flask, render_template, request, make_response, redirect, url_for, session, g
from database import get_db, close_db
from forms import ArtistForm, RecommendationForm, RegistrationForm, LoginForm, MailForm, AddArtistForm
from flask_session import Session
from sqlite3 import IntegrityError
from werkzeug.security import generate_password_hash,  check_password_hash
from functools import wraps


app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"]= "filesystem"
Session(app)

@app.before_request
def load_logged_in_user():
    g.user= session.get("user_id", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("login"))
        return view(**kwargs)
    return wrapped_view

def admin_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user != "admin":
            return redirect(url_for("login"))
        if g.user is None:
            return redirect(url_for("login"))
        
        return view(**kwargs)
    return wrapped_view

@app.route("/")
def index():
    
    return render_template("index.html")





@app.route("/find_new_artists", methods=["GET", "POST"])
@login_required
def find_new_artists():
    
    
    return render_template("find_new_artist.html")

@app.route("/artists/<int:artist_id>", methods=["GET", "POST"])
@login_required
def artists(artist_id):
    form= ArtistForm()
    
    db = get_db()
    
    number=artist_id
    new_artist=None
    artist= db.execute("""SELECT * FROM music WHERE artist_id=?;""", (artist_id,)).fetchone()
    if number >= 10:
            
        return redirect(url_for("saved_artists"))
    if form.validate_on_submit():
        answer=form.answer.data
        if answer=="Yes":
            
            new_artist=db.execute("""SELECT artist_id FROM music WHERE rec= ?;""", (artist_id,)).fetchall()
            for artist_id in new_artist:
                artist_id=artist_id["artist_id"]
                artist_ids=db.execute("""SELECT artist_id FROM music WHERE artist_id= ?;""", (artist_id,)).fetchone()
            
                for artist_id in artist_ids:
                
                    if "saved_artists" not in session:
                        session["saved_artists"]={}
                    if artist_id not in session["saved_artists"]:
                        session["saved_artists"][artist_id] = 0
                        session["saved_artists"][artist_id] = session["saved_artists"][artist_id] +1
            
            number = number +1
        if answer=="No":
            
            number = number +1
        return redirect(url_for("artists", artist_id=number))
    return render_template("artist.html", artist=artist, form=form,)




       
        
    
@app.route("/saved_artists")
@login_required
def saved_artists():
    if "saved_artists" not in session:
        session["saved_artists"]={}
    names = {}
    songs={}
    links={}
    recs={}
    ids={}
    db = get_db()
    for artist_id in session["saved_artists"]:
        artists= db.execute("""SELECT * FROM music WHERE artist_id=?;""", (artist_id,)).fetchone()
        name=artists["name"]
        names[artist_id]= name
        
        song=artists["song"]
        songs[artist_id]= song

        link=artists["link"]
        links[artist_id]=link

        id=artists["artist_id"]
        ids[artist_id]=id
    return render_template("saved_artists.html", saved_artists=session["saved_artists"], names=names, songs=songs, links=links, ids=ids)

@app.route("/register",methods=["GET", "POST"] )
def register():
    form=RegistrationForm()
    
    if form.validate_on_submit():
        user_id= form.user_id.data
        password= form.password.data
        password2= form.password2.data
        db=get_db()
        matching_user =db.execute("""SELECT * FROM users WHERE  user_id =?;""", (user_id,)).fetchone()
        
        if matching_user:
            form.user_id.errors.append("User id is already taken")
        else:
            db.execute("""INSERT INTO users (user_id, password)
                                VALUES (?, ?)""", (user_id, generate_password_hash(password)))
            db.commit()
            
            return redirect( url_for("login"))
        
    return render_template("register.html", form=form)  

@app.route("/login",methods=["GET", "POST"] )
def login():
    form=LoginForm()
    
    if form.validate_on_submit():
        user_id= form.user_id.data
        password= form.password.data
        db=get_db()
        matching_user =db.execute("""SELECT * FROM users WHERE  user_id =?;""", (user_id,)).fetchone()
        if matching_user is None:#user id not in dictionary
            form.user_id.errors.append("Unknown user id, please register")
        elif not check_password_hash(matching_user["password"],password):#not correct password
            form.user_id.errors.append("Incorrect password")
        else: #if user id is in session store you are logged in
            session.clear()
            session["user_id"]=user_id
            next_page= request.args.get("next")
            if not next_page:
                next_page= url_for("index")
            return redirect(next_page)
    return render_template("login.html", form=form)  

@app.route("/logout",methods=["GET", "POST"] )
def logout():
    session.clear()
    return redirect( url_for("index"))

@app.route("/mailing_list",methods=["GET", "POST"] )
def mailing_list():
    form=MailForm()
    message=""
    if form.validate_on_submit():
        email= form.email.data
        name=form.name.data
        db=get_db()
        matching_user =db.execute("""SELECT * FROM mailinglist WHERE  email =?;""", (email,)).fetchone()
        if matching_user:
            form.email.errors.append("Email has already been used")
        else:
            db.execute("""INSERT INTO mailinglist (name, email)
                                    VALUES (?, ?)""", (name, email))
            db.commit()
            message="You have been added to the mailing list!"
            return render_template("mailing_list.html", form=form, message=message)
        
    return render_template("mailing_list.html", form=form, message=message)  

@app.route("/admin",methods=["GET", "POST"] )
@admin_required
def admin():
    return render_template("admin.html")

@app.route("/all_artists")
@admin_required
def all_artists():
    db = get_db()
    links={}
    artists= db.execute("""SELECT * FROM music;""").fetchall()
    for artist in artists:
        link=artist["link"]
        links[artist]=link
    
    return render_template("all_artists.html", artists=artists, links=links)

@app.route("/add_artist",methods=["GET", "POST"])
@admin_required
def add_artist():
    form=AddArtistForm()
    message=""
    db=get_db()
    artists=  db.execute("""SELECT * FROM music WHERE artist_id < 10""").fetchall()
    if form.validate_on_submit():
        name= form.name.data
        rec= form.rec.data
        song=form.song.data
        link=form.link.data
        
        db=get_db()
        
        conflicting_artist= db.execute("""SELECT * FROM music WHERE name =?""", (name,)).fetchone()
        
        if conflicting_artist is not None:
            form.name.errors.append("Artist already added!")
        else:
            db.execute("""INSERT INTO music (name, rec, song, link)
                                VALUES (?, ?, ?, ?)""", (name, rec, song, link))
            db.commit()
            message= "New artist successfully added!"
    return render_template("add_artist.html", form=form, message=message, artists=artists)  

@app.route("/view_mailinglist")
@admin_required
def view_mailinglist():
    db = get_db()
    emails= db.execute("""SELECT * FROM mailinglist;""").fetchall()
    return render_template("view_mailinglist.html", emails=emails)

@app.route("/view_users")
@admin_required
def view_users():
    db = get_db()
    users= db.execute("""SELECT * FROM users;""").fetchall()
    return render_template("view_users.html", users=users)

@app.route("/recommendations",methods=["GET", "POST"])
@login_required
def recommendations():
    form=RecommendationForm()
    message=""
    if form.validate_on_submit():
        name= form.name.data
        rec= form.rec.data
        db = get_db()
        db.execute("""INSERT INTO recommendations (name, rec)
                                    VALUES (?, ?)""", (name, rec))
        db.commit()
        message="Review successfully added!"
    db = get_db()
    recs=db.execute("""SELECT * FROM recommendations;""").fetchall()
    return render_template("recommendations.html", recs=recs, message=message, form=form)

