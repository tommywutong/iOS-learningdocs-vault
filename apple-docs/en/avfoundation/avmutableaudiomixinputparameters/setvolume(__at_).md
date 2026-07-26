---
title: 'setVolume(_:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutableaudiomixinputparameters/setvolume(_:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/setvolume(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableaudiomixinputparameters/setvolume%28_%3Aat%3A%29.json'
content_hash: 'sha256:775e871048eb0271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md)

# setVolume(_:at:)

<sub>Instance Method</sub>

Sets the value of the audio volume starting at the specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setVolume(_ volume: Float, at time: CMTime)
```

## Parameters

- `volume` — The volume. The value must be between `0.0` and `1.0`.

- `time` — The start time at which to set the volume.

## Discussion

This method adds a volume ramp starting at `time`. This volume setting remains in effect until the end of the track unless you set a different volume level to start at a later time.

## See Also

### Setting the volume

- [- setVolumeRampFromStartVolume:toEndVolume:timeRange:](<setvolumeramp(fromstartvolume_toendvolume_timerange_).md>) — Sets a volume ramp to apply during a specified time range.
