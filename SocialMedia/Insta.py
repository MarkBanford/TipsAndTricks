import instaloader
from instaloader import Instaloader, Profile
import os

download_dir = r'E:\\Instagrams\\Bian'


def download():
    L = instaloader.Instaloader()
    L.login("", "")

    PROFILE = "bian_ifbb_pro"
    profile = Profile.from_username(L.context, PROFILE)

    download_dir = r'E:\\Instagrams\\Bian'
    for post in profile.get_posts():
        if post.typename == 'GraphImage':
            os.chdir(download_dir)
            L.download_post(post, PROFILE)


def clean():
    path = r'E:\Instagrams\Bian\bian_ifbb_pro'
    for file in os.listdir(path):
        if not file.endswith('.jpg'):
            os.remove(os.path.join(path, file))

clean()
