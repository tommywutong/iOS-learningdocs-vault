---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/documents/CompositePage.html
archived_at: '2026-07-15T07:23:26.527148Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| documents.h | documents.h | documents.h | documents.h | documents.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  ["xsltexports.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltexports/index.html#//apple_ref/doc/header/xsltexports.h)  ["xsltInternals.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltInternals/index.html#//apple_ref/doc/header/xsltInternals.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltDocLoaderFunc | xsltDocLoaderFunc | xsltDocLoaderFunc | xsltDocLoaderFunc | xsltDocLoaderFunc |

---

```
typedef xmlDocPtr (*xsltDocLoaderFunc) (
    const xmlChar *URI,
    xmlDictPtr dict,
    int options,
    void *ctxt,
    xsltLoadType type);
```

##### Discussion

xsltDocLoaderFunc:
@URI: the URI of the document to load
@dict: the dictionnary to use when parsing that document
@options: parsing options, a set of xmlParserOption
@ctxt: the context, either a stylesheet or a transformation context
@type: the xsltLoadType indicating the kind of loading required

An xsltDocLoaderFunc is a signature for a function which can be
registered to load document not provided by the compilation or
transformation API themselve, for example when an xsl:import,
xsl:include is found at compilation time or when a document()
call is made at runtime.

Returns the pointer to the document (which will be modified and
freed by the engine later), or NULL in case of error.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltLoadType | xsltLoadType | xsltLoadType | xsltLoadType | xsltLoadType |

---

```
typedef enum {
    XSLT_LOAD_START = 0, /* loading for a top stylesheet */
    XSLT_LOAD_STYLESHEET = 1, /* loading for a stylesheet include/import */
    XSLT_LOAD_DOCUMENT = 2 /* loading document at transformation time */
} xsltLoadType;
```

##### Discussion

xsltLoadType:

Enum defining the kind of loader requirement.

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
