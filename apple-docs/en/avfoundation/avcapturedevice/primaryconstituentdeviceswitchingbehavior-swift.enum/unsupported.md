---
title: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported.json'
content_hash: 'sha256:8fe7230b12359d5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [PrimaryConstituentDeviceSwitchingBehavior](../primaryconstituentdeviceswitchingbehavior-swift.enum.md)

# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported

<sub>Case</sub>

The device doesn’t support constituent device switching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case unsupported
```

## Discussion

Switching cameras isn’t supported on devices that don’t have more than one constituent device.

## See Also

### Switching behaviors

- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorAuto](auto.md) — The device automatically selects the best camera for the current scene.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](restricted.md) — The device restricts fallback camera selection to certain conditions.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorLocked](locked.md) — The device locks camera switching to the active primary constituent device.
