from flask import Flask, request, jsonify

app = Flask(__name__)

# This function runs before each request
@app.before_request
def log_request_info():
    print(f'Request URL: {request.url}')
    print(f'Request Method: {request.method}')
    print(f'Request Headers: {request.headers}')
    print(f'Request Body: {request.get_data()}')

@app.route('/connect', methods=['POST'])
def log_post_request():
    # Get the JSON data from the request
    data = request.get_json()
    
    # # Print the data to the console (log)
    # print(data)
    
    # ###You can also log it to a file if you prefer
    # with open('log.txt', 'a') as f:
    #     f.write(str(data) + '\n')
    
    # Return a response
    # return 'Received and logged the POST request successfully!', 200
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
