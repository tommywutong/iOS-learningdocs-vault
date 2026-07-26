---
title: baseForegroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/baseforegroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/baseforegroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/baseforegroundcolor.json'
content_hash: 'sha256:3a1411e8aaf0b90b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# baseForegroundColor

<sub>Instance Property</sub>

The untransformed color for foreground views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var baseForegroundColor: UIColor? { get set }
```

## Discussion

The button configuration may transform the base color before applying it to foreground views.

## See Also

### Configuring button colors

- [baseBackgroundColor](basebackgroundcolor.md) — The untransformed color for background views.
