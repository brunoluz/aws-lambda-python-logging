import json
import uuid
import logs


def lambda_handler(event, context):
    context.order = 0
    context.correlationId = uuid.uuid4()

    logs.info(context, "teste")
    logs.warning(context, "teste")
    logs.error(context, "teste")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
