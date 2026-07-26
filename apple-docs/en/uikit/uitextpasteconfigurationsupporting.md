---
title: UITextPasteConfigurationSupporting
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextpasteconfigurationsupporting
source_url: 'https://developer.apple.com/documentation/uikit/uitextpasteconfigurationsupporting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpasteconfigurationsupporting.json'
content_hash: 'sha256:28830c8297a70daf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextPasteConfigurationSupporting

<sub>Protocol</sub>

The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextPasteConfigurationSupporting : UIPasteConfigurationSupporting
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)

- **Inherited By**: [UITextDroppable](uitextdroppable.md)

- **Conforming Types**: [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Setting the text paste delegate

- [pasteDelegate](uitextpasteconfigurationsupporting/pastedelegate.md) — The text paste delegate that handles pasting and dropping of text, using item providers.

## See Also

### Pasteboard support

- [UITextPasteItem](uitextpasteitem.md) — The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md) — A protocol that supports pasting tokens.
- [UITextPasteDelegate](uitextpastedelegate.md) — The interface for handling pasting and dropping of text, using item providers.
