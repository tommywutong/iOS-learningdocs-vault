---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/exsltexports/CompositePage.html
archived_at: '2026-07-15T07:23:26.596950Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| exsltexports.h | exsltexports.h | exsltexports.h | exsltexports.h | exsltexports.h |

## Introduction

---

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EXSLTCALL | EXSLTCALL | EXSLTCALL | EXSLTCALL | EXSLTCALL |

---

```
#define EXSLTCALL
```

##### Discussion

EXSLTCALL:

Macros which declare the called convention for exported functions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EXSLTPUBFUN | EXSLTPUBFUN | EXSLTPUBFUN | EXSLTPUBFUN | EXSLTPUBFUN |

---

```
/**
EXSLTPUBFUN:

Macros which declare an exportable function
    */
#define EXSLTPUBFUN
```

##### Discussion

EXSLTPUBFUN, EXSLTPUBVAR, EXSLTCALL

Macros which declare an exportable function, an exportable variable and
the calling convention used for functions.

Please use an extra block for every platform/compiler combination when
modifying this, rather than overlong #ifdef lines. This helps
readability as well as the fact that different compilers on the same
platform might need different definitions.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EXSLTPUBVAR | EXSLTPUBVAR | EXSLTPUBVAR | EXSLTPUBVAR | EXSLTPUBVAR |

---

```
#define EXSLTPUBVAR extern
```

##### Discussion

EXSLTPUBVAR:

Macros which declare an exportable variable

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
