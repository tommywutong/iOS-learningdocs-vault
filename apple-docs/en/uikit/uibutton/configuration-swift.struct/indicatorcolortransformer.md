---
title: indicatorColorTransformer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/indicatorcolortransformer
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/indicatorcolortransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/indicatorcolortransformer.json'
content_hash: 'sha256:1c8ccbef2f23aaad'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# indicatorColorTransformer

<sub>Instance Property</sub>

The color transformer for resolving the indicator color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indicatorColorTransformer: UIConfigurationColorTransformer? { get set }
```

## Discussion

Use this color transformer to set a custom color for [indicator](../../uibuttonconfiguration/indicator.md). For example, the following code uses a grayscale color for the indicator instead of the default color.

```swift
var config = UIButton.Configuration.filled()
config.indicatorColorTransformer = UIConfigurationColorTransformer.grayscale
```

## See Also

### Configuring the indicator

- [indicator](indicator-swift.property.md) — The style of the indicator that appears on the button.
- [Indicator](indicator-swift.enum.md) — Constants that determine the style of the indicator that appears on a button.
