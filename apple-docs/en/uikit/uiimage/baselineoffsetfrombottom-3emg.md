---
title: baselineOffsetFromBottom
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/baselineoffsetfrombottom-3emg
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/baselineoffsetfrombottom-3emg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/baselineoffsetfrombottom-3emg.json'
content_hash: 'sha256:49cdc9afd221034d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# baselineOffsetFromBottom

<sub>Instance Property</sub>

The position of the baseline relative to the bottom of the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var baselineOffsetFromBottom: CGFloat? { get }
```

## Discussion

Positive values place the baseline up inside the image, and negative values place the baseline below the bottom of the image. When the value of this property is `0.0`, the baseline position is equal to the bottom of the image.
