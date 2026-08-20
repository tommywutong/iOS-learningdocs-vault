---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tools/CompositePage.html
archived_at: '2026-07-15T07:23:28.883850Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tools.h | tools.h | tools.h | tools.h | tools.h |

## Introduction

@defgroup util Memory Utility Routines
@ingroup library
@{

---

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SNMP_FREE | SNMP_FREE | SNMP_FREE | SNMP_FREE | SNMP_FREE |

---

```
#define SNMP_FREE(
    s) do {
    if (
    s) {
    free((
    void *)s); s=NULL; }
} while(
    0)
```

##### Discussion

@def SNMP_FREE(s)
Frees a pointer only if it is !NULL and sets its value to NULL

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SNMP_MALLOC_STRUCT | SNMP_MALLOC_STRUCT | SNMP_MALLOC_STRUCT | SNMP_MALLOC_STRUCT | SNMP_MALLOC_STRUCT |

---

```
#define SNMP_MALLOC_STRUCT(
    s)
```

##### Discussion

@def SNMP_MALLOC_STRUCT(s)
Mallocs memory of sizeof(struct s), zeros it and returns a pointer to it.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SNMP_MALLOC_TYPEDEF | SNMP_MALLOC_TYPEDEF | SNMP_MALLOC_TYPEDEF | SNMP_MALLOC_TYPEDEF | SNMP_MALLOC_TYPEDEF |

---

```
#define SNMP_MALLOC_TYPEDEF(
    td)
```

##### Discussion

@def SNMP_MALLOC_TYPEDEF(t)
Mallocs memory of sizeof(t), zeros it and returns a pointer to it.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SNMP_MAX | SNMP_MAX | SNMP_MAX | SNMP_MAX | SNMP_MAX |

---

```
#define SNMP_MAX(
    a,b)
```

##### Discussion

@def SNMP_MAX(a, b)
Computers the maximum of a and b.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SNMP_MIN | SNMP_MIN | SNMP_MIN | SNMP_MIN | SNMP_MIN |

---

```
#define SNMP_MIN(
    a,b)
```

##### Discussion

@def SNMP_MIN(a, b)
Computers the minimum of a and b.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SNMP_SWIPE_MEM | SNMP_SWIPE_MEM | SNMP_SWIPE_MEM | SNMP_SWIPE_MEM | SNMP_SWIPE_MEM |

---

```
#define SNMP_SWIPE_MEM(
    n,s) do {
    if (
    n) free((
    void *)n); n = s; s=NULL;
} while(
    0)
```

##### Discussion

@def SNMP_SWIPE_MEM(n, s)
Frees pointer n only if it is !NULL, sets n to s and sets s to NULL

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SNMP_ZERO | SNMP_ZERO | SNMP_ZERO | SNMP_ZERO | SNMP_ZERO |

---

```
#define SNMP_ZERO(
    s,l) do {
    if (
    s) memset(
    s, 0, l);
} while(
    0)
```

##### Discussion

@def SNMP_ZERO(s,l)
Zeros l bytes of memory starting at s.

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
