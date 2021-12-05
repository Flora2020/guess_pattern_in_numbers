class Find_pattern:
    def __init__(self) -> None:
        self.error_message = {
            'not_integers': 'Error, please enter integer only.',
            'not_increasing': 'Error, please enter increasing sequence.'
        }
        self.origional_integer_list = []
        self.number_of_generated_integers = 10
        self.generated_integers = []
        self.result_message = f'The next {self.number_of_generated_integers} integers:\n'
        self.difference = []
        self.quotient_remainder_pairs = []

    def update_initial_setting(self, input: list) -> None:
        try:
            self.origional_integer_list = [int(item) for item in input]
        except:
            raise Exception(self.error_message['not_integers'])

        for i in range(1, len(self.origional_integer_list)):
            prev = self.origional_integer_list[i - 1]
            current = self.origional_integer_list[i]

            if current < prev:
                raise Exception(self.error_message['not_increasing'])
            self.difference.append(current - prev)
            self.quotient_remainder_pairs.append(divmod(current, prev))

    def generate_integers(self, generate_next_int: callable) -> None:
        prev_number = self.origional_integer_list[-1]
        self.generated_integers.append(generate_next_int(prev_number))

        for i in range(self.number_of_generated_integers - 1):
            prev_number = self.generated_integers[-1]
            self.generated_integers.append(generate_next_int(prev_number))

    def find_pattern(self) -> str:
        try:
            integers_string = input(
                'Please enter increasing integers separated by spaces:\n'
            )

            self.update_initial_setting(integers_string.split())
            generate_next_int = None

            # pattern: arithmetic sequence
            if len(set(self.difference)) == 1:
                def generate_next_int(prev): return prev + self.difference[0]

            # pattern: geometric-like sequence
            elif len(set(self.quotient_remainder_pairs)) == 1:
                q, r = self.quotient_remainder_pairs[0]
                def generate_next_int(prev): return prev * q + r

            if generate_next_int is None:
                self.result_message = 'Sorry, I cannot recognize the pattern of the sequence.'
            else:
                self.generate_integers(generate_next_int)
                self.result_message += ' '.join([str(num)
                                                for num in self.generated_integers])

            return self.result_message

        except Exception as e:
            return str(e)


find_pattern = Find_pattern()
print(find_pattern.find_pattern())
