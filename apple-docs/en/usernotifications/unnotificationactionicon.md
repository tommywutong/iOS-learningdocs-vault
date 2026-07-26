---
title: UNNotificationActionIcon
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationactionicon
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationactionicon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationactionicon.json'
content_hash: 'sha256:be790537d6eead9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationActionIcon

<sub>Class</sub>

An icon associated with an action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNNotificationActionIcon
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Essentials

- [+ iconWithSystemImageName:](<unnotificationactionicon/init(systemimagename_).md>) — Creates an action icon by using a system symbol image.
- [+ iconWithTemplateImageName:](<unnotificationactionicon/init(templateimagename_).md>) — Creates an action icon based on an image in your app’s bundle, preferably in an asset catalog.

### Initializers

- [init(coder:)](<unnotificationactionicon/init(coder_).md>)

## See Also

### Notification content

- [Implementing communication notifications](implementing-communication-notifications.md) — Configure and display your app’s communication notifications by using intents.
- [UNNotificationContentProviding](unnotificationcontentproviding.md) — A protocol the system uses to provide context relevant to user notifications.
- [UNMutableNotificationContent](unmutablenotificationcontent.md) — The editable content for a notification.
- [UNNotificationContent](unnotificationcontent.md) — The uneditable content of a notification.
- [UNNotificationAttachment](unnotificationattachment.md) — A media file associated with a notification.
- [UNNotificationSound](unnotificationsound.md) — The sound played upon delivery of a notification.
- [UNNotificationSoundName](unnotificationsoundname.md) — A string providing the name of a sound file.
