import logging
import weewx
import weewx.engine

log = logging.getLogger(__name__)

log.info("ArchiveListenerService running...")

class ArchiveListenerService(weewx.engine.StdService):

    def __init__(self, engine, config_dict):

        super(ArchiveListenerService, self).__init__(engine, config_dict)

        self.bind(weewx.NEW_ARCHIVE_RECORD, self.handle_archive_record)

    def handle_archive_record(self, event):

        record = event.record

        try:
            log.info(f"New archive record! {record}")
        except Exception as e:
            log.info(f"Error! e: {str(e)}")
