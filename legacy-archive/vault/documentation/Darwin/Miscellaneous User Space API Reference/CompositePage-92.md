---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/nanoftp/CompositePage.html
archived_at: '2026-07-15T07:23:27.415003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| nanoftp.h | nanoftp.h | nanoftp.h | nanoftp.h | nanoftp.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ftpDataCallback | ftpDataCallback | ftpDataCallback | ftpDataCallback | ftpDataCallback |

---

```
typedef void (*ftpDataCallback) (
    void *userData,
    const char *data,
    int len);
```

##### Discussion

ftpDataCallback:
@userData: the user provided context
@data: the data received
@len: its size in bytes

A callback for the xmlNanoFTPGet command.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ftpListCallback | ftpListCallback | ftpListCallback | ftpListCallback | ftpListCallback |

---

```
typedef void (*ftpListCallback) (
    void *userData,
    const char *filename,
    const char *attrib,
    const char *owner,
    const char *group,
    unsigned long size,
    int links,
    int year,
    const char *month,
    int day,
    int hour,
    int minute);
```

##### Discussion

ftpListCallback:
@userData: user provided data for the callback
@filename: the file name (including "->" when links are shown)
@attrib: the attribute string
@owner: the owner string
@group: the group string
@size: the file size
@links: the link count
@year: the year
@month: the month
@day: the day
@hour: the hour
@minute: the minute

A callback for the xmlNanoFTPList command.
Note that only one of year and day:minute are specified.

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
