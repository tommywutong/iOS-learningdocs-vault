---
title: activeDepthDataMinFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/activedepthdataminframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/activedepthdataminframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/activedepthdataminframeduration.json'
content_hash: 'sha256:a8cbe9f90aa7139b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# activeDepthDataMinFrameDuration

<sub>Instance Property</sub>

The minimum frame duration of depth data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var activeDepthDataMinFrameDuration: CMTime { get set }
```

## Discussion

Use this property to set an upper limit to the frame rate at which the system produces depth data. Lowering the depth data frame rate typically lowers power consumption which increases the time the camera can run before it reaches an elevated system pressure state. Setting a value outside the active depth data format’s supported frame rate range produces an exception.

Setting this property to [invalid](../../coremedia/cmtime/invalid.md) resets it to the active depth data format’s default minimum frame duration. Setting this property to [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md) results in a depth data frame rate of `0`.

This value gets reset whenever either the active video format or the active depth data format changes.

> [!important] Important
> Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock.

## See Also

### Configuring frame durations

- [activeVideoMinFrameDuration](activevideominframeduration.md) — The currently active minimum frame duration.
- [activeVideoMaxFrameDuration](activevideomaxframeduration.md) — The currently active maximum frame duration.
