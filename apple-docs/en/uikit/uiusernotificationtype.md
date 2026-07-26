---
title: UIUserNotificationType
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationtype
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationtype.json'
content_hash: 'sha256:1698217f500a7813'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserNotificationType

<sub>Structure</sub>

Constants indicating how the app alerts the user when a local or push notification arrives.

> [!warning] Deprecated
> For more information, see [UIUserNotificationSettings](uiusernotificationsettings.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct UIUserNotificationType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [UIUserNotificationTypeBadge](uiusernotificationtype/badge.md) — The app badges its icon. _(deprecated)_
- [UIUserNotificationTypeSound](uiusernotificationtype/sound.md) — The app plays a sound. _(deprecated)_
- [UIUserNotificationTypeAlert](uiusernotificationtype/alert.md) — The app posts an alert. _(deprecated)_

### Initializers

- [init(rawValue:)](<uiusernotificationtype/init(rawvalue_).md>) — Creates a notification type with the specified raw value. _(deprecated)_
