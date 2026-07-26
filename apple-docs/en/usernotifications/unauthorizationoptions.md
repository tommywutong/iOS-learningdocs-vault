---
title: UNAuthorizationOptions
framework: User Notifications
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unauthorizationoptions
source_url: 'https://developer.apple.com/documentation/usernotifications/unauthorizationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unauthorizationoptions.json'
content_hash: 'sha256:25ed38e0ebb0fd07'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNAuthorizationOptions

<sub>Structure</sub>

Options that determine the authorized features of local and remote notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UNAuthorizationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Options

- [UNAuthorizationOptionBadge](unauthorizationoptions/badge.md) — The ability to update the app’s badge.
- [UNAuthorizationOptionSound](unauthorizationoptions/sound.md) — The ability to play sounds.
- [UNAuthorizationOptionAlert](unauthorizationoptions/alert.md) — The ability to display alerts.
- [UNAuthorizationOptionCarPlay](unauthorizationoptions/carplay.md) — The ability to display notifications in a CarPlay environment.
- [UNAuthorizationOptionCriticalAlert](unauthorizationoptions/criticalalert.md) — The ability to play sounds for critical alerts.
- [UNAuthorizationOptionProvidesAppNotificationSettings](unauthorizationoptions/providesappnotificationsettings.md) — An option indicating the system should display a button for in-app notification settings.
- [UNAuthorizationOptionProvisional](unauthorizationoptions/provisional.md) — The ability to post noninterrupting notifications provisionally to the Notification Center.

### Initializers

- [init(rawValue:)](<unauthorizationoptions/init(rawvalue_).md>) — Initializes an authorization options constant using the specified raw value.

### Deprecated

- [UNAuthorizationOptionAnnouncement](unauthorizationoptions/announcement.md) — The ability for Siri to automatically read out messages over AirPods. _(deprecated)_
- [UNAuthorizationOptionTimeSensitive](unauthorizationoptions/timesensitive.md) _(deprecated)_

## See Also

### Requesting authorization

- [- requestAuthorizationWithOptions:completionHandler:](<unusernotificationcenter/requestauthorization(options_completionhandler_).md>) — Requests a person’s authorization to allow local and remote notifications for your app.
