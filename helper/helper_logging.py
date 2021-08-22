import yaml
import logging.config
import variables_global


class SeleniumEasyLogging:
    config_file = open(variables_global.STR_CONFIG_FILE, 'r', encoding="utf-8")
    logging.config.dictConfig(yaml.load(config_file, Loader=yaml.FullLoader))
    config_file.close()

    def loggingInit(self, logger_name):
        """
        Init logger
        """
        logger = logging.getLogger(logger_name)
        logger.debug(f'Set logger \'{logger_name}\'.')
        return logger
