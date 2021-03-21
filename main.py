from polkadots.datasets import MakeImages


def do():
    image_maker = MakeImages(min_width=512, max_width=512, min_height=512, max_height=512,
                             seed=0)
    image_maker.new_image(16, dot_size=32, class_index=12).show()


if __name__ == '__main__':
    do()
