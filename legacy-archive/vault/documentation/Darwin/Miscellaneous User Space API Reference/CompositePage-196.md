---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/Classes/basic_string/CompositePage.html
archived_at: '2026-07-15T07:23:25.375456Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| basic_string | basic_string | basic_string | basic_string | basic_string |

|  |  |
| --- | --- |
| __Declared In:__ | [basic_string.h](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/index.html) |

## Introduction

@brief Managing sequences of characters and character-like objects.

@ingroup Containers
@ingroup Sequences

Meets the requirements of a [container](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/Classes/basic_string/tables.html#65), a
[reversible container](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/Classes/basic_string/tables.html#66), and a
[sequence](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/Classes/basic_string/tables.html#67). Of the
[optional sequence requirements](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/basic_string/Classes/basic_string/tables.html#68), only
@c push_back, @c at, and array access are supported.

@doctodo

@if maint
Documentation? What's that?
Nathan Myers .

A string looks like this:

@code
[_Rep]
_M_length
[basic_string] _M_capacity
_M_dataplus _M_refcount
_M_p ----------------> unnamed array of char_type
@endcode

Where the _M_p points to the first character in the string, and
you cast it to a pointer-to-_Rep and subtract 1 to get a
pointer to the header.

This approach has the enormous advantage that a string object
requires only one allocation. All the ugliness is confined
within a single pair of inline functions, which each compile to
a single "add" instruction: _Rep::_M_data(), and
string::_M_rep(); and the allocation function which gets a
block of raw bytes and with room enough and constructs a _Rep
object at the front.

The reason you want _M_data pointing to the character array and
not the _Rep is so that the debugger can see the string
contents. (Probably we should add a non-inline member to get
the _Rep for the debugger to use, so users can check the actual
string length.)

Note that the _Rep object is a POD so that you can have a
static "empty string" _Rep object already "constructed" before
static constructors have run. The reference-count encoding is
chosen so that a 0 indicates one reference, so you never try to
destroy the empty-string _Rep object.

All but the last paragraph is considered pretty conventional
for a C++ string implementation.
@endif

---

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
