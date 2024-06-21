# import modules/library
from urllib.request import urlretrieve
import ctypes

# download wallpaper function
def download_wallpaper():
    # download wallpaper
    urlretrieve("https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fG1hdHJpeHxlbnwwfHwwfHx8MA%3D%3D","wallpaper.jpg")

# set background function
def set_background():
    wallpaper_path = ("wallpaper.jpg")
    image = ctypes.c_wchar_p(wallpaper_path)
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,0)
    print("TEST")


download_wallpaper()
set_background()
