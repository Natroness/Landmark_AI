import os
from icrawler.builtin import GoogleImageCrawler

project_dir = os.path.dirname(os.path.abspath(__file__))  # directory of your script

landmarks = ['Eiffel Tower', 'Taj Mahal', 'Statue of Liberty','Dharahara']

for landmark in landmarks:
    folder_name = os.path.join(project_dir, 'images', landmark.replace(" ", "_"))
    print(f"Saving images for {landmark} in folder: {folder_name}")
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder_name})
    google_crawler.crawl(keyword=f'{landmark} blurry low light', max_num=50)
