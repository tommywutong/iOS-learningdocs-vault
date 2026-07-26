---
title: UISheetPresentationControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontrollerdelegate.json'
content_hash: 'sha256:0f5e9c74c78b4be8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISheetPresentationControllerDelegate

<sub>Protocol</sub>

The interface that an object implements to respond to size changes in a sheet presentation controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UISheetPresentationControllerDelegate : UIAdaptivePresentationControllerDelegate
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)

## Topics

### Resizing the Sheet Presentation Controller

- [- sheetPresentationControllerDidChangeSelectedDetentIdentifier:](<uisheetpresentationcontrollerdelegate/sheetpresentationcontrollerdidchangeselecteddetentidentifier(__).md>) — Provides an opportunity to respond after the sheet presentation controller’s selected detent changes.

## See Also

### Managing the delegate

- [delegate](uisheetpresentationcontroller/delegate.md) — The delegate of the sheet presentation controller.
