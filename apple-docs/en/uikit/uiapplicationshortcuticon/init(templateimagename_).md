---
title: 'init(templateImageName:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationshortcuticon/init(templateimagename:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(templateimagename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcuticon/init%28templateimagename%3A%29.json'
content_hash: 'sha256:2832d01d9cdde04f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutIcon](../uiapplicationshortcuticon.md)

# init(templateImageName:)

<sub>Initializer</sub>

Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(templateImageName: String)
```

## Parameters

- `templateImageName` — The name of a custom image in the app’s asset catalog. If the image isn’t in your app’s asset catalog, this method searches the app bundle for the image. You don’t need to specify the filename extension or the `@2x` or `@3x` modifiers for this name. This method retrieves the appropriate image based on the system and the available image resources.

## Return Value

A Home Screen quick action icon initialized with the specified template image provided by your app.

## Discussion

Use this method to create icons based on custom artwork that you provide. If the image name you specify doesn’t correspond to a valid image resource in your app bundle, the system won’t display an icon.

For more information about designing custom images, see [Providing images for different appearances](../providing-images-for-different-appearances.md).

## See Also

### Creating a quick action icon

- [+ iconWithType:](<init(type_).md>) — Creates a Home Screen quick action icon using a system-defined image.
- [+ iconWithSystemImageName:](<init(systemimagename_).md>) — Creates a Home Screen quick action icon using a system symbol image.
- [+ iconWithContact:](<init(contact_).md>) — Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.
