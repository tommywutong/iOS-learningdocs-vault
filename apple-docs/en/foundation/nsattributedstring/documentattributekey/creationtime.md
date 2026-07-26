---
title: creationTime
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/creationtime
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/creationtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/creationtime.json'
content_hash: 'sha256:d4539c7b188e7344'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# creationTime

<sub>Type Property</sub>

The creation date of the document.

<sub>macOS</sub>

```swift
static let creationTime: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [NSDate](../../nsdate.md) object containing the creation date of the document; note that this is not the file system creation date of the file, but of the document.

## See Also

### Getting document metadata keys

- [author](author.md) — The author of the document.
- [category](category.md) — The document’s category.
- [characterEncoding](characterencoding.md) — The string encoding for the document.
- [cocoaVersionDocumentAttribute](cocoaversiondocumentattribute.md) — The version of Cocoa that created the file.
- [comment](comment.md) — The document comments.
- [company](company.md) — The company or organization name associated with the document.
- [converted](converted.md) — A value that indicates whether a filter service converted the file.
- [copyright](copyright.md) — The document’s copyright information.
- [editor](editor.md) — The name of person who last edited the document.
- [keywords](keywords.md) — The document keywords.
- [manager](manager.md) — The name of the author’s manager.
- [modificationTime](modificationtime.md) — The modification date of the document.
- [readOnly](readonly.md) — An indication of whether the document is read-only.
- [subject](subject.md) — The subject of the document.
- [title](title.md) — The document title.
