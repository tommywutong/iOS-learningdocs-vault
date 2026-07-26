---
title: XMLDTDNode
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldtdnode
source_url: 'https://developer.apple.com/documentation/foundation/xmldtdnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtdnode.json'
content_hash: 'sha256:650c94d42cf27a43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XMLDTDNode

<sub>Class</sub>

A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.

<sub>Mac Catalyst, macOS</sub>

```swift
class XMLDTDNode
```

## Overview

[XMLDTDNode](xmldtdnode.md) objects are the sole children of a [XMLDTD](xmldtd.md) object (possibly along with comment nodes and processing-instruction nodes). They themselves cannot have any children.

[XMLDTDNode](xmldtdnode.md) objects can be of four kinds—element, attribute-list, entity, or notation declaration—and can also be of a subkind, as specified by a [DTDKind](xmldtdnode/dtdkind-swift.enum.md) constant. For example, a DTD entity-declaration node could represent an unparsed entity declaration ([NSXMLEntityUnparsedKind](xmldtdnode/dtdkind-swift.enum/unparsed.md)) rather than a parameter entity declaration ([NSXMLEntityParameterKind](xmldtdnode/dtdkind-swift.enum/parameter.md)). You can use a DTD node’s subkind to help determine how to handle the value of the node.

You can create an [XMLDTDNode](xmldtdnode.md) object with the [- initWithXMLString:](<xmldtdnode/init(xmlstring_)-1dyhd.md>) method, the [XMLNode](xmlnode.md) class method [+ DTDNodeWithXMLString:](<xmlnode/dtdnode(withxmlstring_).md>), or with the [XMLNode](xmlnode.md) initializer [- initWithKind:options:](<xmlnode/init(kind_options_).md>) (in the latter method supplying the appropriate [Kind](xmlnode/kind-swift.enum.md) constant).

Setting the object value or string value of an [XMLDTDNode](xmldtdnode.md) objects affects different parts of different kinds of declaration. See the related programming topic for more information.

## Relationships

- **Inherits From**: [XMLNode](xmlnode.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing an NSXMLDTDNode Object

- [- initWithXMLString:](<xmldtdnode/init(xmlstring_)-1dyhd.md>) — Returns an `NSXMLDTDNode` object initialized with the DTD declaration in a given string.

### Managing the DTD Node Kind

- [DTDKind](xmldtdnode/dtdkind-swift.property.md) — Returns the receiver’s DTD kind.

### Managing DTD Identifiers

- [external](xmldtdnode/isexternal.md) — True if the system id is set. Valid for entities and notations.
- [notationName](xmldtdnode/notationname.md) — Returns the name of the notation associated with the receiver.
- [publicID](xmldtdnode/publicid.md) — Returns the public identifier associated with the receiver.
- [systemID](xmldtdnode/systemid.md) — Returns the system identifier associated with the receiver.

### Constants

- [DTDKind](xmldtdnode/dtdkind-swift.enum.md) — The type defined for the constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.
- [DTD Node Kind Constants](dtd_node_kind_constants.md) — Constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.

### Initializers

- [- init](<xmldtdnode/init().md>)
- [init(XMLString:)](<xmldtdnode/init(xmlstring_)-1bnga.md>)
- [- initWithKind:options:](<xmldtdnode/init(kind_options_).md>)

## See Also

### Tree-Based Processing

- [XMLDTD](xmldtd.md) — A representation of a Document Type Definition.
- [XMLDocument](xmldocument.md) — An XML document as internalized into a logical tree structure.
- [XMLElement](xmlelement.md) — The element nodes in an XML tree structure.
- [XMLNode](xmlnode.md) — The nodes in the abstract, logical tree structure that represents an XML document.
