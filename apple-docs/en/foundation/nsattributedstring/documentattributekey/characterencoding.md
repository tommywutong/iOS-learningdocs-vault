---
title: characterEncoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/characterencoding
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/characterencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/characterencoding.json'
content_hash: 'sha256:7e4a22591c37e10b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# characterEncoding

<sub>Type Property</sub>

The string encoding for the document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let characterEncoding: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing integer specifying [NSStringEncoding](../../nsstringencoding.md) for the file; default for plain text is the default encoding. This key in options can specify the string encoding for reading the data. Upon return, the document attributes can contain the actual encoding used. For writing methods, this value is used for generating the plain text data.

The string constant in macOS 10.3 and earlier is `@"CharacterEncoding"`.

## See Also

### Getting document metadata keys

- [author](author.md) — The author of the document.
- [category](category.md) — The document’s category.
- [cocoaVersionDocumentAttribute](cocoaversiondocumentattribute.md) — The version of Cocoa that created the file.
- [comment](comment.md) — The document comments.
- [company](company.md) — The company or organization name associated with the document.
- [converted](converted.md) — A value that indicates whether a filter service converted the file.
- [copyright](copyright.md) — The document’s copyright information.
- [creationTime](creationtime.md) — The creation date of the document.
- [editor](editor.md) — The name of person who last edited the document.
- [keywords](keywords.md) — The document keywords.
- [manager](manager.md) — The name of the author’s manager.
- [modificationTime](modificationtime.md) — The modification date of the document.
- [readOnly](readonly.md) — An indication of whether the document is read-only.
- [subject](subject.md) — The subject of the document.
- [title](title.md) — The document title.
