from navigator import FlightGraph
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

global flight_graph

app=Flask(__name__)
cors = CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/shortest_path', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def get_shortest_path():
    
    try:
        start_airport = request.args.get('start')
        end_airport = request.args.get('end')
        print(start_airport,end_airport)
        if not all([start_airport, end_airport]):
            return jsonify({"error": "Please provide start and end parameters"})
        
        # if not FlightGraph.get_coordinates(val=start_airport) or not FlightGraph.get_coordinates(val=end_airport):
        #     return jsonify({f"error": "No path found between {start_airport} and {end_airport}"})

        # flight_graph = FlightGraph()
        # flight_graph.load_coordinates()
        # flight_graph.load_flights()
        flight_graph.update_weights_based_on_weather(start_airport,end_airport)
        route = flight_graph.find_shortest_path(start_airport, end_airport)
        if not route:
            return jsonify({"error": f"No path found between {start_airport} and {end_airport}"})
        print(route)

        return jsonify({"route": route})
    
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/")
def test():

    return 'this is working'


if __name__ == "__main__":

    flight_graph = FlightGraph()
    flight_graph.load_coordinates()
    flight_graph.load_flights()

    app.run(debug=True,host="0.0.0.0",port=5635,ssl_context=('cert.pem','key.pem'))