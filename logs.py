import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = jsonlogger.JsonFormatter()
logger.handlers[0].setFormatter(formatter)

TIME_FORMAT = '%Y/%m/%d %H:%M:%S.%f'


def info(context, msg):
    context.order += 1
    logger.info(msg, extra={'level': 'INFO', 'correlationId': context.correlationId, 'order': context.order,
                            'datetime': datetime.now().strftime(TIME_FORMAT)})


def warning(context, msg):
    context.order += 1
    logger.warning(msg, extra={'level': 'WARN', 'correlationId': context.correlationId, 'order': context.order,
                               'datetime': datetime.now().strftime(TIME_FORMAT)})


def error(context, msg):
    context.order += 1
    logger.error(msg, extra={'level': 'ERROR', 'correlationId': context.correlationId, 'order': context.order,
                             'datetime': datetime.now().strftime(TIME_FORMAT)})
