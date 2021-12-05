def generate_integers():
    # validate user input
    error_message = {
        'not_integers': 'Sorry, Please input integer only.',
        'not_increasing': 'Sorry, the sequence of integers is not increasing.',
    }

    integers = input('Please enter increasing integers separated by spaces:\n')
    integer_list = integers.split()

    try:
        integer_list = [int(item) for item in integer_list]
    except:
        raise Exception(error_message['not_integers'])

    # init
    number_of_generated_integers = 10
    generated_integers = []
    result_message = f'the next {number_of_generated_integers} integers:\n'

    # find the pattern
    difference = []
    quotient_remainder_pairs = []

    for i in range(1, len(integer_list)):
        prev = integer_list[i - 1]
        current = integer_list[i]

        if current < prev:
            raise Exception(error_message['not_increasing'])

        difference.append(current - prev)
        quotient_remainder_pairs.append(divmod(current, prev))

    # pattern: arithmetic sequence
    if len(set(difference)) == 1:
        def append_next_number(prev):
            generated_integers.append((prev + difference[0]))
            return

        append_next_number(integer_list[-1])

        for i in range(number_of_generated_integers - 1):
            append_next_number(generated_integers[-1])

    # pattern: geometric sequence like
    elif len(set(quotient_remainder_pairs)) == 1:
        q, r = quotient_remainder_pairs[0]

        def append_next_number(prev):
            generated_integers.append(prev * q + r)
            return

        append_next_number(integer_list[-1])

        for i in range(number_of_generated_integers - 1):
            append_next_number(generated_integers[-1])

    if generated_integers:
        result_message += ' '.join([str(num) for num in generated_integers])
    else:
        result_message = 'Sorry, I cannot recognize the pattern of the sequence.'
    return result_message


try:
    print(generate_integers())
except Exception as e:
    print(e)
