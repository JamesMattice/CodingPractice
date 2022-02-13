from pathlib import Path

# A file to store global information

ROOT_DIR = Path(__file__).parent.resolve()
# DEFAULT_SAVE_DIR = Path.joinpath(ROOT_DIR, '/featherDuster')
# print(ROOT_DIR)


customSaveDir = None


def get_save_dir():
    if (customSaveDir is not None) and customSaveDir.isInstance(Path):
        print("the custom save dir was " + customSaveDir)
        return customSaveDir
    else:
        default_save_dir = Path.joinpath(ROOT_DIR, '/featherDuster')
        # print("the default save dir was " + default_save_dir.__repr__())
        return default_save_dir


def set_save_dir(self, path):
    if path.isInstance(Path):
        self.customSaveDir = Path(path)
