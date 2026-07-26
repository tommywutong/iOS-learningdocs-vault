---
title: XMLNode
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode.json'
content_hash: 'sha256:091d540ff37b8cd1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XMLNode

<sub>Class</sub>

The nodes in the abstract, logical tree structure that represents an XML document.

<sub>Mac Catalyst, macOS</sub>

```swift
class XMLNode
```

## Overview

Node objects can be of different kinds, corresponding to the following markup constructs in an XML document: element, attribute, text, processing instruction, namespace, and comment. In addition, a document-node object (specifically, an instance of [XMLDocument](xmldocument.md)) represents an XML document in its entirety. [XMLNode](xmlnode.md) objects can also represent document type declarations as well as declarations in Document Type Definitions (DTDs). Class factory methods of [XMLNode](xmlnode.md) enable you to create nodes of each kind. Only document, element, and DTD nodes may have child nodes.

Among the XML family of classes (excluding [XMLParser](xmlparser.md)) the [XMLNode](xmlnode.md) class is the base class. Inheriting from it are the classes [XMLElement](xmlelement.md), [XMLDocument](xmldocument.md), [XMLDTD](xmldtd.md), and [XMLDTDNode](xmldtdnode.md). [XMLNode](xmlnode.md) specifies the interface common to all XML node objects and defines common node behavior and attributes, for example hierarchy level, node name and value, tree traversal, and the ability to emit representative XML markup text.

### Subclassing Notes

You can subclass [XMLNode](xmlnode.md) if you want nodes of kinds different from the supported ones, You can also create a subclass with more specialized attributes or behavior than [XMLNode](xmlnode.md).

#### Methods to Override

To subclass [XMLNode](xmlnode.md) you need to override the primary initializer, [- initWithKind:options:](<xmlnode/init(kind_options_).md>), and the methods listed below. In most cases, you need only invoke the superclass implementation, adding any subclass-specific code before or after the invocation, as necessary.

| [kind](xmlnode/kind-swift.property.md) | [parent](xmlnode/parent.md) |
|---|---|
| [name](xmlnode/name.md) | [- childAtIndex:](<xmlnode/child(at_).md>) |
| [name](xmlnode/name.md) | [childCount](xmlnode/childcount.md) |
| [objectValue](xmlnode/objectvalue.md) | [children](xmlnode/children.md) |
| [objectValue](xmlnode/objectvalue.md) | [- detach](<xmlnode/detach().md>) |
| [stringValue](xmlnode/stringvalue.md) | [localName](xmlnode/localname.md) |
| [- setStringValue:resolvingEntities:](<xmlnode/setstringvalue(__resolvingentities_).md>) | [prefix](xmlnode/prefix.md) |
| [index](xmlnode/index.md) | [URI](xmlnode/uri.md) |

By default [XMLNode](xmlnode.md) implements the `NSObject` [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>) method to perform a deep comparison: two [XMLNode](xmlnode.md) objects are not considered equal unless they have the same name, same child nodes, same attributes, and so on. The comparison looks at the node and its children, but does not include the node’s parent. If you want a different standard of comparison, override `isEqual:`.

#### Special Considerations

Because of the architecture and data model of NSXML, when it parses and processes a source of XML it cannot know about your subclass unless you override the [XMLDocument](xmldocument.md) class method [+ replacementClassForClass:](<xmldocument/replacementclass(for_).md>) to return your custom class in place of an NSXML class. If your custom class has no direct NSXML counterpart—for example, it is a subclass of [XMLNode](xmlnode.md) that represents CDATA sections—then you can walk the tree after it has been created and insert the new node where appropriate.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [XMLDTD](xmldtd.md), [XMLDTDNode](xmldtdnode.md), [XMLDocument](xmldocument.md), [XMLElement](xmlelement.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating and Initializing Node Objects

- [- initWithKind:](<xmlnode/init(kind_).md>) — Returns an `NSXMLNode` instance initialized with the constant indicating node kind.
- [- initWithKind:options:](<xmlnode/init(kind_options_).md>) — Returns an `NSXMLNode` instance initialized with the constant indicating node kind and one or more initialization options.
- [+ document](<xmlnode/document().md>) — Returns an empty document node.
- [+ documentWithRootElement:](<xmlnode/document(withrootelement_).md>) — Returns an [XMLDocument](xmldocument.md) object initialized with a given root element.
- [+ elementWithName:](<xmlnode/element(withname_).md>) — Returns an [XMLElement](xmlelement.md) object with a given tag identifier, or name
- [+ elementWithName:children:attributes:](<xmlnode/element(withname_children_attributes_).md>) — Returns an [XMLElement](xmlelement.md) object with the given tag (name), attributes, and children.
- [+ elementWithName:stringValue:](<xmlnode/element(withname_stringvalue_).md>) — Returns an [XMLElement](xmlelement.md) object with a single text-node child containing the specified text.
- [+ elementWithName:URI:](<xmlnode/element(withname_uri_).md>) — Returns an element whose fully qualified name is specified.
- [+ attributeWithName:stringValue:](<xmlnode/attribute(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing an attribute node with a given name and string.
- [+ attributeWithName:URI:stringValue:](<xmlnode/attribute(withname_uri_stringvalue_).md>) — Returns an `NSXMLNode` object representing an attribute node with a given qualified name and string.
- [+ textWithStringValue:](<xmlnode/text(withstringvalue_).md>) — Returns an `NSXMLNode` object representing a text node with specified content.
- [+ commentWithStringValue:](<xmlnode/comment(withstringvalue_).md>) — Returns an [XMLNode](xmlnode.md) object representing a comment node containing given text.
- [+ namespaceWithName:stringValue:](<xmlnode/namespace(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing a namespace with a specified name and URI.
- [+ DTDNodeWithXMLString:](<xmlnode/dtdnode(withxmlstring_).md>) — Returns a [XMLDTDNode](xmldtdnode.md) object representing the DTD declaration for an element, attribute, entity, or notation based on a given string.
- [+ predefinedNamespaceForPrefix:](<xmlnode/predefinednamespace(forprefix_).md>) — Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.
- [+ processingInstructionWithName:stringValue:](<xmlnode/processinginstruction(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing a processing instruction with a specified name and value.

### Managing XML Node Objects

- [index](xmlnode/index.md) — Returns the index of the receiver identifying its position relative to its sibling nodes.
- [kind](xmlnode/kind-swift.property.md) — Returns the kind of node the receiver is as a constant of type [Kind](xmlnode/kind-swift.enum.md).
- [level](xmlnode/level.md) — Returns the nesting level of the receiver within the tree hierarchy.
- [name](xmlnode/name.md) — Returns the name of the receiver.
- [objectValue](xmlnode/objectvalue.md) — Returns the object value of the receiver.
- [stringValue](xmlnode/stringvalue.md) — Returns the content of the receiver as a string value.
- [- setStringValue:resolvingEntities:](<xmlnode/setstringvalue(__resolvingentities_).md>) — Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](nsxmlnode-seturi.md) — Sets the URI of the receiver.
- [URI](xmlnode/uri.md) — Returns the URI associated with the receiver.

### Navigating the Tree of Nodes

- [rootDocument](xmlnode/rootdocument.md) — Returns the [XMLDocument](xmldocument.md) object containing the root element and representing the XML document as a whole.
- [parent](xmlnode/parent.md) — Returns the parent node of the receiver.
- [- childAtIndex:](<xmlnode/child(at_).md>) — Returns the child node of the receiver at the specified location.
- [childCount](xmlnode/childcount.md) — Returns the number of child nodes the receiver has.
- [children](xmlnode/children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextNode](xmlnode/next.md) — Returns the next `NSXMLNode` object in document order.
- [nextSibling](xmlnode/nextsibling.md) — Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [previousNode](xmlnode/previous.md) — Returns the previous `NSXMLNode` object in document order.
- [previousSibling](xmlnode/previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [- detach](<xmlnode/detach().md>) — Detaches the receiver from its parent node.

### Emitting Node Content

- [XMLString](xmlnode/xmlstring.md) — Returns the string representation of the receiver as it would appear in an XML document.
- [- XMLStringWithOptions:](<xmlnode/xmlstring(options_).md>) — Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.
- [- canonicalXMLStringPreservingComments:](<xmlnode/canonicalxmlstringpreservingcomments(__).md>) — Returns a string object encapsulating the receiver’s XML in canonical form.
- [description](xmlnode/description.md)

### Executing Queries

- [- nodesForXPath:error:](<xmlnode/nodes(forxpath_).md>) — Returns the nodes resulting from executing an XPath query upon the receiver.
- [- objectsForXQuery:error:](<xmlnode/objects(forxquery_).md>) — Returns the objects resulting from executing an XQuery query upon the receiver.
- [- objectsForXQuery:constants:error:](<xmlnode/objects(forxquery_constants_).md>) — Returns the objects resulting from executing an XQuery query upon the receiver.
- [XPath](xmlnode/xpath.md) — Returns the XPath expression identifying the receiver’s location in the document tree.

### Managing Namespaces

- [localName](xmlnode/localname.md) — Returns the local name of the receiver.
- [+ localNameForName:](<xmlnode/localname(forname_).md>) — Returns the local name from the specified qualified name.
- [prefix](xmlnode/prefix.md) — Returns the prefix of the receiver’s name.
- [+ prefixForName:](<xmlnode/prefix(forname_).md>) — Returns the prefix from the specified qualified name.

### Constants

- [Kind](xmlnode/kind-swift.enum.md) — `NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [- initWithKind:](<xmlnode/init(kind_).md>) and [- initWithKind:options:](<xmlnode/init(kind_options_).md>):
- [Options](xmlnode/options.md) — These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [XMLDocument](xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [- initWithKind:options:](<xmlnode/init(kind_options_).md>) and [- XMLStringWithOptions:](<xmlnode/xmlstring(options_).md>).

### Initializers

- [- init](<xmlnode/init().md>)

## See Also

### Tree-Based Processing

- [XMLDTD](xmldtd.md) — A representation of a Document Type Definition.
- [XMLDTDNode](xmldtdnode.md) — A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [XMLDocument](xmldocument.md) — An XML document as internalized into a logical tree structure.
- [XMLElement](xmlelement.md) — The element nodes in an XML tree structure.
