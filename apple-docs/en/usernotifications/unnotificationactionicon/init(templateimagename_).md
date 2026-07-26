---
title: 'init(templateImageName:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationactionicon/init(templateimagename:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationactionicon/init(templateimagename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationactionicon/init%28templateimagename%3A%29.json'
content_hash: 'sha256:e71ea11e63990150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationActionIcon](../unnotificationactionicon.md)

# init(templateImageName:)

<sub>Initializer</sub>

Creates an action icon based on an image in your app’s bundle, preferably in an asset catalog.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(templateImageName: String)
```

## Parameters

- `templateImageName` — The name of a custom image in the app’s asset catalog. If the image isn’t in your app’s asset catalog, this method searches the app bundle for the image. You don’t need to specify the filename extension or the `@2x` or `@3x` modifiers for this name. This method retrieves the appropriate image based on the system and the available image resources.

## Return Value

An action icon initialized with the specified template image provided by your app.

## See Also

### Essentials

- [+ iconWithSystemImageName:](<init(systemimagename_).md>) — Creates an action icon by using a system symbol image.
