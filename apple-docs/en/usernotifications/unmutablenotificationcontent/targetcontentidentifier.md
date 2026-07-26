---
title: targetContentIdentifier
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/targetcontentidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/targetcontentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/targetcontentidentifier.json'
content_hash: 'sha256:eb0d334753385501'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# targetContentIdentifier

<sub>Instance Property</sub>

The value your app uses to determine which scene to display to handle the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var targetContentIdentifier: String? { get set }
```

## Discussion

Use this value to determine the content to show in your app when the user taps the notification.

## See Also

### Configuring app behavior

- [launchImageName](launchimagename.md) — The name of the image or storyboard to use when your app launches because of the notification.
- [badge](badge.md) — The number that your app’s icon displays.
