---
title: UNNotificationSoundName
framework: User Notifications
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsoundname
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsoundname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsoundname.json'
content_hash: 'sha256:e434434f426226de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationSoundName

<sub>Structure</sub>

A string providing the name of a sound file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UNNotificationSoundName
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<unnotificationsoundname/init(__).md>) — Creates a notification sound name using the string parameter.
- [init(rawValue:)](<unnotificationsoundname/init(rawvalue_).md>) — Creates a notification sound name using the string parameter.

## See Also

### Notification content

- [Implementing communication notifications](implementing-communication-notifications.md) — Configure and display your app’s communication notifications by using intents.
- [UNNotificationContentProviding](unnotificationcontentproviding.md) — A protocol the system uses to provide context relevant to user notifications.
- [UNNotificationActionIcon](unnotificationactionicon.md) — An icon associated with an action.
- [UNMutableNotificationContent](unmutablenotificationcontent.md) — The editable content for a notification.
- [UNNotificationContent](unnotificationcontent.md) — The uneditable content of a notification.
- [UNNotificationAttachment](unnotificationattachment.md) — A media file associated with a notification.
- [UNNotificationSound](unnotificationsound.md) — The sound played upon delivery of a notification.
