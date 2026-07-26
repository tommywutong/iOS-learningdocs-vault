---
title: validTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentpickerextensionviewcontroller/validtypes
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/validtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerextensionviewcontroller/validtypes.json'
content_hash: 'sha256:dfef34c92fdb3b72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md)

# validTypes

<sub>Instance Property</sub>

An array of valid uniform type identifiers.

> [!warning] Deprecated
> For more information, see [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var validTypes: [String]? { get }
```

## Discussion

While in the `UIDocumentPickerModeImport` or `UIDocumentPickerModeOpen` modes, this property holds an array of valid UTIs; otherwise, it is `nil`.

Check the value of this property before your Document Picker extension displays any files to the user. You should let the user select only files that match at least one of the given UTIs.

## See Also

### Managing the user interface

- [- dismissGrantingAccessToURL:](<dismissgrantingaccess(to_).md>) — Dismisses the document picker. _(deprecated)_
- [documentPickerMode](documentpickermode.md) — The document picker’s file-transfer operation. (read-only) _(deprecated)_
- [documentStorageURL](documentstorageurl.md) — The root URL for documents provided by the corresponding File Provider extension. (read-only) _(deprecated)_
- [originalURL](originalurl.md) — The URL of the file to be exported. (read-only) _(deprecated)_
- [- prepareForPresentationInMode:](<prepareforpresentation(in_).md>) — Performs any custom configuration of the document picker view controller. _(deprecated)_
- [providerIdentifier](provideridentifier.md) — An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only) _(deprecated)_
