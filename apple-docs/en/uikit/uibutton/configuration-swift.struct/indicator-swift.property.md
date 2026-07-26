---
title: indicator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.property.json'
content_hash: 'sha256:665f6568484a9858'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# indicator

<sub>Instance Property</sub>

The style of the indicator that appears on the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indicator: UIButton.Configuration.Indicator { get set }
```

## Discussion

Use this property to control the style of the indicator that appears on the trailing edge of the button. For example, the following code disables the indicator by setting this style to [UIButton.Configuration.Indicator.none](indicator-swift.enum/none.md).

```swift
var config = UIButton.Configuration.filled()
config.indicator = .none
```

## See Also

### Configuring the indicator

- [Indicator](indicator-swift.enum.md) — Constants that determine the style of the indicator that appears on a button.
- [indicatorColorTransformer](indicatorcolortransformer.md) — The color transformer for resolving the indicator color.
