---
title: nodeLoadExternalEntitiesAlways
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/options/nodeloadexternalentitiesalways
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/options/nodeloadexternalentitiesalways'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/options/nodeloadexternalentitiesalways.json'
content_hash: 'sha256:080035193b699b98'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [XMLNode](../../xmlnode.md) · [Options](../options.md)

# nodeLoadExternalEntitiesAlways

<sub>Type Property</sub>

Requests that external entities are always loaded.

<sub>Mac Catalyst, macOS</sub>

```swift
static var nodeLoadExternalEntitiesAlways: XMLNode.Options { get }
```

## Discussion

Requests that external entities are always loaded. You may choose only one of [NSXMLNodeLoadExternalEntitiesAlways](nodeloadexternalentitiesalways.md), [NSXMLNodeLoadExternalEntitiesSameOriginOnly](nodeloadexternalentitiessameoriginonly.md), or [NSXMLNodeLoadExternalEntitiesNever](nodeloadexternalentitiesnever.md) or none.

Choosing none results in the system-default behavior. For applications linked on OS X v10.6 and earlier, this is `NSXMLNodeLoadExternalEntitiesAlways`. For applications linked on macOS 10.7 or later, all entities that don’t require network access are loaded.

If an external entity fails to load, the document is invalid and the parse is aborted with an error.

## See Also

### Constants

- [NSXMLDocumentIncludeContentTypeDeclaration](documentincludecontenttypedeclaration.md) — Includes a content type declaration for HTML or XHTML in the output of the document.
- [NSXMLDocumentTidyHTML](documenttidyhtml.md) — Formats HTML into valid XHTML during processing of the document.
- [NSXMLDocumentTidyXML](documenttidyxml.md) — Changes malformed XML into valid XML during processing of the document.
- [NSXMLDocumentValidate](documentvalidate.md) — Validates this document against its DTD (internal or external) or XML Schema.
- [NSXMLDocumentXInclude](documentxinclude.md) — Replaces all XInclude nodes in the document with the nodes referred to.
- [NSXMLNodeCompactEmptyElement](nodecompactemptyelement.md) — Requests that an element should be contracted when empty; for example, `<flag/>`.
- [NSXMLNodeExpandEmptyElement](nodeexpandemptyelement.md) — Requests that an element should be expanded when empty; for example, `<flag></flag>`. This is the default.
- [NSXMLNodeIsCDATA](nodeiscdata.md) — Specifies that a text node contains and is written out as a CDATA section.
- [NSXMLNodeLoadExternalEntitiesNever](nodeloadexternalentitiesnever.md) — Requests that external entities are never loaded.
- [NSXMLNodeLoadExternalEntitiesSameOriginOnly](nodeloadexternalentitiessameoriginonly.md) — Requests that external entities are always loaded and only applies when a URL has been provided.
- [NSXMLNodeNeverEscapeContents](nodeneverescapecontents.md)
- [NSXMLNodePreserveAll](nodepreserveall.md)
- [NSXMLNodePreserveAttributeOrder](nodepreserveattributeorder.md) — Requests that NSXMLNode preserve the order of attributes as in the source XML.
- [NSXMLNodePreserveCDATA](nodepreservecdata.md) — Requests that NSXMLNode preserve CDATA blocks where defined in the input XML.
- [NSXMLNodePreserveCharacterReferences](nodepreservecharacterreferences.md) — Specifies that character references (`&#`_nnn_`;`) should not be resolved for XML output of this node.
