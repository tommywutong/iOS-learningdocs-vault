---
title: 'dismissGrantingAccess(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerextensionviewcontroller/dismissgrantingaccess%28to%3A%29.json'
content_hash: 'sha256:574218a96ef83dea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md)

# dismissGrantingAccess(to:)

<sub>Instance Method</sub>

Dismisses the document picker.

> [!warning] Deprecated
> For more information, see [UIDocumentPickerExtensionViewController](../uidocumentpickerextensionviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dismissGrantingAccess(to url: URL?)
```

## Parameters

- `url` — The URL that the extension returns to the host app.

## Discussion

Call this method when the user selects a document or destination. This method dismisses the document picker view controller in the host app and triggers the appropriate file transfer. After the transfer is complete, the method passes the provided URL to the host app’s [- documentPicker:didPickDocumentAtURL:](<../uidocumentpickerdelegate/documentpicker(__didpickdocumentat_).md>) delegate method.

The URL must meet all of the following conditions:

- Import Document Picker mode. Provide a URL for the selected file. The URL only needs to be accessible by the Document Picker View Controller extension.
- Open Document Picker mode. Provide a URL for the selected file. The URL must point to a location inside the directory hierarchy referred to by your [documentStorageURL](documentstorageurl.md) property.
- Export Document Picker mode. Before calling this method, copy the file to the selected destination. Your extensions also need to track the file and make sure it is synced to your server.

After the copy is complete, call this method and provide the URL to the new copy.  This URL needs to be accessible only by the Document Picker View Controller extension. The system returns the URL to the host app to indicate success; however, the host app cannot access the document at this URL.

- Move Document Picker mode. Before calling this method, copy the file to the selected destination. Your extensions also need to track the file and make sure it is synced to your server.

After the copy is complete, call this method and provide the URL to the new copy. The URL needs to be contained inside the hierarchy referred to by your [documentStorageURL](documentstorageurl.md) property. The system returns this URL to the host app, and the host app can continue to access the document at this URL.

## See Also

### Managing the user interface

- [documentPickerMode](documentpickermode.md) — The document picker’s file-transfer operation. (read-only) _(deprecated)_
- [documentStorageURL](documentstorageurl.md) — The root URL for documents provided by the corresponding File Provider extension. (read-only) _(deprecated)_
- [originalURL](originalurl.md) — The URL of the file to be exported. (read-only) _(deprecated)_
- [- prepareForPresentationInMode:](<prepareforpresentation(in_).md>) — Performs any custom configuration of the document picker view controller. _(deprecated)_
- [providerIdentifier](provideridentifier.md) — An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only) _(deprecated)_
- [validTypes](validtypes.md) — An array of valid uniform type identifiers. _(deprecated)_
