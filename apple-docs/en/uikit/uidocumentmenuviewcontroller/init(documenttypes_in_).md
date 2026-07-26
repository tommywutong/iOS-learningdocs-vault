---
title: 'init(documentTypes:in:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentmenuviewcontroller/init(documenttypes:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/init(documenttypes:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenuviewcontroller/init%28documenttypes%3Ain%3A%29.json'
content_hash: 'sha256:88d111f4b2ebf64b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md)

# init(documentTypes:in:)

<sub>Initializer</sub>

Initializes and returns a document menu to import or open the given file types.

> [!warning] Deprecated
> For more information, see [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(documentTypes allowedUTIs: [String], in mode: UIDocumentPickerMode)
```

## Parameters

- `allowedUTIs` — An array of uniform type identifiers. UTIs are strings that uniquely identify a file’s type. For more information, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

- `mode` — The type of file transfer operation the document picker performs. This argument accepts only the [UIDocumentPickerModeImport](../uidocumentpickermode/import.md) or [UIDocumentPickerModeOpen](../uidocumentpickermode/open.md) mode.

## Return Value

Returns an initialized `UIDocumentMenuViewController` object, or `nil` if the object could not be successfully initialized.

## Discussion

The UTI array defines the type of documents that can be imported or opened. The resulting document menu displays all the document pickers appropriate for the given document types and mode.

## See Also

### Creating a document menu

- [- initWithURL:inMode:](<init(url_in_).md>) — Initializes and returns a document menu to export or move the given document. _(deprecated)_
- [- initWithCoder:](<init(coder_).md>) — Creates a document menu from data in an unarchiver. _(deprecated)_
