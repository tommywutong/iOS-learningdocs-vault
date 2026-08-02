---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/parser/CompositePage.html
archived_at: '2026-07-15T07:23:27.507826Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| parser.h | parser.h | parser.h | parser.h | parser.h |

|  |  |
| --- | --- |
| __Includes:__ | <stdarg.h>  [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  <libxml/dict.h>  [<libxml/hash.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/hash/index.html#//apple_ref/doc/header/hash.h)  [<libxml/valid.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/valid/index.html#//apple_ref/doc/header/valid.h)  <libxml/entities.h>  [<libxml/xmlerror.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlerror/index.html#//apple_ref/doc/header/xmlerror.h)  [<libxml/xmlstring.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlstring/index.html#//apple_ref/doc/header/xmlstring.h)  [<libxml/encoding.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/encoding/index.html#//apple_ref/doc/header/encoding.h)  [<libxml/xmlIO.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlIO/index.html#//apple_ref/doc/header/xmlIO.h)  [<libxml/globals.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/globals/index.html#//apple_ref/doc/header/globals.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| attributeDeclSAXFunc | attributeDeclSAXFunc | attributeDeclSAXFunc | attributeDeclSAXFunc | attributeDeclSAXFunc |

---

```
typedef void (*attributeDeclSAXFunc)(
    void *ctx,
    const xmlChar *elem,
    const xmlChar *fullname,
    int type,
    int def,
    const xmlChar *defaultValue,
    xmlEnumerationPtr tree);
```

##### Discussion

attributeDeclSAXFunc:
@ctx: the user data (XML parser context)
@elem: the name of the element
@fullname: the attribute name
@type: the attribute type
@def: the type of default value
@defaultValue: the attribute default value
@tree: the tree of enumerated value set

An attribute definition has been parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| attributeSAXFunc | attributeSAXFunc | attributeSAXFunc | attributeSAXFunc | attributeSAXFunc |

---

```
typedef void (*attributeSAXFunc) (
    void *ctx,
    const xmlChar *name,
    const xmlChar *value);
```

##### Discussion

attributeSAXFunc:
@ctx: the user data (XML parser context)
@name: The attribute name, including namespace prefix
@UNKNOWN: The attribute value

Handle an attribute that has been read by the parser.
The default handling is to convert the attribute into an
DOM subtree and past it in a new xmlAttr element added to
the element.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| cdataBlockSAXFunc | cdataBlockSAXFunc | cdataBlockSAXFunc | cdataBlockSAXFunc | cdataBlockSAXFunc |

---

```
typedef void (*cdataBlockSAXFunc) (
    void *ctx,
    const xmlChar *value,
    int len);
```

##### Discussion

cdataBlockSAXFunc:
@ctx: the user data (XML parser context)
@UNKNOWN: The pcdata content
@len: the block length

Called when a pcdata block has been parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| charactersSAXFunc | charactersSAXFunc | charactersSAXFunc | charactersSAXFunc | charactersSAXFunc |

---

```
typedef void (*charactersSAXFunc) (
    void *ctx,
    const xmlChar *ch,
    int len);
```

##### Discussion

charactersSAXFunc:
@ctx: the user data (XML parser context)
@ch: a xmlChar string
@len: the number of xmlChar

Receiving some chars from the parser.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| commentSAXFunc | commentSAXFunc | commentSAXFunc | commentSAXFunc | commentSAXFunc |

---

```
typedef void (*commentSAXFunc) (
    void *ctx,
    const xmlChar *value);
```

##### Discussion

commentSAXFunc:
@ctx: the user data (XML parser context)
@UNKNOWN: the comment content

A comment has been parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| elementDeclSAXFunc | elementDeclSAXFunc | elementDeclSAXFunc | elementDeclSAXFunc | elementDeclSAXFunc |

---

```
typedef void (*elementDeclSAXFunc)(
    void *ctx,
    const xmlChar *name,
    int type,
    xmlElementContentPtr content);
```

##### Discussion

elementDeclSAXFunc:
@ctx: the user data (XML parser context)
@name: the element name
@type: the element type
@content: the element value tree

An element definition has been parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| endDocumentSAXFunc | endDocumentSAXFunc | endDocumentSAXFunc | endDocumentSAXFunc | endDocumentSAXFunc |

---

```
typedef void (*endDocumentSAXFunc) (
    void *ctx);
```

##### Discussion

endDocumentSAXFunc:
@ctx: the user data (XML parser context)

Called when the document end has been detected.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| endElementNsSAX2Func | endElementNsSAX2Func | endElementNsSAX2Func | endElementNsSAX2Func | endElementNsSAX2Func |

---

```
typedef void (*endElementNsSAX2Func) (
    void *ctx,
    const xmlChar *localname,
    const xmlChar *prefix,
    const xmlChar *URI);
```

##### Discussion

endElementNsSAX2Func:
@ctx: the user data (XML parser context)
@localname: the local name of the element
@prefix: the element namespace prefix if available
@URI: the element namespace name if available

SAX2 callback when an element end has been detected by the parser.
It provides the namespace informations for the element.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| endElementSAXFunc | endElementSAXFunc | endElementSAXFunc | endElementSAXFunc | endElementSAXFunc |

---

```
typedef void (*endElementSAXFunc) (
    void *ctx,
    const xmlChar *name);
```

##### Discussion

endElementSAXFunc:
@ctx: the user data (XML parser context)
@name: The element name

Called when the end of an element has been detected.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| entityDeclSAXFunc | entityDeclSAXFunc | entityDeclSAXFunc | entityDeclSAXFunc | entityDeclSAXFunc |

---

```
typedef void (*entityDeclSAXFunc) (
    void *ctx,
    const xmlChar *name,
    int type,
    const xmlChar *publicId,
    const xmlChar *systemId,
    xmlChar *content);
```

##### Discussion

entityDeclSAXFunc:
@ctx: the user data (XML parser context)
@name: the entity name
@type: the entity type
@publicId: The public ID of the entity
@systemId: The system ID of the entity
@content: the entity value (without processing).

An entity definition has been parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| errorSAXFunc | errorSAXFunc | errorSAXFunc | errorSAXFunc | errorSAXFunc |

---

```
typedef void (*errorSAXFunc) (
    void *ctx,
    const char *msg,
    ...);
```

##### Discussion

errorSAXFunc:
@ctx: an XML parser context
@msg: the message to display/transmit
@...: extra parameters for the message display

Display and format an error messages, callback.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| externalSubsetSAXFunc | externalSubsetSAXFunc | externalSubsetSAXFunc | externalSubsetSAXFunc | externalSubsetSAXFunc |

---

```
typedef void (*externalSubsetSAXFunc) (
    void *ctx,
    const xmlChar *name,
    const xmlChar *ExternalID,
    const xmlChar *SystemID);
```

##### Discussion

externalSubsetSAXFunc:
@ctx: the user data (XML parser context)
@name: the root element name
@ExternalID: the external ID
@SystemID: the SYSTEM ID (e.g. filename or URL)

Callback on external subset declaration.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| fatalErrorSAXFunc | fatalErrorSAXFunc | fatalErrorSAXFunc | fatalErrorSAXFunc | fatalErrorSAXFunc |

---

```
typedef void (*fatalErrorSAXFunc) (
    void *ctx,
    const char *msg,
    ...);
```

##### Discussion

fatalErrorSAXFunc:
@ctx: an XML parser context
@msg: the message to display/transmit
@...: extra parameters for the message display

Display and format fatal error messages, callback.
Note: so far fatalError() SAX callbacks are not used, error()
get all the callbacks for errors.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| getEntitySAXFunc | getEntitySAXFunc | getEntitySAXFunc | getEntitySAXFunc | getEntitySAXFunc |

---

```
typedef xmlEntityPtr (*getEntitySAXFunc) (
    void *ctx,
    const xmlChar *name);
```

##### Discussion

getEntitySAXFunc:
@ctx: the user data (XML parser context)
@name: The entity name

Get an entity by name.

Returns the xmlEntityPtr if found.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| getParameterEntitySAXFunc | getParameterEntitySAXFunc | getParameterEntitySAXFunc | getParameterEntitySAXFunc | getParameterEntitySAXFunc |

---

```
typedef xmlEntityPtr (*getParameterEntitySAXFunc) (
    void *ctx,
    const xmlChar *name);
```

##### Discussion

getParameterEntitySAXFunc:
@ctx: the user data (XML parser context)
@name: The entity name

Get a parameter entity by name.

Returns the xmlEntityPtr if found.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| hasExternalSubsetSAXFunc | hasExternalSubsetSAXFunc | hasExternalSubsetSAXFunc | hasExternalSubsetSAXFunc | hasExternalSubsetSAXFunc |

---

```
typedef int (*hasExternalSubsetSAXFunc) (
    void *ctx);
```

##### Discussion

hasExternalSubsetSAXFunc:
@ctx: the user data (XML parser context)

Does this document has an external subset?

Returns 1 if true

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| hasInternalSubsetSAXFunc | hasInternalSubsetSAXFunc | hasInternalSubsetSAXFunc | hasInternalSubsetSAXFunc | hasInternalSubsetSAXFunc |

---

```
typedef int (*hasInternalSubsetSAXFunc) (
    void *ctx);
```

##### Discussion

hasInternalSubsetSAXFunc:
@ctx: the user data (XML parser context)

Does this document has an internal subset.

Returns 1 if true

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ignorableWhitespaceSAXFunc | ignorableWhitespaceSAXFunc | ignorableWhitespaceSAXFunc | ignorableWhitespaceSAXFunc | ignorableWhitespaceSAXFunc |

---

```
typedef void (*ignorableWhitespaceSAXFunc) (
    void *ctx,
    const xmlChar *ch,
    int len);
```

##### Discussion

ignorableWhitespaceSAXFunc:
@ctx: the user data (XML parser context)
@ch: a xmlChar string
@len: the number of xmlChar

Receiving some ignorable whitespaces from the parser.
UNUSED: by default the DOM building will use characters.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| internalSubsetSAXFunc | internalSubsetSAXFunc | internalSubsetSAXFunc | internalSubsetSAXFunc | internalSubsetSAXFunc |

---

```
typedef void (*internalSubsetSAXFunc) (
    void *ctx,
    const xmlChar *name,
    const xmlChar *ExternalID,
    const xmlChar *SystemID);
```

##### Discussion

internalSubsetSAXFunc:
@ctx: the user data (XML parser context)
@name: the root element name
@ExternalID: the external ID
@SystemID: the SYSTEM ID (e.g. filename or URL)

Callback on internal subset declaration.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| isStandaloneSAXFunc | isStandaloneSAXFunc | isStandaloneSAXFunc | isStandaloneSAXFunc | isStandaloneSAXFunc |

---

```
typedef int (*isStandaloneSAXFunc) (
    void *ctx);
```

##### Discussion

isStandaloneSAXFunc:
@ctx: the user data (XML parser context)

Is this document tagged standalone?

Returns 1 if true

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| notationDeclSAXFunc | notationDeclSAXFunc | notationDeclSAXFunc | notationDeclSAXFunc | notationDeclSAXFunc |

---

```
typedef void (*notationDeclSAXFunc)(
    void *ctx,
    const xmlChar *name,
    const xmlChar *publicId,
    const xmlChar *systemId);
```

##### Discussion

notationDeclSAXFunc:
@ctx: the user data (XML parser context)
@name: The name of the notation
@publicId: The public ID of the entity
@systemId: The system ID of the entity

What to do when a notation declaration has been parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| processingInstructionSAXFunc | processingInstructionSAXFunc | processingInstructionSAXFunc | processingInstructionSAXFunc | processingInstructionSAXFunc |

---

```
typedef void (*processingInstructionSAXFunc) (
    void *ctx,
    const xmlChar *target,
    const xmlChar *data);
```

##### Discussion

processingInstructionSAXFunc:
@ctx: the user data (XML parser context)
@target: the target name
@data: the PI data's

A processing instruction has been parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| referenceSAXFunc | referenceSAXFunc | referenceSAXFunc | referenceSAXFunc | referenceSAXFunc |

---

```
typedef void (*referenceSAXFunc) (
    void *ctx,
    const xmlChar *name);
```

##### Discussion

referenceSAXFunc:
@ctx: the user data (XML parser context)
@name: The entity name

Called when an entity reference is detected.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| resolveEntitySAXFunc | resolveEntitySAXFunc | resolveEntitySAXFunc | resolveEntitySAXFunc | resolveEntitySAXFunc |

---

```
/**
resolveEntitySAXFunc:
@ctx: the user data (XML parser context)
@publicId: The public ID of the entity
@systemId: The system ID of the entity

Callback:
The entity loader, to control the loading of external entities,
the application can either:
- override this resolveEntity() callback in the SAX block
- or better use the xmlSetExternalEntityLoader() function to
set up it's own entity resolution routine

Returns the xmlParserInputPtr if inlined or NULL for DOM behaviour.
    */
typedef xmlParserInputPtr (*resolveEntitySAXFunc) (
    void *ctx,
    const xmlChar *publicId,
    const xmlChar *systemId);
```

##### Discussion

xmlSAXHandler:

A SAX handler is bunch of callbacks called by the parser when processing
of the input generate data or structure informations.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| setDocumentLocatorSAXFunc | setDocumentLocatorSAXFunc | setDocumentLocatorSAXFunc | setDocumentLocatorSAXFunc | setDocumentLocatorSAXFunc |

---

```
typedef void (*setDocumentLocatorSAXFunc) (
    void *ctx,
    xmlSAXLocatorPtr loc);
```

##### Discussion

setDocumentLocatorSAXFunc:
@ctx: the user data (XML parser context)
@loc: A SAX Locator

Receive the document locator at startup, actually xmlDefaultSAXLocator.
Everything is available on the context, so this is useless in our case.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| startDocumentSAXFunc | startDocumentSAXFunc | startDocumentSAXFunc | startDocumentSAXFunc | startDocumentSAXFunc |

---

```
typedef void (*startDocumentSAXFunc) (
    void *ctx);
```

##### Discussion

startDocumentSAXFunc:
@ctx: the user data (XML parser context)

Called when the document start being processed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| startElementNsSAX2Func | startElementNsSAX2Func | startElementNsSAX2Func | startElementNsSAX2Func | startElementNsSAX2Func |

---

```
typedef void (*startElementNsSAX2Func) (
    void *ctx,
    const xmlChar *localname,
    const xmlChar *prefix,
    const xmlChar *URI,
    int nb_namespaces,
    const xmlChar **namespaces,
    int nb_attributes,
    int nb_defaulted,
    const xmlChar **attributes);
```

##### Discussion

startElementNsSAX2Func:
@ctx: the user data (XML parser context)
@localname: the local name of the element
@prefix: the element namespace prefix if available
@URI: the element namespace name if available
@nb_namespaces: number of namespace definitions on that node
@namespaces: pointer to the array of prefix/URI pairs namespace definitions
@nb_attributes: the number of attributes on that node
@nb_defaulted: the number of defaulted attributes. The defaulted
ones are at the end of the array
@attributes: pointer to the array of (localname/prefix/URI/value/end)
attribute values.

SAX2 callback when an element start has been detected by the parser.
It provides the namespace informations for the element, as well as
the new namespace declarations on the element.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| startElementSAXFunc | startElementSAXFunc | startElementSAXFunc | startElementSAXFunc | startElementSAXFunc |

---

```
typedef void (*startElementSAXFunc) (
    void *ctx,
    const xmlChar *name,
    const xmlChar **atts);
```

##### Discussion

startElementSAXFunc:
@ctx: the user data (XML parser context)
@name: The element name, including namespace prefix
@atts: An array of name/value attributes pairs, NULL terminated

Called when an opening tag has been processed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| unparsedEntityDeclSAXFunc | unparsedEntityDeclSAXFunc | unparsedEntityDeclSAXFunc | unparsedEntityDeclSAXFunc | unparsedEntityDeclSAXFunc |

---

```
typedef void (*unparsedEntityDeclSAXFunc)(
    void *ctx,
    const xmlChar *name,
    const xmlChar *publicId,
    const xmlChar *systemId,
    const xmlChar *notationName);
```

##### Discussion

unparsedEntityDeclSAXFunc:
@ctx: the user data (XML parser context)
@name: The name of the entity
@publicId: The public ID of the entity
@systemId: The system ID of the entity
@notationName: the name of the notation

What to do when an unparsed entity declaration is parsed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| warningSAXFunc | warningSAXFunc | warningSAXFunc | warningSAXFunc | warningSAXFunc |

---

```
typedef void (*warningSAXFunc) (
    void *ctx,
    const char *msg,
    ...);
```

##### Discussion

warningSAXFunc:
@ctx: an XML parser context
@msg: the message to display/transmit
@...: extra parameters for the message display

Display and format a warning messages, callback.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlExternalEntityLoader | xmlExternalEntityLoader | xmlExternalEntityLoader | xmlExternalEntityLoader | xmlExternalEntityLoader |

---

```
typedef xmlParserInputPtr (*xmlExternalEntityLoader) (
    const char *URL,
    const char *ID,
    xmlParserCtxtPtr context);
```

##### Discussion

xmlExternalEntityLoader:
@URL: The System ID of the resource requested
@ID: The Public ID of the resource requested
@context: the XML parser context

External entity loaders types.

Returns the entity input parser.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserInputDeallocate | xmlParserInputDeallocate | xmlParserInputDeallocate | xmlParserInputDeallocate | xmlParserInputDeallocate |

---

```
/**
xmlParserInputDeallocate:
@str: the string to deallocate

Callback for freeing some parser input allocations.
    */
typedef void (*xmlParserInputDeallocate)(
    xmlChar *str);
```

##### Discussion

xmlParserInput:

An xmlParserInput is an input flow for the XML processor.
Each entity parsed is associated an xmlParserInput (except the
few predefined ones). This is the case both for internal entities
- in which case the flow is already completely in memory - or
external entities - in which case we use the buf structure for
progressive reading and I18N conversions to the internal UTF-8 format.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserInputState | xmlParserInputState | xmlParserInputState | xmlParserInputState | xmlParserInputState |

---

```
typedef enum {
    XML_PARSER_EOF = -1, /* nothing is to be parsed */
    XML_PARSER_START = 0, /* nothing has been parsed */
    XML_PARSER_MISC, /* Misc* before int subset */
    XML_PARSER_PI, /* Within a processing instruction */
    XML_PARSER_DTD, /* within some DTD content */
    XML_PARSER_PROLOG, /* Misc* after internal subset */
    XML_PARSER_COMMENT, /* within a comment */
    XML_PARSER_START_TAG, /* within a start tag */
    XML_PARSER_CONTENT, /* within the content */
    XML_PARSER_CDATA_SECTION, /* within a CDATA section */
    XML_PARSER_END_TAG, /* within a closing tag */
    XML_PARSER_ENTITY_DECL, /* within an entity declaration */
    XML_PARSER_ENTITY_VALUE, /* within an entity value in a decl */
    XML_PARSER_ATTRIBUTE_VALUE, /* within an attribute value */
    XML_PARSER_SYSTEM_LITERAL, /* within a SYSTEM value */
    XML_PARSER_EPILOG, /* the Misc* after the last end tag */
    XML_PARSER_IGNORE, /* within an IGNORED section */
    XML_PARSER_PUBLIC_LITERAL /* within a PUBLIC value */
} xmlParserInputState;
```

##### Discussion

xmlParserInputState:

The parser is now working also as a state based parser.
The recursive one use the state info for entities processing.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserMode | xmlParserMode | xmlParserMode | xmlParserMode | xmlParserMode |

---

```
typedef enum {
    XML_PARSE_UNKNOWN = 0,
    XML_PARSE_DOM = 1,
    XML_PARSE_SAX = 2,
    XML_PARSE_PUSH_DOM = 3,
    XML_PARSE_PUSH_SAX = 4,
    XML_PARSE_READER = 5
} xmlParserMode;
```

##### Discussion

xmlParserMode:

A parser can operate in various modes

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserNodeInfo | xmlParserNodeInfo | xmlParserNodeInfo | xmlParserNodeInfo | xmlParserNodeInfo |

---

```
typedef struct _xmlParserNodeInfo xmlParserNodeInfo;
```

##### Discussion

xmlParserNodeInfo:

The parser can be asked to collect Node informations, i.e. at what
place in the file they were detected.
NOTE: This is off by default and not very well tested.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserOption | xmlParserOption | xmlParserOption | xmlParserOption | xmlParserOption |

---

```
typedef enum {
    XML_PARSE_RECOVER = 1<<0, /* recover on errors */
    XML_PARSE_NOENT = 1<<1, /* substitute entities */
    XML_PARSE_DTDLOAD = 1<<2, /* load the external subset */
    XML_PARSE_DTDATTR = 1<<3, /* default DTD attributes */
    XML_PARSE_DTDVALID = 1<<4, /* validate with the DTD */
    XML_PARSE_NOERROR = 1<<5, /* suppress error reports */
    XML_PARSE_NOWARNING = 1<<6, /* suppress warning reports */
    XML_PARSE_PEDANTIC = 1<<7, /* pedantic error reporting */
    XML_PARSE_NOBLANKS = 1<<8, /* remove blank nodes */
    XML_PARSE_SAX1 = 1<<9, /* use the SAX1 interface internally */
    XML_PARSE_XINCLUDE = 1<<10,/* Implement XInclude substitition */
    XML_PARSE_NONET = 1<<11,/* Forbid network access */
    XML_PARSE_NODICT = 1<<12,/* Do not reuse the context dictionnary */
    XML_PARSE_NSCLEAN = 1<<13,/* remove redundant namespaces declarations */
    XML_PARSE_NOCDATA = 1<<14,/* merge CDATA as text nodes */
    XML_PARSE_NOXINCNODE= 1<<15 /* do not generate XINCLUDE START/END nodes */
} xmlParserOption;
```

##### Discussion

xmlParserOption:

This is the set of XML parser options that can be passed down
to the xmlReadDoc() and similar calls.

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xmlParserCtxt | _xmlParserCtxt | _xmlParserCtxt | _xmlParserCtxt | _xmlParserCtxt |

---

```
struct _xmlParserCtxt {
    struct _xmlSAXHandler *sax; /* The SAX handler */
    void *userData; /* For SAX interface only, used by DOM build */
    xmlDocPtr myDoc; /* the document being built */
    int wellFormed; /* is the document well formed */
    int replaceEntities; /* shall we replace entities ? */
    const xmlChar *version; /* the XML version string */
    const xmlChar *encoding; /* the declared encoding, if any */
    int standalone; /* standalone document */
    int html; /* an HTML(1)/Docbook(2) document */
    /* Input stream stack */
    xmlParserInputPtr input; /* Current input stream */
    int inputNr; /* Number of current input streams */
    int inputMax; /* Max number of input streams */
    xmlParserInputPtr *inputTab; /* stack of inputs */
    /* Node analysis stack only used for DOM building */
    xmlNodePtr node; /* Current parsed Node */
    int nodeNr; /* Depth of the parsing stack */
    int nodeMax; /* Max depth of the parsing stack */
    xmlNodePtr *nodeTab; /* array of nodes */
    int record_info; /* Whether node info should be kept */
    xmlParserNodeInfoSeq node_seq; /* info about each node parsed */
    int errNo; /* error code */
    int hasExternalSubset; /* reference and external subset */
    int hasPErefs; /* the internal subset has PE refs */
    int external; /* are we parsing an external entity */
    int valid; /* is the document valid */
    int validate; /* shall we try to validate ? */
    xmlValidCtxt vctxt; /* The validity context */
    xmlParserInputState instate; /* current type of input */
    int token; /* next char look-ahead */
    char *directory; /* the data directory */
    /* Node name stack */
    const xmlChar *name; /* Current parsed Node */
    int nameNr; /* Depth of the parsing stack */
    int nameMax; /* Max depth of the parsing stack */
    const xmlChar **nameTab; /* array of nodes */
    long nbChars; /* number of xmlChar processed */
    long checkIndex; /* used by progressive parsing lookup */
    int keepBlanks; /* ugly but ... */
    int disableSAX; /* SAX callbacks are disabled */
    int inSubset; /* Parsing is in int 1/ext 2 subset */
    const xmlChar *intSubName; /* name of subset */
    xmlChar *extSubURI; /* URI of external subset */
    xmlChar *extSubSystem; /* SYSTEM ID of external subset */
    /* xml:space values */
    int *space; /* Should the parser preserve spaces */
    int spaceNr; /* Depth of the parsing stack */
    int spaceMax; /* Max depth of the parsing stack */
    int *spaceTab; /* array of space infos */
    int depth; /* to prevent entity substitution loops */
    xmlParserInputPtr entity; /* used to check entities boundaries */
    int charset; /* encoding of the in-memory content
        */
    int nodelen; /* Those two fields are there to */
    int nodemem; /* Speed up large node parsing */
    int pedantic; /* signal pedantic warnings */
    void *_private; /* For user data, libxml won't touch it */
    int loadsubset; /* should the external subset be loaded */
    int linenumbers; /* set line number in element content */
    void *catalogs; /* document's own catalog */
    int recovery; /* run in recovery mode */
    int progressive; /* is this a progressive parsing */
    xmlDictPtr dict; /* dictionnary for the parser */
    const xmlChar **atts; /* array for the attributes callbacks */
    int maxatts; /* the size of the array */
    int docdict; /* use strings from dict to build tree */
    /*
 * pre-interned strings
        */
    const xmlChar *str_xml;
    const xmlChar *str_xmlns;
    const xmlChar *str_xml_ns;
    /*
 * Everything below is used only by the new SAX mode
        */
    int sax2; /* operating in the new SAX mode */
    int nsNr; /* the number of inherited namespaces */
    int nsMax; /* the size of the arrays */
    const xmlChar **nsTab; /* the array of prefix/namespace name */
    int *attallocs; /* which attribute were allocated */
    void **pushTab; /* array of data for push */
    xmlHashTablePtr attsDefault; /* defaulted attributes if any */
    xmlHashTablePtr attsSpecial; /* non-CDATA attributes if any */
    int nsWellFormed; /* is the document XML Nanespace okay */
    int options; /* Extra options */
    /*
 * Those fields are needed only for treaming parsing so far
        */
    int dictNames; /* Use dictionary names for the tree */
    int freeElemsNr; /* number of freed element nodes */
    xmlNodePtr freeElems; /* List of freed element nodes */
    int freeAttrsNr; /* number of freed attributes nodes */
    xmlAttrPtr freeAttrs; /* List of freed attributes nodes */
    /*
 * the complete error informations for the last error.
        */
    xmlError lastError;
    xmlParserMode parseMode; /* the parser mode */
};
```

##### Discussion

xmlParserCtxt:

The parser context.
NOTE This doesn't completely define the parser state, the (current ?)
design of the parser uses recursive function calls since this allow
and easy mapping from the production rules of the specification
to the actual code. The drawback is that the actual function call
also reflect the parser state. However most of the parsing routines
takes as the only argument the parser context pointer, so migrating
to a state based parser for progressive parsing shouldn't be too hard.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xmlSAXLocator | _xmlSAXLocator | _xmlSAXLocator | _xmlSAXLocator | _xmlSAXLocator |

---

```
struct _xmlSAXLocator {
    const xmlChar *(*getPublicId)(
        void *ctx);
    const xmlChar *(*getSystemId)(
        void *ctx);
    int (*getLineNumber)(
        void *ctx);
    int (*getColumnNumber)(
        void *ctx);
};
```

##### Discussion

xmlSAXLocator:

A SAX Locator.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_COMPLETE_ATTRS | XML_COMPLETE_ATTRS | XML_COMPLETE_ATTRS | XML_COMPLETE_ATTRS | XML_COMPLETE_ATTRS |

---

```
#define XML_COMPLETE_ATTRS 4
```

##### Discussion

XML_COMPLETE_ATTRS:

Bit in the loadsubset context field to tell to do complete the
elements attributes lists with the ones defaulted from the DTDs.
Use it to initialize xmlLoadExtDtdDefaultValue.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_DEFAULT_VERSION | XML_DEFAULT_VERSION | XML_DEFAULT_VERSION | XML_DEFAULT_VERSION | XML_DEFAULT_VERSION |

---

```
#define XML_DEFAULT_VERSION "1.0"
```

##### Discussion

XML_DEFAULT_VERSION:

The default version of XML used: 1.0

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_DETECT_IDS | XML_DETECT_IDS | XML_DETECT_IDS | XML_DETECT_IDS | XML_DETECT_IDS |

---

```
#define XML_DETECT_IDS 2
```

##### Discussion

XML_DETECT_IDS:

Bit in the loadsubset context field to tell to do ID/REFs lookups.
Use it to initialize xmlLoadExtDtdDefaultValue.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SAX2_MAGIC | XML_SAX2_MAGIC | XML_SAX2_MAGIC | XML_SAX2_MAGIC | XML_SAX2_MAGIC |

---

```
#define XML_SAX2_MAGIC 0xDEEDBEAF
```

##### Discussion

XML_SAX2_MAGIC:

Special constant found in SAX2 blocks initialized fields

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SKIP_IDS | XML_SKIP_IDS | XML_SKIP_IDS | XML_SKIP_IDS | XML_SKIP_IDS |

---

```
#define XML_SKIP_IDS 8
```

##### Discussion

XML_SKIP_IDS:

Bit in the loadsubset context field to tell to not do ID/REFs registration.
Used to initialize xmlLoadExtDtdDefaultValue in some special cases.

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Last Updated: 2006-06-20
