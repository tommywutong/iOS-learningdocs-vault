---
title: 'getVolumeRamp(for:startVolume:endVolume:timeRange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avaudiomixinputparameters/getvolumeramp(for:startvolume:endvolume:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/getvolumeramp(for:startvolume:endvolume:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiomixinputparameters/getvolumeramp%28for%3Astartvolume%3Aendvolume%3Atimerange%3A%29.json'
content_hash: 'sha256:197cdd9b83dc9bba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAudioMixInputParameters](../avaudiomixinputparameters.md)

# getVolumeRamp(for:startVolume:endVolume:timeRange:)

<sub>Instance Method</sub>

Retrieves the volume ramp that includes the specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getVolumeRamp(for time: CMTime, startVolume: UnsafeMutablePointer<Float>?, endVolume: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool
```

## Parameters

- `time` — If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.

- `startVolume` — A pointer to a float to receive the starting volume value for the volume ramp. This value may be `NULL`.

- `endVolume` — A pointer to a float to receive the ending volume value for the volume ramp. This value may be `NULL`.

- `timeRange` — A pointer to a [CMTimeRange](../../coremedia/cmtimerange.md) to receive the time range of the volume ramp. This value may be `NULL`.

## Return Value

[true](../../swift/true.md) if the values were retrieved successfully, otherwise [false](../../swift/false.md). Returns [false](../../swift/false.md) if `time` is beyond the duration of the last volume ramp that has been set.

## Discussion

The process of setting up volume ramps requires the configuration of an instance of [AVMutableAudioMixInputParameters](../avmutableaudiomixinputparameters.md).
