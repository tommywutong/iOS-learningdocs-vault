---
title: Processing HDR images with Metal
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/processing-hdr-images-with-metal
source_url: 'https://developer.apple.com/documentation/metal/processing-hdr-images-with-metal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/processing-hdr-images-with-metal.json'
content_hash: 'sha256:7e3bbbd091ccbf8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [HDR content](hdr-content.md)

# Processing HDR images with Metal

<sub>Sample Code</sub>

Implement a post-processing pipeline using the latest features on Apple GPUs.

## Overview

> [!note] Note
> This sample code project is associated with WWDC21 session [10161: Explore HDR rendering with EDR](https://developer.apple.com/wwdc21/10161/), and WWDC20 session [10602: Harness Apple GPUs with Metal](https://developer.apple.com/wwdc20/10602/).

## See Also

### High dynamic range content

- [Displaying HDR content in a Metal layer](displaying-hdr-content-in-a-metal-layer.md) — Bring your high dynamic range (HDR) content to compatible Mac displays.
- [Determining support for EDR values](determining-support-for-edr-values.md) — Check whether a display supports EDR.
- [Using color spaces to display HDR content](using-color-spaces-to-display-hdr-content.md) — Use a color space when you don’t need to edit or process the pixel data.
- [Using system tone mapping on video content](using-system-tone-mapping-on-video-content.md) — Use EDR metadata to apply the default system tone mapping to a layer.
- [Performing your own tone mapping](performing-your-own-tone-mapping.md) — Apply your own tone mapping to get the exact behavior you want.
- [Implementing tone mapping on reference displays](implementing-tone-mapping-on-reference-displays.md) — Detect reference displays and keep your content within the capabilities of the display hardware.

## Download

- [ProcessingHDRImagesWithMetal.zip](https://docs-assets.developer.apple.com/published/8bd4230f1aa0/ProcessingHDRImagesWithMetal.zip)
