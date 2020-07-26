import os


MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", "10"))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", "10"))

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
