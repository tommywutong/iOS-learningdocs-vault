---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/functional_iterate/CompositePage.html
archived_at: '2026-07-15T07:23:26.712448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| functional_iterate.h | functional_iterate.h | functional_iterate.h | functional_iterate.h | functional_iterate.h |

|  |  |
| --- | --- |
| __Includes:__ | [<tr1/bind_repeat.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bind_repeat/index.html#//apple_ref/doc/header/bind_repeat.h)  [<tr1/bind_repeat.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/bind_repeat/index.html#//apple_ref/doc/header/bind_repeat.h) |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Functions

**[function](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3govxgg5djn5xa)**
:

**[function](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3govxgg5djn5xf6rcpjzkeyskojnpta6bsmiywmzjxgq2a)**
:

**[function(const function &)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3govxgg5djn5xf6rcpjzkeyskojnpta6bsmiywmzjtgq2a)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| function | function | function | function | function |

---

```
function() : _Function_base()
```

##### Discussion

@brief Default construct creates an empty function call wrapper.
@post @c !(bool)\*this

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| function | function | function | function | function |

---

```
function(
    _M_clear_type*) : _Function_base()
```

##### Discussion

@brief Default construct creates an empty function call wrapper.
@post @c !(bool)\*this

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| function(const function &) | function(const function &) | function(const function &) | function(const function &) | function(const function &) |

---

```
function(
    const function& __x);
```

##### Parameters

**`x`**
: A %function object with identical call signature.
@pre @c (bool)\*this == (bool)x

The newly-created %function contains a copy of the target of @a
x (if it has one).

##### Discussion

@brief %Function copy constructor.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __enable_if | __enable_if | __enable_if | __enable_if | __enable_if |

---

```
template<typename _Functor _GLIBCXX_COMMA _GLIBCXX_TEMPLATE_PARAMS> inline typename __enable_if< typename result_of<_Functor(
            _GLIBCXX_TEMPLATE_ARGS)>::type, (
        !is_member_pointer<_Functor>::value && !is_function<_Functor>::value && !is_function<typename remove_pointer<_Functor>::type>::value) >::__type __invoke(
            _Functor& __f _GLIBCXX_COMMA _GLIBCXX_REF_PARAMS)
```

##### Discussion

@if maint
Invoke a function object, which may be either a member pointer or a
function object. The first parameter will tell which.
@endif

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Safe_bool | _Safe_bool | _Safe_bool | _Safe_bool | _Safe_bool |

---

```
typedef _Hidden_type* _Hidden_type::* _Safe_bool;
```

##### Discussion

@if maint
This typedef is used to implement the safe_bool idiom.
@endif

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _Hidden_type | _Hidden_type | _Hidden_type | _Hidden_type | _Hidden_type |

---

```
struct _Hidden_type {
    _Hidden_type*_M_bool;
};
```

##### Discussion

@if maint
This class is used to implement the safe_bool idiom.
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
