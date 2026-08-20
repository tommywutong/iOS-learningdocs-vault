---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_function/CompositePage.html
archived_at: '2026-07-15T07:23:28.265024Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_function.h | stl_function.h | stl_function.h | stl_function.h | stl_function.h |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Classes

**[binder1st](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_function/Classes/binder1st/index.html#//apple_ref/cpp/cl/binder1st_DONTLINK_0x2f1706f4)**
:

**[mem_fun_t](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_function/Classes/mem_fun_t/index.html#//apple_ref/cpp/cl/mem_fun_t_DONTLINK_0x2f19f6d8)**
:

**[pointer_to_unary_function](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_function/Classes/pointer_to_unary_function/index.html#//apple_ref/cpp/cl/pointer_to_unary_function_DONTLINK_0x2f17baa8)**
:

**[unary_negate](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_function/Classes/unary_negate/index.html#//apple_ref/cpp/cl/unary_negate_DONTLINK_0x2f1693d4)**
:

---

## Functions

**[operator _Identity](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf6x2jmrsw45djor4v6rcpjzkeyskojnpta6bsmyytoyztgiya)**
:

**[operator equal_to](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf6zlrovqwyx3un5puit2okrgestsll4yhqmtggbrtgojwmm)**
:

**[operator logical_and](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf63dpm5uwgylml5qw4zc7irhu4vcmjfhewxzqpazgmmbwg5rdama)**
:

**[operator plus](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf64dmovzv6rcpjzkeyskojnpta6bsmyyggmjwgu2a)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator _Identity | operator _Identity | operator _Identity | operator _Identity | operator _Identity |

---

```
template <class _Tp> struct _Identity : public unary_function<_Tp,_Tp> {
    _Tp& operator()(
        _Tp& __x) const ;
```

##### Discussion

@}

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator equal_to | operator equal_to | operator equal_to | operator equal_to | operator equal_to |

---

```
// 20.3.3 comparisons
/** @defgroup s20_3_3_comparisons Comparison Classes
The library provides six wrapper functors for all the basic comparisons
in C++, like @c <.

@{
    */
/// One of the @link s20_3_3_comparisons comparison functors@endlink.
template <class _Tp> struct equal_to : public binary_function<_Tp, _Tp, bool> {
    bool operator()(
        const _Tp& __x,
        const _Tp& __y) const ;
```

##### Discussion

@}

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator logical_and | operator logical_and | operator logical_and | operator logical_and | operator logical_and |

---

```
// 20.3.4 logical operations
/** @defgroup s20_3_4_logical Boolean Operations Classes
Here are wrapper functors for Boolean operations: @c &&, @c ||, and @c !.

@{
    */
/// One of the @link s20_3_4_logical Boolean operations functors@endlink.
template <class _Tp> struct logical_and : public binary_function<_Tp, _Tp, bool> {
    bool operator()(
        const _Tp& __x,
        const _Tp& __y) const ;
```

##### Discussion

@}

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator plus | operator plus | operator plus | operator plus | operator plus |

---

```
// 20.3.2 arithmetic
/** @defgroup s20_3_2_arithmetic Arithmetic Classes
Because basic math often needs to be done during an algorithm, the library
provides functors for those operations. See the documentation for
@link s20_3_1_base the base classes@endlink for examples of their use.

@{
    */
/// One of the @link s20_3_2_arithmetic math functors@endlink.
template <class _Tp> struct plus : public binary_function<_Tp, _Tp, _Tp> {
    _Tp operator()(
        const _Tp& __x,
        const _Tp& __y) const ;
```

##### Discussion

@}

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| binary_function | binary_function | binary_function | binary_function | binary_function |

---

```
template <class _Arg1, class _Arg2, class _Result> struct binary_function {
    typedef _Arg1 first_argument_type; ///< the type of the first argument
    /// (no surprises here)
    typedef _Arg2 second_argument_type; ///< the type of the second argument
    typedef _Result result_type; ///< type of the return type
};
```

##### Discussion

This is one of the functor base classes@endlink.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| unary_function | unary_function | unary_function | unary_function | unary_function |

---

```
/**
This is one of the @link s20_3_1_base functor base classes@endlink.
    */
template <class _Arg, class _Result> struct unary_function {
    typedef _Arg argument_type; ///< @c argument_type is the type of the
    /// argument (no surprises here)
    typedef _Result result_type; ///< @c result_type is the return type
};
```

##### Discussion

@defgroup s20_3_1_base Functor Base Classes
Function objects, or @e functors, are objects with an @c operator()
defined and accessible. They can be passed as arguments to algorithm
templates and used in place of a function pointer. Not only is the
resulting expressiveness of the library increased, but the generated
code can be more efficient than what you might write by hand. When we
refer to "functors," then, generally we include function pointers in
the description as well.

Often, functors are only created as temporaries passed to algorithm
calls, rather than being created as named variables.

Two examples taken from the standard itself follow. To perform a
by-element addition of two vectors @c a and @c b containing @c double,
and put the result in @c a, use
\code
transform (a.begin(), a.end(), b.begin(), a.begin(), plus());
\endcode
To negate every element in @c a, use
\code
transform(a.begin(), a.end(), a.begin(), negate());
\endcode
The addition and negation functions will be inlined directly.

The standard functiors are derived from structs named @c unary_function
and @c binary_function. These two classes contain nothing but typedefs,
to aid in generic (template) programming. If you write your own
functors, you might consider doing the same.

@{

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
