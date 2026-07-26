---
title: UNNotificationPresentationOptions
framework: User Notifications
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationpresentationoptions
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationpresentationoptions.json'
content_hash: 'sha256:c1cb416a5e8f6137'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationPresentationOptions

<sub>Structure</sub>

Constants indicating how to present a notification in a foreground app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UNNotificationPresentationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [UNNotificationPresentationOptionBadge](unnotificationpresentationoptions/badge.md) — Apply the notification’s badge value to the app’s icon.
- [UNNotificationPresentationOptionBanner](unnotificationpresentationoptions/banner.md) — Present the notification as a banner.
- [UNNotificationPresentationOptionList](unnotificationpresentationoptions/list.md) — Show the notification in Notification Center.
- [UNNotificationPresentationOptionSound](unnotificationpresentationoptions/sound.md) — Play the sound associated with the notification.
- [UNNotificationPresentationOptionAlert](unnotificationpresentationoptions/alert.md) — Display the alert using the content provided by the notification. _(deprecated)_

### Initializers

- [init(rawValue:)](<unnotificationpresentationoptions/init(rawvalue_).md>) — Initializes a notification presentation options object using the specified raw value.

## See Also

### Receiving Notifications

- [- userNotificationCenter:willPresentNotification:withCompletionHandler:](<unusernotificationcenterdelegate/usernotificationcenter(__willpresent_withcompletionhandler_).md>) — Asks the delegate how to handle a notification that arrived while the app was running in the foreground.
