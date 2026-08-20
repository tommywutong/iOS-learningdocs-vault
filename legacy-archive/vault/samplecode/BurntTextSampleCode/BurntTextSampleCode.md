---
title: BurntTextSampleCode
apple_id: DTS10001014
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BurntTextSampleCode/Introduction/Intro.html
archived_at: '2026-07-18T03:02:20.240286Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ConvertTextMovie.c.md)

# BurntTextSampleCode

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Converts text tracks of a movie to new text tracks with bit map representations of the text. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

ConvertMovie makes a copy of a movie, converting its text tracks to new text tracks with bit map representations of the text. The displayFlags parameter allows one to add new display flags (such as normally time consuming antialias and drop shadow) for the bit map images. The imageTrack parameter indicates whether to save an image of the entire text track or just the text box (as specified by the defaultTextBox field of the text descriptor). The spatial parameter is a pointer to a compression information data structure that specifies how to compress the text bit maps. Note that the resulting movie file (as specified by the dstSpec parameter) will need to be flattened if it contained any non-text tracks in order to make it self-contained. Requires: QuickTime Keywords: QuickTime, movie, convert, text, track

[Next](ConvertTextMovie.c.md)

