---
title: Sequence Grabber - Determining the capture resolution of an IIDC device
apple_id: DTS10003480
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-01-06'
source_url: https://developer.apple.com/library/archive/qa/qa1403/_index.html
archived_at: '2026-07-18T02:30:31.697741Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1403

# Sequence Grabber - Determining the capture resolution of an IIDC device

## Q:  I'm trying to find a way to determine the capture resolution of an IIDC device. I'm currently using two functions; `SGGetSrcVideoBounds` and `VDGetDigitizerRect`. Both however return a size of 1600x1200 instead of 640x480 when using the Apple iSight camera. What's the best way to do this?

A: While the relationship between the Source, Video and Channel bounds is described in [Technical Q&A 1250](https://developer.apple.com/qa/qa2001/qa1250.html), these bounds do not necessarily reflect what a particular device will generate.

In the case of the QuickTime IIDC Video Digitizer (used by the [Apple iSight](http://www.apple.com/isight/)), the actual image size isn't determined until the Sequence Grabber Video Channel is fully configured. Once this is done you can call `SGGetChannelSampleDescription` or the lower level `VDGetImageDescription` to determine the captured image size.

- Sequence Grabber Source, Video and Channel Bounds - [Technical Q&A 1250](https://developer.apple.com/qa/qa2001/qa1250.html)
- Video Capture with multiple IIDC cameras - [Technical Q&A 1365](https://developer.apple.com/qa/qa2004/qa1365.html)
- [SGGetChannelSampleDescription](https://developer.apple.com/documentation/QuickTime/APIREF/sggetchannelsampledescription.htm)
- [VDGetImageDescription](https://developer.apple.com/documentation/QuickTime/APIREF/vdgetimagedescription.htm#//apple_ref/doc/uid/TP40001187-DontLinkChapterID_2-VDGetImageDescription)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-01-06 | New document that discusses how to determine the resolution of a captured image from an IIDC device |

