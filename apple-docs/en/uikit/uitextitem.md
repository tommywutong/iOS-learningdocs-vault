---
title: UITextItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextitem
source_url: 'https://developer.apple.com/documentation/uikit/uitextitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextitem.json'
content_hash: 'sha256:c4c28eeb400f14e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextItem

<sub>Class</sub>

An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITextItem
```

## Overview

A text item represents a link with a URL destination, a custom tag for a topic that you specify in your app, or a text attachment in a text view. In your text view’s [UITextViewDelegate](uitextviewdelegate.md), implement [- textView:primaryActionForTextItem:defaultAction:](<uitextviewdelegate/textview(__primaryactionfor_defaultaction_).md>) to provide a custom action when someone interacts with a text item. Implement [- textView:menuConfigurationForTextItem:defaultMenu:](<uitextviewdelegate/textview(__menuconfigurationfor_defaultmenu_).md>) to provide a custom menu for a text item.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Specifying the content type

- [content](uitextitem/content-swift.property.md) — The content type and related value of the text item.
- [Content](uitextitem/content-swift.enum.md) — Constants that describe and capture the type of content a text item represents along with a specific related value.

### Specifying the range

- [range](uitextitem/range.md) — The range that delineates the text item in an attributed string.

### Creating a menu

- [MenuConfiguration](uitextitem/menuconfiguration.md) — An object that describes what type of menu and preview to show for a text item.

## See Also

### Text actions and menus

- [MenuConfiguration](uitextitem/menuconfiguration.md) — An object that describes what type of menu and preview to show for a text item.
- [UITextViewDelegate](uitextviewdelegate.md) — The methods for receiving editing-related messages for text view objects.
