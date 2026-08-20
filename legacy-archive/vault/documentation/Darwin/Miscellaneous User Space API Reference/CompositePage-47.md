---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bitmap_allocator/CompositePage.html
archived_at: '2026-07-15T07:23:26.094042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ext/bitmap_allocator.h | ext/bitmap_allocator.h | ext/bitmap_allocator.h | ext/bitmap_allocator.h | ext/bitmap_allocator.h |

|  |  |
| --- | --- |
| __Includes:__ | <cstddef>  <utility>  <algorithm>  <vector>  <functional>  <new>  <bits/gthr.h>  [<ext/new_allocator.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/new_allocator/index.html#//apple_ref/doc/header/new_allocator.h)  <cassert>  <cstddef>  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  <utility>  <functional>  <new>  <bits/gthr.h>  <cassert> |

## Introduction

This file is a GNU extension to the Standard C++ Library.

---

## Classes

**[__mini_vector](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bitmap_allocator/Classes/_mini_vector/index.html#//apple_ref/cpp/cl/__mini_vector)**
:

**[_Auto_Lock](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bitmap_allocator/Classes/_Auto_Lock/index.html#//apple_ref/cpp/cl/_Auto_Lock)**
:

**[_Lock](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bitmap_allocator/Classes/_Lock/index.html#//apple_ref/cpp/cl/_Lock)**
:

**[_Mutex](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bitmap_allocator/Classes/_Mutex/index.html#//apple_ref/cpp/cl/_Mutex)**
:

**[operator _Ffit_finder](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bitmap_allocator/Classes/operator_Ffit_finder/index.html#//apple_ref/cpp/cl/operator__Ffit_finder)**
:

---

## Functions

**[__num_bitmaps](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5xhk3k7mjuxi3lbobzq)**
:

**[__num_blocks](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5xhk3k7mjwg6y3lom)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __num_bitmaps | __num_bitmaps | __num_bitmaps | __num_bitmaps | __num_bitmaps |

---

```
template<typename _AddrPair> inline size_t __num_bitmaps(
    _AddrPair __ap)
```

##### Discussion

@brief The number of Bit-maps pointed to by the address pair
passed to the function.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __num_blocks | __num_blocks | __num_blocks | __num_blocks | __num_blocks |

---

```
template<typename _AddrPair> inline size_t __num_blocks(
    _AddrPair __ap)
```

##### Discussion

@brief The number of Blocks pointed to by the address pair
passed to the function.

## Constants

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __threads_enabled | __threads_enabled | __threads_enabled | __threads_enabled | __threads_enabled |

---

```
bool const __threads_enabled = __gthread_active_p();
```

##### Discussion

@brief If true, then the application being compiled will be
using threads, so use mutexes as a synchronization primitive,
else do no use any synchronization primitives.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _BALLOC_ALIGN_BYTES | _BALLOC_ALIGN_BYTES | _BALLOC_ALIGN_BYTES | _BALLOC_ALIGN_BYTES | _BALLOC_ALIGN_BYTES |

---

```
#define _BALLOC_ALIGN_BYTES 8
```

##### Discussion

@brief The constant in the expression below is the alignment
required in bytes.

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
