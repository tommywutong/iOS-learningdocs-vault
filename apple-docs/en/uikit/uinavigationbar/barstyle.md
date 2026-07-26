---
title: barStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/barstyle
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/barstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/barstyle.json'
content_hash: 'sha256:6a762858d597bc36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# barStyle

<sub>Instance Property</sub>

The navigation bar style that specifies its appearance.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var barStyle: UIBarStyle { get set }
```

## Discussion

See [UIBarStyle](../uibarstyle.md) for possible values. The default value is [UIBarStyleDefault](../uibarstyle/default.md).

It is permissible to set the value of this property when the navigation bar is being managed by a navigation controller object.

## See Also

### Setting the bar’s style

- [UIBarStyle](../uibarstyle.md) — Defines the stylistic appearance of different types of views.
