---
title: requiresFrameReordering
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/requiresframereordering
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/requiresframereordering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/requiresframereordering.json'
content_hash: 'sha256:46bb85492cc31b3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# requiresFrameReordering

<sub>Type Property</sub>

A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var requiresFrameReordering: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading frame-based characteristics

- [nominalFrameRate](nominalframerate.md) — The frame rate of the track, in frames per second.
- [minFrameDuration](minframeduration.md) — The minimum duration of the track’s frames.
