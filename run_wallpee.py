"""Main module, that should be ran"""

if __name__ == '__main__':
    import cli
    from config import WallpeeConfig
    from clients.unsplash_client import UnsplashClient
    from misc import exit_with_message

    # Parse options from command line
    cli_options = cli.parse_cli_args()

    # If -v option was specified, print version and exit
    if cli_options.version:
        exit_with_message(f'Wallpee version is {WallpeeConfig.VERSION}')

    # Create client of unsplash.com and download random image from it
    #  that will have size closest to the screen size
    unsplash_client = UnsplashClient(
        cli_options.path or WallpeeConfig.DEFAULT_PATH)

    unsplash_client.download_random_image()
