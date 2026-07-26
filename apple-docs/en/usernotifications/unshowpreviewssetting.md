---
title: UNShowPreviewsSetting
framework: User Notifications
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unshowpreviewssetting
source_url: 'https://developer.apple.com/documentation/usernotifications/unshowpreviewssetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unshowpreviewssetting.json'
content_hash: 'sha256:cff9ece1d32145d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNShowPreviewsSetting

<sub>Enumeration</sub>

Constants indicating the style previewing a notification’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum UNShowPreviewsSetting
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Preview Styes

- [UNShowPreviewsSettingAlways](unshowpreviewssetting/always.md) — The notification’s content is always shown, even when the device is locked.
- [UNShowPreviewsSettingWhenAuthenticated](unshowpreviewssetting/whenauthenticated.md) — The notification’s content is shown only when the device is unlocked.
- [UNShowPreviewsSettingNever](unshowpreviewssetting/never.md) — The notification’s content is never shown, even when the device is unlocked

### Initializers

- [init(rawValue:)](<unshowpreviewssetting/init(rawvalue_).md>)

## See Also

### Getting Interface Settings

- [alertStyle](unnotificationsettings/alertstyle.md) — The type of alert that the app may display when the device is unlocked.
- [UNAlertStyle](unalertstyle.md) — Constants indicating the presentation styles for alerts.
- [showPreviewsSetting](unnotificationsettings/showpreviewssetting.md) — The setting that indicates whether the app shows a preview of the notification’s content.
- [providesAppNotificationSettings](unnotificationsettings/providesappnotificationsettings.md) — A Boolean value indicating the system displays a button for in-app notification settings.
