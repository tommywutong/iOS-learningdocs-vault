---
title: colorYCbCrMatrix
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablevideocomposition/colorycbcrmatrix
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/colorycbcrmatrix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/colorycbcrmatrix.json'
content_hash: 'sha256:353ec57105d1253e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# colorYCbCrMatrix

<sub>Instance Property</sub>

The YCbCr matrix used for video composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorYCbCrMatrix: String? { get set }
```

## Discussion

The default value is `nil`. When the value of this property is `nil`, the source’s matrix is propagated and used. Valid values are those suitable for [AVVideoYCbCrMatrixKey](../avvideoycbcrmatrixkey.md).

## See Also

### Configuring color

- [colorPrimaries](colorprimaries.md) — The color primaries used for video composition.
- [colorTransferFunction](colortransferfunction.md) — The transfer function used for video composition.
