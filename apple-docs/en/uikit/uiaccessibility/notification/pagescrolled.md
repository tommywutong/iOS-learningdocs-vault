---
title: pageScrolled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/notification/pagescrolled
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/notification/pagescrolled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/notification/pagescrolled.json'
content_hash: 'sha256:8c02b9b208255d17'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIAccessibility](../../uiaccessibility.md) · [Notification](../notification.md)

# pageScrolled

<sub>Type Property</sub>

A notification that an app posts when a scroll action completes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let pageScrolled: UIAccessibility.Notification
```

## Discussion

This notification includes a parameter that is an [NSString](../../../foundation/nsstring.md) object that contains a description of the new scroll position. An assistive app outputs the description string in the parameter.

Use this notification to provide custom information about the contents of the screen after a user performs a VoiceOver scroll gesture. For example, a tab-based app might provide a string like `Tab 3 of 5`, or an app that displays information in pages might provide a string like `Page 19 of 27`.

When an assistive app repeatedly receives the same scroll position string, it indicates to users that scrolling can’t continue due to a border or boundary.

Post this notification after the [accessibilityScroll(_:)](<../../../objectivec/nsobject-swift.class/accessibilityscroll(__).md>) method using the [UIAccessibilityPostNotification](<../post(notification_argument_).md>) function.

## See Also

### UI changes

- [UIAccessibilityScreenChangedNotification](screenchanged.md) — A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [UIAccessibilityLayoutChangedNotification](layoutchanged.md) — A notification that an app posts when the layout of a screen changes.
- [UIAccessibilitySwitchControlStatusDidChangeNotification](../switchcontrolstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Switch Control setting changes.
- [UIAccessibilityElementFocusedNotification](../elementfocusednotification.md) — A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [UIAccessibilityReduceTransparencyStatusDidChangeNotification](../reducetransparencystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [UIAccessibilityButtonShapesEnabledStatusDidChangeNotification](../buttonshapesenabledstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Button Shapes setting changes. _(deprecated)_
