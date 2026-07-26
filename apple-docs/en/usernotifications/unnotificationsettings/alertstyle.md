---
title: alertStyle
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings/alertstyle
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings/alertstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings/alertstyle.json'
content_hash: 'sha256:359c011eb4252449'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSettings](../unnotificationsettings.md)

# alertStyle

<sub>Instance Property</sub>

The type of alert that the app may display when the device is unlocked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var alertStyle: UNAlertStyle { get }
```

## Discussion

When alerts are authorized, this property specifies the presentation style for alerts when the device is unlocked. The user may choose to display alerts as automatically disappearing banners or as modal windows that require explicit dismissal. The user may also choose not to display alerts at all.

## See Also

### Getting Interface Settings

- [UNAlertStyle](../unalertstyle.md) — Constants indicating the presentation styles for alerts.
- [showPreviewsSetting](showpreviewssetting.md) — The setting that indicates whether the app shows a preview of the notification’s content.
- [UNShowPreviewsSetting](../unshowpreviewssetting.md) — Constants indicating the style previewing a notification’s content.
- [providesAppNotificationSettings](providesappnotificationsettings.md) — A Boolean value indicating the system displays a button for in-app notification settings.
