---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/CompositePage.html
archived_at: '2026-07-15T07:23:26.427613Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| debug.h | debug.h | debug.h | debug.h | debug.h |

|  |  |
| --- | --- |
| __Includes:__ | <assert.h>  <limits.h>  "wx/wxchar.h"  <cassert>  <stddef.h>  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/type_traits/index.html#//apple_ref/doc/header/type_traits.h)  <debug/support.h>  <cassert>  <stddef.h>  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/type_traits/index.html#//apple_ref/doc/header/type_traits.h)  <cassert>  <stddef.h>  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/cpp_type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/cpp_type_traits/index.html#//apple_ref/doc/header/cpp_type_traits.h) |

## Introduction

---

## Functions

**[__check_dereferenceable](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5rwqzldnnpwizlsmvtgk4tfnzrwkylcnrsv6rcpjzkeyskojnpta6bsmi3dezlfgi2a)**
:

**[__check_dereferenceable(_Iterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5rwqzldnnpwizlsmvtgk4tfnzrwkylcnrsv6rcpjzkeyskojnpta6bsmi3demrqmfrq)**
:

**[__check_dereferenceable(const _Tp \*)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5rwqzldnnpwizlsmvtgk4tfnzrwkylcnrsv6rcpjzkeyskojnpta6bsmi3deylbha2a)**
:

**[__check_singular(const _Safe_iterator _Iterator _Sequence &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5rwqzldnnpxg2lom52wyylsl5ce6tsujreu4s27gb4deyrwgbrtknrq)**
:

**[__check_singular(const _Tp \*)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5rwqzldnnpxg2lom52wyylsl5ce6tsujreu4s27gb4deyrwgfqtknju)**
:

**[__check_string(const _CharT \*)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5rwqzldnnpxg5dsnfxgox2ej5hfitcjjzfv6mdygjrdmn3cgrsdq)**
:

**[__check_string(const _CharT \*, const _Integer &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5rwqzldnnpxg5dsnfxgox2ej5hfitcjjzfv6mdygjrdmnzxhaygg)**
:

**[__valid_range](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l53gc3djmrpxeylom5sv6rcpjzkeyskojnpta6bsmi3dmntemy4a)**
:

**[__valid_range_aux](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l53gc3djmrpxeylom5sv6ylvpbpuit2okrgestsll4yhqmtcgy2ggmrrmm)**
:

**[__valid_range_aux2(const _InputIterator, const _InputIterator, std ::)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l53gc3djmrpxeylom5sv6ylvpazf6rcpjzkeyskojnpta6bsmi3dindbme4a)**
:

**[__valid_range_aux2(const _RandomAccessIterator &, const _RandomAccessIterator &, std ::)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l53gc3djmrpxeylom5sv6ylvpazf6rcpjzkeyskojnpta6bsmi3dgnzumi2a)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __check_dereferenceable | __check_dereferenceable | __check_dereferenceable | __check_dereferenceable | __check_dereferenceable |

---

```
template<typename _Iterator, typename _Sequence> inline bool __check_dereferenceable(
    const _Safe_iterator<_Iterator, _Sequence>& __x)
```

##### Discussion

Safe iterators know if they are singular.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __check_dereferenceable(_Iterator) | __check_dereferenceable(_Iterator) | __check_dereferenceable(_Iterator) | __check_dereferenceable(_Iterator) | __check_dereferenceable(_Iterator) |

---

```
template<typename _Iterator> inline bool __check_dereferenceable(
    _Iterator&)
```

##### Discussion

Assume that some arbitrary iterator is dereferenceable, because we
can't prove that it isn't.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __check_dereferenceable(const _Tp \*) | __check_dereferenceable(const _Tp \*) | __check_dereferenceable(const _Tp \*) | __check_dereferenceable(const _Tp \*) | __check_dereferenceable(const _Tp \*) |

---

```
template<typename _Tp> inline bool __check_dereferenceable(
    const _Tp*__ptr)
```

##### Discussion

Non-NULL pointers are dereferenceable.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __check_singular(const _Safe_iterator _Iterator _Sequence &) | __check_singular(const _Safe_iterator _Iterator _Sequence &) | __check_singular(const _Safe_iterator _Iterator _Sequence &) | __check_singular(const _Safe_iterator _Iterator _Sequence &) | __check_singular(const _Safe_iterator _Iterator _Sequence &) |

---

```
template<typename _Iterator, typename _Sequence> inline bool __check_singular(
    const _Safe_iterator<_Iterator, _Sequence>& __x)
```

##### Discussion

Safe iterators know if they are singular.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __check_singular(const _Tp \*) | __check_singular(const _Tp \*) | __check_singular(const _Tp \*) | __check_singular(const _Tp \*) | __check_singular(const _Tp \*) |

---

```
template<typename _Tp> inline bool __check_singular(
    const _Tp*__ptr)
```

##### Discussion

Non-NULL pointers are nonsingular.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __check_string(const _CharT \*) | __check_string(const _CharT \*) | __check_string(const _CharT \*) | __check_string(const _CharT \*) | __check_string(const _CharT \*) |

---

```
template<typename _CharT> inline const _CharT* __check_string(
    const _CharT*__s)
```

##### Discussion

Checks that __s is non-NULL and then returns __s.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __check_string(const _CharT \*, const _Integer &) | __check_string(const _CharT \*, const _Integer &) | __check_string(const _CharT \*, const _Integer &) | __check_string(const _CharT \*, const _Integer &) | __check_string(const _CharT \*, const _Integer &) |

---

```
template<typename _CharT, typename _Integer> inline const _CharT* __check_string(
    const _CharT*__s,
    const _Integer& __n)
```

##### Discussion

Checks that __s is non-NULL or __n == 0, and then returns __s.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __valid_range | __valid_range | __valid_range | __valid_range | __valid_range |

---

```
template<typename _Iterator, typename _Sequence> inline bool __valid_range(
    const _Safe_iterator<_Iterator, _Sequence>& __first,
    const _Safe_iterator<_Iterator, _Sequence>& __last)
```

##### Discussion

Safe iterators know how to check if they form a valid range.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __valid_range_aux | __valid_range_aux | __valid_range_aux | __valid_range_aux | __valid_range_aux |

---

```
template<typename _Integral> inline bool __valid_range_aux(
    const _Integral&,
    const _Integral&,
    __true_type)
```

##### Discussion

We say that integral types for a valid range, and defer to other
routines to realize what to do with integral types instead of
iterators.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __valid_range_aux2(const _InputIterator, const _InputIterator, std ::) | __valid_range_aux2(const _InputIterator, const _InputIterator, std ::) | __valid_range_aux2(const _InputIterator, const _InputIterator, std ::) | __valid_range_aux2(const _InputIterator, const _InputIterator, std ::) | __valid_range_aux2(const _InputIterator, const _InputIterator, std ::) |

---

```
template<typename _InputIterator> inline bool __valid_range_aux2(
    const _InputIterator&,
    const _InputIterator&,
    std::input_iterator_tag)
```

##### Discussion

Can't test for a valid range with input iterators, because
iteration may be destructive. So we just assume that the range
is valid.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __valid_range_aux2(const _RandomAccessIterator &, const _RandomAccessIterator &, std ::) | __valid_range_aux2(const _RandomAccessIterator &, const _RandomAccessIterator &, std ::) | __valid_range_aux2(const _RandomAccessIterator &, const _RandomAccessIterator &, std ::) | __valid_range_aux2(const _RandomAccessIterator &, const _RandomAccessIterator &, std ::) | __valid_range_aux2(const _RandomAccessIterator &, const _RandomAccessIterator &, std ::) |

---

```
template<typename _RandomAccessIterator> inline bool __valid_range_aux2(
    const _RandomAccessIterator& __first,
    const _RandomAccessIterator& __last,
    std::random_access_iterator_tag)
```

##### Discussion

If the distance between two random access iterators is
nonnegative, assume the range is valid.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __valid_range | __valid_range | __valid_range | __valid_range | __valid_range |

---

```
template<typename _InputIterator> inline bool __valid_range(
    const _InputIterator& __first,
    const _InputIterator& __last)
```

##### Discussion

Don't know what these iterators are, or if they are even
iterators (we may get an integral type for InputIterator), so
see if they are integral and pass them on to the next phase
otherwise.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __valid_range_aux | __valid_range_aux | __valid_range_aux | __valid_range_aux | __valid_range_aux |

---

```
template<typename _InputIterator> inline bool __valid_range_aux(
    const _InputIterator& __first,
    const _InputIterator& __last,
    __false_type)
```

##### Discussion

We have iterators, so figure out what kind of iterators that are
to see if we can check the range ahead of time.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_erase | __glibcxx_check_erase | __glibcxx_check_erase | __glibcxx_check_erase | __glibcxx_check_erase |

---

```
#define __glibcxx_check_erase(
    _Position) \ do {
    \ if (
    ! (
    _Position._M_dereferenceable(
    ))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_erase_bad) \ ._M_sequence(
    *this, "this") \ ._M_iterator(
    _Position, #_Position)._M_error(
    ); \
} while (
    false); \ do {
    \ if (
    ! (
    _Position._M_attached_to(
    this))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_erase_different) \ ._M_sequence(
    *this, "this") \ ._M_iterator(
    _Position, #_Position)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that we can erase the element referenced by the iterator
_Position. We can erase the element if the _Position iterator is
dereferenceable and references this sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_erase_range | __glibcxx_check_erase_range | __glibcxx_check_erase_range | __glibcxx_check_erase_range | __glibcxx_check_erase_range |

---

```
#define __glibcxx_check_erase_range(
    _First,_Last) \ __glibcxx_check_valid_range(
    _First,_Last); \ do {
    \ if (
    ! (
    _First._M_attached_to(
    this))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_erase_different) \ ._M_sequence(
    *this, "this") \ ._M_iterator(
    _First, #_First) \ ._M_iterator(
    _Last, #_Last)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that we can erase the elements in the iterator range
[_First, _Last). We can erase the elements if [_First, _Last) is a
valid iterator range within this sequence.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_heap_pred | __glibcxx_check_heap_pred | __glibcxx_check_heap_pred | __glibcxx_check_heap_pred | __glibcxx_check_heap_pred |

---

```
#define __glibcxx_check_heap_pred(
    _First,_Last,_Pred) \ __glibcxx_check_valid_range(
    _First,_Last); \ do {
    \ if (
    ! (
    ::std::__is_heap(
    _First, _Last, _Pred))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_not_heap_pred) \ ._M_iterator(
    _First, #_First) \ ._M_iterator(
    _Last, #_Last) \ ._M_string(
    #_Pred)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that the iterator range [_First, _Last) is a heap
w.r.t. the predicate _Pred.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_insert | __glibcxx_check_insert | __glibcxx_check_insert | __glibcxx_check_insert | __glibcxx_check_insert |

---

```
#define __glibcxx_check_insert(
    _Position) \ do {
    \ if (
    ! (
    !_Position._M_singular(
    ))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_insert_singular) \ ._M_sequence(
    *this, "this") \ ._M_iterator(
    _Position, #_Position)._M_error(
    ); \
} while (
    false); \ do {
    \ if (
    ! (
    _Position._M_attached_to(
    this))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_insert_different) \ ._M_sequence(
    *this, "this") \ ._M_iterator(
    _Position, #_Position)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that we can insert into \*this with the iterator _Position.
Insertion into a container at a specific position requires that
the iterator be nonsingular (i.e., either dereferenceable or
past-the-end) and that it reference the sequence we are inserting
into. Note that this macro is only valid when the container is a
_Safe_sequence and the iterator is a _Safe_iterator.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_insert_range | __glibcxx_check_insert_range | __glibcxx_check_insert_range | __glibcxx_check_insert_range | __glibcxx_check_insert_range |

---

```
#define __glibcxx_check_insert_range(
    _Position,_First,_Last) \ __glibcxx_check_valid_range(
    _First,_Last); \ do {
    \ if (
    ! (
    !_Position._M_singular(
    ))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_insert_singular) \ ._M_sequence(
    *this, "this") \ ._M_iterator(
    _Position, #_Position)._M_error(
    ); \
} while (
    false); \ do {
    \ if (
    ! (
    _Position._M_attached_to(
    this))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_insert_different) \ ._M_sequence(
    *this, "this") \ ._M_iterator(
    _Position, #_Position)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that we can insert the values in the iterator range
[_First, _Last) into \*this with the iterator _Position. Insertion
into a container at a specific position requires that the iterator
be nonsingular (i.e., either dereferenceable or past-the-end),
that it reference the sequence we are inserting into, and that the
iterator range [_First, Last) is a valid (possibly empty)
range. Note that this macro is only valid when the container is a
_Safe_sequence and the iterator is a _Safe_iterator.

@tbd We would like to be able to check for noninterference of
_Position and the range [_First, _Last), but that can't (in
general) be done.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_partitioned | __glibcxx_check_partitioned | __glibcxx_check_partitioned | __glibcxx_check_partitioned | __glibcxx_check_partitioned |

---

```
#define __glibcxx_check_partitioned(
    _First,_Last,_Value) \ __glibcxx_check_valid_range(
    _First,_Last); \ do {
    \ if (
    ! (
    ::__gnu_debug::__check_partitioned(
    _First, _Last, \ _Value))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_unpartitioned) \ ._M_iterator(
    _First, #_First) \ ._M_iterator(
    _Last, #_Last) \ ._M_string(
    #_Value)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that the iterator range [_First, _Last) is partitioned
w.r.t. the value _Value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_partitioned_pred | __glibcxx_check_partitioned_pred | __glibcxx_check_partitioned_pred | __glibcxx_check_partitioned_pred | __glibcxx_check_partitioned_pred |

---

```
#define __glibcxx_check_partitioned_pred(
    _First,_Last,_Value,_Pred) \ __glibcxx_check_valid_range(
    _First,_Last); \ do {
    \ if (
    ! (
    ::__gnu_debug::__check_partitioned(
    _First, _Last, \ _Value, _Pred))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_unpartitioned_pred) \ ._M_iterator(
    _First, #_First) \ ._M_iterator(
    _Last, #_Last) \ ._M_string(
    #_Pred) \ ._M_string(
    #_Value)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that the iterator range [_First, _Last) is partitioned
w.r.t. the value _Value and predicate _Pred.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __glibcxx_check_sorted_pred | __glibcxx_check_sorted_pred | __glibcxx_check_sorted_pred | __glibcxx_check_sorted_pred | __glibcxx_check_sorted_pred |

---

```
#define __glibcxx_check_sorted_pred(
    _First,_Last,_Pred) \ __glibcxx_check_valid_range(
    _First,_Last); \ __glibcxx_check_strict_weak_ordering_pred(
    _First,_Last,_Pred); \ do {
    \ if (
    ! (
    ::__gnu_debug::__check_sorted(
    _First, _Last, _Pred))) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ . \ _M_message(
    ::__gnu_debug::__msg_unsorted_pred) \ ._M_iterator(
    _First, #_First) \ ._M_iterator(
    _Last, #_Last) \ ._M_string(
    #_Pred)._M_error(
    ); \
} while (
    false)
```

##### Discussion

Verify that the iterator range [_First, _Last) is sorted by the
predicate _Pred.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _GLIBCXX_DEBUG_VERIFY | _GLIBCXX_DEBUG_VERIFY | _GLIBCXX_DEBUG_VERIFY | _GLIBCXX_DEBUG_VERIFY | _GLIBCXX_DEBUG_VERIFY |

---

```
#define _GLIBCXX_DEBUG_VERIFY(
    _Condition,_ErrorMessage) \ do {
    \ if (
    ! (
    _Condition)) \ ::__gnu_debug::_Error_formatter::_M_at(
    __FILE__, __LINE__) \ ._ErrorMessage._M_error(
    ); \
} while (
    false)
```

##### Discussion

Macros used by the implementation to verify certain
properties. These macros may only be used directly by the debug
wrappers. Note that these are macros (instead of the more obviously
"correct" choice of making them functions) because we need line and
file information at the call site, to minimize the distance between
the user error and where the error is reported.

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
