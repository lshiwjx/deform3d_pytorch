import os.path as path
import torch
from torch.utils.ffi import create_extension

sources = ['lib/conv2d_cuda.cpp']
headers = ['lib/conv2d_cuda.h']
# defines = [('WITH_CUDA', None), ('TH_DOUBLE', None)]
defines = [('WITH_CUDA', None)]

this_file = path.dirname(path.realpath(__file__))
extra_objects = ['lib/conv2d_cuda_kernel.cu.o']
extra_objects = [path.join(this_file, fname) for fname in extra_objects]
print(extra_objects)

ffi = create_extension(
    'conv2d_op',
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=True,
    extra_objects=extra_objects
)

if __name__ == '__main__':
    assert torch.cuda.is_available(), 'Please install CUDA for GPU support.'
    ffi.build()
