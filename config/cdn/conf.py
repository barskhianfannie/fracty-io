import os


AWS_ACCESS_KEY_ID = '73FGTIWNSFK22ASIMWQR'
AWS_SECRET_ACCESS_KEY = 'jfjBwAnCbWpUfCkilCQJzIH78wJg+ZzmAPZUyuCeG/Q'
AWS_STORAGE_BUCKET_NAME = 'db-tokinn'

AWS_S3_ENDPOINT_URL = "https://sfo3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = "https://db-tokinn.sfo3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "config.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "config.cdn.backends.StaticRootS3Boto3Storage"
