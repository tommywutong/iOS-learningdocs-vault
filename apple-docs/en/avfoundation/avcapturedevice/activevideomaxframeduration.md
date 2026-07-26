---
title: activeVideoMaxFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.9+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/activevideomaxframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/activevideomaxframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/activevideomaxframeduration.json'
content_hash: 'sha256:c441879bc53c2b8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# activeVideoMaxFrameDuration

<sub>Instance Property</sub>

The currently active maximum frame duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var activeVideoMaxFrameDuration: CMTime { get set }
```

## Discussion

A device’s maximum frame duration is the reciprocal of its minimum frame rate. You can set the value of this property to limit the minimum frame rate during a capture session. The capture device automatically chooses a default maximum frame duration based on its active format. After changing the value of this property, you can return to the default maximum frame duration by setting this property’s value to [invalid](../../coremedia/cmtime/invalid.md). Choosing a new preset for the capture session also resets this property to its default value.

Attempting to set this property to a value not found in the active format’s [videoSupportedFrameRateRanges](format/videosupportedframerateranges.md) array raises an exception ([invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)).

> [!important] Important
> Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock.

This property value is key-value observable.

## See Also

### Configuring frame durations

- [activeVideoMinFrameDuration](activevideominframeduration.md) — The currently active minimum frame duration.
- [activeDepthDataMinFrameDuration](activedepthdataminframeduration.md) — The minimum frame duration of depth data.
