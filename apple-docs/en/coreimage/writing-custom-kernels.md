---
title: Writing Custom Kernels
framework: Core Image
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/writing-custom-kernels
source_url: 'https://developer.apple.com/documentation/coreimage/writing-custom-kernels'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/writing-custom-kernels.json'
content_hash: 'sha256:97e923b2373067a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# Writing Custom Kernels

<sub>Article</sub>

Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.

## Overview

The Core Image Kernel Language is a shading language optimized for writing custom kernels for use in apps leveraging Core Image.  You can add custom image processing routines to a Core Image pipeline.

You can also write your own kernels in the Metal Shading Language.  The following flowchart shows how you decide which language to use for writing custom kernels:

![Flowchart showing how to choose a kernel language for writing custom CIKernel filters.](../../../attachments/475fd86172676d9a39b147cbc2eeac5f/media-3011610@2x.png)

Source code written in Core Image Kernel Language should contain one or more image processing routines and may optionally contain other functions that are called by these routines. The source code is parsed and validated when the code is passed to Core Image’s [CIKernel](cikernel.md) creation APIs. When rendering, Core Image can concatenate kernel functions used within an image graph and construct optimized shader programs. See [Core Image Kernel Language Reference](https://developer.apple.com/go/?id=core-image-kernel-language-reference) for a list of supported data types, functions, and language features.

Alternatively, you can write custom kernels in the Metal Shading Language. If you intend to use Metal-only language features and support exclusively Metal-supported devices, then writing custom kernels in Metal Shading Language can reduce compile-time cost while providing code consistency across your Metal app. See [Metal Shading Language for Core Image Kernels](https://developer.apple.com/go/?id=metal-shading-language-for-core-image-kernels) for a list of supported data types, functions, and language features.

## See Also

### Custom Filters

- [CIKernel](cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIColorKernel](cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIWarpKernel](ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CIBlendKernel](ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CISampler](cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFilterShape](cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [CIFormat](ciformat.md) — Pixel data formats for image input, output, and processing.
