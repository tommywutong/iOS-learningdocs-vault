---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentpickerviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/delegate.json'
content_hash: 'sha256:e61a734a75fd1579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# delegate

<sub>Instance Property</sub>

An object that acts as the delegate of the view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIDocumentPickerDelegate)? { get set }
```

## Discussion

The delegate must adopt the [UIDocumentPickerDelegate](../uidocumentpickerdelegate.md) protocol.

## See Also

### Getting the user-selected document

- [UIDocumentPickerDelegate](../uidocumentpickerdelegate.md) — A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether the user can select more than one document at a time.
- [directoryURL](directoryurl.md) — The initial directory that the document picker displays.
