---
title: resumeAssistiveTechnology
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/notification/resumeassistivetechnology
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/notification/resumeassistivetechnology'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/notification/resumeassistivetechnology.json'
content_hash: 'sha256:9ab5e29963dc2a78'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIAccessibility](../../uiaccessibility.md) · [Notification](../notification.md)

# resumeAssistiveTechnology

<sub>Type Property</sub>

A notification that resumes an assistive app’s operations temporarily.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let resumeAssistiveTechnology: UIAccessibility.Notification
```

## Discussion

When posting the notification, specify the assistive app to resume as the parameter. You must post this notification to balance out the previous posting of a [UIAccessibilityPauseAssistiveTechnologyNotification](pauseassistivetechnology.md) notification. Post this notification using the [UIAccessibilityPostNotification](<../post(notification_argument_).md>) function.

## See Also

### Assistive apps

- [UIAccessibilityAssistiveTouchStatusDidChangeNotification](../assistivetouchstatusdidchangenotification.md) — A notification that indicates a change in the status of AssistiveTouch.
- [UIAccessibilityGuidedAccessStatusDidChangeNotification](../guidedaccessstatusdidchangenotification.md) — A notification that indicates when a Guided Access session starts or ends.
- [UIAccessibilityPauseAssistiveTechnologyNotification](pauseassistivetechnology.md) — A notification that pauses an assistive app’s operations temporarily.
- [AssistiveTechnologyIdentifier](../assistivetechnologyidentifier.md) — Identifiers for assistive apps.
