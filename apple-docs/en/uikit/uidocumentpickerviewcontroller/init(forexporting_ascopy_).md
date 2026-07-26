---
title: 'init(forExporting:asCopy:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentpickerviewcontroller/init(forexporting:ascopy:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(forexporting:ascopy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/init%28forexporting%3Aascopy%3A%29.json'
content_hash: 'sha256:ceab5051c469006f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# init(forExporting:asCopy:)

<sub>Initializer</sub>

Creates and returns a document picker that can export or copy the types of documents you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(forExporting urls: [URL], asCopy: Bool)
```

## Parameters

- `urls` — An array of documents that the document picker exports or copies.

- `asCopy` — A Boolean value that indicates whether the document picker copies the selected document.

## See Also

### Creating a document picker

- [- initWithCoder:](<init(coder_).md>) — Returns an initialized object from data in a specified unarchiver.
- [- initForExportingURLs:](<init(forexporting_).md>) — Creates and returns a document picker that can export the types of documents you specify.
- [- initForOpeningContentTypes:](<init(foropeningcontenttypes_).md>) — Creates and returns a document picker that can open the types of documents you specify.
- [- initForOpeningContentTypes:asCopy:](<init(foropeningcontenttypes_ascopy_).md>) — Creates and returns a document picker that can open or copy the types of documents you specify.
