---
title: primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.json'
content_hash: 'sha256:d16c3f04078b8c2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording

<sub>Instance Property</sub>

The conditions during which camera switching may occur while recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions { get }
```

## Discussion

The default conditions include [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionVideoZoomChanged](../avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md), [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionFocusModeChanged](../avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/focusmodechanged.md), and [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionExposureModeChanged](../avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/exposuremodechanged.md).

This property is key-value observable.

## See Also

### Restricting camera switching

- [primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled](isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md) — A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [- setPrimaryConstituentDeviceSwitchingBehaviorForRecording:restrictedSwitchingBehaviorConditions:](<setprimaryconstituentdeviceswitchingbehaviorforrecording(__restrictedswitchingbehaviorconditions_).md>) — Sets the camera switching behavior to use during recording.
- [primaryConstituentDeviceSwitchingBehaviorForRecording](primaryconstituentdeviceswitchingbehaviorforrecording.md) — The camera switching behavior to use for recording.
