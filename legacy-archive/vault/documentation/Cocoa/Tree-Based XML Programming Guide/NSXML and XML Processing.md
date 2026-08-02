---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/NSXMLFeatures.html
archived_at: '2026-07-15T07:17:02.429308Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](The%20Data%20Model%20of%20NSXML.md)[Previous](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)

# NSXML and XML Processing

With the NSXML set of Foundation classes you can create, manipulate, query, and modify XML documents of various types, including webpages, configuration files, and XML-formatted data files. NSXML operates on abstract, logical tree structures that represent XML documents. You can have these tree representations write themselves out as XML documents. You can also convert them into other XML trees using XSLT. Input documents, output documents, or transformed documents can be HTML as well as XML. With NSXML you can also internalize a DTD (Document Type Definition) as a tree structure and validate an XML document against its DTD.

As a technology, NSXML also includes support for XQuery 1.0 and XPath 2.0, which enable you to perform queries on XML documents. For more information on XQuery and XPath, see [XQuery and Other XML Technologies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjtfu4tmobxg4)

XML is a ubiquitous and increasingly important document-markup format for structuring information that can be applied to virtually any computing purpose. The format is so flexible that XML applications can include technologies as diverse as publishing, electronic data interchange, network management, and vector graphics. The attraction of XML is apparent: It is a text-based, structured, cross-platform storage format for data of any sort.

You can use the NSXML API in your own applications when you need to process information in XML-formatted sources. With NSXML you can create, alter, query, and transform XML documents or website pages in just a few lines of code. The DOM-style tree-based data model of NSXML enables you to insert, delete, and modify nodes at any point in a tree. (For a discussion of this model, see [The Data Model of NSXML](The%20Data%20Model%20of%20NSXML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjufvbuuqsjivdumri).) You can either have NSXML read an existing XML document into an internal tree structure, or you can create a tree representation from scratch. NSXML lets you search for particular nodes and values in the tree by either walking the tree or using the XQuery or XPath query languages. When you have finished working with an XML document, you can ask the tree representation to print itself out as ordered and properly structured XML or XHTML code.

Architecturally, NSXML depends on an event-driven XML parser to parse input XML documents before it converts them into tree structures. The public Cocoa interface to this parser is the NSXMLParser class.

NSXML is not the best solution for all situations where XML must be processed. Internal tree representations can take up a lot of application memory, especially for operations such as validation and XSLT transformations. If you simply need to find certain values in an XML document, and don’t need a persistent representation of the XML to modify, then the better Cocoa alternative is the event-driven parsing model offered by the NSXMLParser class.

In addition to the methods that allow you to create and manipulate the nodes and node values in DOM-style tree structures, NSXML has many other features, including the following:

- _Object values_. Nodes of all kinds, but particularly elements and attributes, can have values associated with them. These values are usually strings, but you can specify object values for nodes that represent non-string types, such as decimal, `float`, and date. Your application can, for example, interpret the format of a string value and convert it to an NSCalendarDate or NSNumber object. When you ask for the string value of an NSXML object, and its value is set as an object, NSXML returns the string formatted as a canonical type according to the W3C XML Schema: Datatypes specification ([http://www.w3.org/TR/xmlschema-2/](http://www.w3.org/TR/xmlschema-2/)). You can also define the string representations of custom objects.
- _DTD nodes_. NSXML parses internal Document Type Definitions (DTDs) and composes trees representing the structure of the declarations. Among the nodes of such trees are objects representing entities, attribute-list declarations, and element declarations. You can programmatically modify such trees or even create them from scratch and then write out the new or modified DTD. When NSXML processes an XML document it can, if requested, validate it against an internal or external DTD. See [DTD and Other Schemas](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjtfu4tmojug4) for further information.
- _Namespaces_. NSXML allows you to distinguish between elements and attributes in different namespaces in an XML document. With methods in the NSXMLNode and NSXMLElement classes you can create namespace nodes, associate them with an element and its attributes, query elements for their declared namespaces, and have the prefixes of namespaces resolve dynamically against the namespace URIs and local names associated with attributes and elements.
- _Tidy XML and HTML_. NSXML uses an open-source tool that checks and corrects HTML and XML documents to make them compliant with the Worldwide Web Consortium (W3C) standards. When HTML is “tidied,” it is converted to XHTML. You request tidy XML or HTML as an option in initialization and output methods.
- _XQuery_ and _XPath _. With XQuery or XPath, you can quickly locate particular nodes or values in an XML document and you can transform or create XML nodes or even documents. See [XQuery and Other XML Technologies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjtfu4tmobxg4) for more information.
- _XSLT_. NSXML lets you apply XSLT (Extensible StyleSheet Language Transformations) to an XML document object (NSXMLDocument). XSLT transforms one XML document into another XML document or a document in another format, such as XHTML, HTML, RTF, or plain text. It does this by applying a set of patterns and template rules. [XQuery and Other XML Technologies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjtfu4tmobxg4) discusses XSLT in greater detail.
- _XInclude_. NSXML supports XInclude, allowing you to merge XML from other sources into the current document.
- _Bindings_. The classes of NSXML conform to the key-value coding protocol and respond to observers conforming to the key-value observing protocol. Consequently you can bind the attributes of NSXML objects to properties of user-interface objects via the Cocoa controller classes.

The public interface of NSXML consists of the five Foundation classes listed in Table 1. NSXML fully supports the XML standard and can efficiently process the largest of XML documents. It relies on existing Foundation classes to avoid redundancy in its programmatic interface.

__Table 1__  NSXML Classes

| NSXMLNode |
| NSXMLDocument |
| NSXMLElement |
| NSXMLDTD |
| NSXMLDTDNode |

The first three of these classes in Table 1 are for processing XML. As defined by the data model of XQuery (described in [The Data Model of NSXML](The%20Data%20Model%20of%20NSXML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjufvbuuqsjivdumri)) instances of these classes either represent the various kinds of nodes of an XML tree or, in the case of the document node, the entire tree itself. NSXML node object represent documents, elements, attributes, namespaces, comments, processing instructions, and text nodes.

The last two classes in Table 1 are for creating and modifying Document Type Definitions. For a discussion of the DTD-related nodes, see [DTD and Other Schemas](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjtfu4tmojug4).

An obvious advantage of an object-oriented framework is that you can extend and specialize behavior through subclassing. This advantage applies to NSXML. For example, if processing instructions play a particularly important role in your application, you could create a subclass of NSXMLNode whose instances represent processing-instruction nodes capable of performing the required tasks. NSXML allows you to substitute your subclass for an NSXML class when the tree is built during the parsing phase. For more information on subclassing the NSXML classes, see the reference documentation.

Within the group of classes listed in Table 1, NSXMLNode is the base class—all of the other classes directly inherit from it. NSXMLNode defines an interface and a set of attributes common to NSXML node objects. Among these are the kind of node, the node name, the string or object value of the node, the location of the node relative to its sibling nodes, the level of the node in the tree hierarchy, and references to the node’s parent and children. Through NSXMLNode, a node can find the nodes adjacent to it in the tree; it can print itself out as XML (or DTD) markup text; and it can be the context object for XQuery and XPath queries.

NSXML includes support for XQuery 1.0, a query language that you can use to retrieve and interpret information from different sources of XML. A functional and strongly typed language, XQuery operates on the abstract, logical structure of an XML document—its tree representation—rather than on its surface syntax. (This logical structure is informed by the data model discussed in [The Data Model of NSXML](The%20Data%20Model%20of%20NSXML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjufvbuuqsjivdumri).) The result of an XQuery query is a sequence of items, each of which is either a node (NSXML object) or an atomic value (string, integer, float, date, and so on).

The basic syntactical unit in XQuery is the expression, which is made up of symbols, keywords, and operands (which are always other expressions). Embedded XPath expressions locate nodes in the XML tree using specific criteria. FLWOR expressions (for the keywords `for`, `let`, `where`, `order`, and `return`) make richer and more precise operations possible, including sorting, joins, and hierarchy inversions. XQuery also enables node construction (although you cannot use it to attach or otherwise manipulate such a node within an NSXML tree). You can use a number of built-in XQuery functions, such as `replace`, `distinct-values`, and `avg`, and you can create your own custom functions.

NSXML also supports XPath as a query language. You can use XPath to locate nodes in an XML tree based on position, relative position, node name, node kind, and several other criteria. Because XQuery 1.0 includes XPath 2.0, a syntactically valid path expression returns the same result in both languages.

NSXML exposes access to XQuery and XPath through two methods of the NSXMLNode class: 

```objc
- (NSArray *)nodesForXPath:(NSString *)xpath error:(NSError **)error;
- (NSArray *)objectsForXQuery:(NSString *)xquery constants:(NSDictionary *)constants error:(NSError **)error;
```

The node object receiving these messages is the context node for the query. Note that the sequence (NSArray object) that an XPath query returns always contains nodes, never atomic values.

NSXML also gives your code access to the Extensible Stylesheet Language Transformation (XSLT) technology. With XSLT, you can create a stylesheet that specifies the patterns and template rules for changing XML in an input tree to differently structured XML in an output tree, or to HTML, XHTML, plain text, or other forms of output. Then an XSLT processor carries out the transformation. A major use for XSLT is transforming an XML document into an XHTML or HTML document. NSXML gives you access to XSLT through the following NSXMLDocument methods: 

```objc
- (id)objectByApplyingXSLT:(NSString *)xslt error:(NSError **)error;
- (id)objectByApplyingXSLTAtURL:(NSURL *)xsltURL arguments:(NSDictionary *)argument error:(NSError **)error;
```


NSXML provides some support for XML validation and for creating and modifying Document Type Definitions (DTDs).

Two NSXML classes, NSXMLDTD and NSXMLDTDNode, allow you create and modify DTDs as a shallow (two-level) tree structure. An instance of the NSXMLDTD class is analogous to an NSXMLDocument in that it represents the entire DTD. It functions as a root node to which instances of the NSXMLDTDNode class are added to as children (along with any comment nodes or processing-instruction nodes). NSXMLDTDNode objects represent element, attribute-list, and entity declarations of various kinds. When you read an XML document with an internal DTD, NSXML processes that DTD, creating a tree representation from it that is composed of NSXMLDTD and NSXMLDTDNode objects (as well as any comment nodes or processing-instruction nodes). Any tree you modify or create you can write out as a DTD document.

NSXML can validate documents when it initially processes them and later upon request. When you read and process an existing XML document and it has an associated schema (XML Schema or internal or external DTD), you can specify an initialization option requesting validation. If the document is successfully parsed and validated, the initialization method returns an NSXMLDocument object. If validation doesn’t succeed, the method reports this as an error and does not create the document object. You can also validate a document as you modify it; if a change is invalid, NSXML reports the reasons for invalidity.

[Next](The%20Data%20Model%20of%20NSXML.md)[Previous](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)

