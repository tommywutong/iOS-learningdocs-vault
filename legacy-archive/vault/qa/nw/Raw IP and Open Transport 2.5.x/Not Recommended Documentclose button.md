---
title: Raw IP and Open Transport 2.5.x
apple_id: DTS10001475
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-25'
source_url: https://developer.apple.com/library/archive/qa/nw/nw63.html
archived_at: '2026-07-18T02:29:47.745348Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW63Raw IP and Open Transport 2.5.x |

|  |
| --- |
| ---   Q: My application sends raw IP packets using an Open Transport "rawip" endpoint in `IP_HDRINCL` mode. Under Open Transport 2.5.x (Mac OS 9.0), the packets never make it to the wire. What's up?  A: Open Transport 2.5 includes a significant upgrade to both the STREAMS infrastructure (Mentat Portable Streams 3.3) and the TCP/IP stack (Mentat TCP/IP 3.5). While we worked hard to ensure compatibility with previously releases of Open Transport, a few things have changed:   - The original behavior of a raw IP endpoint in   `IP_HDRINCL` mode is defined in the   [Limitations   of the Header-Included Mode](https://developer.apple.com/documentation/mac/NetworkingOT/NetworkingWOT-56.html#HEADING56-25) section of   [Inside   Macintosh: Networking with Open Transport](https://developer.apple.com/documentation/mac/NetworkingOT/NetworkingWOT-2.html). Open   Transport 2.5.x and beyond change this definition in one   minor but significant aspect. The text "Version. This   field is forced to a value of 4 to reflect the fact that   you're using IP version 4." should now read "Version.   __You must set this field 4__ to reflect the   fact that you're using IP version 4." - Open Transport now checks that the Total Length field   of the IP header is the same as the length of the data   supplied to `OTSndUData` (i.e.   `udata->udata.len`). If they are not the   same, OT discards the IP packet without sending it. The   debug version of OT will report this event to the STREAMS   log driver, which you can view using   [OTStreamLogViewer](ftp://ftp.apple.com/developer/Sample_Code/Networking/OTStreamLogViewer.sit). |

#### [Oct 25 1999]

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
