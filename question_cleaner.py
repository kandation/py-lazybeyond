import re


def clean_text(text):
    # Remove MULTIPLE CHOICE and point(s) lines
    text = re.sub(r'(?m)^MULTIPLE CHOICE.*\n?', '', text)
    text = re.sub(r'(?m)^\d\/\d point\(s\)\n?', '', text)
    text = re.sub(r'(?m)^\d point\(s\)\n?', '', text)
    text = re.sub(r'(?m)^Response saved\n?', '', text)

    # Remove Feedback and - lines
    text = re.sub(r'(?m)^Feedback\n-+\n?', '', text)

    # Remove extra newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Convert to JSON format
    result = []
    questions = re.split(r'(?m)^Question \d+\n', text)[1:]

    for question in questions:
        lines = question.strip().split('\n')
        question_text = lines[0].strip()
        choices = {}

        temp_choice = []
        for choice in lines[-1:1:-1]:
            choice_text = choice.split('. ', 1)

            line = ''.join(choice_text).strip()
            temp_choice.append(line)

            if line.startswith('A.') or line.startswith('B.') or line.startswith('C.') or line.startswith('D.'):
                letter = re.sub(r'\.', '', line)
                choices[letter] = ''.join(temp_choice[:-1]).strip()
                temp_choice = []

        result.append({
            'question': question_text,
            'choices': choices
        })

    return result


if __name__ == '__main__':
    file_name = 'cit_post'

    with open(f"data/{file_name}.txt", "r", encoding="utf-8") as file:
        text = file.read()

    result = clean_text(text)

    IS_EXCEL = True

    for ii, item in enumerate(result):
        if IS_EXCEL:
            print(f'{ii + 1}\t{item["question"]}', end='\t')
        else:
            print(f"Question {ii + 1}: {item['question']}")

        for letter, choice in reversed(item['choices'].items()):
            if IS_EXCEL:
                print(f"{letter}. {choice}", end='\t')
            else:
                print(f"{letter}. {choice}")

        print()
