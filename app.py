from flask import Flask

app = Flask(__name__)

# Routes go here

if __name__ == '__main__':
    app.run()


@app.route('/')
def home():
    return 'Welcome to the Flask application!'

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

@app.route('/farewell/<username>')
def farewell(username):
    return f'Goodbye, {username}!'


entries = {}

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        entries[key] = value
        return f'Entry created: {key} - {value}'
    else:
        return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key">
            <label for="value">Value:</label>
            <input type="text" id="value" name="value">
            <input type="submit" value="Create">
        </form>
        '''

@app.route('/read')
def read():
    return str(entries)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in entries:
            entries[key] = value
            return f'Entry updated: {key} - {value}'
        else:
            return f'Entry not found: {key}'
    else:
        return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key">
            <label for="value">Value:</label>
            <input type="text" id="value" name="value">
            <input type="submit" value="Update">
        </form>
        '''

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in entries:
            del entries[key]
            return f'Entry deleted: {key}'
        else:
            return f'Entry not found: {key}'
    else:
        return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key">
            <input type="submit" value="Delete">
        </form>
        '''

