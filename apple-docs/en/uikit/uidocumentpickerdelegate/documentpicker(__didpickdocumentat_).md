---
title: 'documentPicker(_:didPickDocumentAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentpickerdelegate/documentpicker(_:didpickdocumentat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/documentpicker(_:didpickdocumentat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerdelegate/documentpicker%28_%3Adidpickdocumentat%3A%29.json'
content_hash: 'sha256:0f5f49ba5d30a12a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerDelegate](../uidocumentpickerdelegate.md)

# documentPicker(_:didPickDocumentAt:)

<sub>Instance Method</sub>

Tells the delegate that the user has selected a document or a destination.

> [!warning] Deprecated
> Use the [- documentPicker:didPickDocumentsAtURLs:](<documentpicker(__didpickdocumentsat_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentAt url: URL)
```

## Parameters

- `controller` — The document picker that called this method.

- `url` — The URL of the selected document or destination.

## Discussion

The meaning of the provided URL varies depending on the document picker’s mode:

- `UIDocumentPickerModeImport`

The URL refers to a copy of the selected document. This document is a temporary file. It remains available only until your application terminates. To keep a permanent copy, you must move this file to a permanent location inside your sandbox.

- `UIDocumentPickerModeOpen`

The URL refers to the selected document. The provided URL is a security-scoped URL referring to a file outside your app’s sandbox. For more information on working with external, security-scoped URLs, see [Requirements](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/AccessingDocuments/AccessingDocuments.html#//apple_ref/doc/uid/TP40014451-CH2-SW3).

- `UIDocumentPickerModeExportToService`

The URL refers to the new copy of the exported document at the selected destination. This URL refers to a file outside your app’s sandbox. You cannot access this copy; the URL is passed only to indicate success.

- `UIDocumentPickerModeMoveToService`

The URL refers to the document’s new location. The provided URL is a security-scoped URL referring to a file outside your app’s sandbox. For more information on working with external, security-scoped URLs, see [Requirements](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/AccessingDocuments/AccessingDocuments.html#//apple_ref/doc/uid/TP40014451-CH2-SW3).

## See Also

### Responding to user actions

- [- documentPicker:didPickDocumentsAtURLs:](<documentpicker(__didpickdocumentsat_).md>) — Tells the delegate that the user has selected one or more documents.
- [- documentPickerWasCancelled:](<documentpickerwascancelled(__).md>) — Tells the delegate that the user canceled the document picker.
