---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/mt_allocator/CompositePage.html
archived_at: '2026-07-15T07:23:27.368362Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ext/mt_allocator.h | ext/mt_allocator.h | ext/mt_allocator.h | ext/mt_allocator.h | ext/mt_allocator.h |

|  |  |
| --- | --- |
| __Includes:__ | <new>  <cstdlib>  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  <bits/gthr.h>  [<bits/atomicity.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/atomicity/index.html#//apple_ref/doc/header/atomicity.h)  <new>  <cstdlib>  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  <bits/gthr.h>  [<bits/atomicity.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/atomicity/index.html#//apple_ref/doc/header/atomicity.h) |

## Introduction

This file is a GNU extension to the Standard C++ Library.

---

## Classes

**[__pool](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/mt_allocator/Classes/_pool/index.html#//apple_ref/cpp/cl/__pool)**
:

---

## Functions

**[operator rebind](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf64tfmjuw4zc7irhu4vcmjfhewxzqpazgem3cmyydcma)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator rebind | operator rebind | operator rebind | operator rebind | operator rebind |

---

```swift
template<typename _Tp, typename _Poolp = __common_pool_policy<__pool, __thread_default> > class __mt_alloc : public __mt_alloc_base<_Tp> {
        public: typedef size_t size_type;
        typedef ptrdiff_t difference_type;
        typedef _Tp* pointer;
        typedef const _Tp* const_pointer;
        typedef _Tp& reference;
        typedef const _Tp& const_reference;
        typedef _Tp value_type;
        typedef _Poolp __policy_type;
        typedef typename _Poolp::pool_type __pool_type;
        template<typename _Tp1, typename _Poolp1 = _Poolp> struct rebind {
            typedef typename _Poolp1::template _M_rebind<_Tp1>::other pol_type;
            typedef __mt_alloc<_Tp1, pol_type> other;
                };
        __mt_alloc() throw() {
            __policy_type::_S_get_pool();
                }  __mt_alloc(
            const __mt_alloc&) throw() {
            __policy_type::_S_get_pool();
                }  template<typename _Tp1, typename _Poolp1> __mt_alloc(
            const __mt_alloc<_Tp1, _Poolp1>& obj) throw() {
            __policy_type::_S_get_pool();
                }  ~__mt_alloc() throw() {
                }  pointer allocate(
            size_type __n,
            const void* = 0);
        void deallocate(
            pointer __p,
            size_type __n);
        const __pool_base::_Tune _M_get_options() {
            // Return a copy, not a reference, for external consumption.
            return __policy_type::_S_get_pool()._M_get_options();
                }  void _M_set_options(__pool_base::_Tune __t) {
            __policy_type::_S_get_pool()._M_set_options(
                __t);
                }
        };  template<typename _Tp, typename _Poolp> typename __mt_alloc<_Tp, _Poolp>::pointer __mt_alloc<_Tp, _Poolp>:: allocate(size_type __n, const void*) {
        if (
            __builtin_expect(
                __n > this->max_size(),
                false)) std::__throw_bad_alloc();
        __policy_type::_S_initialize_once();
        // Requests larger than _M_max_bytes are handled by operator
        // new/delete directly.
        __pool_type& __pool = __policy_type::_S_get_pool();
        const size_t __bytes = __n * sizeof(
            _Tp);
        if (__pool._M_check_threshold(
                __bytes)) {
            void* __ret = ::operator new(
                __bytes);
            return static_cast<_Tp*>(
                __ret);
                }  // Round up to power of 2 and figure out which bin to use.
        const size_t __which = __pool._M_get_binmap(
            __bytes);
        const size_t __thread_id = __pool._M_get_thread_id();
        // Find out if we have blocks on our freelist. If so, go ahead
        // and use them directly without having to lock anything.
        char* __c;
        typedef typename __pool_type::_Bin_record _Bin_record;
        const _Bin_record& __bin = __pool._M_get_bin(
            __which);
        if (
            __bin._M_first[__thread_id])
```

##### Discussion

@brief This is a fixed size (power of 2) allocator which - when
compiled with thread support - will maintain one freelist per
size per thread plus a "global" one. Steps are taken to limit
the per thread freelist sizes (by returning excess back to
the "global" list).

Further details:
http://gcc.gnu.org/onlinedocs/libstdc++/ext/mt_allocator.html

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
