---
title: cinematicVideoCaptureSceneMonitoringStatuses
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/cinematicvideocapturescenemonitoringstatuses
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/cinematicvideocapturescenemonitoringstatuses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/cinematicvideocapturescenemonitoringstatuses.json'
content_hash: 'sha256:27ec35afd5551a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# cinematicVideoCaptureSceneMonitoringStatuses

<sub>Instance Property</sub>

The current scene monitoring statuses related to Cinematic Video capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var cinematicVideoCaptureSceneMonitoringStatuses: Set<AVCaptureSceneMonitoringStatus> { get }
```

## Discussion

Monitor this property via key-value observation to present a UI informing the user that they should reframe their scene for a better Cinematic Video experience (“scene is too dark”).

## See Also

### Configuring Cinematic video

- [- setCinematicVideoFixedFocusAtPoint:focusMode:](<setcinematicvideofixedfocus(at_focusmode_).md>) — Fix focus at a distance.
- [- setCinematicVideoTrackingFocusAtPoint:focusMode:](<setcinematicvideotrackingfocus(at_focusmode_).md>) — Focus on and start tracking an object if it can be detected at the region specified by the point.
- [- setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:](<setcinematicvideotrackingfocus(detectedobjectid_focusmode_).md>) — Focus on and start tracking a detected object.
- [CinematicVideoFocusMode](cinematicvideofocusmode.md) — Constants indicating the focus behavior when recording a Cinematic Video.
- [AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus.md) — An informative status about the scene observed by the device.
- [AVCaptureSceneMonitoringStatusNotEnoughLight](../avcapturescenemonitoringstatus/notenoughlight.md) — The light level of the current scene is insufficient for the current set of features to function optimally.
