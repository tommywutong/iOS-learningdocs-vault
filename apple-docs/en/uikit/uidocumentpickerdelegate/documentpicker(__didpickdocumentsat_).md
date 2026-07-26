---
title: 'documentPicker(_:didPickDocumentsAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentpickerdelegate/documentpicker(_:didpickdocumentsat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/documentpicker(_:didpickdocumentsat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerdelegate/documentpicker%28_%3Adidpickdocumentsat%3A%29.json'
content_hash: 'sha256:2be69a3a8306c941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerDelegate](../uidocumentpickerdelegate.md)

# documentPicker(_:didPickDocumentsAt:)

<sub>Instance Method</sub>

Tells the delegate that the user has selected one or more documents.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentsAt urls: [URL])
```

## Parameters

- `controller` — The document picker that called this method.

- `urls` — The URLs of the selected documents.

## Discussion

The meaning of the provided URLs varies depending on the document picker’s mode:

- `UIDocumentPickerModeImport`

The URLs refer to a copy of the selected documents. These documents are temporary files. They remain available only until your application terminates. To keep a permanent copy, move these files to a permanent location inside your sandbox.

- `UIDocumentPickerModeOpen`

The URLs refer to the selected documents.

- `UIDocumentPickerModeExportToService`

The URLs refer to new copies of the exported documents at the selected destination.

- `UIDocumentPickerModeMoveToService`

The URLs refer to the documents’ new locations.

The provided URLs are security-scoped, referring to files outside your app’s sandbox. For more about working with external, security-scoped URLs, see [Requirements](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/AccessingDocuments/AccessingDocuments.html#//apple_ref/doc/uid/TP40014451-CH2-SW3) in the [Document Picker Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014451).

## See Also

### Responding to user actions

- [- documentPickerWasCancelled:](<documentpickerwascancelled(__).md>) — Tells the delegate that the user canceled the document picker.
- [- documentPicker:didPickDocumentAtURL:](<documentpicker(__didpickdocumentat_).md>) — Tells the delegate that the user has selected a document or a destination. _(deprecated)_
