import requests
import sys
import os

#create a variable to hold urls for the resource(s) we wish to download.
urls = sys.argv[1:]

#function that downloads the resource.
def download(data, url):
    # get file name according to url.
    if url.find('/'):
        filename = url.split('/')[-1]

        #give custom name if filename is empty.
        if filename == "":
            print("File has no name.")
            #try to save the file to disk.
            try:
                filename2 = input("Save file as? e.g index.html, index.jpg :")
                print("Saving file to disk.")
                #saving the file.
                open(filename2, "wb").write(data.content)
                #show where the fie has been saved.
                print("File saved in ", os.path.abspath(filename))
            #handle any errors that occur.
            except:
                print("An unexpected error has ocurred.")
        
        elif filename != "":
            print("Filename: ",filename)
            #try to save the file to disk.
            try:
                print("Saving file to disk.")
                open(filename, "wb").write(data.content)
                #show where the file has been saved.
                print("File saved to ", os.path.abspath(filename))
            #handle any errors that occur.
            except:
                print("An unexpected error occurred. File not saved.")

#make requests for each url given and allow redirects.
def main():
    global url
    print("starting script")
    for url in urls:
        global data
        #make the requests.
        data = requests.get(url, allow_redirects=True)
        print("Status code: ",data.status_code)
        #get the type of file we're downloading.
        download(data, url)

if __name__ == '__main__':
    main()
