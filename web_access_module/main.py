from web import create_app


app = create_app()

if __name__ == '__main__':

    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True,
            host="0.0.0.0")



