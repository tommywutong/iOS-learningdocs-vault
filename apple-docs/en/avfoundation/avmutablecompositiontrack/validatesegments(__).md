---
title: 'validateSegments(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecompositiontrack/validatesegments(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/validatesegments(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/validatesegments%28_%3A%29.json'
content_hash: 'sha256:ca8702cc7e430165'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# validateSegments(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given array of track segments conform to the timing rules for a composition track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func validateSegments(_ trackSegments: [AVCompositionTrackSegment]) throws
```

## Parameters

- `trackSegments` — The track segments to validate.
