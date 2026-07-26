---
title: Modern rendering with Metal
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/modern-rendering-with-metal
source_url: 'https://developer.apple.com/documentation/metal/modern-rendering-with-metal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/modern-rendering-with-metal.json'
content_hash: 'sha256:d0c92bf790bb88b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# Modern rendering with Metal

<sub>Sample Code</sub>

Use advanced Metal features such as indirect command buffers, sparse textures, and variable rate rasterization to implement complex rendering techniques.

## Overview

> [!note] Note
> This sample code project is associated with the [Metal Enhancements for A13 Bionic](http://developer.apple.com/tech-talks/608) tech talk.

### Configure the sample code project

Because this sample app uses indirect command buffers, you can’t run this sample in the Simulator — you need to run it on a device. To run this sample, use one of the following:

- A Mac from mid-2016 and later with macOS 11 and later
- An iPad with A11 Bionic and later using iPadOS 14.1 and later
- An iOS device with A11 Bionic and later using iOS 14.1 and later
- Xcode 12 and later

## See Also

### Multiple techniques

- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md) — Maximize CPU to GPU parallelization by generating render commands on the GPU.

## Download

- [ModernRenderingWithMetal.zip](https://docs-assets.developer.apple.com/published/757ec6a1e5f6/ModernRenderingWithMetal.zip)
