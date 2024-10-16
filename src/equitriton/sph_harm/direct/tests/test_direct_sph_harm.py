import pytest
import torch

from equitriton import __HAS_XPU__, __HAS_CUDA__
from equitriton.sph_harm.direct.utils import (
    torch_spherical_harmonic,
    triton_spherical_harmonic,
)

torch.manual_seed(316165)


@pytest.mark.parametrize("order", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
@pytest.mark.parametrize(
    "device",
    [
        pytest.param(
            "xpu",
            marks=pytest.mark.skipif(not __HAS_XPU__, reason="No XPUs available."),
        ),
        pytest.param(
            "cuda",
            marks=pytest.mark.skipif(
                not __HAS_CUDA__, reason="No CUDA GPUs available."
            ),
        ),
    ],
)
@pytest.mark.parametrize("tensor_shape", [(512, 3), (128, 16, 3), (256, 8, 8, 3)])
@pytest.mark.parametrize(
    "dtype",
    [
        pytest.param(
            torch.float16,
            marks=pytest.mark.xfail(raises=AssertionError, reason="low precision"),
        ),
        pytest.param(
            torch.bfloat16,
            marks=pytest.mark.xfail(raises=AssertionError, reason="low precision"),
        ),
        torch.float32,
        torch.float64,
    ],
)
def test_forward_equivalence(order, device, tensor_shape, dtype):
    """
    Tests the numerical equivalence of the PyTorch versus
    the Triton implementations. This is mostly to ensure that
    writing outputs back out is being done correctly.
    """
    coords = torch.rand(tensor_shape, device=device, dtype=dtype)
    triton_out = triton_spherical_harmonic(order, coords)
    torch_out = torch_spherical_harmonic(order, coords)
    assert torch.allclose(triton_out, torch_out, atol=1e-5, rtol=1e-3)


@pytest.mark.parametrize("order", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
@pytest.mark.parametrize(
    "device",
    [
        pytest.param(
            "xpu",
            marks=pytest.mark.skipif(not __HAS_XPU__, reason="No XPUs available."),
        ),
        pytest.param(
            "cuda",
            marks=pytest.mark.skipif(
                not __HAS_CUDA__, reason="No CUDA GPUs available."
            ),
        ),
    ],
)
@pytest.mark.parametrize("tensor_shape", [(512, 3), (128, 16, 3), (256, 8, 8, 3)])
@pytest.mark.parametrize(
    "dtype",
    [
        pytest.param(
            torch.float16,
            marks=pytest.mark.xfail(raises=AssertionError, reason="low precision"),
        ),
        pytest.param(
            torch.bfloat16,
            marks=pytest.mark.xfail(raises=AssertionError, reason="low precision"),
        ),
        torch.float32,
        torch.float64,
    ],
)
def test_backward_equivalence(order, device, tensor_shape, dtype):
    """
    Tests the numerical equivalence of the PyTorch versus
    the Triton implementation of the backward pass. This is mostly to ensure that
    writing outputs back out is being done correctly.
    """
    coords = torch.rand(tensor_shape, device=device, dtype=dtype, requires_grad=True)
    # run with autograd first
    torch_out = torch_spherical_harmonic(order, coords)
    torch_out.backward(gradient=torch.ones_like(torch_out))
    torch_grad = coords.grad.clone().detach()
    coords.grad.zero_()
    # now run the triton result
    triton_out = triton_spherical_harmonic(order, coords)
    triton_out.backward(gradient=torch.ones_like(triton_out))
    triton_grad = coords.grad.clone().detach()
    assert torch.allclose(triton_grad, torch_grad, atol=1e-5, rtol=1e-3)
