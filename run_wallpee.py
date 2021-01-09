"""Main module, that should be ran"""

if __name__ == '__main__':
    import sys

    import cli
    from config import WallpeeConfig
    from clients.unsplash_client import UnsplashClient

    # Parse options from command line
    cli_options = cli.parse_cli_args()

    # If -v option was specified, print version and exit
    if cli_options.version:
        print(f'Wallpee version is {WallpeeConfig.VERSION}')
        sys.exit(0)

    # Create client of unsplash.com and download random image from it
    #  that will have size closest to the screen size
    unsplash_client = UnsplashClient(
        cli_options.path or WallpeeConfig.DEFAULT_PATH)

    if cli_options.selenium:
        unsplash_client.download_random_image(selenium=True)
    else:
        unsplash_client.download_random_image()
