---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/CompositePage.html
archived_at: '2026-07-15T07:23:28.377591Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_iterator.h | stl_iterator.h | stl_iterator.h | stl_iterator.h | stl_iterator.h |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

This file implements reverse_iterator, back_insert_iterator,
front_insert_iterator, insert_iterator, __normal_iterator, and their
supporting functions and overloaded operators.

---

## Classes

**[back_insert_iterator](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/Classes/back_insert_iterator/index.html#//apple_ref/cpp/cl/back_insert_iterator_DONTLINK_0x2f25d894)**
:

**[front_insert_iterator](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/Classes/front_insert_iterator/index.html#//apple_ref/cpp/cl/front_insert_iterator_DONTLINK_0x2f1dd560)**
:

**[insert_iterator](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/Classes/insert_iterator/index.html#//apple_ref/cpp/cl/insert_iterator_DONTLINK_0x2f2881b0)**
:

---

## Functions

**[back_inserter](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3cmfrwwx3jnzzwk4tumvzf6rcpjzkeyskojnpta6bsmyzdmojvme4a)**
:

**[front_inserter](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gojxw45c7nfxhgzlsorsxex2ej5hfitcjjzfv6mdygjtdentcgazti)**
:

**[inserter](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzzwk4tumvzf6rcpjzkeyskojnpta6bsmyyggmjxme2a)**
:

**[operator ==](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_iterator/CompositePage.html#//apple_ref/c/func/operatoraa_DONTLINK_0x2f2308c0)**
:

**[operator reverse_iterator](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobsxeylun5zf64tfozsxe43fl5uxizlsmf2g64s7irhu4vcmjfhewxzqpazgmmrvmq2dsna)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| back_inserter | back_inserter | back_inserter | back_inserter | back_inserter |

---

```
template<typename _Container> inline back_insert_iterator<_Container> back_inserter(
    _Container& __x)
```

##### Parameters

**`x`**
: A container of arbitrary type.

##### Return Value

An instance of back_insert_iterator working on @p x.

This wrapper function helps in creating back_insert_iterator instances.
Typing the name of the %iterator requires knowing the precise full
type of the container, which can be tedious and impedes generic
programming. Using this function lets you take advantage of automatic
template parameter deduction, making the compiler match the correct
types for you.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| front_inserter | front_inserter | front_inserter | front_inserter | front_inserter |

---

```
template<typename _Container> inline front_insert_iterator<_Container> front_inserter(
    _Container& __x)
```

##### Parameters

**`x`**
: A container of arbitrary type.

##### Return Value

An instance of front_insert_iterator working on @p x.

This wrapper function helps in creating front_insert_iterator instances.
Typing the name of the %iterator requires knowing the precise full
type of the container, which can be tedious and impedes generic
programming. Using this function lets you take advantage of automatic
template parameter deduction, making the compiler match the correct
types for you.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| inserter | inserter | inserter | inserter | inserter |

---

```
template<typename _Container, typename _Iterator> inline insert_iterator<_Container> inserter(
    _Container& __x,
    _Iterator __i)
```

##### Parameters

**`x`**
: A container of arbitrary type.

##### Return Value

An instance of insert_iterator working on @p x.

This wrapper function helps in creating insert_iterator instances.
Typing the name of the %iterator requires knowing the precise full
type of the container, which can be tedious and impedes generic
programming. Using this function lets you take advantage of automatic
template parameter deduction, making the compiler match the correct
types for you.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator == | operator == | operator == | operator == | operator == |

---

```
template<typename _Iterator> inline bool operator==(
    const reverse_iterator<_Iterator>& __x,
    const reverse_iterator<_Iterator>& __y)
```

##### Parameters

**`x`**
: A %reverse_iterator.

**`y`**
: A %reverse_iterator.

##### Return Value

A simple bool.

Reverse iterators forward many operations to their underlying base()
iterators. Others are implemented in terms of one another.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| operator reverse_iterator | operator reverse_iterator | operator reverse_iterator | operator reverse_iterator | operator reverse_iterator |

---

```
template<typename _Iterator> class reverse_iterator : public iterator<typename iterator_traits<_Iterator>::iterator_category, typename iterator_traits<_Iterator>::value_type, typename iterator_traits<_Iterator>::difference_type, typename iterator_traits<_Iterator>::pointer, typename iterator_traits<_Iterator>::reference> {
        protected: _Iterator current;
    public: typedef _Iterator iterator_type;  typedef typename iterator_traits<_Iterator>::difference_type difference_type;  typedef typename iterator_traits<_Iterator>::reference reference;
typedef typename iterator_traits<_Iterator>::pointer pointer;
public: /**
The default constructor default-initializes member @p current.
If it is a pointer, that means it is zero-initialized.
    */
// _GLIBCXX_RESOLVE_LIB_DEFECTS
// 235 No specification of default ctor for reverse_iterator
reverse_iterator() : current() ;  /**
This %iterator will move in the opposite direction that @p x does.
    */
explicit reverse_iterator(
    iterator_type __x) : current(
    __x) ;  /**
The copy constructor is normal.
    */
reverse_iterator(
    const reverse_iterator& __x) : current(
    __x.current) ;  /**
A reverse_iterator across other types can be copied in the normal
fashion.
    */
template<typename _Iter> reverse_iterator(
    const reverse_iterator<_Iter>& __x) : current(
    __x.base()) ;  /**
@return @c current, the %iterator used for underlying work.
    */
iterator_type base() const   /**
@return TODO

@doctodo
    */
reference operator*() const   /**
@return TODO

@doctodo
    */
pointer operator->() const return &(
    operator*());
}  /**
@return TODO

@doctodo
    */
reverse_iterator& operator++() ;
```

##### Discussion

"Bidirectional and random access iterators have corresponding reverse
%iterator adaptors that iterate through the data structure in the
opposite direction. They have the same signatures as the corresponding
iterators. The fundamental relation between a reverse %iterator and its
corresponding %iterator @c i is established by the identity:
@code
&\*(reverse_iterator(i)) == &\*(i - 1)
@endcode

This mapping is dictated by the fact that while there is always a
pointer past the end of an array, there might not be a valid pointer
before the beginning of an array." [24.4.1]/1,2

Reverse iterators can be tricky and surprising at first. Their
semantics make sense, however, and the trickiness is a side effect of
the requirement that the iterators must be safe.

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
