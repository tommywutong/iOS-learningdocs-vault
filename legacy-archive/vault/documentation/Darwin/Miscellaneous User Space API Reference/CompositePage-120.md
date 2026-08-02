---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_algobase/CompositePage.html
archived_at: '2026-07-15T07:23:28.077405Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_algobase.h | stl_algobase.h | stl_algobase.h | stl_algobase.h | stl_algobase.h |

|  |  |
| --- | --- |
| __Includes:__ | <bits/c++config.h>  <cstring>  <climits>  <cstdlib>  <cstddef>  <iosfwd>  [<bits/stl_pair.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_pair/index.html#//apple_ref/doc/header/stl_pair.h)  [<bits/cpp_type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/cpp_type_traits/index.html#//apple_ref/doc/header/cpp_type_traits.h)  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  [<bits/stl_iterator.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/index.html#//apple_ref/doc/header/stl_iterator.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  <bits/c++config.h>  <cstring>  <climits>  <cstdlib>  <cstddef>  <new>  <iosfwd>  [<bits/stl_pair.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_pair/index.html#//apple_ref/doc/header/stl_pair.h)  [<bits/type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/type_traits/index.html#//apple_ref/doc/header/type_traits.h)  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  [<bits/stl_iterator.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/index.html#//apple_ref/doc/header/stl_iterator.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  <bits/c++config.h>  <cstring>  <climits>  <cstdlib>  <cstddef>  <iosfwd>  [<bits/stl_pair.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_pair/index.html#//apple_ref/doc/header/stl_pair.h)  [<bits/cpp_type_traits.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/cpp_type_traits/index.html#//apple_ref/doc/header/cpp_type_traits.h)  [<bits/stl_iterator_base_types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/index.html#//apple_ref/doc/header/stl_iterator_base_types.h)  [<bits/stl_iterator_base_funcs.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_funcs/index.html#//apple_ref/doc/header/stl_iterator_base_funcs.h)  [<bits/stl_iterator.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/index.html#//apple_ref/doc/header/stl_iterator.h)  [<bits/concept_check.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/concept_check/index.html#//apple_ref/doc/header/concept_check.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Functions

**[copy](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3dn5yhsx2ej5hfitcjjzfv6mdygjstayrxmuzwg)**
:

**[copy_backward](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3dn5yhsx3cmfrww53bojsf6rcpjzkeyskojnpta6bsmuyggzjqga2a)**
:

**[equal(_InputIterator1, _InputIterator1, _InputIterator2)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3fof2wc3c7irhu4vcmjfhewxzqpazgkmjsheyteyy)**
:

**[equal(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3fof2wc3c7irhu4vcmjfhewxzqpazgkmjthaydayy)**
:

**[fill](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfwgyx2ej5hfitcjjzfv6mdygjstcmbrguyti)**
:

**[fill_n](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfwgyx3ol5ce6tsujreu4s27gb4dezjrga3gcnzq)**
:

**[lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3mmv4gsy3pm5zgc4dinfrwc3c7mnxw24dbojsv6rcpjzkeyskojnpta6bsmu3ginbrmm4a)**
:

**[lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3mmv4gsy3pm5zgc4dinfrwc3c7mnxw24dbojsv6rcpjzkeyskojnpta6bsmu3gmmddgu2a)**
:

**[max(const _Tp &, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmf4f6rcpjzkeyskojnpta6bsmqztintegzrq)**
:

**[max(const _Tp &, const _Tp &, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmf4f6rcpjzkeyskojnpta6bsmuygcylegzrq)**
:

**[min(const _Tp &, const _Tp &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nnfxf6rcpjzkeyskojnpta6bsmuygkyrymnrq)**
:

**[min(const _Tp &, const _Tp &, _Compare)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nnfxf6rcpjzkeyskojnpta6bsmuydeytbmi4a)**
:

**[mismatch(_InputIterator1, _InputIterator1, _InputIterator2)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nnfzw2ylumnuf6rcpjzkeyskojnpta6bsmuytgzjsha4a)**
:

**[mismatch(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nnfzw2ylumnuf6rcpjzkeyskojnpta6bsmuytcndfgy2a)**
:

**[swap](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3to5qxax2ej5hfitcjjzfv6mdygjstazjtme4ti)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| copy | copy | copy | copy | copy |

---

```
template<typename _InputIterator, typename _OutputIterator> inline _OutputIterator copy(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result)
```

##### Parameters

**`first`**
: An input iterator.

**`last`**
: An input iterator.

**`result`**
: An output iterator.

##### Return Value

result + (first - last)

This inline function will boil down to a call to @c memmove whenever
possible. Failing that, if random access iterators are passed, then the
loop count will be known (and therefore a candidate for compiler
optimizations such as unrolling). Result may not be contained within
[first,last); the copy_backward function should be used instead.

Note that the end of the output range is permitted to be contained
within [first,last).

##### Discussion

@brief Copies the range [first,last) into result.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| copy_backward | copy_backward | copy_backward | copy_backward | copy_backward |

---

```
template <typename _BI1, typename _BI2> inline _BI2 copy_backward(
    _BI1 __first,
    _BI1 __last,
    _BI2 __result)
```

##### Parameters

**`first`**
: A bidirectional iterator.

**`last`**
: A bidirectional iterator.

**`result`**
: A bidirectional iterator.

##### Return Value

result - (first - last)

The function has the same effect as copy, but starts at the end of the
range and works its way to the start, returning the start of the result.
This inline function will boil down to a call to @c memmove whenever
possible. Failing that, if random access iterators are passed, then the
loop count will be known (and therefore a candidate for compiler
optimizations such as unrolling).

Result may not be in the range [first,last). Use copy instead. Note
that the start of the output range may overlap [first,last).

##### Discussion

@brief Copies the range [first,last) into result.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| equal(_InputIterator1, _InputIterator1, _InputIterator2) | equal(_InputIterator1, _InputIterator1, _InputIterator2) | equal(_InputIterator1, _InputIterator1, _InputIterator2) | equal(_InputIterator1, _InputIterator1, _InputIterator2) | equal(_InputIterator1, _InputIterator1, _InputIterator2) |

---

```
template<typename _InputIterator1, typename _InputIterator2> inline bool equal(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2)
```

##### Parameters

**`first1`**
: An input iterator.

**`last1`**
: An input iterator.

**`first2`**
: An input iterator.

##### Return Value

A boolean true or false.

This compares the elements of two ranges using @c == and returns true or
false depending on whether all of the corresponding elements of the
ranges are equal.

##### Discussion

@brief Tests a range for element-wise equality.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| equal(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | equal(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | equal(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | equal(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | equal(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _BinaryPredicate> inline bool equal(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _BinaryPredicate __binary_pred)
```

##### Parameters

**`first1`**
: An input iterator.

**`last1`**
: An input iterator.

**`binary_pred`**
: A binary predicate functorparam first2 An input iterator.
@endlink.

##### Return Value

A boolean true or false.

This compares the elements of two ranges using the binary_pred
parameter, and returns true or
false depending on whether all of the corresponding elements of the
ranges are equal.

##### Discussion

@brief Tests a range for element-wise equality.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| fill | fill | fill | fill | fill |

---

```
template<typename _ForwardIterator, typename _Tp> void fill(
    _ForwardIterator __first,
    _ForwardIterator __last,
    const _Tp& __value)
```

##### Parameters

**`first`**
: A forward iterator.

**`last`**
: A forward iterator.

**`value`**
: A reference-to-const of arbitrary type.

##### Return Value

Nothing.

This function fills a range with copies of the same value. For one-byte
types filling contiguous areas of memory, this becomes an inline call to
@c memset.

##### Discussion

@brief Fills the range [first,last) with copies of value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| fill_n | fill_n | fill_n | fill_n | fill_n |

---

```
template<typename _OutputIterator, typename _Size, typename _Tp> _OutputIterator fill_n(
    _OutputIterator __first,
    _Size __n,
    const _Tp& __value)
```

##### Parameters

**`first`**
: An output iterator.

**`n`**
: The count of copies to perform.

**`value`**
: A reference-to-const of arbitrary type.

##### Return Value

The iterator at first+n.

This function fills a range with copies of the same value. For one-byte
types filling contiguous areas of memory, this becomes an inline call to
@c memset.

##### Discussion

@brief Fills the range [first,first+n) with copies of value.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2) |

---

```
template<typename _InputIterator1, typename _InputIterator2> bool lexicographical_compare(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2)
```

##### Parameters

**`first1`**
: An input iterator.

**`last1`**
: An input iterator.

**`first2`**
: An input iterator.

**`last2`**
: An input iterator.

##### Return Value

A boolean true or false.

"Returns true if the sequence of elements defined by the range
[first1,last1) is lexicographically less than the sequence of elements
defined by the range [first2,last2). Returns false otherwise."
(Quoted from [25.3.8]/1.) If the iterators are all character pointers,
then this is an inline call to @c memcmp.

##### Discussion

@brief Performs "dictionary" comparison on ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) | lexicographical_compare(_InputIterator1, _InputIterator1, _InputIterator2, _InputIterator2, _Compare) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _Compare> bool lexicographical_compare(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _InputIterator2 __last2,
    _Compare __comp)
```

##### Parameters

**`first1`**
: An input iterator.

**`last1`**
: An input iterator.

**`first2`**
: An input iterator.

**`comp`**
: A comparison functorparam last2 An input iterator.
@endlink.

##### Return Value

A boolean true or false.

The same as the four-parameter @c lexigraphical_compare, but uses the
comp parameter instead of @c <.

##### Discussion

@brief Performs "dictionary" comparison on ranges.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| max(const _Tp &, const _Tp &) | max(const _Tp &, const _Tp &) | max(const _Tp &, const _Tp &) | max(const _Tp &, const _Tp &) | max(const _Tp &, const _Tp &) |

---

```
template<typename _Tp> inline const _Tp& max(
    const _Tp& __a,
    const _Tp& __b)
```

##### Parameters

**`a`**
: A thing of arbitrary type.

**`b`**
: Another thing of arbitrary type.

##### Return Value

The greater of the parameters.

This is the simple classic generic implementation. It will work on
temporary expressions, since they are only evaluated once, unlike a
preprocessor macro.

##### Discussion

@brief This does what you think it does.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| max(const _Tp &, const _Tp &, _Compare) | max(const _Tp &, const _Tp &, _Compare) | max(const _Tp &, const _Tp &, _Compare) | max(const _Tp &, const _Tp &, _Compare) | max(const _Tp &, const _Tp &, _Compare) |

---

```
template<typename _Tp, typename _Compare> inline const _Tp& max(
    const _Tp& __a,
    const _Tp& __b,
    _Compare __comp)
```

##### Parameters

**`a`**
: A thing of arbitrary type.

**`comp`**
: A comparison functorparam b Another thing of arbitrary type.
@endlink.

##### Return Value

The greater of the parameters.

This will work on temporary expressions, since they are only evaluated
once, unlike a preprocessor macro.

##### Discussion

@brief This does what you think it does.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| min(const _Tp &, const _Tp &) | min(const _Tp &, const _Tp &) | min(const _Tp &, const _Tp &) | min(const _Tp &, const _Tp &) | min(const _Tp &, const _Tp &) |

---

```
template<typename _Tp> inline const _Tp& min(
    const _Tp& __a,
    const _Tp& __b)
```

##### Parameters

**`a`**
: A thing of arbitrary type.

**`b`**
: Another thing of arbitrary type.

##### Return Value

The lesser of the parameters.

This is the simple classic generic implementation. It will work on
temporary expressions, since they are only evaluated once, unlike a
preprocessor macro.

##### Discussion

@brief This does what you think it does.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| min(const _Tp &, const _Tp &, _Compare) | min(const _Tp &, const _Tp &, _Compare) | min(const _Tp &, const _Tp &, _Compare) | min(const _Tp &, const _Tp &, _Compare) | min(const _Tp &, const _Tp &, _Compare) |

---

```
template<typename _Tp, typename _Compare> inline const _Tp& min(
    const _Tp& __a,
    const _Tp& __b,
    _Compare __comp)
```

##### Parameters

**`a`**
: A thing of arbitrary type.

**`comp`**
: A comparison functorparam b Another thing of arbitrary type.
@endlink.

##### Return Value

The lesser of the parameters.

This will work on temporary expressions, since they are only evaluated
once, unlike a preprocessor macro.

##### Discussion

@brief This does what you think it does.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| mismatch(_InputIterator1, _InputIterator1, _InputIterator2) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2) |

---

```
template<typename _InputIterator1, typename _InputIterator2> pair<_InputIterator1, _InputIterator2> mismatch(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2)
```

##### Parameters

**`first1`**
: An input iterator.

**`last1`**
: An input iterator.

**`first2`**
: An input iterator.

##### Return Value

A pair of iterators pointing to the first mismatch.

This compares the elements of two ranges using @c == and returns a pair
of iterators. The first iterator points into the first range, the
second iterator points into the second range, and the elements pointed
to by the iterators are not equal.

##### Discussion

@brief Finds the places in ranges which don't match.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| mismatch(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) | mismatch(_InputIterator1, _InputIterator1, _InputIterator2, _BinaryPredicate) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _BinaryPredicate> pair<_InputIterator1, _InputIterator2> mismatch(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _BinaryPredicate __binary_pred)
```

##### Parameters

**`first1`**
: An input iterator.

**`last1`**
: An input iterator.

**`binary_pred`**
: A binary predicate functorparam first2 An input iterator.
@endlink.

##### Return Value

A pair of iterators pointing to the first mismatch.

This compares the elements of two ranges using the binary_pred
parameter, and returns a pair
of iterators. The first iterator points into the first range, the
second iterator points into the second range, and the elements pointed
to by the iterators are not equal.

##### Discussion

@brief Finds the places in ranges which don't match.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| swap | swap | swap | swap | swap |

---

```
template<typename _Tp> inline void swap(
    _Tp& __a,
    _Tp& __b)
```

##### Parameters

**`a`**
: A thing of arbitrary type.

**`b`**
: Another thing of arbitrary type.

##### Return Value

Nothing.

This is the simple classic generic implementation. It will work on
any type which has a copy constructor and an assignment operator.

##### Discussion

@brief Swaps two values.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| iter_swap | iter_swap | iter_swap | iter_swap | iter_swap |

---

```
template<typename _ForwardIterator1, typename _ForwardIterator2> inline void iter_swap(
    _ForwardIterator1 __a,
    _ForwardIterator2 __b)
```

##### Discussion

@brief Swaps the contents of two iterators.

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
