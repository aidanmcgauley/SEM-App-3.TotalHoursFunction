from flask import Flask, request, jsonify
# Necessary to import Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

@app.route('/old', methods=['GET'])
def total_hoursOld():

    # Zero returned as default value if no value provided for attendance
    attendance_1 = int(request.args.get('attendance_1', 0))
    attendance_2 = int(request.args.get('attendance_2', 0))
    attendance_3 = int(request.args.get('attendance_3', 0))
    attendance_4 = int(request.args.get('attendance_4', 0))
    
    total = attendance_1 + attendance_2 + attendance_3 + attendance_4
    
    return jsonify({'total_hours': total})


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

        try:
            attendance = int(attendance)
            total_assigned_hours = int(total_assigned_hours)
        except ValueError:
            return jsonify({"error": True, "message": "Attendance hours and total hours must be integers."}), 400

        # Check if attendance is within an acceptable range
        if attendance > total_assigned_hours:
            return jsonify({"error": True, "message": "Attendance hours cannot exceed total assigned hours."}), 400

        # Check if attendance is non-negative
        if attendance < 0:
            return jsonify({"error": True, "message": "Attendance hours cannot be negative."}), 400

        # Check if total hours is non-negative
        if total_assigned_hours < 0:
            return jsonify({"error": True, "message": "Total hours cannot be negative."}), 400

    # Compute the total
    total = sum([int(attendance) for attendance in attendances])

    # You can add the sorted attendance or any other required information to the response
    return jsonify({'total_hours': total})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8003)