---
title: darkerSystemColorsStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/darkersystemcolorsstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/darkersystemcolorsstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/darkersystemcolorsstatusdidchangenotification.json'
content_hash: 'sha256:96442b2fbc64dcd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# darkerSystemColorsStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the system’s Increase Contrast setting changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Colors

- [UIAccessibilityGrayscaleStatusDidChangeNotification](grayscalestatusdidchangenotification.md) — A notification that UIKit posts when the system’s Grayscale setting changes.
- [UIAccessibilityInvertColorsStatusDidChangeNotification](invertcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the settings for inverted colors change.
