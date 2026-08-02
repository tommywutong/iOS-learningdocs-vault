---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/buffio/CompositePage.html
archived_at: '2026-07-15T07:23:26.139681Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| buffio.h - Treat buffer as an I/O stream. | buffio.h - Treat buffer as an I/O stream. | buffio.h - Treat buffer as an I/O stream. | buffio.h - Treat buffer as an I/O stream. | buffio.h - Treat buffer as an I/O stream. |

|  |  |
| --- | --- |
| __Includes:__ | ["platform.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/platform/index.html#//apple_ref/doc/header/platform.h)  ["tidy.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tidy/index.html#//apple_ref/doc/header/tidy.h) |

## Introduction

(c) 1998-2004 (W3C) MIT, ERCIM, Keio University
See tidy.h for the copyright notice.

CVS Info :

$Author: rbraun $
$Date: 2004/05/04 20:05:14 $
$Revision: 1.1.1.1 $

Requires buffer to automatically grow as bytes are added.
Must keep track of current read and write points.

---

## Functions

**[initInputBuffer](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzuxisloob2xiqtvmztgk4q)**
:

**[initOutputBuffer](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzuxit3voryhk5ccovtgmzls)**
:

**[tidyBufAlloc](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzawy3dpmm)**
:

**[tidyBufAppend](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzaxa4dfnzsa)**
:

**[tidyBufAttach](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzaxi5dbmnua)**
:

**[tidyBufCheckAlloc](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzbwqzldnnawy3dpmm)**
:

**[tidyBufClear](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzbwyzlboi)**
:

**[tidyBufDetach](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzcgk5dbmnua)**
:

**[tidyBufEndOfInput](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzcw4zcpmzew44dvoq)**
:

**[tidyBufFree](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzdhezlf)**
:

**[tidyBufGetByte](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzdwk5ccpf2gk)**
:

**[tidyBufInit](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzew42lu)**
:

**[tidyBufPopByte](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzig64ccpf2gk)**
:

**[tidyBufPutByte](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzihk5ccpf2gk)**
:

**[tidyBufUngetByte](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqtvmzkw4z3forbhs5df)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| initInputBuffer | initInputBuffer | initInputBuffer | initInputBuffer | initInputBuffer |

---

```
TIDY_EXPORT void initInputBuffer(
    TidyInputSource*inp,
    TidyBuffer*buf );
```

##### Discussion

Initialize a buffer input source

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| initOutputBuffer | initOutputBuffer | initOutputBuffer | initOutputBuffer | initOutputBuffer |

---

```
TIDY_EXPORT void initOutputBuffer(
    TidyOutputSink*outp,
    TidyBuffer*buf );
```

##### Discussion

Initialize a buffer output sink

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufAlloc | tidyBufAlloc | tidyBufAlloc | tidyBufAlloc | tidyBufAlloc |

---

```
TIDY_EXPORT void tidyBufAlloc(
    TidyBuffer*buf,
    uint allocSize );
```

##### Discussion

Free current buffer, allocate given amount, reset input pointer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufAppend | tidyBufAppend | tidyBufAppend | tidyBufAppend | tidyBufAppend |

---

```
TIDY_EXPORT void tidyBufAppend(
    TidyBuffer*buf,
    void*vp,
    uint size );
```

##### Discussion

Append bytes to buffer. Expand if necessary.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufAttach | tidyBufAttach | tidyBufAttach | tidyBufAttach | tidyBufAttach |

---

```
TIDY_EXPORT void tidyBufAttach(
    TidyBuffer*buf,
    byte*bp,
    uint size );
```

##### Discussion

Attach to existing buffer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufCheckAlloc | tidyBufCheckAlloc | tidyBufCheckAlloc | tidyBufCheckAlloc | tidyBufCheckAlloc |

---

```
TIDY_EXPORT void tidyBufCheckAlloc(
    TidyBuffer*buf,
    uint allocSize,
    uint chunkSize );
```

##### Discussion

Expand buffer to given size.
\*\* Chunk size is minimum growth. Pass 0 for default of 256 bytes.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufClear | tidyBufClear | tidyBufClear | tidyBufClear | tidyBufClear |

---

```
TIDY_EXPORT void tidyBufClear(
    TidyBuffer*buf );
```

##### Discussion

Set buffer bytes to 0

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufDetach | tidyBufDetach | tidyBufDetach | tidyBufDetach | tidyBufDetach |

---

```
TIDY_EXPORT void tidyBufDetach(
    TidyBuffer*buf );
```

##### Discussion

Detach from buffer. Caller must free.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufEndOfInput | tidyBufEndOfInput | tidyBufEndOfInput | tidyBufEndOfInput | tidyBufEndOfInput |

---

```
TIDY_EXPORT Bool tidyBufEndOfInput(
    TidyBuffer*buf );
```

##### Discussion

At end of buffer?

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufFree | tidyBufFree | tidyBufFree | tidyBufFree | tidyBufFree |

---

```
TIDY_EXPORT void tidyBufFree(
    TidyBuffer*buf );
```

##### Discussion

Free current contents and zero out

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufGetByte | tidyBufGetByte | tidyBufGetByte | tidyBufGetByte | tidyBufGetByte |

---

```
TIDY_EXPORT int tidyBufGetByte(
    TidyBuffer*buf );
```

##### Discussion

Get byte from front of buffer. Increment input offset.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufInit | tidyBufInit | tidyBufInit | tidyBufInit | tidyBufInit |

---

```
TIDY_EXPORT void tidyBufInit(
    TidyBuffer*buf );
```

##### Discussion

Zero out data structure

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufPopByte | tidyBufPopByte | tidyBufPopByte | tidyBufPopByte | tidyBufPopByte |

---

```
TIDY_EXPORT int tidyBufPopByte(
    TidyBuffer*buf );
```

##### Discussion

Get byte from end of buffer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufPutByte | tidyBufPutByte | tidyBufPutByte | tidyBufPutByte | tidyBufPutByte |

---

```
TIDY_EXPORT void tidyBufPutByte(
    TidyBuffer*buf,
    byte bv );
```

##### Discussion

Append one byte to buffer. Expand if necessary.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyBufUngetByte | tidyBufUngetByte | tidyBufUngetByte | tidyBufUngetByte | tidyBufUngetByte |

---

```
TIDY_EXPORT void tidyBufUngetByte(
    TidyBuffer*buf,
    byte bv );
```

##### Discussion

Put a byte back into the buffer. Decrement input offset.

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _TidyBuffer | _TidyBuffer | _TidyBuffer | _TidyBuffer | _TidyBuffer |

---

```
TIDY_STRUCT struct _TidyBuffer {
    byte*bp; /**< Pointer to bytes */
    uint size; /**< # bytes currently in use */
    uint allocated; /**< # bytes allocated */
    uint next; /**< Offset of current input position */
};
```

##### Discussion

TidyBuffer - A chunk of memory

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
