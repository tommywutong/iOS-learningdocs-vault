---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/fileio/CompositePage.html
archived_at: '2026-07-15T07:23:26.651803Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| fileio.h - does standard C I/O | fileio.h - does standard C I/O | fileio.h - does standard C I/O | fileio.h - does standard C I/O | fileio.h - does standard C I/O |

|  |  |
| --- | --- |
| __Includes:__ | ["buffio.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/buffio/index.html#//apple_ref/doc/header/buffio.h) |

## Introduction

Implementation of a FILE\* based TidyInputSource and
TidyOutputSink.

(c) 1998-2003 (W3C) MIT, ERCIM, Keio University
See tidy.h for the copyright notice.

CVS Info:
$Author: rbraun $
$Date: 2004/05/04 20:05:14 $
$Revision: 1.1.1.1 $

---

## Functions

**[freeFileSource](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gojswkrtjnrsvg33vojrwk)**
:

**[initFileSink](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzuxirtjnrsvg2lonm)**
:

**[initFileSource](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3jnzuxirtjnrsvg33vojrwk)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| freeFileSource | freeFileSource | freeFileSource | freeFileSource | freeFileSource |

---

```
void freeFileSource(
    TidyInputSource*source,
    Bool closeIt );
```

##### Discussion

Free file input source

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| initFileSink | initFileSink | initFileSink | initFileSink | initFileSink |

---

```
void initFileSink(
    TidyOutputSink*sink,
    FILE*fp );
```

##### Discussion

Initialize file output sink

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| initFileSource | initFileSource | initFileSource | initFileSource | initFileSource |

---

```
void initFileSource(
    TidyInputSource*source,
    FILE*fp );
```

##### Discussion

Allocate and initialize file input source

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
