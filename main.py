from trail_app import create_app
from trail_app.data_ingest import load_data

app = create_app()

load_data.get_first_image()
