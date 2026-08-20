---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator_base_types/CompositePage.html
archived_at: '2026-07-15T07:23:28.414451Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_iterator_base_types.h | stl_iterator_base_types.h | stl_iterator_base_types.h | stl_iterator_base_types.h | stl_iterator_base_types.h |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

This file contains all of the general iterator-related utility types,
such as iterator_traits and struct iterator.

---

## Functions

**[__iterator_category](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl27l5uxizlsmf2g64s7mnqxizlhn5zhsx2ej5hfitcjjzfv6mdygjtdgmdggy3da)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __iterator_category | __iterator_category | __iterator_category | __iterator_category | __iterator_category |

---

```
template<typename _Iter> inline typename iterator_traits<_Iter>::iterator_category __iterator_category(
    const _Iter&)
```

##### Discussion

@if maint
This function is not a part of the C++ standard but is syntactic
sugar for internal library use only.
@endif

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| iterator | iterator | iterator | iterator | iterator |

---

```
template<typename _Category, typename _Tp, typename _Distance =
    ptrdiff_t, typename _Pointer = _Tp*, typename _Reference = _Tp&> struct iterator {
    /// One of the @link iterator_tags tag types@endlink.
    typedef _Category iterator_category;
    /// The type "pointed to" by the iterator.
    typedef _Tp value_type;
    /// Distance between iterators is represented as this type.
    typedef _Distance difference_type;
    /// This type represents a pointer-to-value_type.
    typedef _Pointer pointer;
    /// This type represents a reference-to-value_type.
    typedef _Reference reference;
};
```

##### Discussion

@brief Common %iterator class.

This class does nothing but define nested typedefs. %Iterator classes
can inherit from this class to save some work. The typedefs are then
used in specializations and overloading.

In particular, there are no default implementations of requirements
such as @c operator++ and the like. (How could there be?)

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| iterator_traits | iterator_traits | iterator_traits | iterator_traits | iterator_traits |

---

```
template<typename _Iterator> struct iterator_traits {
    typedef typename _Iterator::iterator_category iterator_category;
    typedef typename _Iterator::value_type value_type;
    typedef typename _Iterator::difference_type difference_type;
    typedef typename _Iterator::pointer pointer;
    typedef typename _Iterator::reference reference;
};
```

##### Discussion

This class does nothing but define nested typedefs. The general
version simply "forwards" the nested typedefs from the Iterator
argument. Specialized versions for pointers and pointers-to-const
provide tighter, more correct semantics.

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| input_iterator_tag | input_iterator_tag | input_iterator_tag | input_iterator_tag | input_iterator_tag |

---

```
/// Marking input iterators.
struct input_iterator_tag {
};
```

##### Discussion

@defgroup iterator_tags Iterator Tags
These are empty types, used to distinguish different iterators. The
distinction is not made by what they contain, but simply by what they
are. Different underlying algorithms can then be used based on the
different operations supporetd by different iterator types.

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
