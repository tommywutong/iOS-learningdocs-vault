---
title: nominalFrameRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/nominalframerate
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/nominalframerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/nominalframerate.json'
content_hash: 'sha256:f04ebdc004107f8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# nominalFrameRate

<sub>Type Property</sub>

The frame rate of the track, in frames per second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var nominalFrameRate: AVAsyncProperty<Root, Float> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

## See Also

### Loading frame-based characteristics

- [minFrameDuration](minframeduration.md) — The minimum duration of the track’s frames.
- [requiresFrameReordering](requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
