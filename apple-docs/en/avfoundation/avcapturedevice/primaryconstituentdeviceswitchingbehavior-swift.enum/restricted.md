---
title: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.json'
content_hash: 'sha256:f6a147b9b1d0f23f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [PrimaryConstituentDeviceSwitchingBehavior](../primaryconstituentdeviceswitchingbehavior-swift.enum.md)

# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted

<sub>Case</sub>

The device restricts fallback camera selection to certain conditions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case restricted
```

## Discussion

The camera doesn’t restrict camera switches necessary to honor the requested video zoom factor.

## See Also

### Switching behaviors

- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorUnsupported](unsupported.md) — The device doesn’t support constituent device switching.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorAuto](auto.md) — The device automatically selects the best camera for the current scene.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorLocked](locked.md) — The device locks camera switching to the active primary constituent device.
