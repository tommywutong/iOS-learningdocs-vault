---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_construct/CompositePage.html
archived_at: '2026-07-15T07:23:28.164675Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_construct.h | stl_construct.h | stl_construct.h | stl_construct.h | stl_construct.h |

|  |  |
| --- | --- |
| __Includes:__ | [<bits/type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/type_traits/index.html#//apple_ref/doc/header/type_traits.h)  <new>  [<bits/type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/type_traits/index.html#//apple_ref/doc/header/type_traits.h)  <new>  [<bits/cpp_type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/cpp_type_traits/index.html#//apple_ref/doc/header/cpp_type_traits.h)  <new> |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Classes

**[allocator](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_construct/Classes/allocator/index.html#//apple_ref/cpp/cl/allocator_DONTLINK_0x2f0420cc)**
:

---

## Functions

**[__destroy_aux( _ForwardIterator, _ForwardIterator, __true_type)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5sgk43uojxxsx3bov4f6rcpjzkeyskojnpta6bsmu3tayrtgi2a)**
:

**[__destroy_aux(_ForwardIterator, _ForwardIterator, __false_type)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5sgk43uojxxsx3bov4f6rcpjzkeyskojnpta6bsmuygkmdcgu2a)**
:

**[_Construct(_T1 \*)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27inxw443uoj2wg5c7irhu4vcmjfhewxzqpazgkmdemeywkma)**
:

**[_Construct(_T1 \*, const _T2 &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27inxw443uoj2wg5c7irhu4vcmjfhewxzqpazgimdfmy2dima)**
:

**[_Destroy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27irsxg5dsn54v6rcpjzkeyskojnpta6bsmuygizjqheya)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __destroy_aux( _ForwardIterator, _ForwardIterator, __true_type) | __destroy_aux( _ForwardIterator, _ForwardIterator, __true_type) | __destroy_aux( _ForwardIterator, _ForwardIterator, __true_type) | __destroy_aux( _ForwardIterator, _ForwardIterator, __true_type) | __destroy_aux( _ForwardIterator, _ForwardIterator, __true_type) |

---

```
template<typename _ForwardIterator> inline void __destroy_aux(
    _ForwardIterator,
    _ForwardIterator,
    __true_type)
```

##### Discussion

@if maint
Destroy a range of objects with trivial destructors. Since the destructors
are trivial, there's nothing to do and hopefully this function will be
entirely optimized away.

This is a helper function used only by _Destroy().
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __destroy_aux(_ForwardIterator, _ForwardIterator, __false_type) | __destroy_aux(_ForwardIterator, _ForwardIterator, __false_type) | __destroy_aux(_ForwardIterator, _ForwardIterator, __false_type) | __destroy_aux(_ForwardIterator, _ForwardIterator, __false_type) | __destroy_aux(_ForwardIterator, _ForwardIterator, __false_type) |

---

```
template<typename _ForwardIterator> inline void __destroy_aux(
    _ForwardIterator __first,
    _ForwardIterator __last,
    __false_type)
```

##### Discussion

@if maint
Destroy a range of objects with nontrivial destructors.

This is a helper function used only by _Destroy().
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Construct(_T1 \*) | _Construct(_T1 \*) | _Construct(_T1 \*) | _Construct(_T1 \*) | _Construct(_T1 \*) |

---

```
template<typename _T1> inline void _Construct(
    _T1*__p)
```

##### Discussion

@if maint
Constructs an object in existing memory by invoking an allocated
object's default constructor (no initializers).
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Construct(_T1 \*, const _T2 &) | _Construct(_T1 \*, const _T2 &) | _Construct(_T1 \*, const _T2 &) | _Construct(_T1 \*, const _T2 &) | _Construct(_T1 \*, const _T2 &) |

---

```
template<typename _T1, typename _T2> inline void _Construct(
    _T1*__p,
    const _T2& __value)
```

##### Discussion

@if maint
Constructs an object in existing memory by invoking an allocated
object's constructor with an initializer.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Destroy | _Destroy | _Destroy | _Destroy | _Destroy |

---

```
template<typename _Tp> inline void _Destroy(
    _Tp*__pointer)
```

##### Discussion

@if maint
Destroy the object pointed to by a pointer type.
@endif

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Destroy | _Destroy | _Destroy | _Destroy | _Destroy |

---

```
template<typename _ForwardIterator> inline void _Destroy(
    _ForwardIterator __first,
    _ForwardIterator __last)
```

##### Discussion

@if maint
Destroy a range of objects. If the value_type of the object has
a trivial destructor, the compiler should optimize all of this
away, otherwise the objects' destructors must be invoked.
@endif

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
