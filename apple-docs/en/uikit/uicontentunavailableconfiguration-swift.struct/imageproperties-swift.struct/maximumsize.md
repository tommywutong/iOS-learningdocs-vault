---
title: maximumSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/maximumsize
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/maximumsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/maximumsize.json'
content_hash: 'sha256:766111e1e3210e5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIContentUnavailableConfiguration](../../uicontentunavailableconfiguration-swift.struct.md) · [ImageProperties](../imageproperties-swift.struct.md)

# maximumSize

<sub>Instance Property</sub>

A maximum size for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximumSize: CGSize { get set }
```

## Discussion

The default value is [CGSizeZero](../../../coregraphics/cgsizezero.md). Setting a [width](../../../corefoundation/cgsize/width.md) or [height](../../../corefoundation/cgsize/height.md) of zero makes the size unconstrained on that dimension. If the image exceeds [maximumSize](maximumsize.md) size on either dimension, the view reduces its size proportionately, maintaining aspect ratio.
