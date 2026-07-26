---
title: 'documentPickerWasCancelled(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentpickerdelegate/documentpickerwascancelled(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/documentpickerwascancelled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerdelegate/documentpickerwascancelled%28_%3A%29.json'
content_hash: 'sha256:6d622f9a24ba5e19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerDelegate](../uidocumentpickerdelegate.md)

# documentPickerWasCancelled(_:)

<sub>Instance Method</sub>

Tells the delegate that the user canceled the document picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentPickerWasCancelled(_ controller: UIDocumentPickerViewController)
```

## Parameters

- `controller` — The document picker that called this method.

## See Also

### Responding to user actions

- [- documentPicker:didPickDocumentsAtURLs:](<documentpicker(__didpickdocumentsat_).md>) — Tells the delegate that the user has selected one or more documents.
- [- documentPicker:didPickDocumentAtURL:](<documentpicker(__didpickdocumentat_).md>) — Tells the delegate that the user has selected a document or a destination. _(deprecated)_
