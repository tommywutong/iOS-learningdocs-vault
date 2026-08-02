---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stdio_sync_filebuf/CompositePage.html
archived_at: '2026-07-15T07:23:27.954371Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ext/stdio_sync_filebuf.h | ext/stdio_sync_filebuf.h | ext/stdio_sync_filebuf.h | ext/stdio_sync_filebuf.h | ext/stdio_sync_filebuf.h |

|  |  |
| --- | --- |
| __Includes:__ | <streambuf>  <unistd.h>  <cstdio>  <cwchar>  <streambuf>  <unistd.h>  <cstdio>  <cwchar> |

## Introduction

This file is a GNU extension to the Standard C++ Library.

---

## Functions

**[file](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3gnfwgkx2ej5hfitcjjzfv6mdygjrdkmjwgrqwg)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| file | file | file | file | file |

---

```
std::__c_file* const file()
```

##### Return Value

The underlying FILE\*.

This function can be used to access the underlying "C" file pointer.
Note that there is no way for the library to track what you do
with the file, so be careful.

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
