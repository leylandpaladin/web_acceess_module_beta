from flask import Blueprint,render_template, request, flash
profile = Blueprint('profile',__name__)

@profile.route('/', methods=['GET', 'POST'])
def user_profile():
    return render_template('profile.html')