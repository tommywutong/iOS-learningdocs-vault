---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/CompositePage.html
archived_at: '2026-07-15T07:23:28.119576Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_alloc.h | stl_alloc.h | stl_alloc.h | stl_alloc.h | stl_alloc.h |

|  |  |
| --- | --- |
| __Includes:__ | <cstddef>  <cstdlib>  <cstring>  [<bits/functexcept.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functexcept/index.html#//apple_ref/doc/header/functexcept.h)  [<bits/stl_threads.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_threads/index.html#//apple_ref/doc/header/stl_threads.h)  [<bits/atomicity.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/atomicity/index.html#//apple_ref/doc/header/atomicity.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Classes

**[__debug_alloc](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/Classes/_debug_alloc/index.html#//apple_ref/cpp/cl/__debug_alloc)**
:

**[__default_alloc_template](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/Classes/_default_alloc_template/index.html#//apple_ref/cpp/cl/__default_alloc_template)**
:

**[__malloc_alloc_template](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/Classes/_malloc_alloc_template/index.html#//apple_ref/cpp/cl/__malloc_alloc_template)**
:

**[__new_alloc](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/Classes/_new_alloc/index.html#//apple_ref/cpp/cl/__new_alloc)**
:

**[__simple_alloc](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/Classes/_simple_alloc/index.html#//apple_ref/cpp/cl/__simple_alloc)**
:

**[allocator](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/Classes/allocator/index.html#//apple_ref/cpp/cl/allocator_DONTLINK_0x16413a18)**
:

---

## Functions

**[operator ==](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_alloc/CompositePage.html#//apple_ref/c/func/operatoraa_DONTLINK_0x16465428)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator == | operator == | operator == | operator == | operator == |

---

```
template<int inst> inline bool operator==(
    const __malloc_alloc_template<inst>&,
    const __malloc_alloc_template<inst>&)
```

##### Discussion

Comparison operators for all of the predifined SGI-style allocators.
This ensures that __allocator (for example) will work
correctly. As required, all allocators compare equal.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Alloc_traits | _Alloc_traits | _Alloc_traits | _Alloc_traits | _Alloc_traits |

---

```
// The fully general version.
template<typename _Tp, typename _Allocator> struct _Alloc_traits {
    static const bool _S_instanceless = false;
    typedef typename _Allocator::template rebind<_Tp>::other allocator_type;
};
```

##### Discussion

@if maint
Another allocator adaptor: _Alloc_traits. This serves two purposes.
First, make it possible to write containers that can use either "SGI"
style allocators or "standard" allocators. Second, provide a mechanism
so that containers can query whether or not the allocator has distinct
instances. If not, the container can avoid wasting a word of memory to
store an empty object. For examples of use, see stl_vector.h, etc, or
any of the other classes derived from this one.

This adaptor uses partial specialization. The general case of
_Alloc_traits<_Tp, _Alloc> assumes that _Alloc is a
standard-conforming allocator, possibly with non-equal instances and
non-static members. (It still behaves correctly even if _Alloc has
static member and if all instances are equal. Refinements affect
performance, not correctness.)

There are always two members: allocator_type, which is a standard-
conforming allocator type for allocating objects of type _Tp, and
_S_instanceless, a static const member of type bool. If
_S_instanceless is true, this means that there is no difference
between any two instances of type allocator_type. Furthermore, if
_S_instanceless is true, then _Alloc_traits has one additional
member: _Alloc_type. This type encapsulates allocation and
deallocation of objects of type _Tp through a static interface; it
has two member functions, whose signatures are

- static _Tp\* allocate(size_t)
- static void deallocate(_Tp\*, size_t)

The size_t parameters are "standard" style (see top of stl_alloc.h) in
that they take counts, not sizes.

@endif
(See allocators info @endlink for more.)

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __allocator | __allocator | __allocator | __allocator | __allocator |

---

```
template<typename _Tp, typename _Alloc> struct __allocator {
    _Alloc __underlying_alloc;
    typedef size_t size_type;
    typedef ptrdiff_t difference_type;
    typedef _Tp*pointer;
    typedef const _Tp*const_pointer;
    typedef _Tp& reference;
    typedef const _Tp& const_reference;
    typedef _Tp value_type;
    template<typename _Tp1> struct rebind {
        typedef __allocator<_Tp1, _Alloc> other;
        };
    __allocator() throw() {
        } __allocator(
        const __allocator& __a) throw() : __underlying_alloc(__a.__underlying_alloc) {
        }  template<typename _Tp1> __allocator(
        const __allocator<_Tp1, _Alloc>& __a) throw() : __underlying_alloc(__a.__underlying_alloc) {
        }  ~__allocator() throw() {
        }  pointer address(
        reference __x) const {
        return &__x;
        }  const_pointer address(
        const_reference __x) const {
        return &__x;
        }  // NB: __n is permitted to be 0. The C++ standard says nothing
    // about what the return value is when __n == 0.
    _Tp* allocate(size_type __n, const void* = 0) {
        _Tp* __ret = 0;
        if (
            __n) __ret = static_cast<_Tp*>(
            _Alloc::allocate(
                __n * sizeof(
                    _Tp)));
        return __ret;
        }  // __p is not permitted to be a null pointer.
    void deallocate(pointer __p, size_type __n) {
        __underlying_alloc.deallocate(
            __p,
            __n * sizeof(
                _Tp));
        }  size_type max_size() const throw() {
        return size_t(
            -1) / sizeof(
            _Tp);
        }  void construct(pointer __p, const _Tp& __val) {
        new(
            __p) _Tp(
            __val);
        }  void destroy(pointer __p) {
        __p->~_Tp();
        }
};
```

##### Discussion

@if maint
Allocator adaptor to turn an "SGI" style allocator (e.g.,
__alloc, __malloc_alloc_template) into a "standard" conforming
allocator. Note that this adaptor does \*not\* assume that all
objects of the underlying alloc class are identical, nor does it
assume that all of the underlying alloc's member functions are
static member functions. Note, also, that __allocator<_Tp,
__alloc> is essentially the same thing as allocator<_Tp>.
@endif
(See allocators info @endlink for more.)

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
