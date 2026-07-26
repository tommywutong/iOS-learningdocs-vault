---
title: 'setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_:restrictedSwitchingBehaviorConditions:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(_:restrictedswitchingbehaviorconditions:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(_:restrictedswitchingbehaviorconditions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording%28_%3Arestrictedswitchingbehaviorconditions%3A%29.json'
content_hash: 'sha256:7f871ba0147a51a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_:restrictedSwitchingBehaviorConditions:)

<sub>Instance Method</sub>

Sets the camera switching behavior to use during recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_ switchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)
```

## Parameters

- `switchingBehavior` — The switching behavior to set on the movie file output. Attempting to restrict the switching behavior of a capture device that doesn’t support constituent device switching results in an error.

- `restrictedSwitchingBehaviorConditions` — The conditions during which camera switching occurs. Only set a condition when you set the switching behavior to [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](../avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md). In all other cases, set the value to [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionNone](../avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditions/avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditionnone.md).

## Discussion

Use this method to control the camera switching behavior the system uses when recording a movie. The behavior you specify takes effect when you enable it by setting the value of [primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled](isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md) to [true](../../swift/true.md).

When a capture device doesn’t support constituent device selection, attempting to set a behavior other than [AVCapturePrimaryConstituentDeviceSwitchingBehaviorUnsupported](../avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported.md) causes the system to throw an invalid argument exception.

## See Also

### Restricting camera switching

- [primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled](isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md) — A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [primaryConstituentDeviceSwitchingBehaviorForRecording](primaryconstituentdeviceswitchingbehaviorforrecording.md) — The camera switching behavior to use for recording.
- [primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording](primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md) — The conditions during which camera switching may occur while recording.
