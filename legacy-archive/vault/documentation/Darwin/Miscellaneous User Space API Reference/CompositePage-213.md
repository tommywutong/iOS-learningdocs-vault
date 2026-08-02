---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_function/Classes/mem_fun_t/CompositePage.html
archived_at: '2026-07-15T07:23:28.212515Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| mem_fun_t | mem_fun_t | mem_fun_t | mem_fun_t | mem_fun_t |

|  |  |
| --- | --- |
| __Superclass:__ | unary_function<_Tp\*, _Ret> |
| __Declared In:__ | [stl_function.h](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_function/index.html) |

## Introduction

@defgroup s20_3_8_memadaptors Adaptors for pointers to members
There are a total of 16 = 2^4 function objects in this family.
(1) Member functions taking no arguments vs member functions taking
one argument.
(2) Call through pointer vs call through reference.
(3) Member function with void return type vs member function with
non-void return type.
(4) Const vs non-const member function.

Note that choice (3) is nothing more than a workaround: according
to the draft, compilers should handle void and non-void the same way.
This feature is not yet widely implemented, though. You can only use
member functions returning void if your compiler supports partial
specialization.

All of this complexity is in the function objects themselves. You can
ignore it by using the helper function mem_fun and mem_fun_ref,
which create whichever type of adaptor is appropriate.

@{

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
