---
title: 'init(url:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentproperties/init(url:)-zeio'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentproperties/init(url:)-zeio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentproperties/init%28url%3A%29-zeio.json'
content_hash: 'sha256:950fa05e100a883f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentProperties](../uidocumentproperties.md)

# init(url:)

<sub>Initializer</sub>

Creates a document properties object from document data at the URL you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(url: URL)
```

## Parameters

- `url` — The URL that points to the document data.

## Discussion

When you initialize a document properties object with a URL, UIKit automatically finds the corresponding metadata and stores it in the document properties object’s [metadata](metadata.md) property.

## See Also

### Creating a document header

- [- initWithMetadata:](<init(metadata_).md>) — Creates a document properties object from the metadata object you specify.
- [metadata](metadata.md) — The document’s metadata.
