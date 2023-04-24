import requests


class FileGetter:
    def __init__(self):
        self.__url = 'https://random.dog/woof.json'
        self.__file_extension = None
        self.__content = None

    @property
    def extension(self):
        return self.__file_extension

    @property
    def content(self):
        return self.__content

    def get_file(self):
        response = requests.get(self.__url)
        if response.status_code == 200:
            data = response.json()
            if 'url' in data:
                self.__file_extension = data['url'][data['url'].rindex('.'):]
                self.__content = requests.get(data['url']).content
        return None


if __name__ == '__main__':
    ig = FileGetter()
    ig.get_file()
    if ig.content is not None:
        with open(f'file{ig.extension}', 'wb') as f:
            f.write(ig.content)
            print(f'Image saved to file{ig.extension}')
    else:
        print('Failed to get file')
