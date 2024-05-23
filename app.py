from navigator import FlightGraph,WeatherFetcher
from flask import Flask, request, jsonify




app=Flask(__name__)

@app.route('/shortest_path', methods=['GET','POST'])
def get_shortest_path():
    start_airport = request.args.get('start')
    end_airport = request.args.get('end')

    if not all([start_airport, end_airport]):
        return jsonify({"error": "Please provide start, end, and weather_api_key parameters"}), 400
    
    try:
        # flight_graph = FlightGraph()
        # flight_graph.load_coordinates()
        # flight_graph.load_flights()
        flight_graph.update_weights_based_on_weather(start_airport,end_airport)
        route = flight_graph.find_shortest_path(start_airport, end_airport)
        print(route)
        return jsonify({"route": route})
    
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

@app.route("/")
def test():

    return 'this is working'


if __name__ == "__main__":

    flight_graph = FlightGraph()
    flight_graph.load_coordinates()
    flight_graph.load_flights()

    app.run(debug=True)