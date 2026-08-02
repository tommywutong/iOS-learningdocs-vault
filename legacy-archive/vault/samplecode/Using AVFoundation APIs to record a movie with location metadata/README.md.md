---
title: Using AVFoundation APIs to record a movie with location metadata
apple_id: TP40014494
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCaptureLocation/Listings/README_md.html
archived_at: '2026-07-18T03:00:03.743293Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVFoundation APIs to record a movie with location metadata](Using%20AVFoundation%20APIs%20to%20record%20a%20movie%20with%20location%20metadata.md)


[Next](AVCaptureLocation-main.m.md)[Previous](Using%20AVFoundation%20APIs%20to%20record%20a%20movie%20with%20location%20metadata.md)

# README.md

```
# Using AVFoundation APIs to write a movie with location timed metadata

This sample shows how to use AVAssetWriterInputMetadataAdaptor API to write timed location metadata, obtained from CoreLocation, during live video capture. The captured movie file has video, audio and metadata track. The metadata track contains location corresponding to where the video was recorded.

## Requirements

Xcode 5.0 or later, iOS 8 or later

### Build

Xcode 5.0 or later, iOS 8 SDK

### Runtime

iOS 8 or later

### Note

The recorded movie will contain metadata in a separate track. To visualize it you would have to use AVAssetReaderOutputMetadataAdaptor or AVPlayerItemMetadataOutput.

Copyright (C) 2014 Apple Inc. All rights reserved.
```

[Next](AVCaptureLocation-main.m.md)[Previous](Using%20AVFoundation%20APIs%20to%20record%20a%20movie%20with%20location%20metadata.md)

