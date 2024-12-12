import os

import matplotlib.pyplot as plt


def get_full_file_name(file_name="image"):
    return os.path.join(os.path.abspath("."), file_name)


def create_and_save_img(data):
    fig, ax = plt.subplots()
    ax.plot(data)
    fig.savefig(get_full_file_name())
    # plt.show()
    plt.close(fig)
