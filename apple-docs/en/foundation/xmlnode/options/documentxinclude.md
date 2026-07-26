---
title: documentXInclude
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/options/documentxinclude
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/options/documentxinclude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/options/documentxinclude.json'
content_hash: 'sha256:8f53036a263dbfc8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [XMLNode](../../xmlnode.md) · [Options](../options.md)

# documentXInclude

<sub>Type Property</sub>

Replaces all XInclude nodes in the document with the nodes referred to.

<sub>Mac Catalyst, macOS</sub>

```swift
static var documentXInclude: XMLNode.Options { get }
```

## Discussion

XInclude allows clients to include parts of another XML document within a document.

(Input)

## See Also

### Constants

- [NSXMLDocumentTidyHTML](documenttidyhtml.md) — Formats HTML into valid XHTML during processing of the document.
- [NSXMLDocumentTidyXML](documenttidyxml.md) — Changes malformed XML into valid XML during processing of the document.
- [NSXMLDocumentValidate](documentvalidate.md) — Validates this document against its DTD (internal or external) or XML Schema.
- [NSXMLDocumentIncludeContentTypeDeclaration](documentincludecontenttypedeclaration.md) — Includes a content type declaration for HTML or XHTML in the output of the document.
