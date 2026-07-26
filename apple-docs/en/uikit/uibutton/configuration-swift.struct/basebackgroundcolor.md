---
title: baseBackgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/basebackgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/basebackgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/basebackgroundcolor.json'
content_hash: 'sha256:f6a771635d18b711'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# baseBackgroundColor

<sub>Instance Property</sub>

The untransformed color for background views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var baseBackgroundColor: UIColor? { get set }
```

## Discussion

The button configuration may transform the base color before applying it to background elements.

## See Also

### Configuring button colors

- [baseForegroundColor](baseforegroundcolor.md) — The untransformed color for foreground views.
