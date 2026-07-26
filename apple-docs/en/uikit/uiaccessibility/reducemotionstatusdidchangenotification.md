---
title: reduceMotionStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/reducemotionstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/reducemotionstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/reducemotionstatusdidchangenotification.json'
content_hash: 'sha256:21147e0f0db7ab94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# reduceMotionStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the system’s Reduce Motion setting changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let reduceMotionStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Motion

- [UIAccessibilityShakeToUndoDidChangeNotification](shaketoundodidchangenotification.md) — A notification that UIKit posts when the system’s Shake to Undo setting changes.
