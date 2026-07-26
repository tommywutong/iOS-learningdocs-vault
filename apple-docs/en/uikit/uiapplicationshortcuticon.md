---
title: UIApplicationShortcutIcon
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationshortcuticon
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcuticon.json'
content_hash: 'sha256:3ffaeb9d33880102'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIApplicationShortcutIcon

<sub>Class</sub>

An image you can optionally associate with a Home Screen quick action to improve its appearance and usability.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIApplicationShortcutIcon
```

## Overview

To associate an icon with a quick action, pass it to the quick action item’s initialization method, as described in [UIApplicationShortcutItem](uiapplicationshortcutitem.md).

There are three types of quick action icon:

- An icon from a system-provided library of common types, as described in the [IconType](uiapplicationshortcuticon/icontype.md) enumeration
- An icon derived from a custom template image in your app’s bundle and preferably in an asset catalog (see [Managing assets with asset catalogs](../xcode/managing-assets-with-asset-catalogs.md))
- An icon representing a contact in the user’s address book, which you access through the [Contacts UI](../contactsui.md) framework

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a quick action icon

- [+ iconWithType:](<uiapplicationshortcuticon/init(type_).md>) — Creates a Home Screen quick action icon using a system-defined image.
- [+ iconWithTemplateImageName:](<uiapplicationshortcuticon/init(templateimagename_).md>) — Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [+ iconWithSystemImageName:](<uiapplicationshortcuticon/init(systemimagename_).md>) — Creates a Home Screen quick action icon using a system symbol image.
- [+ iconWithContact:](<uiapplicationshortcuticon/init(contact_).md>) — Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.

### Constants

- [IconType](uiapplicationshortcuticon/icontype.md) — Constants for system-provided icons.

## See Also

### Home Screen quick actions

- [Add Home Screen quick actions](add-home-screen-quick-actions.md) — Expose commonly used functionality with static or dynamic 3D Touch Home Screen quick actions.
- [UIApplicationShortcutItem](uiapplicationshortcutitem.md) — An application shortcut item, also called a Home Screen dynamic quick action, that specifies a user-initiated action for your app.
- [UIMutableApplicationShortcutItem](uimutableapplicationshortcutitem.md) — A mutable Home Screen dynamic quick action, which is an item that specifies a configurable user-initiated action for your app.
