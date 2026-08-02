---
title: Network Kernel Extensions (legacy)
apple_id: TP40001089
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NetworkKernelExtensions/revision_history/revision_history.html
archived_at: '2026-07-15T07:23:22.766261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions (legacy)](About%20Network%20Kernel%20Extensions.md)


[Next](Glossary.md)[Previous](Network%20Kernel%20Extensions%20Reference.md)

An important change has long been noted in the `<sys/mbuf.h>` header file since the release of Mac OS X 10.2. Note that the header file is bracketed by the `__APPLE_API_UNSTABLE` define. The mbuf structure is a key to the processing of packets in an NKE. As part of the formalizing the NKE APIs, it is expected that the mbuf structure will be changed. Details will be provided in the future. Changes to the existing NKE API are not expected be applied to System Updates to Mac OS X 10.3.x, however, bug fixes or features for future systems may require some interim changes.

For all shipping releases of Mac OS X prior to 10.4, the Network Kernel Extensions (NKE) APIs have not been officially supported. The legacy NKE architecture was implemented as an interim solution. The legacy API was never designed to be officially supported. Other aspects of the OS X networking implementation have received a higher priority, and so the interim solution has remained in effect to OS X 10.3.x.

The NKE mechanism for Mac OS X version 10.4 and later is described in the document _[Network Kernel Extensions Programming Guide](../Network%20Kernel%20Extensions%20Programming%20Guide/Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjy)_.

# Document Revision History

This table describes the changes to _Network Kernel Extensions (legacy)_.

| __Date__ | __Notes__ |
| 2006-10-03 | Clarified the availability of sample code. |
| 2005-10-04 | Corrected some minor formatting issues. |
| 2005-08-11 | Fixed error in code sample. |
| 2005-06-04 | Fixed minor typographical errors. |
| 2005-04-29 | Updated title to reflect legacy status. (This document covers Mac OS X v10.3 and earlier.) |
| 2004-04-22 | Initial republication |

[Next](Glossary.md)[Previous](Network%20Kernel%20Extensions%20Reference.md)

