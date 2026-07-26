---
title: invertColorsStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/invertcolorsstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/invertcolorsstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/invertcolorsstatusdidchangenotification.json'
content_hash: 'sha256:e68ab3bb7b016770'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# invertColorsStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the settings for inverted colors change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let invertColorsStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

Use the [UIAccessibilityIsInvertColorsEnabled](isinvertcolorsenabled.md) function to determine whether the settings for inverted colors are in an enabled state.

## See Also

### Colors

- [UIAccessibilityDarkerSystemColorsStatusDidChangeNotification](darkersystemcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [UIAccessibilityGrayscaleStatusDidChangeNotification](grayscalestatusdidchangenotification.md) — A notification that UIKit posts when the system’s Grayscale setting changes.
