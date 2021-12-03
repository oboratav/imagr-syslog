import logging
import logging.handlers

import falcon

from imagr_syslog import settings

logging.config.dictConfig(settings.LOGGING_CONFIG)

logger = logging.getLogger(__name__)

class ImagrReportLine:
    def on_post(self, req, resp):
        """
        Handles POST requests from Imagr

        """
        # Get the data from the request
        data = {
            "serial_number": req.get_param("serial", ""),
            "status": req.get_param("status", ""),
            "hostname": req.get_param("hostname", ""),
        }
        # If there's no serial number, discard the request
        if data["serial_number"] != "":
            # Send the data to log handler
            logger.log(settings.LOG_LEVEL, req.get_param("message"), extra=data)

        # Return a response
        resp.status = falcon.HTTP_200


application = falcon.App()
application.req_options.auto_parse_form_urlencoded = True

application.add_route('/', ImagrReportLine())