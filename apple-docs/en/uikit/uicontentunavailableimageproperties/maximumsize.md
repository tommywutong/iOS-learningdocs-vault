---
title: maximumSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableimageproperties/maximumsize
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableimageproperties/maximumsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableimageproperties/maximumsize.json'
content_hash: 'sha256:ffc6a52da9ea1944'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentUnavailableImageProperties](../uicontentunavailableimageproperties.md)

# maximumSize

<sub>Instance Property</sub>

A maximum size for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGSize maximumSize;
```

## Discussion

The default value is [CGSizeZero](../../coregraphics/cgsizezero.md). Setting a [width](../../corefoundation/cgsize/width.md) or [height](../../corefoundation/cgsize/height.md) of zero makes the size unconstrained on that dimension. If the image exceeds [maximumSize](../uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/maximumsize.md) size on either dimension, the view reduces its size proportionately, maintaining aspect ratio.
