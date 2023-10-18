from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5050, debug=True)

    # # once i'm done with the account creation,
    # i should add the ability to sent a email to
    # the User saying thanks for making an account



    #python 3.11.4
    #sqlalchemy 2.0.21
    #flask_sqlalchemy 3.1.1
    #Flask 3.0.0
    #Flask-Login 0.6.2
    #Werkzeug 2.3.7
    #jinja2 3.1.2