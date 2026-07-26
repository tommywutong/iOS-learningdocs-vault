---
title: elementFocusedNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/elementfocusednotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/elementfocusednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/elementfocusednotification.json'
content_hash: 'sha256:304fb032c2788a45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# elementFocusedNotification

<sub>Type Property</sub>

A notification that UIKit posts when an assistive app focuses on an accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let elementFocusedNotification: NSNotification.Name
```

## Discussion

Retrieve the [UIAccessibilityFocusedElementKey](focusedelementuserinfokey.md) key from the [userInfo](../../foundation/nsnotification/userinfo.md) dictionary to get the identity of the focused accessibility element.

## See Also

### UI changes

- [UIAccessibilityScreenChangedNotification](notification/screenchanged.md) — A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [UIAccessibilityLayoutChangedNotification](notification/layoutchanged.md) — A notification that an app posts when the layout of a screen changes.
- [UIAccessibilityPageScrolledNotification](notification/pagescrolled.md) — A notification that an app posts when a scroll action completes.
- [UIAccessibilitySwitchControlStatusDidChangeNotification](switchcontrolstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Switch Control setting changes.
- [UIAccessibilityReduceTransparencyStatusDidChangeNotification](reducetransparencystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [UIAccessibilityButtonShapesEnabledStatusDidChangeNotification](buttonshapesenabledstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Button Shapes setting changes. _(deprecated)_
