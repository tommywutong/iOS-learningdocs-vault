---
title: switchControlStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/switchcontrolstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/switchcontrolstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/switchcontrolstatusdidchangenotification.json'
content_hash: 'sha256:b16dedf7656ffd4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# switchControlStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the system’s Switch Control setting changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let switchControlStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### UI changes

- [UIAccessibilityScreenChangedNotification](notification/screenchanged.md) — A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [UIAccessibilityLayoutChangedNotification](notification/layoutchanged.md) — A notification that an app posts when the layout of a screen changes.
- [UIAccessibilityPageScrolledNotification](notification/pagescrolled.md) — A notification that an app posts when a scroll action completes.
- [UIAccessibilityElementFocusedNotification](elementfocusednotification.md) — A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [UIAccessibilityReduceTransparencyStatusDidChangeNotification](reducetransparencystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [UIAccessibilityButtonShapesEnabledStatusDidChangeNotification](buttonshapesenabledstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Button Shapes setting changes. _(deprecated)_
