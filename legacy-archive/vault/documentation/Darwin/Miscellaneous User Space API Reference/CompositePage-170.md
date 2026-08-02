---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/valid/CompositePage.html
archived_at: '2026-07-15T07:23:29.065314Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| valid.h | valid.h | valid.h | valid.h | valid.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/xmlerror.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlerror/index.html#//apple_ref/doc/header/xmlerror.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  [<libxml/list.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/list/index.html#//apple_ref/doc/header/list.h)  [<libxml/xmlautomata.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlautomata/index.html#//apple_ref/doc/header/xmlautomata.h)  [<libxml/xmlregexp.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlregexp/index.html#//apple_ref/doc/header/xmlregexp.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlValidityErrorFunc | xmlValidityErrorFunc | xmlValidityErrorFunc | xmlValidityErrorFunc | xmlValidityErrorFunc |

---

```
typedef void (*xmlValidityErrorFunc) (
    void *ctx,
    const char *msg,
    ...);
```

##### Discussion

xmlValidityErrorFunc:
@ctx: usually an xmlValidCtxtPtr to a validity error context,
but comes from ctxt->userData (which normally contains such
a pointer); ctxt->userData can be changed by the user.
@msg: the string to format \*printf like vararg
@...: remaining arguments to the format

Callback called when a validity error is found. This is a message
oriented function similar to an \*printf function.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlValidityWarningFunc | xmlValidityWarningFunc | xmlValidityWarningFunc | xmlValidityWarningFunc | xmlValidityWarningFunc |

---

```
typedef void (*xmlValidityWarningFunc) (
    void *ctx,
    const char *msg,
    ...);
```

##### Discussion

xmlValidityWarningFunc:
@ctx: usually an xmlValidCtxtPtr to a validity error context,
but comes from ctxt->userData (which normally contains such
a pointer); ctxt->userData can be changed by the user.
@msg: the string to format \*printf like vararg
@...: remaining arguments to the format

Callback called when a validity warning is found. This is a message
oriented function similar to an \*printf function.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_CTXT_FINISH_DTD_0 | XML_CTXT_FINISH_DTD_0 | XML_CTXT_FINISH_DTD_0 | XML_CTXT_FINISH_DTD_0 | XML_CTXT_FINISH_DTD_0 |

---

```
#define XML_CTXT_FINISH_DTD_0 0xabcd1234
```

##### Discussion

XML_CTXT_FINISH_DTD_0:

Special value for finishDtd field when embedded in an xmlParserCtxt

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_CTXT_FINISH_DTD_1 | XML_CTXT_FINISH_DTD_1 | XML_CTXT_FINISH_DTD_1 | XML_CTXT_FINISH_DTD_1 | XML_CTXT_FINISH_DTD_1 |

---

```
#define XML_CTXT_FINISH_DTD_1 0xabcd1235
```

##### Discussion

XML_CTXT_FINISH_DTD_1:

Special value for finishDtd field when embedded in an xmlParserCtxt

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
