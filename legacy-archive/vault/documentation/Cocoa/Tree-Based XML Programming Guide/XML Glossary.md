---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/XMLGlossary.html
archived_at: '2026-07-15T07:17:09.956468Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Tree%20Controllers%20With%20NSXML%20Objects.md)

# XML Glossary

This glossary defines some of the terms specific to XML, DTD, and related specifications and technologies. It focuses primarily on terms that are part of the names of methods and constants declared by the NSXMLParser, NSXMLNode, NSXMLDocument, NSXMLElement, NSXMLDTD, and NSXMLDTDNode classes.

__atomic value__: A value with a simple type as defined by the XML Schema standard. The types include string, decimal, integer, float, double, Boolean, date, URI, array, and binary data. An XQuery query returns a _sequence_ of items that can contain one or more nodes or atomic values.

__attribute__: A property of an _element_ expressed as a name-value pair. Attributes are used to encode data or provide metadata that is associated with an element. In the following example, “version” is the name of an attribute of element `plist` and its value is `“1.0”`:

```xml
<plist version=”1.0”>
```

__attribute list declaration__: Identifies in a DTD an element that has attributes, the names of those attributes, what values the attributes may have, and default values. Example:

```
<!ATTLIST phone location (home | office | mobile) "home">
```

In this example, `phone` is the element name, `location` is the attribute name, `(home | office | mobile)` is the allowable values, and `home` is the default value.

__canonical__: A form of an XML document in which it can be compared against another document for equivalence. If two documents with differing physical representations have the same canonical form, they are considered logically equivalent within the given application context. The canonical form of an XML document is defined by the World Wide Web Consortium at `http://www.w3.org/TR/xml-c14n`.

__CDATA block__: A section of text that the parser should pass uninterpreted to the client application. It appears as element content. CDATA blocks are often used for code or data that contains “prohibited” characters, that is characters of special syntactical significance to the parser (for example, “<“ and “&”). You can also use an _entity reference_ to express any of these prohibited characters (for example, `<`) is a built-in entity reference for specifying the “escaped” `<` character.

__content model__: The part of an _element declaration_ that defines what the element may contain. A content model consists of the names of child elements, `#PCDATA` (indicating text), entity references, or `EMPTY` (indicating an empty element such as `<true/>`). Child elements and `#PCDATA` are enclosed within parentheses. Commas between child elements specify that the elements must occur in the given sequence. The vertical-bar character (“|”) instead of a comma indicates a logical OR relationship and can be used with `#PCDATA`. Occurrence modifiers can be applied to individual elements or groups of elements:

- “+” indicates the element or group can be repeated more than once but must occur at lease once.
- “?” indicates the element or group is optional and may occur only once.
- “\*” indicates the element or group is optional and can occur more than once.
- No modifier indicates that the element or group must occur only once.

Examples of content models.

```
(#PCDATA)
(%plistObject)*
(lastName, middleInitial?, firstName, phone*)*
```

__document order__: The order of XML mark-up constructs as they appear in a document. When you send the NSXMLNode messages `nextNode` (or `previousNode`) to each successive node object encountered in an NSXML tree, you are traversing the tree forward (or backward) in document order.

__DOM (Document Object Model)__: An API for accessing and manipulating XML documents as tree structures. DOM derives from a World Wide Web Consortium recommendation for a general object model for storing hierarchically structured documents in memory.

__DTD (Document Type Definition)__: A way to define the legal elements and other building blocks of an XML document.

__element__: Markup tags that identify the nature of the content they surround. Elements have names and may contain textual data, child elements, _processing instructions_, comments, and _CDATA blocks_. An element has a single parent element, except for a document’s root element, which has no parent. An element may also have _attributes_ and _namespace prefixes_ associated with it. Elements can also be empty (that is, without content) and the developer can use them as flags.

The following is an example of an element with an attribute and mixed content (in this case, text, a child element, and a CDATA block):

```
<para ref_num=”80458”>
    The following C++ code gives an example of how
    <code>cout</code> is used:
    <![CDATA[std::cout << "Hello, World!\n";
    >
</para>
```

__element declaration__: Specifies in a DTD the name of an element and what is permitted as content of the element. The declaration may specify child elements, text, and entity references as content. It prescribes the order of child elements and (for single elements or for the entire group) whether it is required and whether it can appear multiple times. Examples:

```
<!ELEMENT addresses (person)*>
<!ELEMENT person (lastName, firstName, phone*, email*, address*)>
<!ELEMENT lastName (#PCDATA)>
```

See also _content model_.

__entity declaration__: Associates in a DTD a name with some piece of XML content that is identified by an _entity reference_. That content can be a literal value (such as identified by a character reference), a variable value specified elsewhere in the DTD, or some textual or binary value referenced in an external file. The last type of entity is called an external entity. Examples:

```
<!ENTITY % plistObject “(array | date | dict | real | integer | string | true | false )” >
<!ENTITY CompanyLogo SYSTEM “/Library/Images/logo.gif” NDATA GIF87A>
```

__entity and character reference__: A reference in text to an externally or internally declared _entity declaration_. It must begin with an ampersand and end with a semicolon. You can refer to entities that you declare elsewhere. There are five predefined entities: “<“, “>”, “&”, single-quote character, and double-quote character. Character references start with “&#” and are followed by numerical code points. Examples of references are `&apos;`, `>`, `&#231;` ; the first two are built-in entity references and the last is a character reference. See also _unparsed entity_.

__model__: See _content model_.

__namespace__: A URI (Universal Resource Identifier) that qualifies an element or attribute name so as to avoid name conflicts when a document contains XML from different sources. You declare a namespace in the start tag of an element by appending a prefix to the predefined `xmlns` attribute (separated by a colon), and then associating this with the value of the URI; for example:

```
<h:table xmlns:h="http://www.w3.org/TR/html4/">
```

Thereafter, you need only use a _namespace prefix_ (“h” in the above example) with an element (separated by a colon) to identify the element unambiguously. All child elements of the element with the namespace declaration are associated with the same namespace through the prefix. The prefix-element name combination (`h:table` from the example above) is called a _qualified name_. A namespace declaration with no prefix after `xmlns` defines a default namespace, unless the value is an empty string, which means “no namespace.” The URI in a namespace declaration doesn’t have to point to anything; it is just a convenient way to get a unique name.

__namespace prefix__: A prefix defined in a namespace declaration to identify the namespace a particular element is associated with. The namespace's qualified name (`xmlns:`_localname_) appears only during output. All other operations, such as those that get or set a namespace node’s value, use the local name only. See also _namespace_.

__normalize__: To coalesce all adjacent child text nodes into a single text node while removing empty text nodes. Normalization is highly recommended before performing XPath and XQuery queries.

__notation__: Identifies by name the format either of an _unparsed entity_ or an element bearing a specific notation attribute; it can also identify the target of a processing instruction. A notation declaration gives a name to the notation and an external identifier that enables a parser or its client to locate a helper application that can process the data specified by the notation. Notations occur in attribute values, attribute-list declarations, and entity declarations.

__processing instruction__: A construct that provides information to the application processing the XML document. The instructions could instruct the application how, for example, to interpret the XML or display the results. Processing instructions can occur within elements or at the top level of a document. The first word of the processing instruction is called the target (its name) and every thing else is its object value. Example:

```
<?sort alpha-ascending?>
```

__qualified name__: An element’s full name, consisting of prefix, colon, and local name. See also _namespace_.

__sequence__: A collection of items, each of which can be a node or an _atomic value_. XQuery queries return a sequence (an NSArray in Cocoa), which may contain only a single item.

__validation__: A procedure that checks an XML document against the logical structure described by declarations in the associated DTD (or other schema) to see if the XML conforms to it. Some of the constraints involved in validation are proper element sequence and nesting, specification of required attributes, and correct attribute type. For example, if an element is supposed to have one or more child elements but doesn’t, the document containing the element is invalid. Before an XML document can be validated, it must first be _well-formed_.

__unparsed entity__: An external resource referred to by _entity reference_ whose contents may be binary data or text (including non-XML text). Each unparsed entity has a _notation_ associated with it.

__well-formed__: Refers to an XML document that obeys the syntax of XML. A parser cannot parse a document if its XML is not well-formed. Some of the checks for whether a document is well-formed are:

- Element start tags must have end tags (except for empty elements).
- Attribute values must be quoted.
- Parameter entities must be declared before they are used.
- Markup constructs appear only where permitted.

__XHTML__: A more strictly prescribed version of HTML that makes it well-formed XML. XHTML is an official World Wide Web Consortium recommendation.

__XPath__: An XML query language for locating nodes with an XML tree structure. It allows location paths, predicates, and general expressions in queries. The Cocoa implementation uses XPath 2.0, which is a World Wide Web Consortium recommendation. The NSXMLNode class enables XPath queries through its `nodesForXPath:error:` method. (Note that the NSXML classes do not support deprecated XPath 1.0 features such as namespace axis.)

__XQuery__: A flexible and powerful XML query language that lets you compose logically complex queries using operators, quantifiers, functions and FLOWR expressions (referring to the keywords `for`, `let`, `order
by`, `where`, and `return`). The NSXMLNode class enables XQuery 1.0 queries through its `objectsForXQuery:error:` method

__XSLT (Extensible Stylesheet Language Transformations)__: An XML application for transforming an XML document into another XML document or into an HTML, RTF, or plain-text document. The stylesheet used in a transformation has template rules, each consisting of a pattern and a template. The NSXMLDocument class permits access to XSLT through its `objectByApplyingXSLT:error:` and `objectByApplyingXSLTAtURL:error:` methods.

[Next](Document%20Revision%20History.md)[Previous](Using%20Tree%20Controllers%20With%20NSXML%20Objects.md)

