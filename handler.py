import csv
import json
import six


## Suggestion : use Six library for cross compatibility
## Don't change the method name.. This is very important for the process
def calc_method(request):
    """Method that just calculates and thats all"""

    type = request.content_type

    data = request.data.decode('utf-8')
    s = six.StringIO(data)

    input_data = None
    output_data = None

    if type == 'text/csv':
        input_data = csv.reader(s.getvalue().splitlines(), delimiter=',')
        output_data = [row[0].upper() for row in input_data]

    elif type == 'application/json':
        input_data = request.json

        output_data = [row["Name"].upper() for row in input_data]

        print(input_data)

    body = {
        "input": s.getvalue().splitlines(),
        "output": output_data
    }

    responsex = {
        "statusCode": 200,
        "mimetype": type,
        "response": json.dumps(body)
    }

    return responsex
