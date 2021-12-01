import logging


class ImagrLogFilter(logging.Filter):
    """
    Very rudimentary filter that discards empty (or invalid) lines
    """
    def filter(self, record):

        record.message = getattr(record, "msg", "")
        if record.message in [""]:
            return 0

        record.serial_number = str(getattr(record, "serial_number", ""))
        if record.serial_number.strip() in [""]:
            return 0

        # If none of the above apply, clean the message...
        record.message = record.message.replace("\n", " ")
        record.message = record.message.replace("\r", " ")
        record.message = record.message.replace("\t", " ")
        record.message = record.message.strip()

        # ...and pass it through
        return 1