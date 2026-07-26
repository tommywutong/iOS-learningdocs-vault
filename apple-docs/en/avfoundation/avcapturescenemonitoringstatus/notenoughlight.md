---
title: notEnoughLight
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescenemonitoringstatus/notenoughlight
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescenemonitoringstatus/notenoughlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescenemonitoringstatus/notenoughlight.json'
content_hash: 'sha256:56b12b178bcc7790'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus.md)

# notEnoughLight

<sub>Type Property</sub>

The light level of the current scene is insufficient for the current set of features to function optimally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static let notEnoughLight: AVCaptureSceneMonitoringStatus
```

## See Also

### Configuring Cinematic video

- [- setCinematicVideoFixedFocusAtPoint:focusMode:](<../avcapturedevice/setcinematicvideofixedfocus(at_focusmode_).md>) — Fix focus at a distance.
- [- setCinematicVideoTrackingFocusAtPoint:focusMode:](<../avcapturedevice/setcinematicvideotrackingfocus(at_focusmode_).md>) — Focus on and start tracking an object if it can be detected at the region specified by the point.
- [- setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:](<../avcapturedevice/setcinematicvideotrackingfocus(detectedobjectid_focusmode_).md>) — Focus on and start tracking a detected object.
- [CinematicVideoFocusMode](../avcapturedevice/cinematicvideofocusmode.md) — Constants indicating the focus behavior when recording a Cinematic Video.
- [AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus.md) — An informative status about the scene observed by the device.
- [cinematicVideoCaptureSceneMonitoringStatuses](../avcapturedevice/cinematicvideocapturescenemonitoringstatuses.md) — The current scene monitoring statuses related to Cinematic Video capture.
