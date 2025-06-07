from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sys


def printCustmessage(status_code: int, status: str, message: str, data=None):
    response = {
        'code': status_code,
        'status': status,
        'message': message
    }
    if data is None:
        response['data'] = data
    return JSONResponse(status_code=status_code, content=response)

def line_error_details(e: Exception):
    exc_type, exc_obj, tb = sys.exc_info()
    filename = tb.tb_frame.f_code.co_filename
    line_number = tb.tb_lineno
    error_message = f"{type(e).__name__}: {str(e)}"

    return {
        "error": error_message,
        "file": filename,
        "line": line_number
    }