---
title: UITextPasteItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextpasteitem
source_url: 'https://developer.apple.com/documentation/uikit/uitextpasteitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpasteitem.json'
content_hash: 'sha256:8e0f24faa420d620'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextPasteItem

<sub>Protocol</sub>

The interface for obtaining information about, and interacting with, a text item for pasting or dropping.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextPasteItem : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)

## Topics

### Accessing the text paste item’s data

- [itemProvider](uitextpasteitem/itemprovider.md) — The item provider for the item being pasted or dropped.
- [localObject](uitextpasteitem/localobject.md) — The custom local object that the copy or drag source optionally attached to the drag item.

### Getting the default attributes for a string

- [defaultAttributes](uitextpasteitem/defaultattributes.md) — The dictionary of default attributes that the system applies, during pasting or dropping, to plaintext strings from an item provider.

### Setting a text paste item’s result value

- [- setStringResult:](<uitextpasteitem/setresult(string_).md>) — Sets a text paste item’s textual value to a specified plaintext string from the item provider.
- [- setAttributedStringResult:](<uitextpasteitem/setresult(attributedstring_).md>) — Sets a text paste item’s textual value to a specified attributed string from the item provider.
- [- setAttachmentResult:](<uitextpasteitem/setresult(attachment_).md>) — Sets a text paste item’s attachment value to a specified value.
- [- setDefaultResult](<uitextpasteitem/setdefaultresult().md>) — Sets the text paste item’s value to the default value based on the item provider’s data.
- [- setNoResult](<uitextpasteitem/setnoresult().md>) — Sets the text paste item’s textual value to not include data from the item provider.

## See Also

### Pasteboard support

- [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md) — A protocol that supports pasting tokens.
- [UITextPasteDelegate](uitextpastedelegate.md) — The interface for handling pasting and dropping of text, using item providers.
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md) — The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.
