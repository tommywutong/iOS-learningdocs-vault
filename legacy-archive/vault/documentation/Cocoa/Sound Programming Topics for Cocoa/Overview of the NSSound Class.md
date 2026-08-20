---
title: Sound Programming Topics for Cocoa
apple_id: 10000104i
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AppKit
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sound/Concepts/NSSound.html
archived_at: '2026-07-15T07:19:15.000872Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sound Programming Topics for Cocoa](Introduction%20to%20Sound%20Programming%20Topics%20for%20Cocoa.md)


[Next](Loading%20Audio%20Data.md)[Previous](Introduction%20to%20Sound%20Programming%20Topics%20for%20Cocoa.md)

# Overview of the NSSound Class

The `NSSound` class makes it extremely simple for Cocoa applications to load and play sound files. Instance methods provide standard transport control so that a sound can be programmatically started, stopped and paused.

The class supports the following file and data formats:

- File Formats:

  - AIFF
  - WAV
  - NeXT SND

- Data Formats:

  - 16 bit
  - 44.1 Khz
  - 22.05 KHz
  - Mono
  - Stereo

You can load audio data into an `NSSound` object from three sources:

1. a disk file—using a pathname or URL
2. network connection—using a URL
3. the pasteboard

The `NSSound` class can search for named sound resources in the application’s main bundle as well as two standard file system locations: `/Library/Sounds` and `~/Library/Sounds`.

[Next](Loading%20Audio%20Data.md)[Previous](Introduction%20to%20Sound%20Programming%20Topics%20for%20Cocoa.md)

