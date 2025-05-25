from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    li = open(path, 'r')
    lines = li.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    li.close()
    return lines
#w는 쓰기 모드라 읽기모드인 r로 바꿈
def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')
        if '/' in file or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'
#시작은 English로 해야됨
    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)
   #german_file을 english_file에 붙여넣으려 한점을 고쳤다
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end + '\n')
 #template 순서를 바꿨다
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file)
#r는 읽기 모드라 쓰기모드인 w로 바꿈
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) 
#german_file_list와 processed_file_list에 쓰는 함수가 뒤바꼈다
    write_file_list(processed_file_list, path+'concated.json')
