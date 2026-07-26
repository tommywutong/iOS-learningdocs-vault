---
title: attachments
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/attachments
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/attachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/attachments.json'
content_hash: 'sha256:9370481fcfd7f9b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# attachments

<sub>Instance Property</sub>

The visual and audio attachments to display alongside the notification’s main content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var attachments: [UNNotificationAttachment] { get set }
```

## Discussion

Use this property to include images or movies, or to include playable audio files, with the contents of an alert. The system displays the attachments alongside the title and body of your alert. You can also customize the presentation of attachments using a notification content app extension.

All attachments must reside locally on the current device before your app adds them. For local notifications, modify this property before scheduling the notification. For remote notifications, use a notification service app extension to locate and download the specified files and modify the notification content before it’s delivered.

For more information on how to specify attachments, see [UNNotificationAttachment](../unnotificationattachment.md).

## See Also

### Providing supplementary content

- [userInfo](userinfo.md) — The custom data to associate with the notification.
