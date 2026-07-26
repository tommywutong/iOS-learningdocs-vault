---
title: isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.json'
content_hash: 'sha256:8c2a08e78bc83215'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to restrict constituent device switching behavior during recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled: Bool { get set }
```

## Discussion

Use this property to enable camera switching restrictions when recording movies. You set restrictions by calling the output’s [- setPrimaryConstituentDeviceSwitchingBehaviorForRecording:restrictedSwitchingBehaviorConditions:](<setprimaryconstituentdeviceswitchingbehaviorforrecording(__restrictedswitchingbehaviorconditions_).md>) method. The restrictions take effect when you start recording, and revert to the behavior set by the capture device’s [primaryConstituentDeviceSwitchingBehavior](../avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.property.md) when you stop recording.

By default, this property is [true](../../swift/true.md) when connected to a capture device that supports constituent device switching.

## See Also

### Restricting camera switching

- [- setPrimaryConstituentDeviceSwitchingBehaviorForRecording:restrictedSwitchingBehaviorConditions:](<setprimaryconstituentdeviceswitchingbehaviorforrecording(__restrictedswitchingbehaviorconditions_).md>) — Sets the camera switching behavior to use during recording.
- [primaryConstituentDeviceSwitchingBehaviorForRecording](primaryconstituentdeviceswitchingbehaviorforrecording.md) — The camera switching behavior to use for recording.
- [primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording](primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md) — The conditions during which camera switching may occur while recording.
