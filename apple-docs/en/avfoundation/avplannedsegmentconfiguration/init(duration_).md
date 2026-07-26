---
title: 'init(duration:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplannedsegmentconfiguration/init(duration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentconfiguration/init(duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentconfiguration/init%28duration%3A%29.json'
content_hash: 'sha256:99c8603f1ae56d6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedSegmentConfiguration](../avplannedsegmentconfiguration.md)

# init(duration:)

<sub>Initializer</sub>

Creates an instance of AVPlannedSegmentConfiguration specifying the duration of the planned segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(duration: CMTime)
```

## Parameters

- `duration` — The total duration of this planned segment. If an empty edit is included, this duration may be larger than the sum of the durations of the samples in this planned segment.

## Return Value

An instance of AVPlannedSegmentConfiguration, or nil if initialization fails.

## Discussion

The duration parameter must be numeric and greater than 0. Otherwise, the initializer throws NSInvalidArgumentException.
