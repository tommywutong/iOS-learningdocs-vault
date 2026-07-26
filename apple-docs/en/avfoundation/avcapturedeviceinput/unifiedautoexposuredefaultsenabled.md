---
title: unifiedAutoExposureDefaultsEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/unifiedautoexposuredefaultsenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/unifiedautoexposuredefaultsenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/unifiedautoexposuredefaultsenabled.json'
content_hash: 'sha256:5bc9f757faa052fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# unifiedAutoExposureDefaultsEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the input enables unified auto-exposure defaults.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var unifiedAutoExposureDefaultsEnabled: Bool { get set }
```

## Discussion

You may set the value of a capture device’s [activeFormat](../avcapturedevice/activeformat.md) in two ways:

1. Set it directly using one of the formats in the device’s [formats](../avcapturedevice/formats.md) property.
2. The capture session sets it on your behalf when you set its [sessionPreset](../avcapturesession/sessionpreset.md) property.

Depending on the device and format, you may configure the default auto exposure behavior differently when you use one method or the other, resulting in non-uniform auto exposure behavior. Auto exposure defaults include [minFrameRate](../avframeraterange/minframerate.md), [maxFrameRate](../avframeraterange/maxframerate.md), and [maxExposureDuration](../avcapturedevice/format/maxexposureduration.md). You can set this property to [true](../../swift/true.md) to ensure that the system applies consistent default behaviors to the device regardless of the way you set the active format.

The default value is [false](../../swift/false.md).

> [!note] Note
> Manually setting the device’s [minFrameRate](../avframeraterange/minframerate.md), [maxFrameRate](../avframeraterange/maxframerate.md), or [maxExposureDuration](../avcapturedevice/format/maxexposureduration.md) overrides the device defaults, even if you set this property to [true](../../swift/true.md).

## See Also

### Configuring video properties

- [videoMinFrameDurationOverride](videominframedurationoverride.md) — A time value that acts as a modifier to a capture device’s active video minimum frame duration.
