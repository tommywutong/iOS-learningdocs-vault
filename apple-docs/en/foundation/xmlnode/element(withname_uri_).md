---
title: 'element(withName:uri:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/element(withname:uri:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/element(withname:uri:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/element%28withname%3Auri%3A%29.json'
content_hash: 'sha256:f541c9ed30e028b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# element(withName:uri:)

<sub>Type Method</sub>

Returns an element whose fully qualified name is specified.

<sub>Mac Catalyst, macOS</sub>

```swift
class func element(withName name: String, uri URI: String) -> Any
```

## Parameters

- `name` — A string that is the name (or tag identifier) of an element.

- `URI` — A URI (Universal Resource Identifier) that qualifies `name`.

## Return Value

An [XMLElement](../xmlelement.md) object or `nil` if the object cannot be created.

## Discussion

The equivalent XML markup is `<`_URI_`:``name``>``</`_URI_`:``name``>`.

## See Also

### Creating and Initializing Node Objects

- [- initWithKind:](<init(kind_).md>) — Returns an `NSXMLNode` instance initialized with the constant indicating node kind.
- [- initWithKind:options:](<init(kind_options_).md>) — Returns an `NSXMLNode` instance initialized with the constant indicating node kind and one or more initialization options.
- [+ document](<document().md>) — Returns an empty document node.
- [+ documentWithRootElement:](<document(withrootelement_).md>) — Returns an [XMLDocument](../xmldocument.md) object initialized with a given root element.
- [+ elementWithName:](<element(withname_).md>) — Returns an [XMLElement](../xmlelement.md) object with a given tag identifier, or name
- [+ elementWithName:children:attributes:](<element(withname_children_attributes_).md>) — Returns an [XMLElement](../xmlelement.md) object with the given tag (name), attributes, and children.
- [+ elementWithName:stringValue:](<element(withname_stringvalue_).md>) — Returns an [XMLElement](../xmlelement.md) object with a single text-node child containing the specified text.
- [+ attributeWithName:stringValue:](<attribute(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing an attribute node with a given name and string.
- [+ attributeWithName:URI:stringValue:](<attribute(withname_uri_stringvalue_).md>) — Returns an `NSXMLNode` object representing an attribute node with a given qualified name and string.
- [+ textWithStringValue:](<text(withstringvalue_).md>) — Returns an `NSXMLNode` object representing a text node with specified content.
- [+ commentWithStringValue:](<comment(withstringvalue_).md>) — Returns an [XMLNode](../xmlnode.md) object representing a comment node containing given text.
- [+ namespaceWithName:stringValue:](<namespace(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing a namespace with a specified name and URI.
- [+ DTDNodeWithXMLString:](<dtdnode(withxmlstring_).md>) — Returns a [XMLDTDNode](../xmldtdnode.md) object representing the DTD declaration for an element, attribute, entity, or notation based on a given string.
- [+ predefinedNamespaceForPrefix:](<predefinednamespace(forprefix_).md>) — Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.
- [+ processingInstructionWithName:stringValue:](<processinginstruction(withname_stringvalue_).md>) — Returns an `NSXMLNode` object representing a processing instruction with a specified name and value.
