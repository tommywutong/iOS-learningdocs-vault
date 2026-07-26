---
title: XMLDocument.ContentKind
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/contentkind
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/contentkind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/contentkind.json'
content_hash: 'sha256:26f72feb01edc60f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# XMLDocument.ContentKind

<sub>Enumeration</sub>

Type used to define the kind of document content.

<sub>Mac Catalyst, macOS</sub>

```swift
enum ContentKind
```

## Overview

For possible values, see doc:xmldocument/document_content_types.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NSXMLDocumentHTMLKind](contentkind/html.md) — Outputs empty tags in HTML without a close tag, such as `<br>`.
- [NSXMLDocumentTextKind](contentkind/text.md) — Outputs the string value of the document by extracting the string values from all text nodes.
- [NSXMLDocumentXHTMLKind](contentkind/xhtml.md) — The document output is XHTML.
- [NSXMLDocumentXMLKind](contentkind/xml.md) — The default type of document content type, which is XML.

### Initializers

- [init(rawValue:)](<contentkind/init(rawvalue_).md>)

## See Also

### Constants

- [Input and Output Options](../input_and_output_options.md) — Input and output options specifically intended for `NSXMLDocument` objects.
- [Document Content Types](../document-content-types.md) — Define document types.
