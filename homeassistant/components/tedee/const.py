"""Constants for the Tedee integration."""

from datetime import timedelta

DOMAIN = "tedee"
NAME = "Tedee"

SCAN_INTERVAL = timedelta(seconds=10)

CONF_LOCAL_ACCESS_TOKEN = "local_access_token"

# API Token Mode
CONF_API_TOKEN_MODE = "api_token_mode"
API_TOKEN_MODE_SECURE = "secure"
API_TOKEN_MODE_PLAIN = "plain"
