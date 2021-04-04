import pytest
import torch

from pytorch_polkadots.datasets import MakeImages, PolkaDotDataset


def test_image_maker():
    image_maker = MakeImages(max_width=1024, max_height=768,
                             min_width=1024, min_height=768)
    image = image_maker.new_image(16, dot_size=32, class_index=232345232)

    assert image.size == (1024, 768)


def test_dataset():
    dataset = PolkaDotDataset(num_classes=32, length=1)
    assert len(dataset) == 1
    example = dataset[0]
    assert torch.is_tensor(example[0])
    assert type(example[1]) == int


def test_dataset_consistent():
    length = 3
    dataset = PolkaDotDataset(num_classes=32, length=3)
    assert len(dataset) == length
    attempts = 10
    indices = {index: set() for index in range(0, length)}

    for _ in range(attempts):
        for index in range(0, length):
            example, class_index = dataset[index]
            indices[index].add(class_index)
            assert len(indices[index]) == 1
