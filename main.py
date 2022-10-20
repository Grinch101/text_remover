import os

# settings:

FILE_PREFIXES = [
    'CIMO.account.dat',
    'CIMO.DERIV.position.dat',
    'CIMO.NONDERIV.position.dat',
    'reinvest.position'
]

NEW_FILE_PREFIXES = '_edited'
IN_DIR = os.getcwd() + '/in'
OUT_DIR = os.getcwd() + '/out'


def remove_text(text_to_remove='CIG',
                deliminator='|',
                file_to_exclude='CIMO.NONDERIV.position.dat',
                index_columns_to_edit=[0, -2]):
    os.makedirs(IN_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)

    list_of_files = os.listdir(IN_DIR)
    print(f'List of files are: {list_of_files}')
    for file_pattern in list_of_files:
        for file_prefix in FILE_PREFIXES:
            if file_pattern.lower().startswith(file_prefix.lower()):
                temp = ''
                with open(IN_DIR + '/' + file_pattern, 'r') as file:
                    for line in file.readlines():
                        if file_pattern.lower() == file_to_exclude.lower():
                            row = line.split(deliminator)
                            for index in index_columns_to_edit:
                                row[index] = row[index].replace(text_to_remove, '')
                            temp += deliminator.join(row)
                        else:
                            temp += line.replace(text_to_remove, '')
                with open(OUT_DIR + '/' + file_pattern + NEW_FILE_PREFIXES, 'w') as new_file:
                    new_file.write(temp)
                print(f'{file_pattern} has been edited and saved to {OUT_DIR}')


remove_text()
