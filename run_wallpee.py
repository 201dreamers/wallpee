from selenium import webdriver

from clients.unsplash.unsplash_page import UnsplashPage

driver = webdriver.Firefox()

unsplash_page = UnsplashPage(driver)
unsplash_page.open_page()
unsplash_page.search('wallpaper')
unsplash_page.choose_orientation()
unsplash_page.choose_sort_by_newest()
unsplash_page.get_list_of_images()
unsplash_page.download_random_image()
driver.close()
