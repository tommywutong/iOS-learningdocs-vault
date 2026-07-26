---
title: UIContextualAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextualaction
source_url: 'https://developer.apple.com/documentation/uikit/uicontextualaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextualaction.json'
content_hash: 'sha256:511e1218529293ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextualAction

<sub>Class</sub>

An action to display when the user swipes a table row.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIContextualAction
```

## Overview

Create [UIContextualAction](uicontextualaction.md) objects to define the types of actions that can be performed when the user swipes left or right on a table row. Use your actions to initialize a [UISwipeActionsConfiguration](uiswipeactionsconfiguration.md) object in your table view delegate object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating the contextual action

- [+ contextualActionWithStyle:title:handler:](<uicontextualaction/init(style_title_handler_).md>) — Creates a new contextual action with the specified title and handler.

### Configuring the appearance

- [title](uicontextualaction/title.md) — The title displayed on the action button.
- [backgroundColor](uicontextualaction/backgroundcolor.md) — The background color of the action button.
- [image](uicontextualaction/image.md) — The image to display in the action button.

### Getting the configuration details

- [handler](uicontextualaction/handler-swift.property.md) — The handler block to execute when the user selects the action.
- [Handler](uicontextualaction/handler-swift.typealias.md) — The handler block to call in response to the selection of an action.
- [style](uicontextualaction/style-swift.property.md) — The style that applies to the action button.
- [Style](uicontextualaction/style-swift.enum.md) — Constants indicating the style information that applies to the action button.

## See Also

### Row actions

- [UISwipeActionsConfiguration](uiswipeactionsconfiguration.md) — The set of actions to perform when swiping on rows of a table.
- [UITableViewRowAction](uitableviewrowaction.md) — A single action to present when the user swipes horizontally in a table row. _(deprecated)_
