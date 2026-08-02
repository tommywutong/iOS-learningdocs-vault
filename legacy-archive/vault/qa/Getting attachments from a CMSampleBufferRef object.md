---
title: Getting attachments from a CMSampleBufferRef object
apple_id: DTS40017660
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreMedia
published: '2017-07-03'
source_url: https://developer.apple.com/library/archive/qa/qa1957/_index.html
archived_at: '2026-07-18T02:38:00.691859Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1957

# Getting attachments from a CMSampleBufferRef object

## Q:  I’m calling `CMSampleBufferGetSampleAttachmentsArray(_:_:)` in an attempt to get the `kCMSampleBufferAttachmentKey_DroppedFrameReason` from a `CMSampleBufferRef`, but the returned attachments array is always nil. What’s going on?

A: For getting attachments, the general rule is:

- for `kCMSampleBufferAttachmentKey_*`, use `CMGetAttachment(_:_:_:)`

- for `kCMSampleAttachmentKey_*`, use `CMSampleBufferGetSampleAttachmentsArray(_:_:)`

Therefore, to get the `kCMSampleBufferAttachmentKey_DroppedFrameReason` from a `CMSampleBufferRef` use `CMGetAttachment(_:_:_:)`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-07-03 | New document that discusses how to get attachments from a CMSampleBufferRef object. |

