---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_heap/CompositePage.html
archived_at: '2026-07-15T07:23:28.319055Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_heap.h | stl_heap.h | stl_heap.h | stl_heap.h | stl_heap.h |

|  |  |
| --- | --- |
| __Includes:__ | [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Functions

**[make_heap(_RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmfvwkx3imvqxax2ej5hfitcjjzfv6mdygjtdembtgu4ta)**
:

**[make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmfvwkx3imvqxax2ej5hfitcjjzfv6mdygjtdemdemftdi)**
:

**[sort_heap(_RandomAccessIterator, _RandomAccessIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tn5zhix3imvqxax2ej5hfitcjjzfv6mdygjtdemjxmi4wg)**
:

**[sort_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3tn5zhix3imvqxax2ej5hfitcjjzfv6mdygjtdemlegm2ta)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| make_heap(_RandomAccessIterator, _RandomAccessIterator) | make_heap(_RandomAccessIterator, _RandomAccessIterator) | make_heap(_RandomAccessIterator, _RandomAccessIterator) | make_heap(_RandomAccessIterator, _RandomAccessIterator) | make_heap(_RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> void make_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Parameters

**`first`**
: Start of heap.

**`last`**
: End of heap.
@ingroup heap

This operation makes the elements in [first,last) into a heap.

##### Discussion

@brief Construct a heap over a range.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Compare> inline void make_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: Start of heap.

**`last`**
: End of heap.

**`comp`**
: Comparison functor to use.
@ingroup heap

This operation makes the elements in [first,last) into a heap.
Comparisons are made using comp.

##### Discussion

@brief Construct a heap over a range using comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sort_heap(_RandomAccessIterator, _RandomAccessIterator) | sort_heap(_RandomAccessIterator, _RandomAccessIterator) | sort_heap(_RandomAccessIterator, _RandomAccessIterator) | sort_heap(_RandomAccessIterator, _RandomAccessIterator) | sort_heap(_RandomAccessIterator, _RandomAccessIterator) |

---

```
template<typename _RandomAccessIterator> void sort_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Parameters

**`first`**
: Start of heap.

**`last`**
: End of heap.
@ingroup heap

This operation sorts the valid heap in the range [first,last).

##### Discussion

@brief Sort a heap.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sort_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) | sort_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare) |

---

```
template<typename _RandomAccessIterator, typename _Compare> void sort_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Parameters

**`first`**
: Start of heap.

**`last`**
: End of heap.

**`comp`**
: Comparison functor to use.
@ingroup heap

This operation sorts the valid heap in the range [first,last).
Comparisons are made using comp.

##### Discussion

@brief Sort a heap using comparison functor.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| pop_heap | pop_heap | pop_heap | pop_heap | pop_heap |

---

```
template<typename _RandomAccessIterator> inline void pop_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Discussion

@brief Pop an element off a heap.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| pop_heap | pop_heap | pop_heap | pop_heap | pop_heap |

---

```
template<typename _RandomAccessIterator, typename _Compare> inline void pop_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@brief Pop an element off a heap using comparison functor.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| push_heap | push_heap | push_heap | push_heap | push_heap |

---

```
template<typename _RandomAccessIterator> inline void push_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last)
```

##### Discussion

@brief Push an element onto a heap.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| push_heap | push_heap | push_heap | push_heap | push_heap |

---

```
template<typename _RandomAccessIterator, typename _Compare> inline void push_heap(
    _RandomAccessIterator __first,
    _RandomAccessIterator __last,
    _Compare __comp)
```

##### Discussion

@brief Push an element onto a heap using comparison functor.

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
