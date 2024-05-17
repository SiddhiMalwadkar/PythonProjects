from google_images_download import google_images_download

def download_images(query, limit, output_directory):
    response = google_images_download.googleimagesdownload()

    arguments = {"keywords": query, "limit": limit, "print_urls": True, "output_directory": output_directory}
    paths = response.download(arguments)

    print(paths)

if __name__ == "__main__":
    query = input("Enter the keyword to search for: ")
    limit = int(input("Enter the number of images to download: "))
    output_directory = input("Enter the output directory (leave empty for default): ")

    if not output_directory:
        output_directory = None

    download_images(query, limit, output_directory)
