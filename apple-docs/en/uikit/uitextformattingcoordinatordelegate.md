---
title: UITextFormattingCoordinatorDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextformattingcoordinatordelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingcoordinatordelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingcoordinatordelegate.json'
content_hash: 'sha256:b14f64a5c4ce241d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextFormattingCoordinatorDelegate

<sub>Protocol</sub>

The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextFormattingCoordinatorDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Updating Text Attributes

- [- updateTextAttributesWithConversionHandler:](<uitextformattingcoordinatordelegate/updatetextattributes(conversionhandler_).md>) — Applies the current font panel settings to the selected text.

## See Also

### Applying Updated Text Attributes

- [delegate](uitextformattingcoordinator/delegate.md) — The delegate of the text-formatting coordinator.
