from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps', validators=[DataRequired(), URL()])
    open = StringField(label='Opening Time(eg: 10AM)', validators=[DataRequired()])
    close = StringField(label='Closing Time(eg: 4PM)', validators=[DataRequired()])
    kopi_choices = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
    coffee_rate =  SelectField(label='Coffee Rating', choices=kopi_choices, validators=[DataRequired()])
    wifi_choices = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
    wifi = SelectField(label='Wifi Rating', choices=wifi_choices, validators=[DataRequired()])
    psa = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
    ps_avail = SelectField(label='Power Socket Availability', choices=psa, validators=[DataRequired()])
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(f"{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{form.coffee_rate.data},{form.wifi.data},{form.ps_avail.data}")
        with open('cafe-data.csv', "a", newline='') as csv_file:
            row = f"\n{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{form.coffee_rate.data},{form.wifi.data},{form.ps_avail.data}"
            csv_file.write(row)
            csv_file.close()
        return redirect(url_for("cafes"))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
