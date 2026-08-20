---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltInternals/CompositePage.html
archived_at: '2026-07-15T07:23:29.411341Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltInternals.h | xsltInternals.h | xsltInternals.h | xsltInternals.h | xsltInternals.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  [<libxml/hash.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/hash/index.html#//apple_ref/doc/header/hash.h)  [<libxml/xpath.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xpath/index.html#//apple_ref/doc/header/xpath.h)  [<libxml/xmlerror.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlerror/index.html#//apple_ref/doc/header/xmlerror.h)  <libxml/dict.h>  [<libxslt/xslt.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xslt/index.html#//apple_ref/doc/header/xslt.h)  ["xsltexports.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltexports/index.html#//apple_ref/doc/header/xsltexports.h)  ["numbersInternals.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/numbersInternals/index.html#//apple_ref/doc/header/numbersInternals.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltDecimalFormat | xsltDecimalFormat | xsltDecimalFormat | xsltDecimalFormat | xsltDecimalFormat |

---

```
typedef struct _xsltDecimalFormat xsltDecimalFormat;
```

##### Discussion

xsltDecimalFormat:

Data structure of decimal-format.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltDocument | xsltDocument | xsltDocument | xsltDocument | xsltDocument |

---

```
typedef struct _xsltDocument xsltDocument;
```

##### Discussion

xsltDocument:

Data structure associated to a parsed document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltElemPreComp | xsltElemPreComp | xsltElemPreComp | xsltElemPreComp | xsltElemPreComp |

---

```
typedef struct _xsltElemPreComp xsltElemPreComp;
```

##### Discussion

xsltElemPreComp:

The in-memory structure corresponding to element precomputed data,
designed to be extended by extension implementors.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltElemPreCompDeallocator | xsltElemPreCompDeallocator | xsltElemPreCompDeallocator | xsltElemPreCompDeallocator | xsltElemPreCompDeallocator |

---

```
typedef void (*xsltElemPreCompDeallocator) (
    xsltElemPreCompPtr comp);
```

##### Discussion

xsltElemPreCompDeallocator:
@comp: the #xsltElemPreComp to free up

Deallocates an #xsltElemPreComp structure.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltRuntimeExtra | xsltRuntimeExtra | xsltRuntimeExtra | xsltRuntimeExtra | xsltRuntimeExtra |

---

```
typedef struct _xsltRuntimeExtra xsltRuntimeExtra;
```

##### Discussion

xsltRuntimeExtra:

Extra information added to the transformation context.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltSortFunc | xsltSortFunc | xsltSortFunc | xsltSortFunc | xsltSortFunc |

---

```
typedef void (*xsltSortFunc) (
    xsltTransformContextPtr ctxt,
    xmlNodePtr *sorts,
    int nbsorts);
```

##### Discussion

xsltSortFunc:
@ctxt: a transformation context
@sorts: the node-set to sort
@nbsorts: the number of sorts

Signature of the function to use during sorting

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltStylePreComp | xsltStylePreComp | xsltStylePreComp | xsltStylePreComp | xsltStylePreComp |

---

```
typedef struct _xsltStylePreComp xsltStylePreComp;
```

##### Discussion

xsltStylePreComp:

The in-memory structure corresponding to XSLT stylesheet constructs
precomputed data.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltTemplate | xsltTemplate | xsltTemplate | xsltTemplate | xsltTemplate |

---

```
typedef struct _xsltTemplate xsltTemplate;
```

##### Discussion

xsltTemplate:

The in-memory structure corresponding to an XSLT Template.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltTransformFunction | xsltTransformFunction | xsltTransformFunction | xsltTransformFunction | xsltTransformFunction |

---

```
typedef void (*xsltTransformFunction) (
    xsltTransformContextPtr ctxt,
    xmlNodePtr node,
    xmlNodePtr inst,
    xsltElemPreCompPtr comp);
```

##### Discussion

xsltTransformFunction:
@ctxt: the XSLT transformation context
@node: the input node
@inst: the stylesheet node
@comp: the compiled information from the stylesheet

Signature of the function associated to elements part of the
stylesheet language like xsl:if or xsl:apply-templates.

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xsltElemPreComp | _xsltElemPreComp | _xsltElemPreComp | _xsltElemPreComp | _xsltElemPreComp |

---

```
struct _xsltElemPreComp {
    xsltElemPreCompPtr next; /* chained list */
    xsltStyleType type; /* type of the element */
    xsltTransformFunction func; /* handling function */
    xmlNodePtr inst; /* the instruction */
    /* end of common part */
    xsltElemPreCompDeallocator free; /* the deallocator */
};
```

##### Discussion

xsltElemPreComp:

The in-memory structure corresponding to element precomputed data,
designed to be extended by extension implementors.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_STOPPED | CHECK_STOPPED | CHECK_STOPPED | CHECK_STOPPED | CHECK_STOPPED |

---

```swift
#define CHECK_STOPPED if (
    ctxt->state == XSLT_STATE_STOPPED) return;
```

##### Discussion

CHECK_STOPPED:

Macro to check if the XSLT processing should be stopped.
Will return from the function.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_STOPPED0 | CHECK_STOPPED0 | CHECK_STOPPED0 | CHECK_STOPPED0 | CHECK_STOPPED0 |

---

```swift
#define CHECK_STOPPED0 if (
    ctxt->state == XSLT_STATE_STOPPED) return(
    0);
```

##### Discussion

CHECK_STOPPED0:

Macro to check if the XSLT processing should be stopped.
Will return from the function with a 0 value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHECK_STOPPEDE | CHECK_STOPPEDE | CHECK_STOPPEDE | CHECK_STOPPEDE | CHECK_STOPPEDE |

---

```swift
#define CHECK_STOPPEDE if (
    ctxt->state == XSLT_STATE_STOPPED) goto error;
```

##### Discussion

CHECK_STOPPEDE:

Macro to check if the XSLT processing should be stopped.
Will goto the error: label.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_MAX_SORT | XSLT_MAX_SORT | XSLT_MAX_SORT | XSLT_MAX_SORT | XSLT_MAX_SORT |

---

```
#define XSLT_MAX_SORT 15
```

##### Discussion

XSLT_MAX_SORT:

Max number of specified xsl:sort on an element.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_PAT_NO_PRIORITY | XSLT_PAT_NO_PRIORITY | XSLT_PAT_NO_PRIORITY | XSLT_PAT_NO_PRIORITY | XSLT_PAT_NO_PRIORITY |

---

```
#define XSLT_PAT_NO_PRIORITY -12345789
```

##### Discussion

XSLT_PAT_NO_PRIORITY:

Specific value for pattern without priority expressed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_RUNTIME_EXTRA | XSLT_RUNTIME_EXTRA | XSLT_RUNTIME_EXTRA | XSLT_RUNTIME_EXTRA | XSLT_RUNTIME_EXTRA |

---

```
#define XSLT_RUNTIME_EXTRA(
    ctxt, nr)
```

##### Discussion

XSLT_RUNTIME_EXTRA:
@ctxt: the transformation context
@nr: the index

Macro used to define extra information stored in the context

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_RUNTIME_EXTRA_FREE | XSLT_RUNTIME_EXTRA_FREE | XSLT_RUNTIME_EXTRA_FREE | XSLT_RUNTIME_EXTRA_FREE | XSLT_RUNTIME_EXTRA_FREE |

---

```
#define XSLT_RUNTIME_EXTRA_FREE(
    ctxt, nr)
```

##### Discussion

XSLT_RUNTIME_EXTRA_FREE:
@ctxt: the transformation context
@nr: the index

Macro used to free extra information stored in the context

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_RUNTIME_EXTRA_LST | XSLT_RUNTIME_EXTRA_LST | XSLT_RUNTIME_EXTRA_LST | XSLT_RUNTIME_EXTRA_LST | XSLT_RUNTIME_EXTRA_LST |

---

```
#define XSLT_RUNTIME_EXTRA_LST(
    ctxt, nr)
```

##### Discussion

XSLT_RUNTIME_EXTRA_LST:
@ctxt: the transformation context
@nr: the index

Macro used to access extra information stored in the context

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
