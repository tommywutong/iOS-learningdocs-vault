---
title: 'init(type:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationshortcuticon/init(type:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcuticon/init%28type%3A%29.json'
content_hash: 'sha256:8ab6c700fdbee385'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutIcon](../uiapplicationshortcuticon.md)

# init(type:)

<sub>Initializer</sub>

Creates a Home Screen quick action icon using a system-defined image.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(type: UIApplicationShortcutIcon.IconType)
```

## Parameters

- `type` — The system-defined image to use for the icon. For a list of possible images, see the [IconType](icontype.md) enumeration.

## Return Value

A Home Screen quick action icon initialized with the specified system image.

## Discussion

Use this method to create icons for actions supported by the system. Users expect system-defined action images to be used only for the intended action.

## See Also

### Creating a quick action icon

- [+ iconWithTemplateImageName:](<init(templateimagename_).md>) — Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [+ iconWithSystemImageName:](<init(systemimagename_).md>) — Creates a Home Screen quick action icon using a system symbol image.
- [+ iconWithContact:](<init(contact_).md>) — Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.
