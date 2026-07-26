---
title: providerIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentpickerextensionviewcontroller/provideridentifier
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/provideridentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerextensionviewcontroller/provideridentifier.json'
content_hash: 'sha256:4c7f7e49e28709bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md)

# providerIdentifier

<sub>Instance Property</sub>

An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)

> [!warning] Deprecated
> For more information, see [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var providerIdentifier: String { get }
```

## Discussion

Both the Document Picker View Controller extension and the File Provider extension should pass this identifier to their file coordinator’s `setPurposeIdentifier:` method. This approach helps coordinate the read and write operations between the two extensions, preventing possible deadlocks.

This property holds the value returned by calling the File Provider extension’s [providerIdentifier](../../fileprovider/nsfileproviderextension/provideridentifier.md) method.

## See Also

### Managing the user interface

- [- dismissGrantingAccessToURL:](<dismissgrantingaccess(to_).md>) — Dismisses the document picker. _(deprecated)_
- [documentPickerMode](documentpickermode.md) — The document picker’s file-transfer operation. (read-only) _(deprecated)_
- [documentStorageURL](documentstorageurl.md) — The root URL for documents provided by the corresponding File Provider extension. (read-only) _(deprecated)_
- [originalURL](originalurl.md) — The URL of the file to be exported. (read-only) _(deprecated)_
- [- prepareForPresentationInMode:](<prepareforpresentation(in_).md>) — Performs any custom configuration of the document picker view controller. _(deprecated)_
- [validTypes](validtypes.md) — An array of valid uniform type identifiers. _(deprecated)_
