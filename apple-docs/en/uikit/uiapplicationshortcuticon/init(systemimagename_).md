---
title: 'init(systemImageName:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationshortcuticon/init(systemimagename:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(systemimagename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcuticon/init%28systemimagename%3A%29.json'
content_hash: 'sha256:d24fa65cf9a5e86c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutIcon](../uiapplicationshortcuticon.md)

# init(systemImageName:)

<sub>Initializer</sub>

Creates a Home Screen quick action icon using a system symbol image.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(systemImageName: String)
```

## Parameters

- `systemImageName` — The name of the system symbol image. Use the SF Symbols app to look up the names of system symbol images. You can download this app from the design resources page at [developer.apple.com](https://developer.apple.com/design/resources/).

## Return Value

A Home Screen quick action icon initialized with the specified system symbol image.

## See Also

### Creating a quick action icon

- [+ iconWithType:](<init(type_).md>) — Creates a Home Screen quick action icon using a system-defined image.
- [+ iconWithTemplateImageName:](<init(templateimagename_).md>) — Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [+ iconWithContact:](<init(contact_).md>) — Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.
