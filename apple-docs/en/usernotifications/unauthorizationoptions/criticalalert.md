---
title: criticalAlert
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unauthorizationoptions/criticalalert
source_url: 'https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/criticalalert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unauthorizationoptions/criticalalert.json'
content_hash: 'sha256:c470ca8437557596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNAuthorizationOptions](../unauthorizationoptions.md)

# criticalAlert

<sub>Type Property</sub>

The ability to play sounds for critical alerts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var criticalAlert: UNAuthorizationOptions { get }
```

## Discussion

Critical alerts ignore the mute switch and Do Not Disturb; the system plays a critical alert’s sound regardless of the device’s mute or Do Not Disturb settings. You can specify a custom sound and volume.

Critical alerts require a special entitlement issued by Apple.

## See Also

### Options

- [UNAuthorizationOptionBadge](badge.md) — The ability to update the app’s badge.
- [UNAuthorizationOptionSound](sound.md) — The ability to play sounds.
- [UNAuthorizationOptionAlert](alert.md) — The ability to display alerts.
- [UNAuthorizationOptionCarPlay](carplay.md) — The ability to display notifications in a CarPlay environment.
- [UNAuthorizationOptionProvidesAppNotificationSettings](providesappnotificationsettings.md) — An option indicating the system should display a button for in-app notification settings.
- [UNAuthorizationOptionProvisional](provisional.md) — The ability to post noninterrupting notifications provisionally to the Notification Center.
