---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/encoding/CompositePage.html
archived_at: '2026-07-15T07:23:26.552897Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| encoding.h | encoding.h | encoding.h | encoding.h | encoding.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  <iconv.h>  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlCharEncodingInputFunc | xmlCharEncodingInputFunc | xmlCharEncodingInputFunc | xmlCharEncodingInputFunc | xmlCharEncodingInputFunc |

---

```
typedef int (*xmlCharEncodingInputFunc)(
    unsigned char *out,
    int *outlen,
    const unsigned char *in,
    int *inlen);
```

##### Discussion

xmlCharEncodingInputFunc:
@out: a pointer to an array of bytes to store the UTF-8 result
@outlen: the length of @out
@in: a pointer to an array of chars in the original encoding
@inlen: the length of @in

Take a block of chars in the original encoding and try to convert
it to an UTF-8 block of chars out.

Returns the number of bytes written, -1 if lack of space, or -2
if the transcoding failed.
The value of @inlen after return is the number of octets consumed
if the return value is positive, else unpredictiable.
The value of @outlen after return is the number of octets consumed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlCharEncodingOutputFunc | xmlCharEncodingOutputFunc | xmlCharEncodingOutputFunc | xmlCharEncodingOutputFunc | xmlCharEncodingOutputFunc |

---

```
typedef int (*xmlCharEncodingOutputFunc)(
    unsigned char *out,
    int *outlen,
    const unsigned char *in,
    int *inlen);
```

##### Discussion

xmlCharEncodingOutputFunc:
@out: a pointer to an array of bytes to store the result
@outlen: the length of @out
@in: a pointer to an array of UTF-8 chars
@inlen: the length of @in

Take a block of UTF-8 chars in and try to convert it to another
encoding.
Note: a first call designed to produce heading info is called with
in = NULL. If stateful this should also initialize the encoder state.

Returns the number of bytes written, -1 if lack of space, or -2
if the transcoding failed.
The value of @inlen after return is the number of octets consumed
if the return value is positive, else unpredictiable.
The value of @outlen after return is the number of octets produced.

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
