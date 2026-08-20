---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/boost_shared_ptr/CompositePage.html
archived_at: '2026-07-15T07:23:26.123280Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| boost_memory.h | boost_memory.h | boost_memory.h | boost_memory.h | boost_memory.h |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## COM Interfaces

**[__unspecified_bool_type](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/boost_shared_ptr/Classes/_unspecified_bool_type/index.html#//apple_ref/cpp/cl/__unspecified_bool_type)**
:

---

## Functions

**[_Sp_counted_base_impl](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27knyf6y3povxhizlel5rgc43fl5uw24dm)**
:

**[const_pointer_cast](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3dn5xhg5c7obxws3tumvzf6y3bon2a)**
:

**[dynamic_pointer_cast](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3epfxgc3ljmnpxa33jnz2gk4s7mnqxg5a)**
:

**[static_pointer_cast](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3torqxi2ldl5yg62loorsxex3dmfzxi)**
:

**[swap(tr1 :: shared_ptr _Tp &, tr1 :: shared_ptr _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3to5qxax2ej5hfitcjjzfv6mdygjrdczdfhe4ta)**
:

**[swap(tr1 :: weak_ptr _Tp &, tr1 :: weak_ptr _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3to5qxax2ej5hfitcjjzfv6mdygjrdczrrmnrti)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Sp_counted_base_impl | _Sp_counted_base_impl | _Sp_counted_base_impl | _Sp_counted_base_impl | _Sp_counted_base_impl |

---

```
_Sp_counted_base_impl(
    _Ptr __p,
    _Deleter __d) : _M_ptr(
    __p), _M_del(
    __d)
```

##### Discussion

@brief
@pre d(p) must not throw.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| const_pointer_cast | const_pointer_cast | const_pointer_cast | const_pointer_cast | const_pointer_cast |

---

```
template <typename _Tp, typename _Tp1> shared_ptr<_Tp> const_pointer_cast(
    const shared_ptr<_Tp1>& __r)
```

##### Discussion

@warning The seemingly equivalent
`shared_ptr(const_cast(r.get()))`
will eventually result in undefined behaviour,
attempting to delete the same object twice.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| dynamic_pointer_cast | dynamic_pointer_cast | dynamic_pointer_cast | dynamic_pointer_cast | dynamic_pointer_cast |

---

```
template <typename _Tp, typename _Tp1> shared_ptr<_Tp> dynamic_pointer_cast(
    const shared_ptr<_Tp1>& __r)
```

##### Discussion

@warning The seemingly equivalent
`shared_ptr(dynamic_cast(r.get()))`
will eventually result in undefined behaviour,
attempting to delete the same object twice.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| static_pointer_cast | static_pointer_cast | static_pointer_cast | static_pointer_cast | static_pointer_cast |

---

```
template <typename _Tp, typename _Tp1> shared_ptr<_Tp> static_pointer_cast(
    const shared_ptr<_Tp1>& __r)
```

##### Discussion

@warning The seemingly equivalent
`shared_ptr(static_cast(r.get()))`
will eventually result in undefined behaviour,
attempting to delete the same object twice.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| swap(tr1 :: shared_ptr _Tp &, tr1 :: shared_ptr _Tp &) | swap(tr1 :: shared_ptr _Tp &, tr1 :: shared_ptr _Tp &) | swap(tr1 :: shared_ptr _Tp &, tr1 :: shared_ptr _Tp &) | swap(tr1 :: shared_ptr _Tp &, tr1 :: shared_ptr _Tp &) | swap(tr1 :: shared_ptr _Tp &, tr1 :: shared_ptr _Tp &) |

---

```
template <typename _Tp> inline void swap(
    tr1::shared_ptr<_Tp>& __a,
    tr1::shared_ptr<_Tp>& __b)
```

##### Discussion

@brief std::swap() specialisation for shared_ptr.
@relates shared_ptr.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| swap(tr1 :: weak_ptr _Tp &, tr1 :: weak_ptr _Tp &) | swap(tr1 :: weak_ptr _Tp &, tr1 :: weak_ptr _Tp &) | swap(tr1 :: weak_ptr _Tp &, tr1 :: weak_ptr _Tp &) | swap(tr1 :: weak_ptr _Tp &, tr1 :: weak_ptr _Tp &) | swap(tr1 :: weak_ptr _Tp &, tr1 :: weak_ptr _Tp &) |

---

```
template <typename _Tp> void swap(
    tr1::weak_ptr<_Tp>& __a,
    tr1::weak_ptr<_Tp>& __b)
```

##### Discussion

@brief std::swap() specialisation for weak_ptr.
@relates weak_ptr.

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
