"""Main module, that should be ran"""

if __name__ == '__main__':
    import sys

    import cli
    from config import WallpeeConfig
    from clients.unsplash.unsplash_client import UnsplashClient

    # Parse options from command line
    options = cli.parse_cli_args()

    # If -v option was specified, print version and exit
    if options.version:
        print(f'Wallpee version is {WallpeeConfig.VERSION}')
        sys.exit(0)

    # Create client of unsplash.com and download random image from it
    #  that will have size closest to the screen size
    unsplash_client = UnsplashClient(
        options.path or WallpeeConfig.DEFAULT_PATH)
    unsplash_client.get_random_image()
