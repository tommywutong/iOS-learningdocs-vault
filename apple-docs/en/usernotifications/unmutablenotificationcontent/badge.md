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
doc_path: /documentation/usernotifications/unmutablenotificationcontent/badge
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/badge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/badge.json'
content_hash: 'sha256:49698ad81a23ec2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# badge

<sub>Instance Property</sub>

The number that your app’s icon displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var badge: NSNumber? { get set }
```

## Discussion

Use this property to specify the number to apply to the app’s icon when the notification arrives. If your app isn’t authorized to display badge-based notifications, the system ignores this property.

Specify the number `0` to remove the current badge, if present. Specify a number greater than `0` to display a badge with that number. Specify `nil` to leave the current badge unchanged.

## See Also

### Configuring app behavior

- [launchImageName](launchimagename.md) — The name of the image or storyboard to use when your app launches because of the notification.
- [targetContentIdentifier](targetcontentidentifier.md) — The value your app uses to determine which scene to display to handle the notification.
