import matplotlib.pyplot as plt

from utils import get_full_file_name


def create_and_save_img(data, file_name: str):
    fig, ax = plt.subplots()
    ax.plot(data)
    fig.savefig(get_full_file_name(file_name))
    # plt.show()
    plt.close(fig)
