---
title: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.locked
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/locked
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/locked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/locked.json'
content_hash: 'sha256:018d7b62eee7a2f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [PrimaryConstituentDeviceSwitchingBehavior](../primaryconstituentdeviceswitchingbehavior-swift.enum.md)

# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.locked

<sub>Case</sub>

The device locks camera switching to the active primary constituent device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case locked
```

## Discussion

A locked value restricts the [minAvailableVideoZoomFactor](../minavailablevideozoomfactor.md) property value to the switch-over zoom factor of the active primary constituent device. See [virtualDeviceSwitchOverVideoZoomFactors](../virtualdeviceswitchovervideozoomfactors.md) for more information.

## See Also

### Switching behaviors

- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorUnsupported](unsupported.md) — The device doesn’t support constituent device switching.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorAuto](auto.md) — The device automatically selects the best camera for the current scene.
- [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](restricted.md) — The device restricts fallback camera selection to certain conditions.
