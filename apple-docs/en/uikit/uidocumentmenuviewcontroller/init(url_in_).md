---
title: 'init(url:in:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentmenuviewcontroller/init(url:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/init(url:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenuviewcontroller/init%28url%3Ain%3A%29.json'
content_hash: 'sha256:f1eeccf66c660fda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md)

# init(url:in:)

<sub>Initializer</sub>

Initializes and returns a document menu to export or move the given document.

> [!warning] Deprecated
> For more information, see [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(url: URL, in mode: UIDocumentPickerMode)
```

## Parameters

- `url` — The document to be exported or moved.

- `mode` — The type of file-transfer operation that the document picker performs. This argument accepts only the UIDocumentPickerModeExportToService or UIDocumentPickerModeMoveToService mode.

## Return Value

Returns an initialized `UIDocumentMenuViewController` object, or `nil` if the object could not be successfully initialized.

## Discussion

The resulting document menu displays all the document pickers appropriate for the given mode.

## See Also

### Creating a document menu

- [- initWithDocumentTypes:inMode:](<init(documenttypes_in_).md>) — Initializes and returns a document menu to import or open the given file types. _(deprecated)_
- [- initWithCoder:](<init(coder_).md>) — Creates a document menu from data in an unarchiver. _(deprecated)_
