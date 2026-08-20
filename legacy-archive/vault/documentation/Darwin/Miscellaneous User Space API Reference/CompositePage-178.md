---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlIO/CompositePage.html
archived_at: '2026-07-15T07:23:29.144241Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlIO.h | xmlIO.h | xmlIO.h | xmlIO.h | xmlIO.h |

|  |  |
| --- | --- |
| __Includes:__ | <stdio.h>  [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/globals.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/globals/index.html#//apple_ref/doc/header/globals.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  [<libxml/parser.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/parser/index.html#//apple_ref/doc/header/parser.h)  [<libxml/encoding.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/encoding/index.html#//apple_ref/doc/header/encoding.h) |

## Introduction

---

## Functions

**[xmlFileMatch](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3ynvwem2lmmvgwc5ddna)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlFileMatch | xmlFileMatch | xmlFileMatch | xmlFileMatch | xmlFileMatch |

---

```
XMLPUBFUN int XMLCALL xmlFileMatch (
    const char *filename);
```

##### Discussion

Default 'file://' protocol callbacks

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlInputCloseCallback | xmlInputCloseCallback | xmlInputCloseCallback | xmlInputCloseCallback | xmlInputCloseCallback |

---

```
typedef int (*xmlInputCloseCallback) (
    void *context);
```

##### Discussion

xmlInputCloseCallback:
@context: an Input context

Callback used in the I/O Input API to close the resource

Returns 0 or -1 in case of error

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlInputMatchCallback | xmlInputMatchCallback | xmlInputMatchCallback | xmlInputMatchCallback | xmlInputMatchCallback |

---

```
typedef int (*xmlInputMatchCallback) (
    char const *filename);
```

##### Discussion

xmlInputMatchCallback:
@filename: the filename or URI

Callback used in the I/O Input API to detect if the current handler
can provide input fonctionnalities for this resource.

Returns 1 if yes and 0 if another Input module should be used

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlInputOpenCallback | xmlInputOpenCallback | xmlInputOpenCallback | xmlInputOpenCallback | xmlInputOpenCallback |

---

```
typedef void * (*xmlInputOpenCallback) (
    char const *filename);
```

##### Discussion

xmlInputOpenCallback:
@filename: the filename or URI

Callback used in the I/O Input API to open the resource

Returns an Input context or NULL in case or error

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlInputReadCallback | xmlInputReadCallback | xmlInputReadCallback | xmlInputReadCallback | xmlInputReadCallback |

---

```
typedef int (*xmlInputReadCallback) (
    void *context,
    char *buffer,
    int len);
```

##### Discussion

xmlInputReadCallback:
@context: an Input context
@buffer: the buffer to store data read
@len: the length of the buffer in bytes

Callback used in the I/O Input API to read the resource

Returns the number of bytes read or -1 in case of error

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlOutputCloseCallback | xmlOutputCloseCallback | xmlOutputCloseCallback | xmlOutputCloseCallback | xmlOutputCloseCallback |

---

```
typedef int (*xmlOutputCloseCallback) (
    void *context);
```

##### Discussion

xmlOutputCloseCallback:
@context: an Output context

Callback used in the I/O Output API to close the resource

Returns 0 or -1 in case of error

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlOutputMatchCallback | xmlOutputMatchCallback | xmlOutputMatchCallback | xmlOutputMatchCallback | xmlOutputMatchCallback |

---

```
typedef int (*xmlOutputMatchCallback) (
    char const *filename);
```

##### Discussion

xmlOutputMatchCallback:
@filename: the filename or URI

Callback used in the I/O Output API to detect if the current handler
can provide output fonctionnalities for this resource.

Returns 1 if yes and 0 if another Output module should be used

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlOutputOpenCallback | xmlOutputOpenCallback | xmlOutputOpenCallback | xmlOutputOpenCallback | xmlOutputOpenCallback |

---

```
typedef void * (*xmlOutputOpenCallback) (
    char const *filename);
```

##### Discussion

xmlOutputOpenCallback:
@filename: the filename or URI

Callback used in the I/O Output API to open the resource

Returns an Output context or NULL in case or error

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlOutputWriteCallback | xmlOutputWriteCallback | xmlOutputWriteCallback | xmlOutputWriteCallback | xmlOutputWriteCallback |

---

```
typedef int (*xmlOutputWriteCallback) (
    void *context,
    const char *buffer,
    int len);
```

##### Discussion

xmlOutputWriteCallback:
@context: an Output context
@buffer: the buffer of data to write
@len: the length of the buffer in bytes

Callback used in the I/O Output API to write to the resource

Returns the number of bytes written or -1 in case of error

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
