---
title: converted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/converted
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/converted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/converted.json'
content_hash: 'sha256:3f5e9b237bb85c7e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# converted

<sub>Type Property</sub>

A value that indicates whether a filter service converted the file.

<sub>macOS</sub>

```swift
static let converted: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing an integer. Indicates whether the file was converted by a filter service.

If missing or 0, the file was originally in the format specified by [documentType](documenttype.md). If negative, the file was originally in the format specified by document type, but the conversion to [NSAttributedString](../../nsattributedstring.md) may have been lossy. If 1 or more, it was converted to this type by a filter service.

The string constant in macOS 10.3 and earlier is `@"Converted"`.

## See Also

### Getting document metadata keys

- [author](author.md) — The author of the document.
- [category](category.md) — The document’s category.
- [characterEncoding](characterencoding.md) — The string encoding for the document.
- [cocoaVersionDocumentAttribute](cocoaversiondocumentattribute.md) — The version of Cocoa that created the file.
- [comment](comment.md) — The document comments.
- [company](company.md) — The company or organization name associated with the document.
- [copyright](copyright.md) — The document’s copyright information.
- [creationTime](creationtime.md) — The creation date of the document.
- [editor](editor.md) — The name of person who last edited the document.
- [keywords](keywords.md) — The document keywords.
- [manager](manager.md) — The name of the author’s manager.
- [modificationTime](modificationtime.md) — The modification date of the document.
- [readOnly](readonly.md) — An indication of whether the document is read-only.
- [subject](subject.md) — The subject of the document.
- [title](title.md) — The document title.
