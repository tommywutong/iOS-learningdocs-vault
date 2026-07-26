---
title: launchImageName
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcontent/launchimagename
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/launchimagename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/launchimagename.json'
content_hash: 'sha256:3e0122b3a59a3ade'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# launchImageName

<sub>Instance Property</sub>

The name of the image or storyboard to use when your app launches because of the notification.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
var launchImageName: String { get }
```

## Discussion

If you specify a value for this property, the system displays the specified image or storyboard when the system launches your app. The string in this property must match the name of an image file or storyboard in your app’s bundle.

## See Also

### Reading app configuration

- [badge](badge.md) — The number that your app’s icon displays.
- [targetContentIdentifier](targetcontentidentifier.md) — The value your app uses to determine which scene to display to handle the notification.
