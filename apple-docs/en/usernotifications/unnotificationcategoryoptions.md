---
title: UNNotificationCategoryOptions
framework: User Notifications
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcategoryoptions
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategoryoptions.json'
content_hash: 'sha256:ad410240497080a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationCategoryOptions

<sub>Structure</sub>

Constants indicating how to handle notifications associated with this category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct UNNotificationCategoryOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Creating an option

- [init(rawValue:)](<unnotificationcategoryoptions/init(rawvalue_).md>) — Initializes a notification category options object using the specified raw value.

### Customizing a category

- [UNNotificationCategoryOptionAllowInCarPlay](unnotificationcategoryoptions/allowincarplay.md) — Allow CarPlay to display notifications of this type.
- [UNNotificationCategoryOptionAllowAnnouncement](unnotificationcategoryoptions/allowannouncement.md) — An option that grants Siri permission to read incoming messages out loud when the user has a compatible audio output device connected. _(deprecated)_

### Managing hidden preview behavior

- [UNNotificationCategoryOptionHiddenPreviewsShowTitle](unnotificationcategoryoptions/hiddenpreviewsshowtitle.md) — Show the notification’s title, even if the user has disabled notification previews for the app.
- [UNNotificationCategoryOptionHiddenPreviewsShowSubtitle](unnotificationcategoryoptions/hiddenpreviewsshowsubtitle.md) — Show the notification’s subtitle, even if the user has disabled notification previews for the app.

### Managing action handling behavior

- [UNNotificationCategoryOptionCustomDismissAction](unnotificationcategoryoptions/customdismissaction.md) — Send dismiss actions to the `UNUserNotificationCenter` object’s delegate for handling.

## See Also

### Getting the Options

- [options](unnotificationcategory/options.md) — Options for how to handle notifications of this type.
