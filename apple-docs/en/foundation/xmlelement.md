---
title: XMLElement
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlelement
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement.json'
content_hash: 'sha256:f81c877e337932f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XMLElement

<sub>Class</sub>

The element nodes in an XML tree structure.

<sub>Mac Catalyst, macOS</sub>

```swift
class XMLElement
```

## Overview

An [XMLElement](xmlelement.md) object may have child nodes, specifically comment nodes, processing-instruction nodes, text nodes, and other [XMLElement](xmlelement.md) nodes. It may also have attribute nodes and namespace nodes associated with it (however, namespace and attribute nodes are not considered children). Any attempt to add a [XMLDocument](xmldocument.md) node, [XMLDTD](xmldtd.md) node, namespace node, or attribute node as a child raises an exception. If you add a child node to an [XMLElement](xmlelement.md) object and that child already has a parent, [XMLElement](xmlelement.md) raises an exception; the child must be detached or copied first.

### Subclassing Notes

You can subclass `NSXMLElement` if you want element nodes with more specialized attributes or behavior, for example, paragraph and font attributes that specify how the string value of the element should appear.

#### Methods to Override

To subclass `NSXMLElement` you need to override the primary initializer, [- initWithName:URI:](<xmlelement/init(name_uri_)-1r286.md>), and the methods listed below. In most cases, you need only invoke the superclass implementation, adding any subclass-specific code before or after the invocation, as necessary.

| [- addAttribute:](<xmlelement/addattribute(__).md>) | [- removeNamespaceForPrefix:](<xmlelement/removenamespace(forprefix_).md>) |
|---|---|
| [- removeAttributeForName:](<xmlelement/removeattribute(forname_).md>) | [namespaces](xmlelement/namespaces.md) |
| [attributes](xmlelement/attributes.md) | [namespaces](xmlelement/namespaces.md) |
| [- attributeForLocalName:URI:](<xmlelement/attribute(forlocalname_uri_).md>) | [- insertChild:atIndex:](<xmlelement/insertchild(__at_).md>) |
| [attributes](xmlelement/attributes.md) | [- removeChildAtIndex:](<xmlelement/removechild(at_).md>) |
| [- addNamespace:](<xmlelement/addnamespace(__).md>) | [- setChildren:](<xmlelement/setchildren(__).md>) |

`NSXMLElement` implements  [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>) to perform a deep comparison: two [XMLDocument](xmldocument.md) objects are not considered equal unless they have the same name, same child nodes, same attributes, and so on. If you want a different standard of comparison, override `isEqual:`.

#### Special Considerations

Because of the architecture and data model of NSXML, when it parses and processes a source of XML it cannot know about your subclass unless you override the class method [+ replacementClassForClass:](<xmldocument/replacementclass(for_).md>) to return your custom class in place of an NSXML class. If your custom class has no direct NSXML counterpart—for example, it is a subclass of `NSXMLNode` that represents CDATA sections—then you can walk the tree after it has been created and insert the new node where appropriate.

Note that you can safely set the root element of the XML document (using the `NSXMLDocument` [- setRootElement:](<xmldocument/setrootelement(__).md>)method) to be an instance of your subclass because this method only checks to see if the added node is of an element kind (`NSXMLElementKind`). These precautions do not apply, of course, if you are creating an XML tree programmatically.

## Relationships

- **Inherits From**: [XMLNode](xmlnode.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing NSXMLElement Objects

- [- initWithName:](<xmlelement/init(name_).md>) — Returns an `NSXMLElement` object initialized with the specified name.
- [- initWithName:stringValue:](<xmlelement/init(name_stringvalue_).md>) — Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [- initWithName:URI:](<xmlelement/init(name_uri_)-1r286.md>) — Returns an `NSXMLElement` object initialized with the specified name and URI.
- [- initWithXMLString:error:](<xmlelement/init(xmlstring_)-7vkg7.md>) — Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [- initWithKind:options:](<xmlelement/init(kind_options_).md>)

### Obtaining Child Elements

- [- elementsForName:](<xmlelement/elements(forname_).md>) — Returns the child element nodes (as `NSXMLElement` objects) of the receiver that have a specified name.
- [- elementsForLocalName:URI:](<xmlelement/elements(forlocalname_uri_).md>) — Returns the child element nodes (as `NSXMLElement` objects) of the receiver that are matched with the specified local name and URI.

### Manipulating Child Elements

- [- addChild:](<xmlelement/addchild(__).md>) — Adds a child node at the end of the receiver’s current list of children.
- [- insertChild:atIndex:](<xmlelement/insertchild(__at_).md>) — Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [- insertChildren:atIndex:](<xmlelement/insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<xmlelement/removechild(at_).md>) — Removes the child node of the receiver identified by a given index.
- [- replaceChildAtIndex:withNode:](<xmlelement/replacechild(at_with_).md>) — Replaces a child node at a specified location with another child node.
- [- setChildren:](<xmlelement/setchildren(__).md>) — Sets all child nodes of the receiver at once, replacing any existing children.
- [- normalizeAdjacentTextNodesPreservingCDATA:](<xmlelement/normalizeadjacenttextnodespreservingcdata(__).md>) — Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.

### Handling Attributes

- [- addAttribute:](<xmlelement/addattribute(__).md>) — Adds an attribute node to the receiver.
- [- attributeForName:](<xmlelement/attribute(forname_).md>) — Returns the attribute node of the receiver with the specified name.
- [- attributeForLocalName:URI:](<xmlelement/attribute(forlocalname_uri_).md>) — Returns the attribute node of the receiver that is identified by a local name and URI.
- [attributes](xmlelement/attributes.md) — Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [- removeAttributeForName:](<xmlelement/removeattribute(forname_).md>) — Removes an attribute node identified by name.
- [- setAttributesWithDictionary:](<xmlelement/setattributeswith(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [- setAttributesAsDictionary:](<xmlelement/setattributesas(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary. _(deprecated)_

### Setting Element URI

- [setURI:](nsxmlnode-seturi.md) — Sets the URI of the receiver.

### Handling Namespaces

- [- addNamespace:](<xmlelement/addnamespace(__).md>) — Adds a namespace node to the receiver.
- [namespaces](xmlelement/namespaces.md) — Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [- namespaceForPrefix:](<xmlelement/namespace(forprefix_).md>) — Returns the namespace node with a specified prefix.
- [- removeNamespaceForPrefix:](<xmlelement/removenamespace(forprefix_).md>) — Removes a namespace node that is identified by a given prefix.
- [- resolveNamespaceForName:](<xmlelement/resolvenamespace(forname_).md>) — Returns the namespace node with the prefix matching the given qualified name.
- [- resolvePrefixForNamespaceURI:](<xmlelement/resolveprefix(fornamespaceuri_).md>) — Returns the prefix associated with the specified URI.

### Initializers

- [init(XMLString:)](<xmlelement/init(xmlstring_)-1wgno.md>)
- [init(name:URI:)](<xmlelement/init(name_uri_)-67uti.md>)

## See Also

### Tree-Based Processing

- [XMLDTD](xmldtd.md) — A representation of a Document Type Definition.
- [XMLDTDNode](xmldtdnode.md) — A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [XMLDocument](xmldocument.md) — An XML document as internalized into a logical tree structure.
- [XMLNode](xmlnode.md) — The nodes in the abstract, logical tree structure that represents an XML document.
