import requests
url = "https://geraldinetop10.co.nz/wp-content/plugins/admin-menu-editor-pro/readme.txt"

r = requests.get(url, allow_redirects=True)

if url.endswith('.txt'):
    print("Your web file is a text document.")
    print("Trying to write content to disk.")
    try:
        print("\nWriting file to disk.")
        open('D:/Projects/File Downloader Python/Downloads/readme.txt', 'wb').write(r.content)
        print("\nFile written to disk.")
    except:
        print("\nCould not write file to disk.")
