---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/gslice/Classes/gslice/CompositePage.html
archived_at: '2026-07-15T07:23:26.754849Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| gslice | gslice | gslice | gslice | gslice |

|  |  |
| --- | --- |
| __Declared In:__ | [gslice.h](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/gslice/index.html) |

## Introduction

@brief Class defining multi-dimensional subset of an array.

The slice class represents a multi-dimensional subset of an array,
specified by three parameter sets: start offset, size array, and stride
array. The start offset is the index of the first element of the array
that is part of the subset. The size and stride array describe each
dimension of the slice. Size is the number of elements in that
dimension, and stride is the distance in the array between successive
elements in that dimension. Each dimension's size and stride is taken
to begin at an array element described by the previous dimension. The
size array and stride array must be the same size.

For example, if you have offset==3, stride[0]==11, size[1]==3,
stride[1]==3, then slice[0,0]==array[3], slice[0,1]==array[6],
slice[0,2]==array[9], slice[1,0]==array[14], slice[1,1]==array[17],
slice[1,2]==array[20].

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
