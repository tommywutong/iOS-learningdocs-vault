---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_deque/CompositePage.html
archived_at: '2026-07-15T07:23:28.183414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_deque.h | stl_deque.h | stl_deque.h | stl_deque.h | stl_deque.h |

|  |  |
| --- | --- |
| __Includes:__ | [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  <debug/support.h>  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Classes

**[_Deque_base](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_deque/Classes/_Deque_base/index.html#//apple_ref/cpp/cl/_Deque_base_DONTLINK_0x2f0fd7e4)**
:

---

## Functions

**[__deque_buf_size](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5sgk4lvmvpwe5lgl5zws6tfl5ce6tsujreu4s27gb4dezrqg44gimju)**
:

**[_M_initialize_map](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27jvpws3tjoruwc3djpjsv63lbobpuit2okrgestsll4yhqmtggbrginrygq)**
:

**[operator _Deque_iterator](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf6x2emvyxkzk7nf2gk4tborxxex2ej5hfitcjjzfv6mdygjtdan3bmzsti)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __deque_buf_size | __deque_buf_size | __deque_buf_size | __deque_buf_size | __deque_buf_size |

---

```
inline size_t __deque_buf_size(
    size_t __size)
```

##### Parameters

**`size`**
: The size of an element.

##### Return Value

The number (not byte size) of elements per node.

This function started off as a compiler kludge from SGI, but seems to
be a useful wrapper around a repeated constant expression. The '512' is
tuneable (and no other code needs to change), but no investigation has
been done since inheriting the SGI code.
@endif

##### Discussion

@if maint
@brief This function controls the size of memory nodes.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _M_initialize_map | _M_initialize_map | _M_initialize_map | _M_initialize_map | _M_initialize_map |

---

```
template<typename _Tp, typename _Alloc> void _Deque_base<_Tp, _Alloc>:: _M_initialize_map(
    size_t __num_elements)
```

##### Parameters

**`num_elements`**
: The count of T's for which to allocate space
at first.

##### Return Value

Nothing.

The initial underlying memory layout is a bit complicated...
@endif

##### Discussion

@if maint
@brief Layout storage.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator _Deque_iterator | operator _Deque_iterator | operator _Deque_iterator | operator _Deque_iterator | operator _Deque_iterator |

---

```
template<typename _Tp, typename _Ref, typename _Ptr> struct _Deque_iterator {
    typedef _Deque_iterator<_Tp, _Tp&, _Tp*> iterator;
    typedef _Deque_iterator<_Tp, const _Tp&, const _Tp*> const_iterator;
    static size_t _S_buffer_size() {
        return __deque_buf_size(
            sizeof(
                _Tp));
        }  typedef random_access_iterator_tag iterator_category;
    typedef _Tp value_type;
    typedef _Ptr pointer;
    typedef _Ref reference;
    typedef size_t size_type;
    typedef ptrdiff_t difference_type;
    typedef _Tp** _Map_pointer;
    typedef _Deque_iterator _Self;
    _Tp*_M_cur;
    _Tp*_M_first;
    _Tp*_M_last;
    _Map_pointer _M_node;
    _Deque_iterator(
        _Tp* __x,
        _Map_pointer __y) : _M_cur(
        __x), _M_first(
        *__y), _M_last(
        *__y + _S_buffer_size()), _M_node(__y) {
        }  _Deque_iterator() : _M_cur(0), _M_first(0), _M_last(0), _M_node(0) {
        }  _Deque_iterator(
        const iterator& __x) : _M_cur(
        __x._M_cur), _M_first(
        __x._M_first), _M_last(
        __x._M_last), _M_node(__x._M_node) {
        }  reference operator*() const ;
```

##### Discussion

@brief A deque::iterator.

Quite a bit of intelligence here. Much of the functionality of
deque is actually passed off to this class. A deque holds two
of these internally, marking its valid range. Access to
elements is done as offsets of either of those two, relying on
operator overloading in this class.

@if maint
All the functions are op overloads except for _M_set_node.
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
