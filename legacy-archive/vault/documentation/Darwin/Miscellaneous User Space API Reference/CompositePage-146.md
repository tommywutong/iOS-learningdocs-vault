---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_vector/CompositePage.html
archived_at: '2026-07-15T07:23:28.662235Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_vector.h | stl_vector.h | stl_vector.h | stl_vector.h | stl_vector.h |

|  |  |
| --- | --- |
| __Includes:__ | [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  <debug/support.h>  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Vector_base | _Vector_base | _Vector_base | _Vector_base | _Vector_base |

---

```swift
template<typename _Tp, typename _Alloc> struct _Vector_base {
    struct _Vector_impl : public _Alloc {
        _Tp* _M_start;
        _Tp* _M_finish;
        _Tp* _M_end_of_storage;
        _Vector_impl(
            _Alloc const& __a) : _Alloc(
            __a), _M_start(0), _M_finish(0), _M_end_of_storage(0) {
                }
        };
    public: typedef _Alloc allocator_type;
    allocator_type get_allocator() const {
        return *static_cast<const _Alloc*>(
            &this->_M_impl);
        }  _Vector_base(
        const allocator_type& __a) : _M_impl(__a) {
        }  _Vector_base(
        size_t __n,
        const allocator_type& __a) : _M_impl(__a) {
        this->_M_impl._M_start = this->_M_allocate(
            __n);
        this->_M_impl._M_finish = this->_M_impl._M_start;
        this->_M_impl._M_end_of_storage = this->_M_impl._M_start + __n;
        }  ~_Vector_base() {
        _M_deallocate(
            this->_M_impl._M_start,
            this->_M_impl._M_end_of_storage - this->_M_impl._M_start);
        }  public: _Vector_impl _M_impl;
    _Tp* _M_allocate(size_t __n) {
        return _M_impl.allocate(
            __n);
        }  void _M_deallocate(_Tp* __p, size_t __n) {
        if (
            __p) _M_impl.deallocate(
            __p,
            __n);
        }
};
```

##### Discussion

@if maint
See bits/stl_deque.h's _Deque_base for an explanation.
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
