---
title: screenChanged
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/notification/screenchanged
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/notification/screenchanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/notification/screenchanged.json'
content_hash: 'sha256:07f3c09d4ef8b5cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIAccessibility](../../uiaccessibility.md) · [Notification](../notification.md)

# screenChanged

<sub>Type Property</sub>

A notification that an app posts when a new view appears that occupies a major portion of the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let screenChanged: UIAccessibility.Notification
```

## Discussion

Post this notification using the [UIAccessibilityPostNotification](<../post(notification_argument_).md>) function. Optionally, include a parameter that contains the accessibility element for VoiceOver to move to after processing the notification.

## See Also

### UI changes

- [UIAccessibilityLayoutChangedNotification](layoutchanged.md) — A notification that an app posts when the layout of a screen changes.
- [UIAccessibilityPageScrolledNotification](pagescrolled.md) — A notification that an app posts when a scroll action completes.
- [UIAccessibilitySwitchControlStatusDidChangeNotification](../switchcontrolstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Switch Control setting changes.
- [UIAccessibilityElementFocusedNotification](../elementfocusednotification.md) — A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [UIAccessibilityReduceTransparencyStatusDidChangeNotification](../reducetransparencystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [UIAccessibilityButtonShapesEnabledStatusDidChangeNotification](../buttonshapesenabledstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Button Shapes setting changes. _(deprecated)_
