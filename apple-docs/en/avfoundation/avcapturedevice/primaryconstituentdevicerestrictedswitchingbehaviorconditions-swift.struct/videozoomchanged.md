---
title: videoZoomChanged
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.json'
content_hash: 'sha256:7738bb0661c3be59'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](../primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct.md)

# videoZoomChanged

<sub>Type Property</sub>

Restrict switching to a fallback camera only when the device’s video zoom changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static var videoZoomChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions { get }
```

## Discussion

This condition switches cameras when the video zoom factor changes, either by setting a value for the device’s [videoZoomFactor](../videozoomfactor.md) property or calling its [- rampToVideoZoomFactor:withRate:](<../ramp(tovideozoomfactor_withrate_).md>) method.

> [!note] Note
> All changes to video zoom factor allow switching to a fallback camera, not only those changes across switch-over zoom factors.

## See Also

### Switching behavior conditions

- [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionExposureModeChanged](exposuremodechanged.md) — Restrict switching to a fallback camera only when the device’s exposure mode changes.
- [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionFocusModeChanged](focusmodechanged.md) — Restrict switching to a fallback camera only when the device’s focus mode changes.
