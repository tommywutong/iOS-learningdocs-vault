---
title: 'init(metadata:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentproperties/init(metadata:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentproperties/init(metadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentproperties/init%28metadata%3A%29.json'
content_hash: 'sha256:16ac2fa900c356a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentProperties](../uidocumentproperties.md)

# init(metadata:)

<sub>Initializer</sub>

Creates a document properties object from the metadata object you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(metadata: LPLinkMetadata)
```

## Parameters

- `metadata` — Metadata about a document.

## Discussion

If you don’t have a URL backing your document, create a metadata object manually to initialize a document properties object.

## See Also

### Creating a document header

- [- initWithURL:](<init(url_)-zeio.md>) — Creates a document properties object from document data at the URL you specify.
- [metadata](metadata.md) — The document’s metadata.
