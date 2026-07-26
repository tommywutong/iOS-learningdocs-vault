---
title: nodeExpandEmptyElement
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/options/nodeexpandemptyelement
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/options/nodeexpandemptyelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/options/nodeexpandemptyelement.json'
content_hash: 'sha256:2eaa5b4779507bea'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [XMLNode](../../xmlnode.md) · [Options](../options.md)

# nodeExpandEmptyElement

<sub>Type Property</sub>

Requests that an element should be expanded when empty; for example, `<flag></flag>`. This is the default.

<sub>Mac Catalyst, macOS</sub>

```swift
static var nodeExpandEmptyElement: XMLNode.Options { get }
```

## See Also

### Constants

- [NSXMLDocumentIncludeContentTypeDeclaration](documentincludecontenttypedeclaration.md) — Includes a content type declaration for HTML or XHTML in the output of the document.
- [NSXMLDocumentTidyHTML](documenttidyhtml.md) — Formats HTML into valid XHTML during processing of the document.
- [NSXMLDocumentTidyXML](documenttidyxml.md) — Changes malformed XML into valid XML during processing of the document.
- [NSXMLDocumentValidate](documentvalidate.md) — Validates this document against its DTD (internal or external) or XML Schema.
- [NSXMLDocumentXInclude](documentxinclude.md) — Replaces all XInclude nodes in the document with the nodes referred to.
- [NSXMLNodeCompactEmptyElement](nodecompactemptyelement.md) — Requests that an element should be contracted when empty; for example, `<flag/>`.
- [NSXMLNodeIsCDATA](nodeiscdata.md) — Specifies that a text node contains and is written out as a CDATA section.
- [NSXMLNodeLoadExternalEntitiesAlways](nodeloadexternalentitiesalways.md) — Requests that external entities are always loaded.
- [NSXMLNodeLoadExternalEntitiesNever](nodeloadexternalentitiesnever.md) — Requests that external entities are never loaded.
- [NSXMLNodeLoadExternalEntitiesSameOriginOnly](nodeloadexternalentitiessameoriginonly.md) — Requests that external entities are always loaded and only applies when a URL has been provided.
- [NSXMLNodeNeverEscapeContents](nodeneverescapecontents.md)
- [NSXMLNodePreserveAll](nodepreserveall.md)
- [NSXMLNodePreserveAttributeOrder](nodepreserveattributeorder.md) — Requests that NSXMLNode preserve the order of attributes as in the source XML.
- [NSXMLNodePreserveCDATA](nodepreservecdata.md) — Requests that NSXMLNode preserve CDATA blocks where defined in the input XML.
- [NSXMLNodePreserveCharacterReferences](nodepreservecharacterreferences.md) — Specifies that character references (`&#`_nnn_`;`) should not be resolved for XML output of this node.
