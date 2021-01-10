from image_providers.unsplash.unsplash_provider import UnsplashProvider


class UnsplashClient:

    __slots__ = ('path_for_image')

    def __init__(self, path_for_image) -> None:
        self.path_for_image = path_for_image

    def download_random_image(self) -> None:
        image_provider = UnsplashProvider(self.path_for_image)
        image_path = image_provider.download_random_image()
        print(f'Image was saved to {image_path} :)')
