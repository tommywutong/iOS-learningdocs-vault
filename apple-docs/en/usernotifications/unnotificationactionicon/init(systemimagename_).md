---
title: 'init(systemImageName:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationactionicon/init(systemimagename:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationactionicon/init(systemimagename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationactionicon/init%28systemimagename%3A%29.json'
content_hash: 'sha256:e3ff08ce5ce6b5b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationActionIcon](../unnotificationactionicon.md)

# init(systemImageName:)

<sub>Initializer</sub>

Creates an action icon by using a system symbol image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(systemImageName: String)
```

## Parameters

- `systemImageName` — The name of the system symbol image. Use the SF Symbols app to look up the names of system symbol images. Download this app from the design resources page at [developer.apple.com](https://developer.apple.com/design/resources/).

## Return Value

An action icon that the system initializes with the system symbol image that your app specifies.

## See Also

### Essentials

- [+ iconWithTemplateImageName:](<init(templateimagename_).md>) — Creates an action icon based on an image in your app’s bundle, preferably in an asset catalog.
