---
title: closedCaptioningStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/closedcaptioningstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/closedcaptioningstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/closedcaptioningstatusdidchangenotification.json'
content_hash: 'sha256:72bdc83b32b2ebb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# closedCaptioningStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the setting for Closed Captions + SDH changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let closedCaptioningStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Text

- [UIAccessibilityBoldTextStatusDidChangeNotification](boldtextstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Bold Text setting changes.
