---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_numeric/CompositePage.html
archived_at: '2026-07-15T07:23:28.478145Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_numeric.h | stl_numeric.h | stl_numeric.h | stl_numeric.h | stl_numeric.h |

|  |  |
| --- | --- |
| __Includes:__ | [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h)  [<debug/debug.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debug/index.html#//apple_ref/doc/header/debug.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Functions

**[accumulate(_InputIterator, _InputIterator, _Tp)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3bmnrxk3lvnrqxizk7irhu4vcmjfhewxzqpazgmmbvga3dima)**
:

**[accumulate(_InputIterator, _InputIterator, _Tp, _BinaryOperation)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3bmnrxk3lvnrqxizk7irhu4vcmjfhewxzqpazgmndbmfrwima)**
:

**[adjacent_difference(_InputIterator, _InputIterator, _OutputIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3bmrvgcy3fnz2f6zdjmztgk4tfnzrwkx2ej5hfitcjjzfv6mdygjtdizjxmu2gg)**
:

**[adjacent_difference(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3bmrvgcy3fnz2f6zdjmztgk4tfnzrwkx2ej5hfitcjjzfv6mdygjtdizrqmi2di)**
:

**[inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzxgk4s7obzg6zdvmn2f6rcpjzkeyskojnpta6bsmy2genbwgzrq)**
:

**[inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp, _BinaryOperation1, _BinaryOperation2)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzxgk4s7obzg6zdvmn2f6rcpjzkeyskojnpta6bsmy2ggmjqgbrq)**
:

**[partial_sum(_InputIterator, _InputIterator, _OutputIterator)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfzhi2lbnrpxg5lnl5ce6tsujreu4s27gb4dezrumm4timry)**
:

**[partial_sum(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfzhi2lbnrpxg5lnl5ce6tsujreu4s27gb4dezrumrsdomrq)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| accumulate(_InputIterator, _InputIterator, _Tp) | accumulate(_InputIterator, _InputIterator, _Tp) | accumulate(_InputIterator, _InputIterator, _Tp) | accumulate(_InputIterator, _InputIterator, _Tp) | accumulate(_InputIterator, _InputIterator, _Tp) |

---

```
template<typename _InputIterator, typename _Tp> _Tp accumulate(
    _InputIterator __first,
    _InputIterator __last,
    _Tp __init)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

**`init`**
: Starting value to add other values to.

##### Return Value

The final sum.

##### Discussion

@brief Accumulate values in a range.

Accumulates the values in the range [first,last) using operator+(). The
initial value is @a init. The values are processed in order.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| accumulate(_InputIterator, _InputIterator, _Tp, _BinaryOperation) | accumulate(_InputIterator, _InputIterator, _Tp, _BinaryOperation) | accumulate(_InputIterator, _InputIterator, _Tp, _BinaryOperation) | accumulate(_InputIterator, _InputIterator, _Tp, _BinaryOperation) | accumulate(_InputIterator, _InputIterator, _Tp, _BinaryOperation) |

---

```
template<typename _InputIterator, typename _Tp, typename _BinaryOperation> _Tp accumulate(
    _InputIterator __first,
    _InputIterator __last,
    _Tp __init,
    _BinaryOperation __binary_op)
```

##### Parameters

**`first`**
: Start of range.

**`last`**
: End of range.

**`init`**
: Starting value to add other values to.

**`binary_op`**
: Function object to accumulate with.

##### Return Value

The final sum.

##### Discussion

@brief Accumulate values in a range with operation.

Accumulates the values in the range [first,last) using the function
object @a binary_op. The initial value is @a init. The values are
processed in order.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| adjacent_difference(_InputIterator, _InputIterator, _OutputIterator) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator) |

---

```
template<typename _InputIterator, typename _OutputIterator> _OutputIterator adjacent_difference(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result)
```

##### Parameters

**`first`**
: Start of input range.

**`last`**
: End of input range.

**`result`**
: Output to write sums to.

##### Return Value

Iterator pointing just beyond the values written to result.

##### Discussion

@brief Return differences between adjacent values.

Computes the difference between adjacent values in the range
[first,last) using operator-() and writes the result to @a result.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| adjacent_difference(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | adjacent_difference(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _BinaryOperation> _OutputIterator adjacent_difference(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    _BinaryOperation __binary_op)
```

##### Parameters

**`first`**
: Start of input range.

**`last`**
: End of input range.

**`result`**
: Output to write sums to.

##### Return Value

Iterator pointing just beyond the values written to result.

##### Discussion

@brief Return differences between adjacent values.

Computes the difference between adjacent values in the range
[first,last) using the function object @a binary_op and writes the
result to @a result.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _Tp> _Tp inner_product(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _Tp __init)
```

##### Parameters

**`first1`**
: Start of range 1.

**`last1`**
: End of range 1.

**`first2`**
: Start of range 2.

**`init`**
: Starting value to add other values to.

##### Return Value

The final inner product.

##### Discussion

@brief Compute inner product of two ranges.

Starting with an initial value of @a init, multiplies successive
elements from the two ranges and adds each product into the accumulated
value using operator+(). The values in the ranges are processed in
order.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp, _BinaryOperation1, _BinaryOperation2) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp, _BinaryOperation1, _BinaryOperation2) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp, _BinaryOperation1, _BinaryOperation2) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp, _BinaryOperation1, _BinaryOperation2) | inner_product(_InputIterator1, _InputIterator1, _InputIterator2, _Tp, _BinaryOperation1, _BinaryOperation2) |

---

```
template<typename _InputIterator1, typename _InputIterator2, typename _Tp, typename _BinaryOperation1, typename _BinaryOperation2> _Tp inner_product(
    _InputIterator1 __first1,
    _InputIterator1 __last1,
    _InputIterator2 __first2,
    _Tp __init,
    _BinaryOperation1 __binary_op1,
    _BinaryOperation2 __binary_op2)
```

##### Parameters

**`first1`**
: Start of range 1.

**`last1`**
: End of range 1.

**`first2`**
: Start of range 2.

**`init`**
: Starting value to add other values to.

**`binary_op1`**
: Function object to accumulate with.

**`binary_op2`**
: Function object to apply to pairs of input values.

##### Return Value

The final inner product.

##### Discussion

@brief Compute inner product of two ranges.

Starting with an initial value of @a init, applies @a binary_op2 to
successive elements from the two ranges and accumulates each result into
the accumulated value using @a binary_op1. The values in the ranges are
processed in order.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| partial_sum(_InputIterator, _InputIterator, _OutputIterator) | partial_sum(_InputIterator, _InputIterator, _OutputIterator) | partial_sum(_InputIterator, _InputIterator, _OutputIterator) | partial_sum(_InputIterator, _InputIterator, _OutputIterator) | partial_sum(_InputIterator, _InputIterator, _OutputIterator) |

---

```
template<typename _InputIterator, typename _OutputIterator> _OutputIterator partial_sum(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result)
```

##### Parameters

**`first`**
: Start of input range.

**`last`**
: End of input range.

**`result`**
: Output to write sums to.

##### Return Value

Iterator pointing just beyond the values written to result.

##### Discussion

@brief Return list of partial sums

Accumulates the values in the range [first,last) using operator+().
As each successive input value is added into the total, that partial sum
is written to @a result. Therefore, the first value in result is the
first value of the input, the second value in result is the sum of the
first and second input values, and so on.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| partial_sum(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | partial_sum(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | partial_sum(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | partial_sum(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) | partial_sum(_InputIterator, _InputIterator, _OutputIterator, _BinaryOperation) |

---

```
template<typename _InputIterator, typename _OutputIterator, typename _BinaryOperation> _OutputIterator partial_sum(
    _InputIterator __first,
    _InputIterator __last,
    _OutputIterator __result,
    _BinaryOperation __binary_op)
```

##### Parameters

**`first`**
: Start of input range.

**`last`**
: End of input range.

**`result`**
: Output to write sums to.

##### Return Value

Iterator pointing just beyond the values written to result.

##### Discussion

@brief Return list of partial sums

Accumulates the values in the range [first,last) using operator+().
As each successive input value is added into the total, that partial sum
is written to @a result. Therefore, the first value in result is the
first value of the input, the second value in result is the sum of the
first and second input values, and so on.

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
