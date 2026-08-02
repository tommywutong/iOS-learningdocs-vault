---
title: QTRecorder
apple_id: DTS10004043
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2011-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/QTRecorder/History/History.html
archived_at: '2026-07-18T03:21:09.850603Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTRecorder](QTRecorder.md)


[Previous](QTRDocument.m.md)

# Document Revision History

This table describes the changes to _QTRecorder_.

| __Date__ | __Notes__ |
| 2011-08-25 | Update for Xcode 4 |
| 2009-12-14 | Updated the shouldChangeOutputFile delegate call to return NO, since it does not change the file. Fixed build warnings due to use of deprecated APIs. |
| 2007-04-10 | This revision demonstrates modifications made to device selection. Also included in this revision is additional logic demonstrating audio preview and audio level metering. QTKit classes provide support for controlling FireWire AVC devices. This functionality enables your applications to integrate the ability to determine device recording and playback modes as well as both control and monitor tape speed and direction. QTRecorder provides a tape control user interface that is enabled synchronously with a selected FireWire AVC device such as a compliant DV camera. This revision now also provides an example of how to handle input format change notifications and retrieve media format summaries. Additionally shown is the ability to intercept video frames being rendered to a preview output and, optionally, using this to pass video through some fun CoreImage filter pipelines. QTKit has removed the need to post-process a movie at the end of a recording session and subsequently flatten the movie. Replacing this are a collection capture output notifications which mark the stages of a capture session. |

[Previous](QTRDocument.m.md)

