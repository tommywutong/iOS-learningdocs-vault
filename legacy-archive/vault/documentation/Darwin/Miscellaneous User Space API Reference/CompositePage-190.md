---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltutils/CompositePage.html
archived_at: '2026-07-15T07:23:29.462830Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltutils.h | xsltutils.h | xsltutils.h | xsltutils.h | xsltutils.h |

|  |  |
| --- | --- |
| __Includes:__ | <libxslt/xsltwin32config.h>  [<libxslt/xsltconfig.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltconfig/index.html#//apple_ref/doc/header/xsltconfig.h)  <stdarg.h>  [<libxml/xpath.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xpath/index.html#//apple_ref/doc/header/xpath.h)  <libxml/dict.h>  [<libxml/xmlerror.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlerror/index.html#//apple_ref/doc/header/xmlerror.h)  ["xsltexports.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltexports/index.html#//apple_ref/doc/header/xsltexports.h)  ["xsltInternals.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltInternals/index.html#//apple_ref/doc/header/xsltInternals.h) |

## Introduction

---

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_XSLT_ELEM | IS_XSLT_ELEM | IS_XSLT_ELEM | IS_XSLT_ELEM | IS_XSLT_ELEM |

---

```swift
#define IS_XSLT_ELEM(
    n) \ (((
    n) != NULL) && ((
    n)->ns != NULL) && \ (
    xmlStrEqual((
    n)->ns->href, ((
    xmlChar *) "http:/*www.w3.org/1999/XSL/Transform") \

        */)))
```

##### Discussion

IS_XSLT_ELEM:

Checks that the element pertains to XSLT namespace.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_XSLT_NAME | IS_XSLT_NAME | IS_XSLT_NAME | IS_XSLT_NAME | IS_XSLT_NAME |

---

```swift
#define IS_XSLT_NAME(
    n, val) \ (
    xmlStrEqual((
    n)->name, (
    const xmlChar *) (
    val)))
```

##### Discussion

IS_XSLT_NAME:

Checks the value of an element in XSLT namespace.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_XSLT_REAL_NODE | IS_XSLT_REAL_NODE | IS_XSLT_REAL_NODE | IS_XSLT_REAL_NODE | IS_XSLT_REAL_NODE |

---

```swift
#define IS_XSLT_REAL_NODE(
    n) \ (((
    n) != NULL) && \ (((
    n)->type == XML_ELEMENT_NODE) || \ ((
    n)->type == XML_TEXT_NODE) || \ ((
    n)->type == XML_ATTRIBUTE_NODE) || \ ((
    n)->type == XML_DOCUMENT_NODE) || \ ((
    n)->type == XML_HTML_DOCUMENT_NODE) || \ ((
    n)->type == XML_PI_NODE)))
```

##### Discussion

IS_XSLT_REAL_NODE:

Check that a node is a 'real' one: document, element, text or attribute.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_STRANGE | XSLT_STRANGE | XSLT_STRANGE | XSLT_STRANGE | XSLT_STRANGE |

---

```
#define XSLT_STRANGE \ xsltGenericError(
    xsltGenericErrorContext, \ "Internal error at %s:%d\n", \ __FILE__, __LINE__);
```

##### Discussion

XSLT_STRANGE:

Macro to flag that a problem was detected internally.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_TIMESTAMP_TICS_PER_SEC | XSLT_TIMESTAMP_TICS_PER_SEC | XSLT_TIMESTAMP_TICS_PER_SEC | XSLT_TIMESTAMP_TICS_PER_SEC | XSLT_TIMESTAMP_TICS_PER_SEC |

---

```
#define XSLT_TIMESTAMP_TICS_PER_SEC 100000l
```

##### Discussion

XSLT_TIMESTAMP_TICS_PER_SEC:

Sampling precision for profiling

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_TODO | XSLT_TODO | XSLT_TODO | XSLT_TODO | XSLT_TODO |

---

```
#define XSLT_TODO \ xsltGenericError(
    xsltGenericErrorContext, \ "Unimplemented block at %s:%d\n", \ __FILE__, __LINE__);
```

##### Discussion

XSLT_TODO:

Macro to flag unimplemented blocks.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_TRACE | XSLT_TRACE | XSLT_TRACE | XSLT_TRACE | XSLT_TRACE |

---

```swift
#define XSLT_TRACE(
    ctxt,code,call) \ if (
    ctxt->traceCode && (
    *(
    ctxt->traceCode) & code)) \ call
```

##### Discussion

XSLT_TRACE:

Control the type of xsl debugtrace messages emitted.

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
