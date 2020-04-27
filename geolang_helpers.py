
def normalize_surname(surname):
    '''
    gets georgian surname and returns it in base form
    (სახელობითი ბრუნვა)

    ---------------------------------------------
    Warning:
    ---------------------------------------------
        function does not remove things like
            'თან', 'თვის' ... from the end...
    ---------------------------------------------

    ex:
        'სააკაშვილი' --> 'სააკაშვილი'
        'სააკაშვილმა' --> 'სააკაშვილი'
        'სააკაშვილს' --> 'სააკაშვილი'

    helper link - http://www.nplg.gov.ge/civil/statiebi/wignebi/qartul_enis_marTlwera/qartul_enis_marTlwera-tavi-3.htm
    '''
    last_4_letters = surname[-4:]
    last_3_letters = surname[-3:]
    last_2_letters = surname[-2:]
    last_letter = surname[-1]

    vowels = 'აეიოუ'

    # წოდებითი
    if last_letter == 'ო':
        if last_3_letters[0] in vowels:
            return f'{surname[:-1]}ი'
        else:
            return surname

    # მოთხრობითი
    if last_letter == 'მ': return f'{surname[:-1]}'
    if last_2_letters == 'მა': return f'{surname[:-2]}ი'

    # ვითარებითი | - ლ
    if last_2_letters == 'ად' and last_3_letters[0] != 'ლ':
        if last_3_letters[0] not in vowels:
            return f'{surname[:-2]}ი'
        else:
            return f'{surname[:-1]}'
    if last_letter == 'დ' and last_3_letters[0] != 'ლ': 
        return f'{surname[:-1]}'

    # მიცემითი
    if last_letter == 'ს' and last_2_letters[0] != 'ი':
        if last_2_letters[0] in vowels:
            return f'{surname[:-1]}'
        else:
            return f'{surname[:-1]}ი'

    # ნათესაობითი & მოქმედებითი
    if last_3_letters in ['ძის', 'ძით']:
        return f'{surname[:-2]}ე'
    if last_3_letters in ['ლის', 'ლით', 'ლად'] and last_4_letters[0] not in vowels:
        return f'{surname[:-3]}ელი'
    if last_3_letters in ['ლად'] and last_4_letters[0] in vowels:
        return f'{surname[:-2]}ი'
    if last_letter in ['ს', 'თ']:
        return f'{surname[:-1]}'

    return surname

if __name__ == '__main__':
    tests = {
        'სააკაშვილი': 'სააკაშვილი',
        'სააკაშვილმა': 'სააკაშვილი',
        'სააკაშვილს': 'სააკაშვილი',
        'სააკაშვილის': 'სააკაშვილი',
        'სააკაშვილით': 'სააკაშვილი',
        'სააკაშვილად': 'სააკაშვილი',
        'სააკაშვილო': 'სააკაშვილი',

        'ბრეგვაძე':'ბრეგვაძე',
        'ბრეგვაძემ':'ბრეგვაძე',
        'ბრეგვაძეს':'ბრეგვაძე',
        'ბრეგვაძის':'ბრეგვაძე',
        'ბრეგვაძით':'ბრეგვაძე',
        'ბრეგვაძედ':'ბრეგვაძე',
        'ბრეგვაძე':'ბრეგვაძე',

        'ბოკერია': 'ბოკერია',
        'ბოკერიამ': 'ბოკერია',
        'ბოკერიას': 'ბოკერია',
        'ბოკერიას': 'ბოკერია',
        'ბოკერიათ': 'ბოკერია',
        'ბოკერიად': 'ბოკერია',
        'ბოკერია': 'ბოკერია',

        'გილაური': 'გილაური',
        'გილაურმა': 'გილაური',
        'გილაურს': 'გილაური',
        'გილაურის': 'გილაური',
        'გილაურით': 'გილაური',
        'გილაურად': 'გილაური',
        'გილაურო': 'გილაური',

        'წერეთელი': 'წერეთელი',
        'წერეთელმა': 'წერეთელი',
        'წერეთელს': 'წერეთელი',
        'წერეთლის': 'წერეთელი',
        'წერეთლით': 'წერეთელი',
        'წერეთლად': 'წერეთელი',
        'წერეთელი': 'წერეთელი',

        'ბოდაველი': 'ბოდაველი',
        'ბოდაველმა': 'ბოდაველი',
        'ბოდაველს': 'ბოდაველი',
        'ბოდაველის': 'ბოდაველი',
        'ბოდაველით': 'ბოდაველი',
        'ბოდაველად': 'ბოდაველი',
        'ბოდაველო': 'ბოდაველი',

        'სერგეენკო': 'სერგეენკო',
        'სერგეენკომ': 'სერგეენკო',
        'სერგეენკოს': 'სერგეენკო',
        'სერგეენკოს': 'სერგეენკო',
        'სერგეენკოთ': 'სერგეენკო',
        'სერგეენკოდ': 'სერგეენკო',
        'სერგეენკო': 'სერგეენკო',
    }

    for i, correct in tests.items():
        res = normalize_surname(i)
        if res != correct:
            print(" Error: ", i, "-->", res, "!=", correct)
        # assert normalize_surname(i) == correct
