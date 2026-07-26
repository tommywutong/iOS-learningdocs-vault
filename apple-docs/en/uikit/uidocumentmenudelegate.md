---
title: UIDocumentMenuDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentmenudelegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenudelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenudelegate.json'
content_hash: 'sha256:0ad01a581b1ee8a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentMenuDelegate

<sub>Protocol</sub>

A set of methods that you must implement to track user interactions with a document menu view controller.

> [!warning] Deprecated
> For more information, see [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol UIDocumentMenuDelegate : NSObjectProtocol
```

## Overview

The document menu calls the methods of this protocol when the user selects a document picker or dismisses the menu. If the user selects a document picker, set the picker’s delegate and present it.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to user actions

- [- documentMenu:didPickDocumentPicker:](<uidocumentmenudelegate/documentmenu(__didpickdocumentpicker_).md>) — Tells the delegate that the user has selected a document picker from the menu. _(deprecated)_
- [- documentMenuWasCancelled:](<uidocumentmenudelegate/documentmenuwascancelled(__).md>) — Tells the delegate that the user dismissed the document menu. _(deprecated)_

## See Also

### Getting the user-selected document picker

- [delegate](uidocumentmenuviewcontroller/delegate.md) — The document menu’s delegate. _(deprecated)_
