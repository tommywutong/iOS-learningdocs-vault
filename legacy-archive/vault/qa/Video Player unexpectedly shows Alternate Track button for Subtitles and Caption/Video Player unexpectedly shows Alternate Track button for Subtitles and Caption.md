---
title: Video Player unexpectedly shows Alternate Track button for Subtitles and Captions
apple_id: DTS40013901
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-10-29'
source_url: https://developer.apple.com/library/archive/qa/qa1801/_index.html
archived_at: '2026-07-18T02:34:51.843150Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1801

# Video Player unexpectedly shows Alternate Track button for Subtitles and Captions

## Q:  When playing a video stream the player controls show a alternate track button even though the stream does not contain closed caption content. Are there any options to disable this feature?

A: As part of the new automatic media selection feature on iOS 7, the presence of closed captions and subtitles must be known prior to playback. Prior to iOS 7, there is no way to declare the presence of closed caption data in the playlist.

By default, the alternate track button (see Figure 1) will be displayed along with the various other player controls and will be set to the "Unknown CC" option as shown in Figure 2.

__Figure 1__  The alternate track button alongside the player controls.

!

__Figure 2__  Options for the alternate track button.

!

When the "Unknown CC" option is selected, closed caption content will be shown during playback if present.

iOS 7 now supports the `TYPE` attribute of the `EXT-X-MEDIA` tag having a value of `CLOSED-CAPTIONS`. This allows for explicit declaration of closed caption content in the playlist file. See the [HTTP Live Streaming Draft Protocol Specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming) for the details.

iOS 7 also supports a `CLOSED-CAPTIONS` attribute for the `EXT-X-STREAM-INF` tag. You can declare the absence of closed caption content in the playlist by specifying `CLOSED-CAPTIONS=NONE` on the `EXT-X-STREAM-INF` tag. The "Unknown CC" option as shown in Figure 1 will not be displayed in the selection when the absence of closed caption content is declared.

Also, if the media does not contain alternate audio or subtitles, and the absence of closed caption content is declared, the alternate track button will not be displayed.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-10-29 | New document that discusses how to enable or disable the alternate track button while streaming video |

