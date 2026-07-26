---
title: UISearchTextFieldPasteItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfieldpasteitem
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfieldpasteitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfieldpasteitem.json'
content_hash: 'sha256:0bdbef3f7e52b449'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchTextFieldPasteItem

<sub>Protocol</sub>

A protocol that supports pasting tokens.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UISearchTextFieldPasteItem : UITextPasteItem
```

## Overview

When implementing [- textPasteConfigurationSupporting:transformPasteItem:](<uitextpastedelegate/textpasteconfigurationsupporting(__transform_).md>), your [UITextPasteDelegate](uitextpastedelegate.md) can decide whether to paste the item as text or as a token. If the [UITextPasteItem](uitextpasteitem.md) it receives is a [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md), you can call [- setSearchTokenResult:](<uisearchtextfieldpasteitem/setsearchtokenresult(__).md>) to prepare a token for pasting instead of text.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UITextPasteItem](uitextpasteitem.md)

## Topics

### Providing a token

- [- setSearchTokenResult:](<uisearchtextfieldpasteitem/setsearchtokenresult(__).md>) — Sets a paste item’s search token from an item provider.

## See Also

### Pasteboard support

- [UITextPasteItem](uitextpasteitem.md) — The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [UITextPasteDelegate](uitextpastedelegate.md) — The interface for handling pasting and dropping of text, using item providers.
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md) — The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.
