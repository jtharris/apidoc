from app import app

if __name__ == "__main__":
    # Dev mode
    app.run(host='0.0.0.0', port=5000, debug=True)
