from km.constants import (
    DEFAULT_DATABASE_URI,
    DEFAULT_KEYWORD_MODEL_NAME,
    DEFAULT_SERIALIZED_MODELS_DIR,
    DEFAULT_TOPIC_MODEL_NAME,
)


class Config:
    PORT = 5001
    DATABASE_URI = DEFAULT_DATABASE_URI
    SERIALIZED_MODEL_DIR = DEFAULT_SERIALIZED_MODELS_DIR
    SERIALIZED_TOPIC_MODEL_NAME = DEFAULT_TOPIC_MODEL_NAME + ".pkl"
    SERIALIZED_KEYWORD_MODEL_NAME = DEFAULT_KEYWORD_MODEL_NAME + ".pkl"
