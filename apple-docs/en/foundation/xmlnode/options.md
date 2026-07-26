---
title: XMLNode.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/options
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/options.json'
content_hash: 'sha256:aeeef25e63d213b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# XMLNode.Options

<sub>Structure</sub>

These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [XMLDocument](../xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [- initWithKind:options:](<init(kind_options_).md>) and [- XMLStringWithOptions:](<xmlstring(options_).md>).

<sub>Mac Catalyst, macOS</sub>

```swift
struct Options
```

## Overview

The options with “Preserve” in their names are applicable only when external sources of XML are parsed; they have no effect on node objects that are programmatically created. Other options are used in initialization and output methods of `NSXMLDocument`; see the [XMLDocument](../xmldocument.md) reference documentation for details.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSXMLDocumentIncludeContentTypeDeclaration](options/documentincludecontenttypedeclaration.md) — Includes a content type declaration for HTML or XHTML in the output of the document.
- [NSXMLDocumentTidyHTML](options/documenttidyhtml.md) — Formats HTML into valid XHTML during processing of the document.
- [NSXMLDocumentTidyXML](options/documenttidyxml.md) — Changes malformed XML into valid XML during processing of the document.
- [NSXMLDocumentValidate](options/documentvalidate.md) — Validates this document against its DTD (internal or external) or XML Schema.
- [NSXMLDocumentXInclude](options/documentxinclude.md) — Replaces all XInclude nodes in the document with the nodes referred to.
- [NSXMLNodeCompactEmptyElement](options/nodecompactemptyelement.md) — Requests that an element should be contracted when empty; for example, `<flag/>`.
- [NSXMLNodeExpandEmptyElement](options/nodeexpandemptyelement.md) — Requests that an element should be expanded when empty; for example, `<flag></flag>`. This is the default.
- [NSXMLNodeIsCDATA](options/nodeiscdata.md) — Specifies that a text node contains and is written out as a CDATA section.
- [NSXMLNodeLoadExternalEntitiesAlways](options/nodeloadexternalentitiesalways.md) — Requests that external entities are always loaded.
- [NSXMLNodeLoadExternalEntitiesNever](options/nodeloadexternalentitiesnever.md) — Requests that external entities are never loaded.
- [NSXMLNodeLoadExternalEntitiesSameOriginOnly](options/nodeloadexternalentitiessameoriginonly.md) — Requests that external entities are always loaded and only applies when a URL has been provided.
- [NSXMLNodeNeverEscapeContents](options/nodeneverescapecontents.md)
- [NSXMLNodePreserveAll](options/nodepreserveall.md)
- [NSXMLNodePreserveAttributeOrder](options/nodepreserveattributeorder.md) — Requests that NSXMLNode preserve the order of attributes as in the source XML.
- [NSXMLNodePreserveCDATA](options/nodepreservecdata.md) — Requests that NSXMLNode preserve CDATA blocks where defined in the input XML.
- [NSXMLNodePreserveCharacterReferences](options/nodepreservecharacterreferences.md) — Specifies that character references (`&#`_nnn_`;`) should not be resolved for XML output of this node.
- [NSXMLNodePreserveDTD](options/nodepreservedtd.md) — Specifies that declarations in a DTD should be preserved until it the DTD is modified. For example, parameter entities are by default expanded; with this option, they are written out as they originally occur in the DTD.
- [NSXMLNodePreserveEmptyElements](options/nodepreserveemptyelements.md) — Specifies that empty elements in the input XML be preserved in their contracted or expanded form.
- [NSXMLNodePreserveEntities](options/nodepreserveentities.md) — Specifies that entities (`&`_xyz_`;`) should not be resolved for XML output of this node.
- [NSXMLNodePreserveNamespaceOrder](options/nodepreservenamespaceorder.md) — Requests NSXML to preserve the order of namespace URI definitions as in the source XML.
- [NSXMLNodePreservePrefixes](options/nodepreserveprefixes.md) — Requests NSXMLNode not to choose prefixes based on the closest namespace URI definition.
- [NSXMLNodePreserveQuotes](options/nodepreservequotes.md) — Specifies that the quoting style used in the input XML (single or double quotes) be preserved.
- [NSXMLNodePreserveWhitespace](options/nodepreservewhitespace.md) — Requests NSXMLNode to preserve whitespace characters (such as tabs and carriage returns) in the XML source that are not part of node content.
- [NSXMLNodePrettyPrint](options/nodeprettyprint.md) — Print this node with extra space for readability. (Output)
- [NSXMLNodePromoteSignificantWhitespace](options/nodepromotesignificantwhitespace.md)
- [NSXMLNodeUseDoubleQuotes](options/nodeusedoublequotes.md) — Requests that NSXML use double quotes for the value of an attribute or namespace node. This is the default.
- [NSXMLNodeUseSingleQuotes](options/nodeusesinglequotes.md) — Requests that NSXML use single quotes for the value of an attribute or namespace node.

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)

## See Also

### Constants

- [Kind](kind-swift.enum.md) — `NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [- initWithKind:](<init(kind_).md>) and [- initWithKind:options:](<init(kind_options_).md>):
