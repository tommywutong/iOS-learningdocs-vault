---
title: UIDocumentPickerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentpickerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerdelegate.json'
content_hash: 'sha256:48d6e647e23f56e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentPickerDelegate

<sub>Protocol</sub>

A set of methods for tracking when the user selects a document or destination, or cancels the operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIDocumentPickerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to user actions

- [- documentPicker:didPickDocumentsAtURLs:](<uidocumentpickerdelegate/documentpicker(__didpickdocumentsat_).md>) — Tells the delegate that the user has selected one or more documents.
- [- documentPickerWasCancelled:](<uidocumentpickerdelegate/documentpickerwascancelled(__).md>) — Tells the delegate that the user canceled the document picker.
- [- documentPicker:didPickDocumentAtURL:](<uidocumentpickerdelegate/documentpicker(__didpickdocumentat_).md>) — Tells the delegate that the user has selected a document or a destination. _(deprecated)_

## See Also

### Getting the user-selected document

- [delegate](uidocumentpickerviewcontroller/delegate.md) — An object that acts as the delegate of the view controller.
- [allowsMultipleSelection](uidocumentpickerviewcontroller/allowsmultipleselection.md) — A Boolean value that determines whether the user can select more than one document at a time.
- [directoryURL](uidocumentpickerviewcontroller/directoryurl.md) — The initial directory that the document picker displays.
