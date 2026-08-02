---
title: Customizing subtitles with AVPlayer
apple_id: DTS40013643
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-08-17'
source_url: https://developer.apple.com/library/archive/qa/qa1794/_index.html
archived_at: '2026-07-18T02:34:45.524382Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1794

# Customizing subtitles with AVPlayer

## Q:  I'm trying to display a subtitle track with `AVPlayer` and set the text style using the `textStyleRules` property, but the text style remains unchanged. What am I doing wrong?

A: The `AVPlayer` `textStyleRules` property only applies to Web Video Text Tracks (WebVTT). Setting a text style with the `textStyleRules` property for local movie files (.mp4 or .mov) with subtitle tracks will have no effect on the text style.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-17 | New document that discusses customizing subtitles with AVPlayer |

