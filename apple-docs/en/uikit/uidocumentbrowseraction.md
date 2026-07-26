---
title: UIDocumentBrowserAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowseraction
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowseraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowseraction.json'
content_hash: 'sha256:ac44b49438dc10d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentBrowserAction

<sub>Class</sub>

A custom action that you can create and add to a document browser’s Edit menu or navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIDocumentBrowserAction
```

## Overview

By default, the system provides a number of standard actions (copy, move, rename, delete, and share). To add custom actions, assign an array of [UIDocumentBrowserAction](uidocumentbrowseraction.md) objects to the browser’s [customActions](uidocumentbrowserviewcontroller/customactions.md) property.

Document browser actions can appear in either the navigation bar or the Edit menu.

- _Navigation bar_ actions appear in the navigation bar when the user places the browser into the Select mode.
- _Menu_ actions appear in the Edit Menu when the user long presses on a document or folder.

When triggered, these actions are passed the URLs of the currently selected items.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating and configuring actions

- [- initWithIdentifier:localizedTitle:availability:handler:](<uidocumentbrowseraction/init(identifier_localizedtitle_availability_handler_).md>) — Instantiates and returns a new browser action item.
- [image](uidocumentbrowseraction/image.md) — The action’s image displayed in the navigation bar.
- [supportedContentTypes](uidocumentbrowseraction/supportedcontenttypes.md) — An array of uniform type identifiers that define the types of documents that the action supports.
- [supportsMultipleItems](uidocumentbrowseraction/supportsmultipleitems.md) — A Boolean value that determines whether the action can be triggered on more than one document at a time.

### Accessing activity data

- [identifier](uidocumentbrowseraction/identifier.md) — The action’s unique identifier.
- [localizedTitle](uidocumentbrowseraction/localizedtitle.md) — The title that appears in the menu or navigation bar.
- [availability](uidocumentbrowseraction/availability-swift.property.md) — A value that defines where the action can appear (in the Edit Menu, the navigation bar, or both).
- [Availability](uidocumentbrowseraction/availability-swift.struct.md) — Values that determine where the action can appear in the document browser.

## See Also

### Related Documentation

- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — A view controller for browsing and performing actions on documents that you store locally and in the cloud.

### Adding custom actions

- [customActions](uidocumentbrowserviewcontroller/customactions.md) — Custom document browser actions.
