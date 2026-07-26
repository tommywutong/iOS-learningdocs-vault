---
title: announcement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/notification/announcement
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/notification/announcement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/notification/announcement.json'
content_hash: 'sha256:8d32b68513af877a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIAccessibility](../../uiaccessibility.md) · [Notification](../notification.md)

# announcement

<sub>Type Property</sub>

A notification that an app posts when it needs to convey an announcement to the assistive app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let announcement: UIAccessibility.Notification
```

## Discussion

This notification includes a parameter that is an [NSString](../../../foundation/nsstring.md) object that contains the announcement. An assistive app outputs the announcement string in the parameter.

Use this notification to provide accessibility information about events that don’t update the app’s UI, or that update the UI only briefly.

Post this notification using the [UIAccessibilityPostNotification](<../post(notification_argument_).md>) function.

## See Also

### VoiceOver

- [UIAccessibilityVoiceOverStatusDidChangeNotification](../voiceoverstatusdidchangenotification.md) — A notification that UIKit posts when VoiceOver starts or stops.
- [UIAccessibilityAnnouncementDidFinishNotification](../announcementdidfinishnotification.md) — A notification that UIKit posts when the system finishes reading an announcement.
- [UIAccessibilityVoiceOverStatusChanged](../../uiaccessibilityvoiceoverstatuschanged.md) — A notification that UIKit posts when VoiceOver starts or stops. _(deprecated)_
