from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pets
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Initialize SQLAlchemy with your app
db.init_app(app)

# Initialize DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route("/")
def homepage():
    """Homepage to redirect """
    pets = Pets.query.all()

    return render_template('index.html', pets = pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        """Creat new pet object from form data"""
        new_pet = Pets(
            name= form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
            available = form.available.data
        )


        db.session.add(new_pet)
        db.session.commit()

        return redirect(url_for('homepage'))

    return render_template('add_pet.html', form = form)


@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def view_and_edit_pet(pet_id):
    # Query the database to get the pet based on ID
    pet = Pets.query.get_or_404(pet_id)
    # Create an instance of the EditPetForm and populate
    form = EditPetForm(obj = pet)

    if form.validate_on_submit():
        #Update the pet's data based on the form
        form.populate_obj(pet)

        #Commit the changes to the database
        db.session.commit()

        #Redirect back to the pet's detail  page
        return redirect(url_for('view_and_edit_pet', pet_id = pet_id))

        return render_template('view_and_edit_pet.html', pet=pet, form=form)


if __name__ == '__main__':
    app.run(debug=True)