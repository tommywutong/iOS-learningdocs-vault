---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xpathInternals/CompositePage.html
archived_at: '2026-07-15T07:23:29.366171Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xpathInternals.h | xpathInternals.h | xpathInternals.h | xpathInternals.h | xpathInternals.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/xpath.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xpath/index.html#//apple_ref/doc/header/xpath.h) |

## Introduction

---

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

NodeSet handling.

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

Extending a context.

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

Utilities to extend XPath.

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

Really internal functions

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CAST_TO_BOOLEAN | CAST_TO_BOOLEAN | CAST_TO_BOOLEAN | CAST_TO_BOOLEAN | CAST_TO_BOOLEAN |

---

```swift
#define CAST_TO_BOOLEAN \ if ((
    ctxt->value != NULL) && (
    ctxt->value->type != XPATH_BOOLEAN)) \ xmlXPathBooleanFunction(
    ctxt, 1);
```

##### Discussion

CAST_TO_BOOLEAN:

Macro to try to cast the value on the top of the XPath stack to a boolean.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CAST_TO_NUMBER | CAST_TO_NUMBER | CAST_TO_NUMBER | CAST_TO_NUMBER | CAST_TO_NUMBER |

---

```swift
#define CAST_TO_NUMBER \ if ((
    ctxt->value != NULL) && (
    ctxt->value->type != XPATH_NUMBER)) \ xmlXPathNumberFunction(
    ctxt, 1);
```

##### Discussion

CAST_TO_NUMBER:

Macro to try to cast the value on the top of the XPath stack to a number.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CAST_TO_STRING | CAST_TO_STRING | CAST_TO_STRING | CAST_TO_STRING | CAST_TO_STRING |

---

```swift
#define CAST_TO_STRING \ if ((
    ctxt->value != NULL) && (
    ctxt->value->type != XPATH_STRING)) \ xmlXPathStringFunction(
    ctxt, 1);
```

##### Discussion

CAST_TO_STRING:

Macro to try to cast the value on the top of the XPath stack to a string.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_ARITY | CHECK_ARITY | CHECK_ARITY | CHECK_ARITY | CHECK_ARITY |

---

```
#define CHECK_ARITY(
    x) \ if (
    ctxt == NULL) return; \ if (
    nargs != (
    x)) \ {
    xmlXPathErr(
    ctxt, XPATH_INVALID_ARITY); return; };
```

##### Discussion

CHECK_ARITY:
@x: the number of expected args

Macro to check that the number of args passed to an XPath function matches.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_ERROR | CHECK_ERROR | CHECK_ERROR | CHECK_ERROR | CHECK_ERROR |

---

```swift
#define CHECK_ERROR \ if (
    ctxt->error != XPATH_EXPRESSION_OK) return
```

##### Discussion

CHECK_ERROR:

Macro to return from the function if an XPath error was detected.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_ERROR0 | CHECK_ERROR0 | CHECK_ERROR0 | CHECK_ERROR0 | CHECK_ERROR0 |

---

```swift
#define CHECK_ERROR0 \ if (
    ctxt->error != XPATH_EXPRESSION_OK) return(
    0)
```

##### Discussion

CHECK_ERROR0:

Macro to return 0 from the function if an XPath error was detected.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_TYPE | CHECK_TYPE | CHECK_TYPE | CHECK_TYPE | CHECK_TYPE |

---

```swift
#define CHECK_TYPE(
    typeval) \ if ((
    ctxt->value == NULL) || (
    ctxt->value->type != typeval)) \ {
    xmlXPathErr(
    ctxt, XPATH_INVALID_TYPE); return;
}
```

##### Discussion

CHECK_TYPE:
@typeval: the XPath type

Macro to check that the value on top of the XPath stack is of a given
type.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_TYPE0 | CHECK_TYPE0 | CHECK_TYPE0 | CHECK_TYPE0 | CHECK_TYPE0 |

---

```swift
#define CHECK_TYPE0(
    typeval) \ if ((
    ctxt->value == NULL) || (
    ctxt->value->type != typeval)) \ {
    xmlXPathErr(
    ctxt, XPATH_INVALID_TYPE); return(
    0);
}
```

##### Discussion

CHECK_TYPE0:
@typeval: the XPath type

Macro to check that the value on top of the XPath stack is of a given
type. Return(0) in case of failure

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathCheckError | xmlXPathCheckError | xmlXPathCheckError | xmlXPathCheckError | xmlXPathCheckError |

---

```
#define xmlXPathCheckError(
    ctxt)
```

##### Discussion

xmlXPathCheckError:
@ctxt: an XPath parser context

Check if an XPath error was raised.

Returns true if an error has been raised, false otherwise.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathEmptyNodeSet | xmlXPathEmptyNodeSet | xmlXPathEmptyNodeSet | xmlXPathEmptyNodeSet | xmlXPathEmptyNodeSet |

---

```swift
#define xmlXPathEmptyNodeSet(
    ns) \ {
    while ((
    ns)->nodeNr > 0) (
    ns)->nodeTab[(
    ns)->nodeNr--] = NULL;
}
```

##### Discussion

xmlXPathEmptyNodeSet:
@ns: a node-set

Empties a node-set.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathGetContextNode | xmlXPathGetContextNode | xmlXPathGetContextNode | xmlXPathGetContextNode | xmlXPathGetContextNode |

---

```
#define xmlXPathGetContextNode(
    ctxt)
```

##### Discussion

xmlXPathGetContextNode:
@ctxt: an XPath parser context

Get the context node of an XPath context.

Returns the context node.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathGetDocument | xmlXPathGetDocument | xmlXPathGetDocument | xmlXPathGetDocument | xmlXPathGetDocument |

---

```
#define xmlXPathGetDocument(
    ctxt)
```

##### Discussion

xmlXPathGetDocument:
@ctxt: an XPath parser context

Get the document of an XPath context.

Returns the context document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathGetError | xmlXPathGetError | xmlXPathGetError | xmlXPathGetError | xmlXPathGetError |

---

```
#define xmlXPathGetError(
    ctxt)
```

##### Discussion

xmlXPathGetError:
@ctxt: an XPath parser context

Get the error code of an XPath context.

Returns the context error.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnBoolean | xmlXPathReturnBoolean | xmlXPathReturnBoolean | xmlXPathReturnBoolean | xmlXPathReturnBoolean |

---

```
#define xmlXPathReturnBoolean(
    ctxt, val) \ valuePush((
    ctxt), xmlXPathNewBoolean(
    val))
```

##### Discussion

xmlXPathReturnBoolean:
@ctxt: an XPath parser context
@val: a boolean

Pushes the boolean @val on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnEmptyNodeSet | xmlXPathReturnEmptyNodeSet | xmlXPathReturnEmptyNodeSet | xmlXPathReturnEmptyNodeSet | xmlXPathReturnEmptyNodeSet |

---

```
#define xmlXPathReturnEmptyNodeSet(
    ctxt) \ valuePush((
    ctxt), xmlXPathNewNodeSet(
    NULL))
```

##### Discussion

xmlXPathReturnEmptyNodeSet:
@ctxt: an XPath parser context

Pushes an empty node-set on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnEmptyString | xmlXPathReturnEmptyString | xmlXPathReturnEmptyString | xmlXPathReturnEmptyString | xmlXPathReturnEmptyString |

---

```
#define xmlXPathReturnEmptyString(
    ctxt) \ valuePush((
    ctxt), xmlXPathNewCString(
    ""))
```

##### Discussion

xmlXPathReturnEmptyString:
@ctxt: an XPath parser context

Pushes an empty string on the stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnExternal | xmlXPathReturnExternal | xmlXPathReturnExternal | xmlXPathReturnExternal | xmlXPathReturnExternal |

---

```
#define xmlXPathReturnExternal(
    ctxt, val) \ valuePush((
    ctxt), xmlXPathWrapExternal(
    val))
```

##### Discussion

xmlXPathReturnExternal:
@ctxt: an XPath parser context
@val: user data

Pushes user data on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnFalse | xmlXPathReturnFalse | xmlXPathReturnFalse | xmlXPathReturnFalse | xmlXPathReturnFalse |

---

```
#define xmlXPathReturnFalse(
    ctxt) valuePush(((
    ctxt)), xmlXPathNewBoolean(
    0))
```

##### Discussion

xmlXPathReturnFalse:
@ctxt: an XPath parser context

Pushes false on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnNodeSet | xmlXPathReturnNodeSet | xmlXPathReturnNodeSet | xmlXPathReturnNodeSet | xmlXPathReturnNodeSet |

---

```
#define xmlXPathReturnNodeSet(
    ctxt, ns) \ valuePush((
    ctxt), xmlXPathWrapNodeSet(
    ns))
```

##### Discussion

xmlXPathReturnNodeSet:
@ctxt: an XPath parser context
@ns: a node-set

Pushes the node-set @ns on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnNumber | xmlXPathReturnNumber | xmlXPathReturnNumber | xmlXPathReturnNumber | xmlXPathReturnNumber |

---

```
#define xmlXPathReturnNumber(
    ctxt, val) \ valuePush((
    ctxt), xmlXPathNewFloat(
    val))
```

##### Discussion

xmlXPathReturnNumber:
@ctxt: an XPath parser context
@val: a double

Pushes the double @val on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnString | xmlXPathReturnString | xmlXPathReturnString | xmlXPathReturnString | xmlXPathReturnString |

---

```
#define xmlXPathReturnString(
    ctxt, str) \ valuePush((
    ctxt), xmlXPathWrapString(
    str))
```

##### Discussion

xmlXPathReturnString:
@ctxt: an XPath parser context
@str: a string

Pushes the string @str on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathReturnTrue | xmlXPathReturnTrue | xmlXPathReturnTrue | xmlXPathReturnTrue | xmlXPathReturnTrue |

---

```
#define xmlXPathReturnTrue(
    ctxt) valuePush(((
    ctxt)), xmlXPathNewBoolean(
    1))
```

##### Discussion

xmlXPathReturnTrue:
@ctxt: an XPath parser context

Pushes true on the context stack.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathSetArityError | xmlXPathSetArityError | xmlXPathSetArityError | xmlXPathSetArityError | xmlXPathSetArityError |

---

```swift
#define xmlXPathSetArityError(
    ctxt) \ {
    xmlXPatherror(((
    ctxt)), __FILE__, __LINE__, (
    XPATH_INVALID_ARITY)); \ if (((
    ctxt)) != NULL) ((
    ctxt))->error = (
    XPATH_INVALID_ARITY);
}
```

##### Discussion

xmlXPathSetArityError:
@ctxt: an XPath parser context

Raises an XPATH_INVALID_ARITY error.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathSetError | xmlXPathSetError | xmlXPathSetError | xmlXPathSetError | xmlXPathSetError |

---

```swift
#define xmlXPathSetError(
    ctxt, err) \ {
    xmlXPatherror((
    ctxt), __FILE__, __LINE__, (
    err)); \ if ((
    ctxt) != NULL) (
    ctxt)->error = (
    err);
}
```

##### Discussion

xmlXPathSetError:
@ctxt: an XPath parser context
@err: an xmlXPathError code

Raises an error.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathSetTypeError | xmlXPathSetTypeError | xmlXPathSetTypeError | xmlXPathSetTypeError | xmlXPathSetTypeError |

---

```swift
#define xmlXPathSetTypeError(
    ctxt) \ {
    xmlXPatherror(((
    ctxt)), __FILE__, __LINE__, (
    XPATH_INVALID_TYPE)); \ if (((
    ctxt)) != NULL) ((
    ctxt))->error = (
    XPATH_INVALID_TYPE);
}
```

##### Discussion

xmlXPathSetTypeError:
@ctxt: an XPath parser context

Raises an XPATH_INVALID_TYPE error.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathStackIsExternal | xmlXPathStackIsExternal | xmlXPathStackIsExternal | xmlXPathStackIsExternal | xmlXPathStackIsExternal |

---

```swift
#define xmlXPathStackIsExternal(
    ctxt) \ ((
    ctxt->value != NULL) && (
    ctxt->value->type == XPATH_USERS))
```

##### Discussion

xmlXPathStackIsExternal:
@ctxt: an XPath parser context

Checks if the current value on the XPath stack is an external
object.

Returns true if the current object on the stack is an external
object.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlXPathStackIsNodeSet | xmlXPathStackIsNodeSet | xmlXPathStackIsNodeSet | xmlXPathStackIsNodeSet | xmlXPathStackIsNodeSet |

---

```swift
#define xmlXPathStackIsNodeSet(
    ctxt) \ (((
    ctxt)->value != NULL) \ && (((
    ctxt)->value->type == XPATH_NODESET) \ || ((
    ctxt)->value->type == XPATH_XSLT_TREE)))
```

##### Discussion

xmlXPathStackIsNodeSet:
@ctxt: an XPath parser context

Check if the current value on the XPath stack is a node set or
an XSLT value tree.

Returns true if the current object on the stack is a node-set.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XP_ERROR | XP_ERROR | XP_ERROR | XP_ERROR | XP_ERROR |

---

```
#define XP_ERROR(
    X) \ {
    xmlXPathErr(
    ctxt, X); return;
}
```

##### Discussion

XP_ERROR:
@X: the error code

Macro to raise an XPath error and return.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XP_ERROR0 | XP_ERROR0 | XP_ERROR0 | XP_ERROR0 | XP_ERROR0 |

---

```
#define XP_ERROR0(
    X) \ {
    xmlXPathErr(
    ctxt, X); return(
    0);
}
```

##### Discussion

XP_ERROR0:
@X: the error code

Macro to raise an XPath error and return 0.

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
