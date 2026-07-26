---
title: 'init(kind:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/init(kind:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/init(kind:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/init%28kind%3Aoptions%3A%29.json'
content_hash: 'sha256:33cc5bc88010744f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# init(kind:options:)

<sub>Initializer</sub>

Returns an `NSXMLNode` instance initialized with the constant indicating node kind and one or more initialization options.

<sub>Mac Catalyst, macOS</sub>

```swift
init(kind: XMLNode.Kind, options: XMLNode.Options = [])
```

## Parameters

- `kind` — An `enum` constant of type [Kind](kind-swift.enum.md) that indicates the type of node. See Constants for a list of valid NSXMLNodeKind constants.

- `options` — One or more constants that specify initialization options; if there are multiple constants, bit-OR them together. These options request operations on the represented XML related to fidelity (for example, preserving entities), quoting style, handling of empty elements, and other things. See Constants for a list of valid node-initialization constants.

## Return Value

An `NSXMLNode` object initialized with the given kind and options, or `nil` if the object couldn’t be created. If `kind` is not a valid NSXMLNodeKind constant, the method returns an `NSXMLNode` object of kind `NSXMLInvalidKind`.

## Discussion

Do not use this initializer for creating instances of [XMLDTDNode](../xmldtdnode.md) for attribute-list declarations. Instead, use the [+ DTDNodeWithXMLString:](<dtdnode(withxmlstring_).md>) class method of this class or the [- initWithXMLString:](<../xmldtdnode/init(xmlstring_)-1dyhd.md>) method of the `NSXMLDTDNode` class.

## See Also

### Creating and Initializing Node Objects

- [- initWithKind:](<init(kind_).md>) — Returns an `NSXMLNode` instance initialized with the constant indicating node kind.
- [+ document](<document().md>) — Returns an empty document node.
- [+ documentWithRootElement:](<document(withrootelement_).md>) — Returns an [XMLDocument](../xmldocument.md) object initialized with a given root element.
- [+ elementWithName:](<element(withname_).md>) — Returns an [XMLElement](../xmlelement.md) object with a given tag identifier, or name
- [+ elementWithName:children:attributes:](<element(withname_children_attributes_).md>) — Returns an [XMLElement](../xmlelement.md) object with the given tag (name), attributes, and children.
- [+ elementWithName:stringValue:](<element(withname_stringvalue_).md>) — Returns an [XMLElement](../xmlelement.md) object with a single text-node child containing the specified text.
- [+ elementWithName:URI:](<element(withname_uri_).md>) — Returns an element whose fully qualified name is specified.
- [+ attributeWithName:stringValue:](<attribute(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing an attribute node with a given name and string.
- [+ attributeWithName:URI:stringValue:](<attribute(withname_uri_stringvalue_).md>) — Returns an `NSXMLNode` object representing an attribute node with a given qualified name and string.
- [+ textWithStringValue:](<text(withstringvalue_).md>) — Returns an `NSXMLNode` object representing a text node with specified content.
- [+ commentWithStringValue:](<comment(withstringvalue_).md>) — Returns an [XMLNode](../xmlnode.md) object representing a comment node containing given text.
- [+ namespaceWithName:stringValue:](<namespace(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing a namespace with a specified name and URI.
- [+ DTDNodeWithXMLString:](<dtdnode(withxmlstring_).md>) — Returns a [XMLDTDNode](../xmldtdnode.md) object representing the DTD declaration for an element, attribute, entity, or notation based on a given string.
- [+ predefinedNamespaceForPrefix:](<predefinednamespace(forprefix_).md>) — Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.
- [+ processingInstructionWithName:stringValue:](<processinginstruction(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing a processing instruction with a specified name and value.
