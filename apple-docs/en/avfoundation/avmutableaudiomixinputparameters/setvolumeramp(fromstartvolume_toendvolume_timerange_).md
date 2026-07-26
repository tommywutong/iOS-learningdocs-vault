---
title: 'setVolumeRamp(fromStartVolume:toEndVolume:timeRange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutableaudiomixinputparameters/setvolumeramp(fromstartvolume:toendvolume:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/setvolumeramp(fromstartvolume:toendvolume:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableaudiomixinputparameters/setvolumeramp%28fromstartvolume%3Atoendvolume%3Atimerange%3A%29.json'
content_hash: 'sha256:35d33f87a00c1654'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md)

# setVolumeRamp(fromStartVolume:toEndVolume:timeRange:)

<sub>Instance Method</sub>

Sets a volume ramp to apply during a specified time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setVolumeRamp(fromStartVolume startVolume: Float, toEndVolume endVolume: Float, timeRange: CMTimeRange)
```

## Parameters

- `startVolume` — The starting volume. The value must be between `0.0` and 1.0.

- `endVolume` — The end volume. The value must be between `0.0` and `1.0`.

- `timeRange` — The time range over which to apply the ramp.

## See Also

### Setting the volume

- [- setVolume:atTime:](<setvolume(__at_).md>) — Sets the value of the audio volume starting at the specified time.
