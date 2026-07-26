---
title: barStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/barstyle
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/barstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/barstyle.json'
content_hash: 'sha256:9913430de05ca55f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# barStyle

<sub>Instance Property</sub>

The tab bar style that specifies its appearance.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var barStyle: UIBarStyle { get set }
```

## Discussion

This property determines whether the tab bar uses a dark or light visual style when no background image or tint color is specified. Together with the [translucent](istranslucent.md) property, this property defines the default visual style of the tab bar. Set this property to the value that best matches the style of your interface. For a list of possible values, see [UIBarStyle](../uibarstyle.md). The default value of this property is [UIBarStyleDefault](../uibarstyle/default.md).

## See Also

### Setting the bar’s style

- [UIBarStyle](../uibarstyle.md) — Defines the stylistic appearance of different types of views.
