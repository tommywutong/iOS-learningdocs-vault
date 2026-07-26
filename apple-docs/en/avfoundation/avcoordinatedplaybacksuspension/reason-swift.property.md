---
title: reason
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.property.json'
content_hash: 'sha256:0e2d9ff682058b25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCoordinatedPlaybackSuspension](../avcoordinatedplaybacksuspension.md)

# reason

<sub>Instance Property</sub>

The reason for the suspension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var reason: AVCoordinatedPlaybackSuspension.Reason { get }
```

## Discussion

The coordinator communicates the suspension reason to other participants.

## See Also

### Inspecting a suspension

- [beginDate](begindate.md) — The time the suspension begins.
- [Reason](reason-swift.struct.md) — Constants that identify playback suspension reasons.
