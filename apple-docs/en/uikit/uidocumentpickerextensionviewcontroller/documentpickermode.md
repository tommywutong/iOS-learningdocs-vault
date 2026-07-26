---
title: documentPickerMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentpickerextensionviewcontroller/documentpickermode
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/documentpickermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerextensionviewcontroller/documentpickermode.json'
content_hash: 'sha256:35909d0f62b9dfea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md)

# documentPickerMode

<sub>Instance Property</sub>

The document picker’s file-transfer operation. (read-only)

> [!warning] Deprecated
> For more information, see [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var documentPickerMode: UIDocumentPickerMode { get }
```

## Discussion

For a list of available modes, see `Document Picker Modes` in [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md).

## See Also

### Managing the user interface

- [- dismissGrantingAccessToURL:](<dismissgrantingaccess(to_).md>) — Dismisses the document picker. _(deprecated)_
- [documentStorageURL](documentstorageurl.md) — The root URL for documents provided by the corresponding File Provider extension. (read-only) _(deprecated)_
- [originalURL](originalurl.md) — The URL of the file to be exported. (read-only) _(deprecated)_
- [- prepareForPresentationInMode:](<prepareforpresentation(in_).md>) — Performs any custom configuration of the document picker view controller. _(deprecated)_
- [providerIdentifier](provideridentifier.md) — An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only) _(deprecated)_
- [validTypes](validtypes.md) — An array of valid uniform type identifiers. _(deprecated)_
