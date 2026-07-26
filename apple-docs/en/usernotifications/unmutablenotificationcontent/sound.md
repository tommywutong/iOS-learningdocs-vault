---
title: sound
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/sound
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/sound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/sound.json'
content_hash: 'sha256:4834fd25f48c7eef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# sound

<sub>Instance Property</sub>

The sound that plays when the system delivers the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@NSCopying var sound: UNNotificationSound? { get set }
```

## Discussion

Use this property to specify the sound that you want played when the notification arrives. If your app isn’t authorized to play sounds for notifications, the system ignores this property.

For information on how to specify sounds for your notifications, see [UNNotificationSound](../unnotificationsound.md).

## See Also

### Integrating with the system

- [interruptionLevel](interruptionlevel.md) — The notification’s importance and required delivery timing.
- [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md) — Constants that indicate the importance and delivery timing of a notification.
- [relevanceScore](relevancescore.md) — The score the system uses to determine if the notification is the summary’s featured notification.
- [filterCriteria](filtercriteria.md) — The criteria the system evaluates to determine if it displays the notification in the current Focus.
