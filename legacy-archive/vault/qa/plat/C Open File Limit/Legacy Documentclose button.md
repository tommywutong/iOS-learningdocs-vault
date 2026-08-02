---
title: C Open File Limit
apple_id: DTS10001516
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat06.html
archived_at: '2026-07-18T02:29:51.370374Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Tools](https://developer.apple.com/referencelibrary/Java/idxTools-date.html)

|  |
| --- |
| Technical Q&A PLAT06C Open File Limit |

|  |
| --- |
| ---   Q: Our development group has encountered a problem with their Macintosh port (they are developing for the 68K only, under MPW 3.3.1 with the MPW C 3.2.4 compiler). They allocate a large number of FILE streams via `fopen()`, and eventually, the `fopen()` calls begin to fail. We believe that they have encountered MPW's limit of 20 open files.  A: Microsoft has provided a standard C library that has a larger static FILE stream buffer to circumvent this problem, and they would like get a similar MPW C library from Apple.  A: The `_NFILES` macro in stdio.h defines the maximum number of files that can be opened. This is set to 40 in the ETO #16 pre-release, SC-compatible, MPW libraries (otherwise it's 20). Support for more than 40 files is not planned, so there won't be a final version of libraries for MPW C with a larger open-file limit.  There is a possible workaround - use our low-level I/O calls instead of the stream I/O calls. The number of files you can open with low-level calls is limited only by available memory. (These calls are documented in the __chapter on building MPW tools in _Building and Managing Programs with MPW)___. Low-level I/O calls can be used in applications, but this isn't obvious because the documentation isn't well organized.  It's possible that our low-level I/O calls may not provide you with sufficient functionality for your port, assuming that you are using `fprintf` or a related function, and there is no low-level equivalent for this. If your usage is limited to `getc/putc/fread/fwrite`, it would be fairly simple to emulate these on top of low-level I/O using the low-level read and write functions. However, a better, long-term solution would be to move to the SC compiler and its associated libraries. |

#### [Jun 01 1995]

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

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
