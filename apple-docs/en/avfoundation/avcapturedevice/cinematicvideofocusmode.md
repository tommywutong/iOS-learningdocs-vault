---
title: AVCaptureDevice.CinematicVideoFocusMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/cinematicvideofocusmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/cinematicvideofocusmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/cinematicvideofocusmode.json'
content_hash: 'sha256:14cf5cae6e48e119'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.CinematicVideoFocusMode

<sub>Enumeration</sub>

Constants indicating the focus behavior when recording a Cinematic Video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum CinematicVideoFocusMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Focus modes

- [AVCaptureCinematicVideoFocusModeNone](cinematicvideofocusmode/none.md) — Indicates that no focus mode is specified, in which case weak focus is used as default.
- [AVCaptureCinematicVideoFocusModeStrong](cinematicvideofocusmode/strong.md) — Indicates that the subject should remain in focus until it exits the scene.
- [AVCaptureCinematicVideoFocusModeWeak](cinematicvideofocusmode/weak.md) — Indicates that the Cinematic Video algorithm should automatically adjust focus according to the prominence of the subjects in the scene.

### Initializers

- [init(rawValue:)](<cinematicvideofocusmode/init(rawvalue_).md>)

## See Also

### Configuring Cinematic video

- [- setCinematicVideoFixedFocusAtPoint:focusMode:](<setcinematicvideofixedfocus(at_focusmode_).md>) — Fix focus at a distance.
- [- setCinematicVideoTrackingFocusAtPoint:focusMode:](<setcinematicvideotrackingfocus(at_focusmode_).md>) — Focus on and start tracking an object if it can be detected at the region specified by the point.
- [- setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:](<setcinematicvideotrackingfocus(detectedobjectid_focusmode_).md>) — Focus on and start tracking a detected object.
- [AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus.md) — An informative status about the scene observed by the device.
- [AVCaptureSceneMonitoringStatusNotEnoughLight](../avcapturescenemonitoringstatus/notenoughlight.md) — The light level of the current scene is insufficient for the current set of features to function optimally.
- [cinematicVideoCaptureSceneMonitoringStatuses](cinematicvideocapturescenemonitoringstatuses.md) — The current scene monitoring statuses related to Cinematic Video capture.
