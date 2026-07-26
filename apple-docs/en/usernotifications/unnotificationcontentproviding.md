---
title: UNNotificationContentProviding
framework: User Notifications
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcontentproviding
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontentproviding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontentproviding.json'
content_hash: 'sha256:e2d0bc69475a6090'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationContentProviding

<sub>Protocol</sub>

A protocol the system uses to provide context relevant to user notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol UNNotificationContentProviding : NSObjectProtocol
```

## Overview

The system allows only objects in the Apple SDK that conform to `UNNotificationContentProviding`. The system ignores objects outside of the Apple SDK that your app conforms to `UNNotificationContentProviding`.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UNNotificationAttributedMessageContext](unnotificationattributedmessagecontext.md)

## See Also

### Notification content

- [Implementing communication notifications](implementing-communication-notifications.md) — Configure and display your app’s communication notifications by using intents.
- [UNNotificationActionIcon](unnotificationactionicon.md) — An icon associated with an action.
- [UNMutableNotificationContent](unmutablenotificationcontent.md) — The editable content for a notification.
- [UNNotificationContent](unnotificationcontent.md) — The uneditable content of a notification.
- [UNNotificationAttachment](unnotificationattachment.md) — A media file associated with a notification.
- [UNNotificationSound](unnotificationsound.md) — The sound played upon delivery of a notification.
- [UNNotificationSoundName](unnotificationsoundname.md) — A string providing the name of a sound file.
