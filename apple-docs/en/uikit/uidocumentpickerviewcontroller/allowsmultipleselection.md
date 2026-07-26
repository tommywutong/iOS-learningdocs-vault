---
title: allowsMultipleSelection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentpickerviewcontroller/allowsmultipleselection
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/allowsmultipleselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/allowsmultipleselection.json'
content_hash: 'sha256:ccdab42d6adae23e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# allowsMultipleSelection

<sub>Instance Property</sub>

A Boolean value that determines whether the user can select more than one document at a time.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsMultipleSelection: Bool { get set }
```

## Discussion

By default, this property is [false](../../swift/false.md).

## See Also

### Getting the user-selected document

- [delegate](delegate.md) — An object that acts as the delegate of the view controller.
- [UIDocumentPickerDelegate](../uidocumentpickerdelegate.md) — A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [directoryURL](directoryurl.md) — The initial directory that the document picker displays.
