---
title: badge
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcontent/badge
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/badge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/badge.json'
content_hash: 'sha256:ab199581dd2e208a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# badge

<sub>Instance Property</sub>

The number that your app’s icon displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var badge: NSNumber? { get }
```

## Discussion

When the number in this property is `0`, the system doesn’t display a badge. When the number is greater than `0`, the system displays the badge with the specified number. When the value in this property is `nil`, the system leaves the current badge unchanged.

## See Also

### Reading app configuration

- [launchImageName](launchimagename.md) — The name of the image or storyboard to use when your app launches because of the notification.
- [targetContentIdentifier](targetcontentidentifier.md) — The value your app uses to determine which scene to display to handle the notification.
