---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/imports/CompositePage.html
archived_at: '2026-07-15T07:23:26.862048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| imports.h | imports.h | imports.h | imports.h | imports.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  ["xsltexports.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltexports/index.html#//apple_ref/doc/header/xsltexports.h)  ["xsltInternals.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xsltInternals/index.html#//apple_ref/doc/header/xsltInternals.h) |

## Introduction

---

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_GET_IMPORT_INT | XSLT_GET_IMPORT_INT | XSLT_GET_IMPORT_INT | XSLT_GET_IMPORT_INT | XSLT_GET_IMPORT_INT |

---

```
#define XSLT_GET_IMPORT_INT(
    res, style, name)
```

##### Discussion

XSLT_GET_IMPORT_INT:

A macro to import intergers from the stylesheet cascading order.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XSLT_GET_IMPORT_PTR | XSLT_GET_IMPORT_PTR | XSLT_GET_IMPORT_PTR | XSLT_GET_IMPORT_PTR | XSLT_GET_IMPORT_PTR |

---

```
#define XSLT_GET_IMPORT_PTR(
    res, style, name)
```

##### Discussion

XSLT_GET_IMPORT_PTR:

A macro to import pointers from the stylesheet cascading order.

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
