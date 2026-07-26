---
title: boldTextStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/boldtextstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/boldtextstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/boldtextstatusdidchangenotification.json'
content_hash: 'sha256:443388da8fd1ccf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# boldTextStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the system’s Bold Text setting changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let boldTextStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Text

- [UIAccessibilityClosedCaptioningStatusDidChangeNotification](closedcaptioningstatusdidchangenotification.md) — A notification that UIKit posts when the setting for Closed Captions + SDH changes.
