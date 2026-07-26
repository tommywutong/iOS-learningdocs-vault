---
title: 'init(numberOfFrames:duration:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplannedvideosegmentconfiguration/init(numberofframes:duration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentconfiguration/init(numberofframes:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedvideosegmentconfiguration/init%28numberofframes%3Aduration%3A%29.json'
content_hash: 'sha256:7fd2fc714593217a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedVideoSegmentConfiguration](../avplannedvideosegmentconfiguration.md)

# init(numberOfFrames:duration:)

<sub>Initializer</sub>

Creates an instance of AVPlannedVideoSegmentConfiguration specifying the number of frames in and total duration of the segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(numberOfFrames frameCount: Int, duration: CMTime)
```

## Parameters

- `frameCount` — The number of frames in this planned video segment.

- `duration` — The duration of this planned video segment.

## Return Value

An instance of AVPlannedVideoSegmentConfiguration.

## Discussion

For best results, frameCount and duration should be greater or equal to the minimumFrameCount and minimumDuration of AVPlannedVideoSegmentBoundaryGuidelines respectively. This initializer throws NSInvalidArgumentException if frameCount is less than or equal to 0, or duration is not numeric, or duration is less than or equal to 0.
