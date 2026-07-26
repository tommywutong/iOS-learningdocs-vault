---
title: XMLDTD
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldtd
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd.json'
content_hash: 'sha256:74a8ea3afdb86c6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XMLDTD

<sub>Class</sub>

A representation of a Document Type Definition.

<sub>Mac Catalyst, macOS</sub>

```swift
class XMLDTD
```

## Overview

An instance of the [XMLDTD](xmldtd.md) class is held as a property of an [XMLDocument](xmldocument.md) instance, accessed through the [XMLDocument](xmldocument.md) property [DTD](xmldocument/dtd.md).

In the data model, an [XMLDTD](xmldtd.md) object is conceptually similar to namespace and attribute nodes: it is not considered to be a child of the [XMLDocument](xmldocument.md) object although it is closely associated with it. It is at the “root” of a shallow tree consisting primarily of nodes representing DTD declarations. Acceptable child nodes are instances of the [XMLDTDNode](xmldtdnode.md) class as well as [XMLNode](xmlnode.md) objects representing comment nodes and processing-instruction nodes.

You create an `NSXMLDTD` object in one of three ways:

- By processing an XML document with its own internal (in-line) DTD
- By process a standalone (external) DTD
- Programmatically

Once an [XMLDTD](xmldtd.md) instance is in place, you can add, remove, and change the [XMLDTDNode](xmldtdnode.md) objects representing various DTD declarations. When you write the document out as XML, the new or modified internal DTD is included (assuming you set the DTD in the [XMLDocument](xmldocument.md) instance). You may also programmatically create an external DTD and write that out to its own file.

## Relationships

- **Inherits From**: [XMLNode](xmlnode.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing an NSXMLDTD Object

- [- initWithContentsOfURL:options:error:](<xmldtd/init(contentsof_options_).md>) — Initializes and returns an `NSXMLDTD` object created from the DTD declarations in a URL-referenced source.
- [- initWithData:options:error:](<xmldtd/init(data_options_).md>) — Initializes and returns an `NSXMLDTD` object created from the DTD declarations encapsulated in an [NSData](nsdata.md) object

### Managing DTD Identifiers

- [publicID](xmldtd/publicid.md) — Returns the receiver’s public identifier.
- [systemID](xmldtd/systemid.md) — Returns the receiver’s system identifier.

### Manipulating Child Nodes

- [- addChild:](<xmldtd/addchild(__).md>) — Adds a child node to the end of the list of existing children.
- [- insertChild:atIndex:](<xmldtd/insertchild(__at_).md>) — Inserts a child node in the receiver’s list of children at a specific location in the list.
- [- insertChildren:atIndex:](<xmldtd/insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<xmldtd/removechild(at_).md>) — Removes the child node at a particular location in the receiver’s list of children.
- [- replaceChildAtIndex:withNode:](<xmldtd/replacechild(at_with_).md>) — Replaces a child at a particular index with another child.
- [- setChildren:](<xmldtd/setchildren(__).md>) — Removes all existing children of the receiver and replaces them with an array of new child nodes.

### Getting DTD Nodes by Name

- [+ predefinedEntityDeclarationForName:](<xmldtd/predefinedentitydeclaration(forname_).md>) — Returns a DTD node representing the predefined entity declaration with the specified name.
- [- elementDeclarationForName:](<xmldtd/elementdeclaration(forname_).md>) — Returns the DTD node representing an element declaration for a specified element.
- [- attributeDeclarationForName:elementName:](<xmldtd/attributedeclaration(forname_elementname_).md>) — Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [- entityDeclarationForName:](<xmldtd/entitydeclaration(forname_).md>) — Returns the DTD node representing the entity declaration for a specified entity.
- [- notationDeclarationForName:](<xmldtd/notationdeclaration(forname_).md>) — Returns the DTD node representing the notation declaration identified by the specified notation name.

### Initializers

- [- init](<xmldtd/init().md>)
- [init(contentsOfURL:options:)](<xmldtd/init(contentsofurl_options_).md>)

## See Also

### Tree-Based Processing

- [XMLDTDNode](xmldtdnode.md) — A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [XMLDocument](xmldocument.md) — An XML document as internalized into a logical tree structure.
- [XMLElement](xmlelement.md) — The element nodes in an XML tree structure.
- [XMLNode](xmlnode.md) — The nodes in the abstract, logical tree structure that represents an XML document.
