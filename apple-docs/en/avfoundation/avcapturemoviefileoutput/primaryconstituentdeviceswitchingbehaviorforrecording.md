---
title: primaryConstituentDeviceSwitchingBehaviorForRecording
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording.json'
content_hash: 'sha256:3dba6725f21c7a4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# primaryConstituentDeviceSwitchingBehaviorForRecording

<sub>Instance Property</sub>

The camera switching behavior to use for recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var primaryConstituentDeviceSwitchingBehaviorForRecording: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior { get }
```

## Discussion

The default value of this property is [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](../avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md).

This property is key-value observable.

## See Also

### Restricting camera switching

- [primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled](isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md) — A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [- setPrimaryConstituentDeviceSwitchingBehaviorForRecording:restrictedSwitchingBehaviorConditions:](<setprimaryconstituentdeviceswitchingbehaviorforrecording(__restrictedswitchingbehaviorconditions_).md>) — Sets the camera switching behavior to use during recording.
- [primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording](primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md) — The conditions during which camera switching may occur while recording.
