---
title: AVCompositionDebugViewer
apple_id: DTS40013400
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/AVCompositionDebugViewer/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:00:08.576796Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCompositionDebugViewer](AVCompositionDebugViewer.md)


[Next](AVCompositionDebugViewer-APLAppDelegate.h.md)[Previous](AVCompositionDebugViewer.md)

# ReadMe.txt

```
AVCompositionDebugViewer

This sample application has an AVCompositionDebugView which presents a visual description of the underlying AVComposition, AVVideoComposition and AVAudioMix objects which form the composition made using two clips, adding a cross fade transition in between and audio ramps to the two audio tracks.

The main files are as follows:

APLAppDelegate.m/.h:
The app delegate setups playback of AVMutableComposition and also initializes an APLCompositionDebugView which then represents the underlying composition, video composition and audio mix

APLSimpleEditor.m/.h:
Simple editor setups an AVMutableComposition using supplied clips and time ranges. It also setups AVVideoComposition to add a crossfade transition.

AVCompositionDebugView.m/.h:
 A subclass of NSView that represents the composition, video composition and audio mix objects in a diagram. It also contains a time marker layer which is synchronized to the current player item using AVSynchronizedLayer, to track the currentTime of a player.

main.m:
Standard main file.

========================================================================
Copyright © 2013 Apple Inc. All rights reserved.
```

[Next](AVCompositionDebugViewer-APLAppDelegate.h.md)[Previous](AVCompositionDebugViewer.md)

