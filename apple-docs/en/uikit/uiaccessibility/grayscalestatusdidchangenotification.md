---
title: grayscaleStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/grayscalestatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/grayscalestatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/grayscalestatusdidchangenotification.json'
content_hash: 'sha256:22f939514d0411bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# grayscaleStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the system’s Grayscale setting changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let grayscaleStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Colors

- [UIAccessibilityDarkerSystemColorsStatusDidChangeNotification](darkersystemcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [UIAccessibilityInvertColorsStatusDidChangeNotification](invertcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the settings for inverted colors change.
