import os
#using icrawler to get the pictures
from icrawler.builtin import GoogleImageCrawler

#saving the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))  # directory of your script

#listing the names of the landmarks we need
landmarks = ['Eiffel Tower', 'Taj Mahal', 'Statue of Liberty','Dharahara']

#starting a loop so that each landmark is downloaded
for landmark in landmarks:
    #To save the images in the folder
    folder_name = os.path.join(project_dir, 'images', landmark.replace(" ", "_"))
    #just to know whats going on and I should be able to track from the terminal
    print(f"Saving images for {landmark} in folder: {folder_name}")
    #using the crawler
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder_name})
    #keeping the maximum number 50 to limit the download
    google_crawler.crawl(keyword=f'{landmark} blurry low light', max_num=50)

    #Also, I deleted some of the pictures manually as they were not openable
