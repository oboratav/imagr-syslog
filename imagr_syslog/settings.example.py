LOG_LEVEL = 30

LOGGER_NAME = "imagr_syslog"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "ImagrLogFilter": {
            "()": "imagr_syslog.utils.ImagrLogFilter",
        },
    },
    "handlers": {
        "graylog": {
            "class": "pygelf.GelfTcpHandler",
            "filters": ["ImagrLogFilter"],
            "formatter": "gelf",
            "host": "graylog-instance.example.ca",
            "port": 12201,
            "include_extra_fields": True,
            "chunk_size": 1300,
            "compress": True,
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "filters": ["ImagrLogFilter"],
        }
    },
    "formatters": {
        "gelf": {
            "()": "gelfformatter.GelfFormatter",
            # "format": "{levelname} {asctime} {name} {message}",
        },
        "verbose": {
            "format": "{levelname} {asctime} {name} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {name} {message}",
            "style": "{",
        },
    },
    "loggers": {
        "imagr_syslog.server": {
            "handlers": ["console", "graylog"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}