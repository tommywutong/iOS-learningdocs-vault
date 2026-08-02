---
title: XML Programming Topics for Core Foundation
apple_id: 10000138i
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/Concepts/CFXMLParser.html
archived_at: '2026-07-15T07:23:00.491002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [XML Programming Topics for Core Foundation](Introduction%20to%20XML%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Parsing%20XML%20Documents.md)[Previous](About%20XML.md)

# Core Foundation XML Parser

Core Foundation provides a parser that your applications can use to read data in XML format. Core Foundation’s XML parser has two programming interfaces, one tree-based and the other event-driven. The tree-based interface parses an XML document and returns the data to you in the form of a [CFXMLTreeRef](https://developer.apple.com/documentation/corefoundation/cfxmltreeref) object. There is also a configurable, callback-based API that allows event-driven parsing of an XML document. Event-driven parsing allows you to customize the parser’s behavior so your application can respond only to the specific XML constructs that interest you. Event-driven parsing is also useful for large documents because the parser doesn’t have to build the entire tree in memory. However, tree-based parsing allows you to add or modify nodes in the tree structure, and thus modify the original XML document.

Both of the XML parser interfaces rely on a single data structure to return XML data to your application: the [CFXMLNodeRef](https://developer.apple.com/documentation/corefoundation/cfxmlnode) opaque object. This Core Foundation type describes an individual XML construct, such as a element, a comment, an attribute, or a string of character data.

Each `CFXMLNode` object contains three main pieces of information—the node’s type, the data string, and a pointer to a data structure with additional information. You extract this data using simple accessor functions. The node’s type is encoded as an enumeration constant describing the type of XML structure. The data string is always a `CFString` object; the meaning of the string depends on the node's type ID. The format of the additional data also depends on the node’s type; there is a specific structure for each type that requires additional data.

As it processes an XML document, the parser converts each XML construct it encounters into a `CFXMLNode` object that represents that construct. For example, when parsing the document shown in [Listing 1](About%20XML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgizdqlktk4yq), the parser would respond to the tag `<birthday>` by creating a new `CFXMLNode` whose node type would be set to the identifier `kCFXMLNodeTypeElement`. The `CFXMLNode` data string would contain the `CFString` object “birthday”, and the additional data pointer would point to a `CFXMLElementInfo` structure containing information about the element’s attributes.

In order to handle some of the more complex XML entities, Core Foundation defines several additional data structures. The structures that contain additional information are described briefly in Table 1.

__Table 1__  XML parser additional information structures

| Structure | Content Description |
| `CFXMLElementInfo` | A list of element attributes. |
| `CFXMLProcessingInstructionInfo` | The processing instruction. |
| `CFXMLDocumentInfo` | The source URL for the document along with character encoding information. |
| `CFXMLDocumentTypeInfo` | The system and public IDs for the DTD. |
| `CFXMLNotationInfo` | The system and public IDs for the notation. |
| `CFXMLElementTypeDeclarationInfo` | The string that describes the element’s permissible content. |
| `CFXMLAttributeDeclarationInfo` | The name of the attribute being declared, the string describing the attribute’s type, and the attribute’s default value. |
| `CFXMLAttributeListDeclarationInfo` | A list of `CFXMLAttributeDeclarationInfo` structures. |
| `CFXMLEntityInfo` | The type of the entity, the text to be substituted for the entity when referenced, the location of the entity (for external entities), and the name of the entity’s notation if the entity is not parsed. |
| `CFXMLEntityReferenceInfo` | The type of the entity reference. |

To briefly illustrate how these structures are used by the parser, consider once again the XML document shown in [Listing 1](About%20XML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgizdqlktk4yq). The fourth line of the document contains the tag `<address region="USA">`. The string `region="USA"` defines an _element attribute_ called `region` whose string value is `USA`. Element attributes are a way to associate additional data with a given element.

The XML parser returns a tag’s attributes to your application as a `CFXMLElementInfo` structure. This structure is shown in Listing 1.

__Listing 1__  The CFXMLElementInfo structure

```
typedef struct {
    CFDictionaryRef attributes;
    CFArrayRef attributeOrder;
    Boolean isEmpty;
} CFXMLElementInfo;
```

When parsing this tag, the parser creates a `CFXMLNode` object whose type code is `kCFXMLNodeTypeElement`, and whose data string is `“address”`. The additional information pointer is set to point to a `CFXMLElementInfo` structure describing the element and its attributes. The `attributes` field contains a `CFDictionary` object holding the attribute data in the key/value format. The `attributeOrder` field contains a `CFArray` object holding the `attributes` dictionary keys in the order they were encountered. The Boolean value of the `isEmpty` field indicates whether the element is empty. See _[Collections Programming Topics for Core Foundation](../Collections%20Programming%20Topics%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdi2i)_ for more information about `CFDictionary` and `CFArray`.

The tree-based parser API provides a very simple method for reading XML data. One call to the function `CFXMLTreeCreateFromData` reads an entire XML document—specified by a pointer to XML data in memory, or by a URL string—and returns the XML data to you in the form of a `CFXMLTree` object. A `CFXMLTree` object is simply a `CFTree` object that contains a pointer to a `CFXMLNode` object in each node’s context. See _[Collections Programming Topics for Core Foundation](../Collections%20Programming%20Topics%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdi2i)_ for more information about [CFTreeRef](https://developer.apple.com/documentation/corefoundation/cftree) and its API.

Once the `CFXMLTree` object has been created, you can use the `CFTree` API to examine the tree and extract information from a given node. Core Foundation also provides convenience functions that make it even easier to access the content of a `CFXMLTree` object. For example, `CFXMLTreeGetNode` takes a reference to one of the tree’s nodes and returns a pointer to that node.

The section [Using the Tree-Based Parser Interface](Parsing%20XML%20Documents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgizteljrgaytanzx) shows you how to parse, examine, and modify an XML document using the tree-based parser API.

The tree-based XML parser API is sufficient for many needs. However, there are some cases where using the event-driven interface of `CFXML` is appropriate:

- You want fine-tuned control of the parsing process.
- You need access to data within a very large XML document and converting the entire document into a `CFXMLTree` object requires too much memory.
- A `CFXMLTree` object is inappropriate for your application’s needs, and you want to build a custom data structure from the contents of an XML document.
- You wish to provide additional error checking as parsing progresses.
- You wish to control when and how external entities are loaded.

For these and other situations you can use the callback-based event-driven API. This API is somewhat more complex to use, but provides much more flexibility than the tree-based API.

Conceptually, the event-driven API is simple. You first define a set of callback functions that are invoked as the parsing process proceeds. As the parser encounters each XML structure, your functions are called, giving you an opportunity to handle the data however you wish.

In order to use the event-driven parser, you must implement three of the five callbacks described in this section—`CFXMLParserCreateXMLStructureCallBack`, `CFXMLParserAddChildCallBack`, and `CFXMLParserEndXMLStructureCallBack`. The other callbacks are optional.

The `CFXMLParserCreateXMLStructureCallBack` function is called when the parser encounters a new XML structure. It passes a pointer to a CFXMLNode. If the function returns `NULL`, the parser skips the structure.

The `CFXMLParserAddChildCallBack` function is called when the parser encounters a child structure. It notifies you of the parent–child relationship and passes the data you returned from `CFXMLParserCreateXMLStructureCallBack` for both the parent and child.

The `CFXMLParserEndXMLStructureCallBack` function is called when the parser exits an XML structure reported by `CFXMLParserCreateXMLStructureCallBack`. It passes the data you returned from `CFXMLParserCreateXMLStructureCallBack`.

The `CFXMLParserResolveExternalEntityCallBack` function is called when the parser encounters an XML external entity reference. It passes the `publicID` and `systemID` data for the entity. It is up to you to load the data if you wish and return it as a CFData. Not currently supported.

The `CFXMLParserHandleErrorCallBack` is called when the parser encounters an error condition. It passes an error code indicating the nature of the error. From within your error handler, you can use the function `CFXMLParserCopyErrorDescription` to get a CFString describing the error condition. You can also use the functions `CFXMLParserGetLineNumber` and `CFXMLParserGetLocation` to learn the exact location of the error within the XML document.

At any point during the parsing you can use the function `CFXMLParserGetStatusCode` to find out what the parser is doing. You can also call `CFXMLParserAbort` to signal an error.

There are various options you can use to configure the parser’s behavior. An option flag of `0`, or `kCFXMLParserNoOptions`, leaves the XML as “intact” as possible. In other words, this option causes the parser to report all structures and performs no entity replacements. To make the parser do the most work, returning only the pure element tree, set the option flag to `kCFXMLParserAllOptions`.

__Table 2__  Parser option Flags

| Flag | Description | Status |
| `kCFXMLParserValidateDocument` | Validate the document against its DTD schema, reporting any errors. | Not supported |
| `kCFXMLParserSkipMetaData` | Silently skip over metadata constructs (the DTD and comments). | Supported |
| `kCFXMLParserReplacePhysicalEntities` | Replace declared entities like `<`. | Not supported |
| `kCFXMLParserSkipWhitespace` | Skip over all whitespace that does not abut non-whitespace character data. For example, given `<foo> <bar> blah </bar></foo>`, the whitespace between foo’s open tag and bar’s open tag would be suppressed, but the whitespace around blah would be preserved. | Supported |
| `kCFXMLParserAddImpliedAttributes` | Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. | Not Supported |
| `kCFXMLParserAllOptions` | All of the supported options. | Supported |
| `kCFXMLParserNoOptions` | No options. | Supported |

The section [Using the Event-Driven Parser Interface](Parsing%20XML%20Documents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgizteljrgaytgmrt) shows you how to parse an XML document using the event-driven parser API.

[Next](Parsing%20XML%20Documents.md)[Previous](About%20XML.md)

