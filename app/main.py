from config import app, logging
import router
import api

if __name__ == '__main__':
    logging.info('Starting application')
    app.run(debug=True)
