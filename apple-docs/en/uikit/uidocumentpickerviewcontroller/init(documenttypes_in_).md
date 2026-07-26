---
title: 'init(documentTypes:in:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentpickerviewcontroller/init(documenttypes:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(documenttypes:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/init%28documenttypes%3Ain%3A%29.json'
content_hash: 'sha256:6e2093af50d7534e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# init(documentTypes:in:)

<sub>Initializer</sub>

Creates and returns a document picker that can open or copy the specified file types.

> [!warning] Deprecated
> Use [- initForOpeningContentTypes:](<init(foropeningcontenttypes_).md>) or [- initForOpeningContentTypes:asCopy:](<init(foropeningcontenttypes_ascopy_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(documentTypes allowedUTIs: [String], in mode: UIDocumentPickerMode)
```

## Parameters

- `allowedUTIs` — An array of uniform type identifiers (UTIs). UTIs are strings that uniquely identify a file’s type. For more information, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

- `mode` — The type of file-transfer operation that the document picker performs. This argument accepts only the [UIDocumentPickerModeImport](../uidocumentpickermode/import.md) or [UIDocumentPickerModeOpen](../uidocumentpickermode/open.md) mode.

## Return Value

Returns an initialized `UIDocumentPickerViewController` object, or `nil` if the object could not be successfully initialized.

## Discussion

In iOS 10 and earlier, this method returns the document picker view controller from the most recently used Document Provider extension. If no valid Document Provider can be found, it defaults back to iCloud Drive.

In iOS 11 and later, it returns the standard browser interface. This interface is the same one used by the [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md) class.

## See Also

### Deprecated

- [- initWithURL:inMode:](<init(url_in_).md>) — Initializes and returns a document picker that can export or copy the specified document. _(deprecated)_
- [- initWithURLs:inMode:](<init(urls_in_).md>) — Creates and returns a document picker that can export or move the specified documents. _(deprecated)_
