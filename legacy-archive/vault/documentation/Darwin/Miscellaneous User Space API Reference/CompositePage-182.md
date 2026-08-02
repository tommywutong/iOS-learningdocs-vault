---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/CompositePage.html
archived_at: '2026-07-15T07:23:29.312173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlversion.h | xmlversion.h | xmlversion.h | xmlversion.h | xmlversion.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlexports.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlexports/index.html#//apple_ref/doc/header/xmlexports.h)  <ansidecl.h> |

## Introduction

---

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LIBXML_DOTTED_VERSION | LIBXML_DOTTED_VERSION | LIBXML_DOTTED_VERSION | LIBXML_DOTTED_VERSION | LIBXML_DOTTED_VERSION |

---

```
#define LIBXML_DOTTED_VERSION "2.6.16"
```

##### Discussion

LIBXML_DOTTED_VERSION:

the version string like "1.2.3"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LIBXML_TEST_VERSION | LIBXML_TEST_VERSION | LIBXML_TEST_VERSION | LIBXML_TEST_VERSION | LIBXML_TEST_VERSION |

---

```
#define LIBXML_TEST_VERSION xmlCheckVersion(
    20616);
```

##### Discussion

LIBXML_TEST_VERSION:

Macro to check that the libxml version in use is compatible with
the version the software has been compiled against

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LIBXML_VERSION | LIBXML_VERSION | LIBXML_VERSION | LIBXML_VERSION | LIBXML_VERSION |

---

```
#define LIBXML_VERSION 20616
```

##### Discussion

LIBXML_VERSION:

the version number: 1.2.3 value is 1002003

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LIBXML_VERSION_EXTRA | LIBXML_VERSION_EXTRA | LIBXML_VERSION_EXTRA | LIBXML_VERSION_EXTRA | LIBXML_VERSION_EXTRA |

---

```
#define LIBXML_VERSION_EXTRA ""
```

##### Discussion

LIBXML_VERSION_EXTRA:

extra version information, used to show a CVS compilation

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LIBXML_VERSION_STRING | LIBXML_VERSION_STRING | LIBXML_VERSION_STRING | LIBXML_VERSION_STRING | LIBXML_VERSION_STRING |

---

```
#define LIBXML_VERSION_STRING "20616"
```

##### Discussion

LIBXML_VERSION_STRING:

the version number string, 1.2.3 value is "1002003"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| WITH_TRIO | WITH_TRIO | WITH_TRIO | WITH_TRIO | WITH_TRIO |

---

```
#define WITH_TRIO
```

##### Discussion

WITH_TRIO:

defined if the trio support need to be configured in

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| WITH_TRIO | WITH_TRIO | WITH_TRIO | WITH_TRIO | WITH_TRIO |

---

```
#define WITH_TRIO 1
```

##### Discussion

WITH_TRIO:

defined if the trio support need to be configured in

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| WITHOUT_TRIO | WITHOUT_TRIO | WITHOUT_TRIO | WITHOUT_TRIO | WITHOUT_TRIO |

---

```
#define WITHOUT_TRIO
```

##### Discussion

WITHOUT_TRIO:

defined if the trio support should not be configured in

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
