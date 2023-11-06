import json
import random
import re
import math

with open('intents.json', 'r') as f:
    intents = json.load(f)

def get_response(predicted_tag, user_input):
    response = "test"

    if predicted_tag == 'addition':
        # Perform addition
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = number1 + number2

            for intent in intents['intents']:
                if intent['tag'] == 'addition':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1, number2, result)
                    return response
        return "Sorry, I couldn't extract two numbers for addition."


    elif predicted_tag == 'subtraction':
        # Perform subtraction
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = number1 - number2
            for intent in intents['intents']:
                if intent['tag'] == 'subtraction':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(result)
                    return response
        return "Sorry, I couldn't extract two numbers for subtraction."

    elif predicted_tag == 'multiplication':
        # Perform multiplication
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = number1 * number2
            for intent in intents['intents']:
                if intent['tag'] == 'multiplication':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(result)
                    return response
        return "Sorry, I couldn't extract two numbers for multiplication."

    elif predicted_tag == 'division':
        # Perform division
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            if number2 != 0:
                result = number1 / number2
                for intent in intents['intents']:
                    if intent['tag'] == 'division':
                        responses = intent['responses']
                        reply = random.choice(responses)
                        response = reply.format(number1,number2,result)
                        return response
                return "Sorry, division by zero is not possible."

        return "Sorry, I couldn't extract two numbers for division."

    elif predicted_tag == 'convert_celsius_to_fahrenheit':
        # Perform Celsius to Fahrenheit conversion
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = round((number1 * 9/5) + 32, 2)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_celsius_to_fahrenheit':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response

        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_fahrenheit_to_celsius':
        # Perform Fahrenheit to Celsius conversion
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = round((number1 - 32) * 5/9, 2)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_fahrenheit_to_celsius':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response

        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_fahrenheit_to_celsius':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = round((number1*5/9)-32, 2)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_fahrenheit_to_celsius':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_celsius_to_kelvin':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = round(number1 + 273.15, 2)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_celsius_to_kelvin':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_kelvin_to_celsius':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = round(number1-273.15, 2)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_kelvin_to_celsius':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_fahrenheit_to_kelvin':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = float(numbers[0])
            result = (number1 + 459.67) * (5 / 9)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_fahrenheit_to_kelvin':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the Fahrenheit temperature for conversion."

    elif predicted_tag == 'convert_kelvin_to_fahrenheit':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = float(numbers[0])
            result = (number1 * (9 / 5)) - 459.67
            for intent in intents['intents']:
                if intent['tag'] == 'convert_kelvin_to_fahrenheit':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the Kelvin temperature for conversion."

    elif predicted_tag == 'convert_miles_to_kilometers':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = round(number1 * 1.60934, 2)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_miles_to_kilometers':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."


    elif predicted_tag == 'convert_kilometers_to_miles':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = round(number1 / 1.60934, 2)
            for intent in intents['intents']:
                if intent['tag'] == 'convert_kilometers_to_miles':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response

        return "Sorry, I couldn't extract a number for the conversion."


    elif predicted_tag == 'calculate_bmi':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = round(number1 / (number2 ** 2), 2)
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_bmi':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,number2,result)
                    return response
        return "Sorry, I couldn't extract weight and height for BMI calculation."

    elif predicted_tag == 'convert_hours_to_seconds':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1*3600
            for intent in intents['intents']:
                if intent['tag'] == 'convert_hours_to_seconds':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response  
        return ("Sorry, I couldn't extract a number for the conversion.")


    elif predicted_tag == 'convert_hours_to_minutes':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1*60
            for intent in intents['intents']:
                if intent['tag'] == 'convert_hours_to_minutes':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."


    elif predicted_tag == 'convert_seconds_to_hours':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1/3600
            for intent in intents['intents']:
                if intent['tag'] == 'convert_seconds_to_hours':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_seconds_to_minutes':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1/60
            for intent in intents['intents']:
                if intent['tag'] == 'convert_seconds_to_minutes':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."
    

    elif predicted_tag == 'convert_minutes_to_hours':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1/60
            for intent in intents['intents']:
                if intent['tag'] == 'convert_minutes_to_hours':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."
    

    elif predicted_tag == 'convert_minutes_to_seconds':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result =number1*60
            for intent in intents['intents']:
                if intent['tag'] == 'convert_minutes_to_seconds':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."
    
    elif predicted_tag == 'convert_kg_to_g':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1 * 1000
            for intent in intents['intents']:
                if intent['tag'] == 'convert_kg_to_g':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_g_to_kg':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1 / 1000
            for intent in intents['intents']:
                if intent['tag'] == 'convert_g_to_kg':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_t_to_kg':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1 * 1000
            for intent in intents['intents']:
                if intent['tag'] == 'convert_t_to_kg':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_kg_to_t':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1 / 1000
            for intent in intents['intents']:
                if intent['tag'] == 'convert_kg_to_t':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_t_to_g':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1 * 1000000
            for intent in intents['intents']:
                if intent['tag'] == 'convert_t_to_g':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'convert_g_to_t':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1 / 1000000
            for intent in intents['intents']:
                if intent['tag'] == 'convert_g_to_t':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract a number for the conversion."

    elif predicted_tag == 'calculate_square_perimeter':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = 4 * number1
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_square_perimeter':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
            response = "Sorry, I couldn't extract the side length of the square."

    elif predicted_tag == 'calculate_square_area':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = number1 ** 2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_square_area':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the side length of the square."

    elif predicted_tag == 'calculate_rectangle_perimeter':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = 2 * (number1 + number2)
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_rectangle_perimeter':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,number2,result)
                    return response
        return "Sorry, I couldn't extract the length and width of the rectangle."

    elif predicted_tag == 'calculate_rectangle_area':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = number1 * number2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_rectangle_area':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,number2,result)
                    return response
        return "Sorry, I couldn't extract the length and width of the rectangle."

    elif predicted_tag == 'calculate_triangle_area':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = 0.5 * number1 * number2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_triangle_area':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,number2,result)
                    return response
        return "Sorry, I couldn't extract the base and height of the triangle."

    elif predicted_tag == 'calculate_triangle_perimeter':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 3:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            number3 = int(numbers[2])
            perimeter = side1 + side2 + side3
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_triangle_perimeter':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,number2,number3,result)
                    return response
        return "Sorry, I couldn't extract the lengths of the triangle sides."

    elif predicted_tag == 'calculate_circle_area':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = 3.14159 * number1**2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_circle_area':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the radius of the circle."

    
    elif predicted_tag == 'calculate_circle_perimeter':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = int(numbers[0])
            result = 2 * 3.14159 * number1
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_circle_perimeter':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the radius of the circle."

    elif predicted_tag == 'calculate_parallelogram_area':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            result = number1 * number2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_parallelogram_area':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(result)
                    return response
        return "Sorry, I couldn't extract the base and height of the parallelogram."

    elif predicted_tag == 'calculate_parallelogram_perimeter':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            perimeter = 2 * (side1 + side2)
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_parallelogram_perimeter':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response = reply.format(result)
                    return response
        return "Sorry, I couldn't extract the side lengths of the parallelogram."

    elif predicted_tag == 'calculate_cube_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = float(numbers[0])
            result = number1 ** 3
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_cube_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    response=reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the side length of the cube for volume calculation."

    elif predicted_tag == 'calculate_cuboid_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 3:
            number1 = float(numbers[0])
            number2 = float(numbers[1])
            number3 = float(numbers[2])
            result = number1 * number2 * number3
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_cuboid_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,number2,number3,result)
                    return response
        return "Sorry, I couldn't extract the dimensions of the cuboid for volume calculation."

    elif predicted_tag == 'calculate_cone_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = float(numbers[0])
            number2 = float(numbers[1])
            result = (1/3) * math.pi * number1**2 * number2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_cone_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,number2,result)
                    return response
        return "Sorry, I couldn't extract the dimensions of the cone for volume calculation."

    elif predicted_tag == 'calculate_cylinder_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = float(numbers[0])
            number2 = float(numbers[1])
            result = math.pi * number1**2 * number2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_cylinder_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,number2,result)
                    return response
        return "Sorry, I couldn't extract the dimensions of the cylinder for volume calculation."

    elif predicted_tag == 'calculate_sphere_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = float(numbers[0])
            result = (4/3) * math.pi * radius**3
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_sphere_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the radius of the sphere for volume calculation."

    elif predicted_tag == 'calculate_frustum_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 3:
            number1 = float(numbers[0])
            number2 = float(numbers[1])
            number3 = float(numbers[2])
            result= (1/3) * math.pi * number1 * (number2**2 + number3**2 + radius1*radius2)
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_frustum_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,number2,number3,result)
                    return response
        return "Sorry, I couldn't extract the necessary dimensions for frustum volume calculation."

    elif predicted_tag == 'calculate_prism_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 2:
            number1 = float(numbers[0])
            number2 = float(numbers[1])
            result = number1 * number2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_prism_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,number2,result)
                    return response
        return "Sorry, I couldn't extract the necessary dimensions for prism volume calculation."


    elif predicted_tag == 'calculate_pyramid_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 3:
            number1 = float(numbers[0])
            number2 = float(numbers[1])
            result = (number1*number2) / 3
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_pyramid_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,number2,result)
                    return response
            return "Sorry, I couldn't extract the necessary dimensions for pyramid volume calculation."

    elif predicted_tag == 'calculate_hemisphere_volume':
        numbers = re.findall(r'[0-9]+', user_input)
        if len(numbers) >= 1:
            number1 = float(numbers[0])
            result = (4/3) * math.pi * (number1 ** 3) / 2
            for intent in intents['intents']:
                if intent['tag'] == 'calculate_hemisphere_volume':
                    responses = intent['responses']
                    reply = random.choice(responses)
                    sentence = random.choice(responses)
                    response=reply.format(number1,result)
                    return response
        return "Sorry, I couldn't extract the necessary dimensions for hemisphere volume calculation."


    else:
        for intent in intents['intents']:
            if intent['tag'] == predicted_tag:
                responses = intent['responses']
                response = random.choice(responses)
                break
#
    return response

