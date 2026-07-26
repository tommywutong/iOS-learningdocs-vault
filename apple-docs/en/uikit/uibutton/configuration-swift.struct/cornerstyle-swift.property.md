---
title: cornerStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.property.json'
content_hash: 'sha256:e937f81e18563087'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# cornerStyle

<sub>Instance Property</sub>

The button style that controls the display behavior of the background corner radius.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cornerStyle: UIButton.Configuration.CornerStyle { get set }
```

## Discussion

This property controls the behavior of the [cornerRadius](../../uibackgroundconfiguration-swift.struct/cornerradius.md) you set on the configuration background. The default corner style is [UIButton.Configuration.CornerStyle.dynamic](cornerstyle-swift.enum/dynamic.md).

## See Also

### Configuring the button background

- [background](background.md) — The configuration to customize the button background.
- [CornerStyle](cornerstyle-swift.enum.md) — Settings that determine the appearance of the background corner radius.
