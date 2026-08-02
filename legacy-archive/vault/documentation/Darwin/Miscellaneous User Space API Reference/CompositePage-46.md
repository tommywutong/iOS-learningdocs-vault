---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/array_allocator/CompositePage.html
archived_at: '2026-07-15T07:23:25.299470Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ext/array_allocator.h | ext/array_allocator.h | ext/array_allocator.h | ext/array_allocator.h | ext/array_allocator.h |

|  |  |
| --- | --- |
| __Includes:__ | <cstddef>  <new>  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  <tr1/array> |

## Introduction

This file is a GNU extension to the Standard C++ Library.

---

## Functions

**[operator rebind](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf64tfmjuw4za)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator rebind | operator rebind | operator rebind | operator rebind | operator rebind |

---

```swift
template<typename _Tp, typename _Array = std::tr1::array<_Tp> > class array_allocator : public array_allocator_base<_Tp> {
        public: typedef size_t size_type;
        typedef ptrdiff_t difference_type;
        typedef _Tp* pointer;
        typedef const _Tp* const_pointer;
        typedef _Tp& reference;
        typedef const _Tp& const_reference;
        typedef _Tp value_type;
        typedef _Array array_type;
        array_type* _M_array;
        template<typename _Tp1, typename _Array1 = _Array> struct rebind {
            typedef array_allocator<_Tp1, _Array1> other;
                };
        array_allocator(
            array_type* __array = NULL) throw() : _M_array(__array) {
                }  array_allocator(
            const array_allocator& __o) throw() : _M_array(__o._M_array) {
                }  template<typename _Tp1, typename _Array1> array_allocator(
            const array_allocator<_Tp1, _Array1>&) throw() : _M_array(NULL) {
                }  ~array_allocator() throw() {
                }  pointer allocate(size_type __n, const void* = 0) {
            static size_type __array_used;
            if (
                _M_array == 0 || __array_used + __n > _M_array->size()) std::__throw_bad_alloc();
            pointer __ret = _M_array->begin() + __array_used;
            __array_used += __n;
            return __ret;
                }
        };  template<typename _Tp, typename _Array> inline bool operator==(
        const array_allocator<_Tp, _Array>&,
        const array_allocator<_Tp, _Array>&)
```

##### Discussion

@brief An allocator that uses previously allocated memory.
This memory can be externally, globally, or otherwise allocated.

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
