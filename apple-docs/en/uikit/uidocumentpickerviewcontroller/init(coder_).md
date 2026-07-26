---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentpickerviewcontroller/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/init%28coder%3A%29.json'
content_hash: 'sha256:13e186fc3b12c2a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# init(coder:)

<sub>Initializer</sub>

Returns an initialized object from data in a specified unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — An unarchiver object.

## See Also

### Creating a document picker

- [- initForExportingURLs:](<init(forexporting_).md>) — Creates and returns a document picker that can export the types of documents you specify.
- [- initForExportingURLs:asCopy:](<init(forexporting_ascopy_).md>) — Creates and returns a document picker that can export or copy the types of documents you specify.
- [- initForOpeningContentTypes:](<init(foropeningcontenttypes_).md>) — Creates and returns a document picker that can open the types of documents you specify.
- [- initForOpeningContentTypes:asCopy:](<init(foropeningcontenttypes_ascopy_).md>) — Creates and returns a document picker that can open or copy the types of documents you specify.
