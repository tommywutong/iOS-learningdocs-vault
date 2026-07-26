---
title: UIAccessibility.Notification
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/notification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/notification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/notification.json'
content_hash: 'sha256:5c9d114571b04b33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# UIAccessibility.Notification

<sub>Structure</sub>

An accessibility notification that an app can send.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct Notification
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Notifications

- [UIAccessibilityAnnouncementNotification](notification/announcement.md) — A notification that an app posts when it needs to convey an announcement to the assistive app.
- [UIAccessibilityLayoutChangedNotification](notification/layoutchanged.md) — A notification that an app posts when the layout of a screen changes.
- [UIAccessibilityScreenChangedNotification](notification/screenchanged.md) — A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [UIAccessibilityPageScrolledNotification](notification/pagescrolled.md) — A notification that an app posts when a scroll action completes.
- [UIAccessibilityPauseAssistiveTechnologyNotification](notification/pauseassistivetechnology.md) — A notification that pauses an assistive app’s operations temporarily.
- [UIAccessibilityResumeAssistiveTechnologyNotification](notification/resumeassistivetechnology.md) — A notification that resumes an assistive app’s operations temporarily.
- [AssistiveTechnologyIdentifier](assistivetechnologyidentifier.md) — Identifiers for assistive apps.

### Initializer

- [init(rawValue:)](<notification/init(rawvalue_).md>) — Creates an accessibility notification with the specified raw value.

## See Also

### Handling notifications

- [Notification names](../notification-names.md) — The names of notifications that the accessibility system generates.
- [Notification dictionary keys](../notification-dictionary-keys.md) — Handle notifications with keys in the user info dictionary.
- [UIAccessibilityPostNotification](<post(notification_argument_).md>) — Posts a notification to assistive apps.
