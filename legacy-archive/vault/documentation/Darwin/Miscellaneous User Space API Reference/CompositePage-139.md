---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_relops/CompositePage.html
archived_at: '2026-07-15T07:23:28.557923Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_relops.h | stl_relops.h | stl_relops.h | stl_relops.h | stl_relops.h |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

@if maint
Inclusion of this file has been removed from
all of the other STL headers for safety reasons, except std_utility.h.
For more information, see the thread of about twenty messages starting
with http://gcc.gnu.org/ml/libstdc++/2001-01/msg00223.html , or the
FAQ at http://gcc.gnu.org/onlinedocs/libstdc++/faq/index.html#4_4 .

Short summary: the rel_ops operators should be avoided for the present.
@endif

---

## Functions

**[operator !=](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_relops/CompositePage.html#//apple_ref/c/func/operator!a_DONTLINK_0x2f52250c)**
:

**[operator <=](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_relops/CompositePage.html#//apple_ref/c/func/operator`a_DONTLINK_0x2f56f1bc)**
:

**[operator >=](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_relops/CompositePage.html#//apple_ref/c/func/operatorba_DONTLINK_0x2f57949c)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator != | operator != | operator != | operator != | operator != |

---

```
/**
@brief Defines @c != for arbitrary types, in terms of @c ==.
@param x A thing.
@param y Another thing.
@return x != y

This function uses @c == to determine its result.
    */
template <class _Tp> inline bool operator!=(
    const _Tp& __x,
    const _Tp& __y)
```

##### Discussion

@namespace std::rel_ops
@brief The generated relational operators are sequestered here.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator <= | operator <= | operator <= | operator <= | operator <= |

---

```
template <class _Tp> inline bool operator<=(
    const _Tp& __x,
    const _Tp& __y)
```

##### Parameters

**`x`**
: A thing.

**`y`**
: Another thing.

##### Return Value

x <= y

This function uses @c < to determine its result.

##### Discussion

@brief Defines @c <= for arbitrary types, in terms of @c <.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator >= | operator >= | operator >= | operator >= | operator >= |

---

```
template <class _Tp> inline bool operator>=(
    const _Tp& __x,
    const _Tp& __y)
```

##### Parameters

**`x`**
: A thing.

**`y`**
: Another thing.

##### Return Value

x >= y

This function uses @c < to determine its result.

##### Discussion

@brief Defines @c >= for arbitrary types, in terms of @c <.

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
