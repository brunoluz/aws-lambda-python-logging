from lambda_local.context import Context
from lambda_local.main import call
import lambda_function

if __name__ == '__main__':
    event = {
        "answer": 42
    }
    context = Context(99999)
    call(lambda_function.lambda_handler, event, context)
