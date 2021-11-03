import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = jsonlogger.JsonFormatter()
logger.handlers[0].setFormatter(formatter)


def info(context, msg):
    context.order += 1
    logger.info(msg, extra={'level': 'INFO', 'correlationId': context.correlationId, 'order': context.order})


def warning(context, msg):
    context.order += 1
    logger.warning(msg, extra={'level': 'WARN', 'correlationId': context.correlationId, 'order': context.order})


def error(context, msg):
    context.order += 1
    logger.error(msg, extra={'level': 'ERROR', 'correlationId': context.correlationId, 'order': context.order})
