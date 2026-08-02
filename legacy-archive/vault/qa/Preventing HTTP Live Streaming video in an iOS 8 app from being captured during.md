---
title: Preventing HTTP Live Streaming video in an iOS 8 app from being captured during
  screen recording on Yosemite
apple_id: DTS40015202
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: QuickTime
published: '2015-03-10'
source_url: https://developer.apple.com/library/archive/qa/qa1891/_index.html
archived_at: '2026-07-18T02:35:23.395523Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1891

# Preventing HTTP Live Streaming video in an iOS 8 app from being captured during screen recording on Yosemite

## Q:  How can I prevent my iOS 8 app's streaming video media from being captured by QuickTime Player on Yosemite during screen recording?

A: HTTP Live Streams that have their media encrypted will not be recorded by QuickTime Player on Yosemite while screen recording. These will be blacked out in the recording.

To learn more about using encrypted media with HTTP Live Streaming, see the [HTTP Live Streaming Guide](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/StreamingMediaGuide.pdf) and [HTTP Live Streaming Internet Draft](https://tools.ietf.org/html/draft-pantos-http-live-streaming).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-10 | New document that discusses how to prevent an iOS 8 app's streaming video from being captured by QuickTime Player during screen recording on Yosemite |

