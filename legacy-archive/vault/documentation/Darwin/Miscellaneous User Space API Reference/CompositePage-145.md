---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_uninitialized/CompositePage.html
archived_at: '2026-07-15T07:23:28.647877Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_uninitialized.h | stl_uninitialized.h | stl_uninitialized.h | stl_uninitialized.h | stl_uninitialized.h |

|  |  |
| --- | --- |
| __Includes:__ | <cstring>  <cstring>  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  <cstring> |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| uninitialized_copy | uninitialized_copy | uninitialized_copy | uninitialized_copy | uninitialized_copy |

---

```
template<typename _InputIterator, typename _ForwardIterator> inline _ForwardIterator uninitialized_copy(
    _InputIterator __first,
    _InputIterator __last,
    _ForwardIterator __result)
```

##### Discussion

@brief Copies the range [first,last) into result.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| uninitialized_fill | uninitialized_fill | uninitialized_fill | uninitialized_fill | uninitialized_fill |

---

```
template<typename _ForwardIterator, typename _Tp> inline void uninitialized_fill(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __x)
```

##### Discussion

@brief Copies the value x into the range [first,last).

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| uninitialized_fill_n | uninitialized_fill_n | uninitialized_fill_n | uninitialized_fill_n | uninitialized_fill_n |

---

```
template<typename _ForwardIterator, typename _Size, typename _Tp> inline void uninitialized_fill_n(
    _ForwardIterator __first,
    _Size __n,
    const _Tp& __x)
```

##### Discussion

@brief Copies the value x into the range [first,first+n).

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
