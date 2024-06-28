from app import app

if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=8085, debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
