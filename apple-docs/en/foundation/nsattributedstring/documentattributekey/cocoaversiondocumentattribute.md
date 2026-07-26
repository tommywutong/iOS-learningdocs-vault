---
title: cocoaVersionDocumentAttribute
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/cocoaversiondocumentattribute
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/cocoaversiondocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/cocoaversiondocumentattribute.json'
content_hash: 'sha256:7e58970387a0597d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# cocoaVersionDocumentAttribute

<sub>Type Property</sub>

The version of Cocoa that created the file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let cocoaVersionDocumentAttribute: NSAttributedString.DocumentAttributeKey
```

<sub>macOS</sub>

```swift
static let cocoaVersion: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing a float. For RTF files only, stores the version of Cocoa with which the file was created. Absence of this value indicates RTF file not created by Cocoa or its predecessors.

Values less than `100` are pre–macOS; `100` is macOS 10.0 or 10.1; `102` is macOS 10.2 and 10.3; values greater than `102` correspond to values of `NSAppKitVersionNumber` in macOS 10.4 and later.

The string constant in macOS 10.3 and earlier is `@"CocoaRTFVersion"`.

## See Also

### Getting document metadata keys

- [author](author.md) — The author of the document.
- [category](category.md) — The document’s category.
- [characterEncoding](characterencoding.md) — The string encoding for the document.
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
