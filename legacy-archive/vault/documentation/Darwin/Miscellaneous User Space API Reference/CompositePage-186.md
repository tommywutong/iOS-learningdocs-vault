---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xslt/CompositePage.html
archived_at: '2026-07-15T07:23:29.394085Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xslt.h | xslt.h | xslt.h | xslt.h | xslt.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  ["xsltexports.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltexports/index.html#//apple_ref/doc/header/xsltexports.h) |

## Introduction

---

## Constants

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltEngineVersion | xsltEngineVersion | xsltEngineVersion | xsltEngineVersion | xsltEngineVersion |

---

```
XSLTPUBVAR const char *xsltEngineVersion;
```

##### Discussion

xsltEngineVersion:

The version string for libxslt.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltLibxmlVersion | xsltLibxmlVersion | xsltLibxmlVersion | xsltLibxmlVersion | xsltLibxmlVersion |

---

```
XSLTPUBVAR const int xsltLibxmlVersion;
```

##### Discussion

xsltLibxmlVersion:

The version of libxml libxslt was compiled against.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltLibxsltVersion | xsltLibxsltVersion | xsltLibxsltVersion | xsltLibxsltVersion | xsltLibxsltVersion |

---

```
XSLTPUBVAR const int xsltLibxsltVersion;
```

##### Discussion

xsltLibxsltVersion:

The version of libxslt compiled.

## Globals

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xsltMaxDepth | xsltMaxDepth | xsltMaxDepth | xsltMaxDepth | xsltMaxDepth |

---

```
XSLTPUBVAR int xsltMaxDepth;
```

##### Discussion

xsltMaxDepth:

This value is used to detect templates loops.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_DEFAULT_URL | XSLT_DEFAULT_URL | XSLT_DEFAULT_URL | XSLT_DEFAULT_URL | XSLT_DEFAULT_URL |

---

```
#define XSLT_DEFAULT_URL "http://xmlsoft.org/XSLT/"
```

##### Discussion

XSLT_DEFAULT_URL:

The XSLT "vendor" URL for this processor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_DEFAULT_VENDOR | XSLT_DEFAULT_VENDOR | XSLT_DEFAULT_VENDOR | XSLT_DEFAULT_VENDOR | XSLT_DEFAULT_VENDOR |

---

```
#define XSLT_DEFAULT_VENDOR "libxslt"
```

##### Discussion

XSLT_DEFAULT_VENDOR:

The XSLT "vendor" string for this processor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_DEFAULT_VERSION | XSLT_DEFAULT_VERSION | XSLT_DEFAULT_VERSION | XSLT_DEFAULT_VERSION | XSLT_DEFAULT_VERSION |

---

```
#define XSLT_DEFAULT_VERSION "1.0"
```

##### Discussion

XSLT_DEFAULT_VERSION:

The default version of XSLT supported.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_NAMESPACE | XSLT_NAMESPACE | XSLT_NAMESPACE | XSLT_NAMESPACE | XSLT_NAMESPACE |

---

```
#define XSLT_NAMESPACE
```

##### Discussion

XSLT_NAMESPACE:

The XSLT specification namespace.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_PARSE_OPTIONS | XSLT_PARSE_OPTIONS | XSLT_PARSE_OPTIONS | XSLT_PARSE_OPTIONS | XSLT_PARSE_OPTIONS |

---

```
#define XSLT_PARSE_OPTIONS \ XML_PARSE_NOENT | XML_PARSE_DTDLOAD | XML_PARSE_DTDATTR | XML_PARSE_NOCDATA
```

##### Discussion

XSLT_PARSE_OPTIONS:

The set of options to pass to an xmlReadxxx when loading files for
XSLT consumption.

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
