---
title: metadata
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentproperties/metadata
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentproperties/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentproperties/metadata.json'
content_hash: 'sha256:d765a2af500738c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentProperties](../uidocumentproperties.md)

# metadata

<sub>Instance Property</sub>

The document’s metadata.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var metadata: LPLinkMetadata { get set }
```

## Discussion

If you initialize the document properties object using [- initWithURL:](<init(url_)-zeio.md>), UIKit generates this metadata automatically. Typically, you don’t need to access the value of this property directly because UIKit updates the metadata asynchronously to display the latest information in the document header.

If you initialize the document properties object using [- initWithMetadata:](<init(metadata_).md>), you can use this property to manually set metadata if it requires an update.

## See Also

### Creating a document header

- [- initWithURL:](<init(url_)-zeio.md>) — Creates a document properties object from document data at the URL you specify.
- [- initWithMetadata:](<init(metadata_).md>) — Creates a document properties object from the metadata object you specify.
