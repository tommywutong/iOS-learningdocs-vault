---
title: 'prepareForPresentation(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentpickerextensionviewcontroller/prepareforpresentation(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/prepareforpresentation(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerextensionviewcontroller/prepareforpresentation%28in%3A%29.json'
content_hash: 'sha256:8d89536edd8bae22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md)

# prepareForPresentation(in:)

<sub>Instance Method</sub>

Performs any custom configuration of the document picker view controller.

> [!warning] Deprecated
> For more information, see [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func prepareForPresentation(in mode: UIDocumentPickerMode)
```

## Parameters

- `mode` — The type of file-transfer operation that the document picker performs. For a list of valid modes, see `Document Picker Modes`.

## Discussion

The system calls this method when a host app presents a document picker view controller for your Document Picker extension. Override this method to provide a custom user interface based on the provided mode.

Different modes may require different user interfaces. For example, the UIDocumentPickerModeImport and UIDocumentPickerModeOpen modes should let the user explore the available documents, whereas the UIDocumentPickerModeExportToService and UIDocumentPickerModeMoveToService modes let the user select the destination.

When overriding this method, examine the mode and present an appropriate user interface for the task at hand. If the differences between the modes are significant, consider creating separate child view controllers for each mode and then present the appropriate child in this method.

If your extension can manage multiple file types, check the [validTypes](validtypes.md) property and make sure you are presenting only files that match one or more of the specified types.

## See Also

### Managing the user interface

- [- dismissGrantingAccessToURL:](<dismissgrantingaccess(to_).md>) — Dismisses the document picker. _(deprecated)_
- [documentPickerMode](documentpickermode.md) — The document picker’s file-transfer operation. (read-only) _(deprecated)_
- [documentStorageURL](documentstorageurl.md) — The root URL for documents provided by the corresponding File Provider extension. (read-only) _(deprecated)_
- [originalURL](originalurl.md) — The URL of the file to be exported. (read-only) _(deprecated)_
- [providerIdentifier](provideridentifier.md) — An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only) _(deprecated)_
- [validTypes](validtypes.md) — An array of valid uniform type identifiers. _(deprecated)_
