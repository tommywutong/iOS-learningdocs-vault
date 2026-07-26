---
title: UNAlertStyle
framework: User Notifications
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unalertstyle
source_url: 'https://developer.apple.com/documentation/usernotifications/unalertstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unalertstyle.json'
content_hash: 'sha256:348883d906362e3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNAlertStyle

<sub>Enumeration</sub>

Constants indicating the presentation styles for alerts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum UNAlertStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Presentation Styles

- [UNAlertStyleNone](unalertstyle/none.md) — No alert.
- [UNAlertStyleBanner](unalertstyle/banner.md) — Banner alerts.
- [UNAlertStyleAlert](unalertstyle/alert.md) — Modal alerts.

### Initializers

- [init(rawValue:)](<unalertstyle/init(rawvalue_).md>)

## See Also

### Getting Interface Settings

- [alertStyle](unnotificationsettings/alertstyle.md) — The type of alert that the app may display when the device is unlocked.
- [showPreviewsSetting](unnotificationsettings/showpreviewssetting.md) — The setting that indicates whether the app shows a preview of the notification’s content.
- [UNShowPreviewsSetting](unshowpreviewssetting.md) — Constants indicating the style previewing a notification’s content.
- [providesAppNotificationSettings](unnotificationsettings/providesappnotificationsettings.md) — A Boolean value indicating the system displays a button for in-app notification settings.
