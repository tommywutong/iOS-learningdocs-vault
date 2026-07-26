---
title: Document Content Types
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/document-content-types
source_url: 'https://developer.apple.com/documentation/foundation/document-content-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/document-content-types.json'
content_hash: 'sha256:c0f5d199b27a615c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Archives and Serialization](archives-and-serialization.md) · [XML Processing and Modeling](xml-processing-and-modeling.md) · [XMLDocument](xmldocument.md)

# Document Content Types

<sub>API Collection</sub>

Define document types.

## Overview

You specify one of the NSXMLDocumentContentKind constants in [documentContentKind](xmldocument/documentcontentkind.md) to indicate the kind of content required for document output.

## Topics

### Constants

- [NSXMLDocumentXMLKind](xmldocument/contentkind/xml.md) — The default type of document content type, which is XML.
- [NSXMLDocumentXHTMLKind](xmldocument/contentkind/xhtml.md) — The document output is XHTML.
- [NSXMLDocumentHTMLKind](xmldocument/contentkind/html.md) — Outputs empty tags in HTML without a close tag, such as `<br>`.
- [NSXMLDocumentTextKind](xmldocument/contentkind/text.md) — Outputs the string value of the document by extracting the string values from all text nodes.

## See Also

### Constants

- [Input and Output Options](input_and_output_options.md) — Input and output options specifically intended for `NSXMLDocument` objects.
- [ContentKind](xmldocument/contentkind.md) — Type used to define the kind of document content.
