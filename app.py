from flask import Flask, render_template,request, flash

# instantiate the app
app =  Flask(__name__)
app.config['SECRET_KEY'] = 'whatever!'

# index route
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # get the form values
        field1 = request.form['field1']
        field2 = request.form['field2']
        field3 = request.form['field3']
        field4 = request.form['field4']

        # Old way i do messaging 
        '''if field1 and field2 and field3 and field4:
            message = 'Fields validated!'
            css_class = 'alert alert-success'
        else:
            message = 'All fields required!'
            css_class = 'alert alert-danger'''

        if not field1: # field1 == ''
            flash(u'Field 1 is required!', 'alert alert-danger')
        else:
            flash(u'Field 1 is valid!', 'alert alert-success')
        
        if not field2: # field2 == ''
            flash(u'Field 2 is required!', 'alert alert-danger')
        else:
            flash(u'Field 2 is valid!', 'alert alert-success')
        
        if not field3: # field3 == ''
            flash(u'Field 3 is required!', 'alert alert-danger')
        else:
            flash(u'Field 3 is valid!', 'alert alert-success')

        if not field4: # field4 == ''
            flash(u'Field 4 is required!', 'alert alert-danger')
        else:
            flash(u'Field 4 is valid!', 'alert alert-success')

        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
