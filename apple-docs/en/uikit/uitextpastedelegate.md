---
title: UITextPasteDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextpastedelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextpastedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpastedelegate.json'
content_hash: 'sha256:278159b4207de879'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextPasteDelegate

<sub>Protocol</sub>

The interface for handling pasting and dropping of text, using item providers.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextPasteDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Preparing to paste a text paste item

- [- textPasteConfigurationSupporting:transformPasteItem:](<uitextpastedelegate/textpasteconfigurationsupporting(__transform_).md>) — Tells the delegate to transform the pasted or dropped text item.

### Pasting the text paste item

- [- textPasteConfigurationSupporting:combineItemAttributedStrings:forRange:](<uitextpastedelegate/textpasteconfigurationsupporting(__combineitemattributedstrings_for_).md>) — Asks the delegate to combine multiple strings into a single attributed string.
- [- textPasteConfigurationSupporting:performPasteOfAttributedString:toRange:](<uitextpastedelegate/textpasteconfigurationsupporting(__performpasteof_to_).md>) — Asks the delegate to explicitly handle the final incorporation of a pasted or dropped string of text into the text view.

### Animating the paste operation

- [- textPasteConfigurationSupporting:shouldAnimatePasteOfAttributedString:toRange:](<uitextpastedelegate/textpasteconfigurationsupporting(__shouldanimatepasteof_to_).md>) — Asks the delegate if the paste or drop operation should be animated.

## See Also

### Pasteboard support

- [UITextPasteItem](uitextpasteitem.md) — The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md) — A protocol that supports pasting tokens.
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md) — The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.
