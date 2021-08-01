from flask import Blueprint,render_template, request, flash

index = Blueprint('index',__name__)

@index.route('/', methods=['GET', 'POST'])
def start():
    return render_template('_BAK_.html')