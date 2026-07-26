---
title: XMLDocument
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument.json'
content_hash: 'sha256:3eabf54918b72555'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XMLDocument

<sub>Class</sub>

An XML document as internalized into a logical tree structure.

<sub>Mac Catalyst, macOS</sub>

```swift
class XMLDocument
```

## Overview

An [XMLDocument](xmldocument.md) object can have multiple child nodes but only one element, the root element. Any other node must be a [XMLNode](xmlnode.md) object representing a comment or a processing instruction. If you attempt to add any other kind of child node to an [XMLDocument](xmldocument.md) object, such as an attribute, namespace, another document object, or an element other than the root, [XMLDocument](xmldocument.md) raises an exception. If you add a valid child node and that object already has a parent, [XMLDocument](xmldocument.md) raises an exception. An [XMLDocument](xmldocument.md) object may also have document-global attributes, such as XML version, character encoding, referenced DTD, and MIME type.

The initializers of the [XMLDocument](xmldocument.md) class read an external source of XML, whether it be a local file or remote website, parse it, and process it into the tree representation. You can also construct an [XMLDocument](xmldocument.md) programmatically. There are accessor methods for getting and setting document attributes, methods for transforming documents using XSLT, a method for dynamically validating a document, and methods for printing out the content of an [XMLDocument](xmldocument.md) as XML, XHTML, HTML, or plain text.

The [XMLDocument](xmldocument.md) class is thread-safe as long as any given instance is used only in one thread.

### Subclassing Notes

#### Methods to Override

To subclass `NSXMLDocument` you need to override the primary initializer, [- initWithData:options:error:](<xmldocument/init(data_options_).md>), and the methods listed below. In most cases, you need only invoke the superclass implementation, adding any subclass-specific code before or after the invocation, as necessary.

- [- rootElement](<xmldocument/rootelement().md>)
- [- setChildren:](<xmldocument/setchildren(__).md>)
- [- removeChildAtIndex:](<xmldocument/removechild(at_).md>)
- [- insertChild:atIndex:](<xmldocument/insertchild(__at_).md>)
- [characterEncoding](xmldocument/characterencoding.md)
- [characterEncoding](xmldocument/characterencoding.md)
- [documentContentKind](xmldocument/documentcontentkind.md)
- [documentContentKind](xmldocument/documentcontentkind.md)
- [DTD](xmldocument/dtd.md)
- [MIMEType](xmldocument/mimetype.md)
- [standalone](xmldocument/isstandalone.md)
- [version](xmldocument/version.md)
- [version](xmldocument/version.md)

By default `NSXMLDocument` implements the `NSObject` [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>) method to perform a deep comparison: two `NSXMLDocument` objects are not considered equal unless they have the same name, same child nodes, same attributes, and so on. The comparison does not consider the parent node (and hence the node’s location). If you want a different standard of comparison, override `isEqual:`.

#### Special Considerations

Because of the architecture and data model of NSXML, when it parses and processes a source of XML it cannot know about your subclass unless you override the class method [+ replacementClassForClass:](<xmldocument/replacementclass(for_).md>) to return your custom class in place of an `NSXML` class. If your custom class has no direct `NSXML` counterpart—for example, it is a subclass of `NSXMLNode` that represents CDATA sections—then you can walk the tree after it has been created and insert the new node where appropriate.

## Relationships

- **Inherits From**: [XMLNode](xmlnode.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing NSXMLDocument Objects

- [- initWithContentsOfURL:options:error:](<xmldocument/init(contentsof_options_).md>) — Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [- initWithData:options:error:](<xmldocument/init(data_options_).md>) — Initializes and returns an `NSXMLDocument` object created from an [NSData](nsdata.md) object.
- [- initWithRootElement:](<xmldocument/init(rootelement_).md>) — Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [- initWithXMLString:options:error:](<xmldocument/init(xmlstring_options_)-65m2r.md>) — Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.
- [+ replacementClassForClass:](<xmldocument/replacementclass(for_).md>) — Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.

### Managing Document Attributes

- [characterEncoding](xmldocument/characterencoding.md) — Sets the character encoding of the receiver to `encoding`,
- [documentContentKind](xmldocument/documentcontentkind.md) — Sets the kind of output content for the receiver.
- [DTD](xmldocument/dtd.md) — Returns an [XMLDTD](xmldtd.md) object representing the internal DTD associated with the receiver.
- [standalone](xmldocument/isstandalone.md) — Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [MIMEType](xmldocument/mimetype.md) — Returns the MIME type for the receiver.
- [version](xmldocument/version.md) — Sets the version of the receiver’s XML.

### Setting Document URI

- [setURI:](nsxmlnode-seturi.md) — Sets the URI of the receiver.

### Managing the Root Element

- [- rootElement](<xmldocument/rootelement().md>) — Returns the root element of the receiver.
- [- setRootElement:](<xmldocument/setrootelement(__).md>) — Set the root element of the receiver.

### Adding and Removing Child Nodes

- [- addChild:](<xmldocument/addchild(__).md>) — Adds a child node after the last of the receiver’s existing children.
- [- insertChild:atIndex:](<xmldocument/insertchild(__at_).md>) — Inserts a node object at specified position in the receiver’s array of children.
- [- insertChildren:atIndex:](<xmldocument/insertchildren(__at_).md>) — Inserts an array of children at a specified position in the receiver’s array of children.
- [- removeChildAtIndex:](<xmldocument/removechild(at_).md>) — Removes the child node of the receiver located at a specified position in its array of children.
- [- replaceChildAtIndex:withNode:](<xmldocument/replacechild(at_with_).md>) — Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [- setChildren:](<xmldocument/setchildren(__).md>) — Sets the child nodes of the receiver.

### Transforming a Document Using XSLT

- [- objectByApplyingXSLT:arguments:error:](<xmldocument/object(byapplyingxslt_arguments_).md>) — Applies the XSLT pattern rules and templates (specified as a data object) to the receiver and returns a document object containing transformed XML or HTML markup.
- [- objectByApplyingXSLTString:arguments:error:](<xmldocument/object(byapplyingxsltstring_arguments_).md>) — Applies the XSLT pattern rules and templates (specified as a string) to the receiver and returns a document object containing transformed XML or HTML markup.
- [- objectByApplyingXSLTAtURL:arguments:error:](<xmldocument/objectbyapplyingxslt(at_arguments_).md>) — Applies the XSLT pattern rules and templates located at a specified URL to the receiver and returns a document object containing transformed XML markup or an [NSData](nsdata.md) object containing plain text, RTF text, and so on.

### Writing a Document as XML Data

- [XMLData](xmldocument/xmldata.md) — Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.
- [- XMLDataWithOptions:](<xmldocument/xmldata(options_).md>) — Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.

### Validating a Document

- [- validateAndReturnError:](<xmldocument/validate().md>) — Validates the document against the governing schema and returns whether the document conforms to the schema.

### Constants

- [Input and Output Options](input_and_output_options.md) — Input and output options specifically intended for `NSXMLDocument` objects.
- [ContentKind](xmldocument/contentkind.md) — Type used to define the kind of document content.
- [Document Content Types](document-content-types.md) — Define document types.

### Initializers

- [- init](<xmldocument/init().md>)
- [init(XMLString:options:)](<xmldocument/init(xmlstring_options_)-87dms.md>)
- [init(contentsOfURL:options:)](<xmldocument/init(contentsofurl_options_).md>)

## See Also

### Tree-Based Processing

- [XMLDTD](xmldtd.md) — A representation of a Document Type Definition.
- [XMLDTDNode](xmldtdnode.md) — A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [XMLElement](xmlelement.md) — The element nodes in an XML tree structure.
- [XMLNode](xmlnode.md) — The nodes in the abstract, logical tree structure that represents an XML document.
