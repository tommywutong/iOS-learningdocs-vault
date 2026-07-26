---
title: MTLPixelFormat.gbgr422
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/gbgr422
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/gbgr422'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/gbgr422.json'
content_hash: 'sha256:13ee6245efbc79fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.gbgr422

<sub>Case</sub>

A pixel format where the red and green components are subsampled horizontally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case gbgr422
```

## Discussion

Two pixels are stored in 32 bits, with shared red and blue values, and unique green values. The component arrangement is the same as it is in YUY2, YUYV, yuvs, and kYUVS pixel formats, except there is no implicit format conversion from a YUV to RGB color space. Only 2D non-mipmapped textures can be created with this pixel format, and the width needs to be a multiple of 2. Neither [MTLTextureType2DArray](../mtltexturetype/type2darray.md) nor [MTLTextureTypeCube](../mtltexturetype/typecube.md) textures are supported. This format is a compressed format with a block size of 2x1 in a 32-bit block. During sampling, the address mode needs to be set to [MTLSamplerAddressModeClampToEdge](../mtlsampleraddressmode/clamptoedge.md).

## See Also

### YUV pixel formats

- [MTLPixelFormatBGRG422](bgrg422.md) — A pixel format where the red and green components are subsampled horizontally.
