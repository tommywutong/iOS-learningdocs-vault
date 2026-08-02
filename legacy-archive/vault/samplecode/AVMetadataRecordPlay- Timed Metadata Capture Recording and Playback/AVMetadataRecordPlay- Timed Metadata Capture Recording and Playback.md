---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Introduction/Intro.html
archived_at: '2026-07-18T03:00:19.427073Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Objective-C-AVMetadataRecordPlay-main.m.md)

# AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2017-03-09 Adds Swift version [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnrvfvjgk5tjonuw63sinfzxi33spewui33oorggs3tlivwgk3lfnz2esrc7ge) |
| __Build Requirements:__ | Xcode 8.1, iOS SDK 10.0 |
| __Runtime Requirements:__ | iOS 10.0 |

The AVMetadataRecordPlay sample demonstrates how to use AVFoundation capture APIs to record and play movies with timed metadata content. The sample also shows how to use timed-metadata tracks to record detected-face, video orientation, and GPS metadata. When playing back content, the AVMetadataRecordPlay class reads the detected-face and GPS timed metadata tracks and uses it to render augmentations on the video layer to indicate their values. AVMetadataRecordPlay also reads the video orientation metadata and dynamically adjusts the video layer to properly render the content. The sample runs only on an actual device (iPad or iPhone); you can’t run it in the Simulator.

[Next](Objective-C-AVMetadataRecordPlay-main.m.md)

