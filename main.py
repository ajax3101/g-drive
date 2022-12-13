from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def create_and_upload_file(file_name='test.txt', file_content='Hi!'):

    try:
        drive = GoogleDrive(gauth)

        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentString(file_content)
        my_file.Upload()

        return f'File {file_name} was uploaded! Super!'
    except Exception as _ex:
        return 'Trouble, check your code please!'


def main():
    print(create_and_upload_file(
        file_name='hello.txt', file_content='Hello Freands!'))


if __name__ == '__main__':
    main()
