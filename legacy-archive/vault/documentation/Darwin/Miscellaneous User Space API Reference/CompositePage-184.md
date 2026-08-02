---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xpath/CompositePage.html
archived_at: '2026-07-15T07:23:29.343079Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xpath.h | xpath.h | xpath.h | xpath.h | xpath.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/xmlerror.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlerror/index.html#//apple_ref/doc/header/xmlerror.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  [<libxml/hash.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/hash/index.html#//apple_ref/doc/header/hash.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathAxisFunc | xmlXPathAxisFunc | xmlXPathAxisFunc | xmlXPathAxisFunc | xmlXPathAxisFunc |

---

```
typedef xmlXPathObjectPtr (*xmlXPathAxisFunc) (
    xmlXPathParserContextPtr ctxt,
    xmlXPathObjectPtr cur);
```

##### Discussion

xmlXPathAxisFunc:
@ctxt: the XPath interpreter context
@cur: the previous node being explored on that axis

An axis traversal function. To traverse an axis, the engine calls
the first time with cur == NULL and repeat until the function returns
NULL indicating the end of the axis traversal.

Returns the next node in that axis or NULL if at the end of the axis.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathConvertFunc | xmlXPathConvertFunc | xmlXPathConvertFunc | xmlXPathConvertFunc | xmlXPathConvertFunc |

---

```
typedef int (*xmlXPathConvertFunc) (
    xmlXPathObjectPtr obj,
    int type);
```

##### Discussion

xmlXPathConvertFunc:
@obj: an XPath object
@type: the number of the target type

A conversion function is associated to a type and used to cast
the new type to primitive values.

Returns -1 in case of error, 0 otherwise

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathError | xmlXPathError | xmlXPathError | xmlXPathError | xmlXPathError |

---

```
typedef enum {
    XPATH_EXPRESSION_OK = 0,
    XPATH_NUMBER_ERROR,
    XPATH_UNFINISHED_LITERAL_ERROR,
    XPATH_START_LITERAL_ERROR,
    XPATH_VARIABLE_REF_ERROR,
    XPATH_UNDEF_VARIABLE_ERROR,
    XPATH_INVALID_PREDICATE_ERROR,
    XPATH_EXPR_ERROR,
    XPATH_UNCLOSED_ERROR,
    XPATH_UNKNOWN_FUNC_ERROR,
    XPATH_INVALID_OPERAND,
    XPATH_INVALID_TYPE,
    XPATH_INVALID_ARITY,
    XPATH_INVALID_CTXT_SIZE,
    XPATH_INVALID_CTXT_POSITION,
    XPATH_MEMORY_ERROR,
    XPTR_SYNTAX_ERROR,
    XPTR_RESOURCE_ERROR,
    XPTR_SUB_RESOURCE_ERROR,
    XPATH_UNDEF_PREFIX_ERROR,
    XPATH_ENCODING_ERROR,
    XPATH_INVALID_CHAR_ERROR,
    XPATH_INVALID_CTXT
} xmlXPathError;
```

##### Discussion

The set of XPath error codes.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathEvalFunc | xmlXPathEvalFunc | xmlXPathEvalFunc | xmlXPathEvalFunc | xmlXPathEvalFunc |

---

```
typedef void (*xmlXPathEvalFunc)(
    xmlXPathParserContextPtr ctxt,
    int nargs);
```

##### Discussion

xmlXPathEvalFunc:
@ctxt: an XPath parser context
@nargs: the number of arguments passed to the function

An XPath evaluation function, the parameters are on the XPath context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathFuncLookupFunc | xmlXPathFuncLookupFunc | xmlXPathFuncLookupFunc | xmlXPathFuncLookupFunc | xmlXPathFuncLookupFunc |

---

```
typedef xmlXPathFunction (*xmlXPathFuncLookupFunc) (
    void *ctxt,
    const xmlChar *name,
    const xmlChar *ns_uri);
```

##### Discussion

xmlXPathFuncLookupFunc:
@ctxt: an XPath context
@name: name of the function
@ns_uri: the namespace name hosting this function

Prototype for callbacks used to plug function lookup in the XPath
engine.

Returns the XPath function or NULL if not found.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathFunction | xmlXPathFunction | xmlXPathFunction | xmlXPathFunction | xmlXPathFunction |

---

```
typedef void (*xmlXPathFunction) (
    xmlXPathParserContextPtr ctxt,
    int nargs);
```

##### Discussion

xmlXPathFunction:
@ctxt: the XPath interprestation context
@nargs: the number of arguments

An XPath function.
The arguments (if any) are popped out from the context stack
and the result is pushed on the stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathVariableLookupFunc | xmlXPathVariableLookupFunc | xmlXPathVariableLookupFunc | xmlXPathVariableLookupFunc | xmlXPathVariableLookupFunc |

---

```
typedef xmlXPathObjectPtr (*xmlXPathVariableLookupFunc) (
    void *ctxt,
    const xmlChar *name,
    const xmlChar *ns_uri);
```

##### Discussion

xmlXPathVariableLookupFunc:
@ctxt: an XPath context
@name: name of the variable
@ns_uri: the namespace name hosting this variable

Prototype for callbacks used to plug variable lookup in the XPath
engine.

Returns the XPath object value or NULL if not found.

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xmlXPathContext | _xmlXPathContext | _xmlXPathContext | _xmlXPathContext | _xmlXPathContext |

---

```
struct _xmlXPathContext {
    xmlDocPtr doc; /* The current document */
    xmlNodePtr node; /* The current node */
    int nb_variables_unused; /* unused (hash table) */
    int max_variables_unused; /* unused (hash table) */
    xmlHashTablePtr varHash; /* Hash table of defined variables */
    int nb_types; /* number of defined types */
    int max_types; /* max number of types */
    xmlXPathTypePtr types; /* Array of defined types */
    int nb_funcs_unused; /* unused (hash table) */
    int max_funcs_unused; /* unused (hash table) */
    xmlHashTablePtr funcHash; /* Hash table of defined funcs */
    int nb_axis; /* number of defined axis */
    int max_axis; /* max number of axis */
    xmlXPathAxisPtr axis; /* Array of defined axis */
    /* the namespace nodes of the context node */
    xmlNsPtr *namespaces; /* Array of namespaces */
    int nsNr; /* number of namespace in scope */
    void *user; /* function to free */
    /* extra variables */
    int contextSize; /* the context size */
    int proximityPosition; /* the proximity position */
    /* extra stuff for XPointer */
    int xptr; /* it this an XPointer context */
    xmlNodePtr here; /* for here() */
    xmlNodePtr origin; /* for origin() */
    /* the set of namespace declarations in scope for the expression */
    xmlHashTablePtr nsHash; /* The namespaces hash table */
    xmlXPathVariableLookupFunc varLookupFunc;/* variable lookup func */
    void *varLookupData; /* variable lookup data */
    /* Possibility to link in an extra item */
    void *extra; /* needed for XSLT */
    /* The function name and URI when calling a function */
    const xmlChar *function;
    const xmlChar *functionURI;
    /* function lookup function and data */
    xmlXPathFuncLookupFunc funcLookupFunc;/* function lookup func */
    void *funcLookupData; /* function lookup data */
    /* temporary namespace lists kept for walking the namespace axis */
    xmlNsPtr *tmpNsList; /* Array of namespaces */
    int tmpNsNr; /* number of namespace in scope */
    /* error reporting mechanism */
    void *userData; /* user specific data block */
    xmlStructuredErrorFunc error; /* the callback in case of errors */
    xmlError lastError; /* the last error */
    xmlNodePtr debugNode; /* the source node XSLT */
    /* dictionnary */
    xmlDictPtr dict; /* dictionnary if any */
};
```

##### Discussion

xmlXPathContext:

Expression evaluation occurs with respect to a context.
he context consists of:
- a node (the context node)
- a node list (the context node list)
- a set of variable bindings
- a function library
- the set of namespace declarations in scope for the expression
Following the switch to hash tables, this need to be trimmed up at
the next binary incompatible release.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xmlXPathParserContext | _xmlXPathParserContext | _xmlXPathParserContext | _xmlXPathParserContext | _xmlXPathParserContext |

---

```
struct _xmlXPathParserContext {
    const xmlChar *cur; /* the current char being parsed */
    const xmlChar *base; /* the full expression */
    int error; /* error code */
    xmlXPathContextPtr context; /* the evaluation context */
    xmlXPathObjectPtr value; /* the current value */
    int valueNr; /* number of values stacked */
    int valueMax; /* max number of values stacked */
    xmlXPathObjectPtr *valueTab; /* stack of values */
    xmlXPathCompExprPtr comp; /* the precompiled expression */
    int xptr; /* it this an XPointer expression */
    xmlNodePtr ancestor; /* used for walking preceding axis */
};
```

##### Discussion

xmlXPathParserContext:

An XPath parser context. It contains pure parsing informations,
an xmlXPathContext, and the stack of objects.

## Globals

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Conversion functions to basic types.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Context handling.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Evaluation functions.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Separate compilation/evaluation entry points.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathNAN | xmlXPathNAN | xmlXPathNAN | xmlXPathNAN | xmlXPathNAN |

---

```
extern  double xmlXPathNAN;
```

##### Discussion

Objects and Nodesets handling

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathNodeSetGetLength | xmlXPathNodeSetGetLength | xmlXPathNodeSetGetLength | xmlXPathNodeSetGetLength | xmlXPathNodeSetGetLength |

---

```
#define xmlXPathNodeSetGetLength(
    ns)
```

##### Discussion

xmlXPathNodeSetGetLength:
@ns: a node-set

Implement a functionality similar to the DOM NodeList.length.

Returns the number of nodes in the node-set.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathNodeSetIsEmpty | xmlXPathNodeSetIsEmpty | xmlXPathNodeSetIsEmpty | xmlXPathNodeSetIsEmpty | xmlXPathNodeSetIsEmpty |

---

```swift
#define xmlXPathNodeSetIsEmpty(
    ns) \ (((
    ns) == NULL) || ((
    ns)->nodeNr == 0) || ((
    ns)->nodeTab == NULL))
```

##### Discussion

xmlXPathNodeSetIsEmpty:
@ns: a node-set

Checks whether @ns is empty or not.

Returns %TRUE if @ns is an empty node-set.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathNodeSetItem | xmlXPathNodeSetItem | xmlXPathNodeSetItem | xmlXPathNodeSetItem | xmlXPathNodeSetItem |

---

```swift
#define xmlXPathNodeSetItem(
    ns, index) \ ((((
    ns) != NULL) && \ ((
    index) >= 0) && ((
    index) < (
    ns)->nodeNr)) ? \ (
    ns)->nodeTab[(
    index)] \ : NULL)
```

##### Discussion

xmlXPathNodeSetItem:
@ns: a node-set
@index: index of a node in the set

Implements a functionality similar to the DOM NodeList.item().

Returns the xmlNodePtr at the given @index in @ns or NULL if
@index is out of range (0 to length-1)

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
