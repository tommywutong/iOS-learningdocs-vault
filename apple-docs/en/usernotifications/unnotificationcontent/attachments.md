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
doc_path: /documentation/usernotifications/unnotificationcontent/attachments
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/attachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/attachments.json'
content_hash: 'sha256:690d8622f38dc0dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# attachments

<sub>Instance Property</sub>

The visual and audio attachments to display alongside the notification’s main content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var attachments: [UNNotificationAttachment] { get }
```

## Discussion

Use this property to retrieve the images, movies, and audio files associated with your notification’s content. A notification content app extension might use these values to add the associated content to its view controller.

## See Also

### Accessing supplementary content

- [userInfo](userinfo.md) — The custom data to associate with the notification.
