---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/CompositePage.html
archived_at: '2026-07-15T07:23:28.398039Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_iterator_base_funcs.h | stl_iterator_base_funcs.h | stl_iterator_base_funcs.h | stl_iterator_base_funcs.h | stl_iterator_base_funcs.h |

|  |  |
| --- | --- |
| __Includes:__ | [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

This file contains all of the general iterator-related utility
functions, such as distance() and advance().

---

## Functions

**[advance](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3bmr3gc3tdmvpuit2okrgestsll4yhqmtdmrrtizbzha)**
:

**[distance](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3enfzxiylomnsv6rcpjzkeyskojnpta6bsmyydkmzrmvrq)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| advance | advance | advance | advance | advance |

---

```
template<typename _InputIterator, typename _Distance> inline void advance(
    _InputIterator& __i,
    _Distance __n)
```

##### Parameters

**`i`**
: An input iterator.

**`n`**
: The "delta" by which to change @p i.

##### Return Value

Nothing.

This increments @p i by @p n. For bidirectional and random access
iterators, @p n may be negative, in which case @p i is decremented.

For random access iterators, this uses their @c + and @c - operations
and are constant time. For other %iterator classes they are linear time.

##### Discussion

@brief A generalization of pointer arithmetic.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| distance | distance | distance | distance | distance |

---

```
template<typename _InputIterator> inline typename iterator_traits<_InputIterator>::difference_type distance(
    _InputIterator __first,
    _InputIterator __last)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

##### Return Value

The distance between them.

Returns @c n such that first + n == last. This requires that @p last
must be reachable from @p first. Note that @c n may be negative.

For random access iterators, this uses their @c + and @c - operations
and are constant time. For other %iterator classes they are linear time.

##### Discussion

@brief A generalization of pointer arithmetic.

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
