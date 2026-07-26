---
title: videoFrameRateRangeForReactionEffectsInProgress
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videoframeraterangeforreactioneffectsinprogress
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforreactioneffectsinprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforreactioneffectsinprogress.json'
content_hash: 'sha256:8e8d62792ac46441'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFrameRateRangeForReactionEffectsInProgress

<sub>Instance Property</sub>

Indicates the minimum and maximum frame rates available when a reaction effect runs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoFrameRateRangeForReactionEffectsInProgress: AVFrameRateRange? { get }
```

## Discussion

Unlike other video effects, enabling reaction effects doesn’t limit the stream’s frame rate because most of the time the system isn’t rendering the effect. The frame rate only ramps down when the system renders a reaction on the stream.

## See Also

### Determining reaction effects support

- [reactionEffectsSupported](reactioneffectssupported.md) — A Boolean value that indicates whether the device supports reaction effects.
