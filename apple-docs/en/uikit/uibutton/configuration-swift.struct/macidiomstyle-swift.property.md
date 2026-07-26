---
title: macIdiomStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/macidiomstyle-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/macidiomstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/macidiomstyle-swift.property.json'
content_hash: 'sha256:c3820ca2714c2dbc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# macIdiomStyle

<sub>Instance Property</sub>

The style to use when this button appears in macOS.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var macIdiomStyle: UIButton.Configuration.MacIdiomStyle { get set }
```

## Discussion

Use this property when building your app with Mac Catalyst. The value [UIButton.Configuration.MacIdiomStyle.automatic](macidiomstyle-swift.enum/automatic.md) lets the system choose the appropriate style. Select a specific style to force the button to always use that style.

## See Also

### Configuring the appearance on macOS

- [MacIdiomStyle](macidiomstyle-swift.enum.md) — The button style your app uses when running in macOS.
