from flask import Flask, request, jsonify
# Necessary to import Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
from flask_cors import CORS 
from addHours import add_hours

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['GET'])
def total_hours():
    items = [request.args.get(f'item_{i}') for i in range(1, 5)]
    attendances = [request.args.get(f'attendance_{i}', 0) for i in range(1, 5)]
    total_hours = [request.args.get(f'total_hours_{i}', 0) for i in range(1, 5)]

    # Check if any session names are empty
    for item in items:
        if not item:
            return jsonify({"error": True, "message": "Item names cannot be empty."}), 400

    for i in range(len(attendances)):
        attendance = attendances[i]
        total_assigned_hours = total_hours[i]  # Get the corresponding total hours

        # Check that the user has entered an int for every attentance value
        try:
            attendance = int(attendance)
        except ValueError:
            return jsonify({"error": True, "message": "Attendance hours must be integers."}), 400
        
        # Check that all the total hours have been entered in code correctly
        try:
            total_assigned_hours = int(total_assigned_hours)
        except ValueError:
            return jsonify({"error": True, "message": "A valid number for total hours has not been entered in the frontend code."}), 400

        # Check if attendance is non-negative
        if attendance < 0:
            return jsonify({"error": True, "message": "Attendance hours cannot be negative."}), 400

        # Check if total hours is non-negative
        if total_assigned_hours < 0:
            return jsonify({"error": True, "message": "Total hours cannot be negative."}), 400
        
        # Check if attendance is within an acceptable range
        if attendance > total_assigned_hours:
            return jsonify({"error": True, "message": "Attendance hours cannot exceed total assigned hours."}), 400


    # Compute the total
    total = add_hours(attendances)

    # Add the total or any other required information to the response
    return jsonify({'total_hours': total})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8003)