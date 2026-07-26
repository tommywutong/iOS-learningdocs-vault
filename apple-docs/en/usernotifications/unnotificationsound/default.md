---
title: default
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsound/default
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsound/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsound/default.json'
content_hash: 'sha256:cfe5b05c8c6f9b2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSound](../unnotificationsound.md)

# default

<sub>Type Property</sub>

Returns an object representing the default sound for notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@NSCopying class var `default`: UNNotificationSound { get }
```

## Return Value

A sound object that represents the default notification sound.

## See Also

### Creating Notification Sounds

- [+ soundNamed:](<init(named_).md>) — Creates a sound object that represents a custom sound file.
