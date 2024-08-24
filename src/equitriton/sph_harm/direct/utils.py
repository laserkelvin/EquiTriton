from __future__ import annotations

from importlib import import_module

import torch

__all__ = ["torch_spherical_harmonic", "triton_spherical_harmonic"]


def torch_spherical_harmonic(l: int, coords: torch.Tensor) -> torch.Tensor:
    """
    Utility function that will call the PyTorch implementation
    of a spherical harmonic order.

    This is not intended for production use, but mainly for
    sanity checking and convenience.

    Parameters
    ----------
    l : int
        Order of spherical harmonic requested.
    coords : torch.Tensor
        N-d tensor, where the last dimension should correspond
        to xyz vectors.

    Returns
    -------
    torch.Tensor
        N-d tensor of the same dimensionality as the input coordinates,
        but the size of the last dimension equal to [2 * l + 1].

    Raises
    ------
    ModuleNotFoundError
        If order of spherical harmonic requested is not found, it is
        likely not yet implemented.
    RuntimeError
        If the PyTorch implementation of the spherical harmonic is
        not found within the module.
    RuntimeError
        If the shape of the last dimension of the ``coords`` tensor
        is not equal to three.
    """
    try:
        target_module = import_module(f"equitriton.sph_harm.direct.y_{l}")
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            f"Spherical harmonic order l={l} requested, but not found!"
        ) from e
    torch_func = getattr(target_module, "_torch_fwd", None)
    if not torch_func:
        raise RuntimeError(f"PyTorch implementation of l={l} not found.")
    if coords.size(-1) != 3:
        raise RuntimeError("Expects last dimension of coordinate tensor to be 3!")
    return torch_func(coords)


def triton_spherical_harmonic(
    l: int, coords: torch.Tensor, mask: torch.Tensor | None = None
) -> torch.Tensor:
    """
    Utility function that will call the Triton implementation
    of a spherical harmonic order.

    This is not intended for production use, but mainly for
    sanity checking and convenience.

    Parameters
    ----------
    l : int
        Order of spherical harmonic requested.
    coords : torch.Tensor
        N-d tensor, where the last dimension should correspond
        to xyz vectors.

    Returns
    -------
    torch.Tensor
        N-d tensor of the same dimensionality as the input coordinates,
        but the size of the last dimension equal to [2 * l + 1].

    Raises
    ------
    ModuleNotFoundError
        If order of spherical harmonic requested is not found, it is
        likely not yet implemented.
    RuntimeError
        If the Triton implementation of the spherical harmonic is
        not found within the module.
    RuntimeError
        If the shape of the last dimension of the ``coords`` tensor
        is not equal to three.
    """
    try:
        target_module = import_module(f"equitriton.sph_harm.direct.y_{l}")
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            f"Spherical harmonic order l={l} requested, but not found!"
        ) from e
    defined_classes: list = getattr(target_module, "__all__")
    # there should only be one entry in __all__, which is the autograd wrapper
    sph_harm_func = getattr(target_module, defined_classes[0], None)
    if not sph_harm_func:
        raise RuntimeError(f"Triton implementation of l={l} not found.")
    if coords.size(-1) != 3:
        raise RuntimeError("Expects last dimension of coordinate tensor to be 3!")
    return sph_harm_func.apply(coords)