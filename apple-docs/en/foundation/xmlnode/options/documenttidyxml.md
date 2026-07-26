---
title: documentTidyXML
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/options/documenttidyxml
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/options/documenttidyxml'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/options/documenttidyxml.json'
content_hash: 'sha256:2666772f8d569226'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [XMLNode](../../xmlnode.md) · [Options](../options.md)

# documentTidyXML

<sub>Type Property</sub>

Changes malformed XML into valid XML during processing of the document.

<sub>Mac Catalyst, macOS</sub>

```swift
static var documentTidyXML: XMLNode.Options { get }
```

## Discussion

It also eliminates “pretty-printing” formatting, such as leading tab characters. It does respect the `xml:space="preserve"` attribute.

(Input)

## See Also

### Constants

- [NSXMLDocumentTidyHTML](documenttidyhtml.md) — Formats HTML into valid XHTML during processing of the document.
- [NSXMLDocumentValidate](documentvalidate.md) — Validates this document against its DTD (internal or external) or XML Schema.
- [NSXMLDocumentXInclude](documentxinclude.md) — Replaces all XInclude nodes in the document with the nodes referred to.
- [NSXMLDocumentIncludeContentTypeDeclaration](documentincludecontenttypedeclaration.md) — Includes a content type declaration for HTML or XHTML in the output of the document.
