def lambda_handler(event, context):
    """Adds two numbers"""

    x = event['x']
    y = event['y']
    z = event['z']
    add = x+y+z
    print(f"The total of x:{x} and y:{y} and z:{z} == {add}")
    return {
        "Total": add,
    }