---
title: UITextItem.MenuConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextitem/menuconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitextitem/menuconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextitem/menuconfiguration.json'
content_hash: 'sha256:c88c117b526feecb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextItem](../uitextitem.md)

# UITextItem.MenuConfiguration

<sub>Class</sub>

An object that describes what type of menu and preview to show for a text item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class MenuConfiguration
```

## Overview

Create and return a menu configuration for a text item in [- textView:menuConfigurationForTextItem:defaultMenu:](<../uitextviewdelegate/textview(__menuconfigurationfor_defaultmenu_).md>) to provide a custom menu that the system shows when someone interacts with the text item. Provide a custom view for the item’s preview, or specify that the system displays a default preview.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Creating a menu configuration

- [init(preview:menu:)](<menuconfiguration/init(preview_menu_).md>) — Creates a text item menu configuration with the specified menu and preview.
- [Preview](menuconfiguration/preview.md) — Constants that indicate what type of preview to display alongside the text item’s menu.

## See Also

### Text actions and menus

- [UITextItem](../uitextitem.md) — An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.
- [UITextViewDelegate](../uitextviewdelegate.md) — The methods for receiving editing-related messages for text view objects.
