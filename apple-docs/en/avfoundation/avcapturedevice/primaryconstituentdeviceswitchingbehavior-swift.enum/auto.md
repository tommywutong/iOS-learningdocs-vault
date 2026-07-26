---
title: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.auto
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/auto
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/auto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/auto.json'
content_hash: 'sha256:ffe405c58b28543e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [PrimaryConstituentDeviceSwitchingBehavior](../primaryconstituentdeviceswitchingbehavior-swift.enum.md)

# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.auto

<sub>Case</sub>

The device automatically selects the best camera for the current scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case auto
```

## Discussion

This mode places no restrictions on when a camera switch can occur.

## See Also

### Switching behaviors

- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorUnsupported](unsupported.md) — The device doesn’t support constituent device switching.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](restricted.md) — The device restricts fallback camera selection to certain conditions.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorLocked](locked.md) — The device locks camera switching to the active primary constituent device.
