---
title: NSAttributedString.DocumentType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documenttype
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documenttype.json'
content_hash: 'sha256:9af1051f88c59cbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.DocumentType

<sub>Structure</sub>

Constants for the document type document attribute key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DocumentType
```

## Overview

Use these constants as values for the [documentType](documentattributekey/documenttype.md) key in the document attributes dictionary.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting keys for document types

- [docFormat](documenttype/docformat.md) — Microsoft Word document.
- [html](documenttype/html.md) — Hypertext markup language (HTML) document.
- [macSimpleText](documenttype/macsimpletext.md) — Macintosh SimpleText document.
- [officeOpenXML](documenttype/officeopenxml.md) — ECMA Office Open XML text document format.
- [openDocument](documenttype/opendocument.md) — OASIS Open Document text document format.
- [plain](documenttype/plain.md) — Plain text document.
- [rtf](documenttype/rtf.md) — Rich text format document.
- [rtfd](documenttype/rtfd.md) — Rich text format with attachments document.
- [webArchive](documenttype/webarchive.md) — WebKit WebArchive document.
- [wordML](documenttype/wordml.md) — Microsoft Word XML (WordML schema) document.

### Initializers

- [init(_:)](<documenttype/init(__).md>) — Creates a document type.
- [init(rawValue:)](<documenttype/init(rawvalue_).md>) — Creates a document type with the specified raw value.

## See Also

### Getting document-wide attributes

- [DocumentAttributeKey](documentattributekey.md) — The attributes you apply to an entire document.
- [DocumentReadingOptionKey](documentreadingoptionkey.md) — Options for constructing an attributed string from data you read from disk.
- [HTML attributes](../html-attributes.md) — Documentwide attributes that provide control over the form of generated HTML.
- [TextLayoutSectionKey](textlayoutsectionkey.md) — Constants for the text layout sections document attribute key.
- [NSTextScalingType](../../uikit/nstextscalingtype.md) — Constants that specify the text scaling.
