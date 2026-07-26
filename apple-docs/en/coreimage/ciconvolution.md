---
title: CIConvolution
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciconvolution
source_url: 'https://developer.apple.com/documentation/coreimage/ciconvolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciconvolution.json'
content_hash: 'sha256:51addba0d5e9f07d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIConvolution

<sub>Protocol</sub>

The properties you use to configure a convolution filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIConvolution : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [bias](ciconvolution/bias.md) — A value that’s added to each output pixel.
- [inputImage](ciconvolution/inputimage.md) — The image to use as an input image.
- [weights](ciconvolution/weights.md) — The convolution kernel.

## See Also

### Related Documentation

- [+ convolution3X3Filter](<cifilter-swift.class/convolution3x3().md>) — Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [+ convolution5X5Filter](<cifilter-swift.class/convolution5x5().md>) — Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [+ convolution7X7Filter](<cifilter-swift.class/convolution7x7().md>) — Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [+ convolution9HorizontalFilter](<cifilter-swift.class/convolution9horizontal().md>) — Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [+ convolution9VerticalFilter](<cifilter-swift.class/convolution9vertical().md>) — Applies a convolution-9 vertical filter to the `RGBA` components of an image.
