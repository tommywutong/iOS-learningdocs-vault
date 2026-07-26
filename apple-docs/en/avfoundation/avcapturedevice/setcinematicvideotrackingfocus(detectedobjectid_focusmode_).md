---
title: 'setCinematicVideoTrackingFocus(detectedObjectID:focusMode:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setcinematicvideotrackingfocus(detectedobjectid:focusmode:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setcinematicvideotrackingfocus(detectedobjectid:focusmode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setcinematicvideotrackingfocus%28detectedobjectid%3Afocusmode%3A%29.json'
content_hash: 'sha256:934914aa4b0e5b2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setCinematicVideoTrackingFocus(detectedObjectID:focusMode:)

<sub>Instance Method</sub>

Focus on and start tracking a detected object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)
```

## Parameters

- `detectedObjectID` — The ID of the detected object.

- `focusMode` — Specify whether to focus strongly or weakly.

## See Also

### Configuring Cinematic video

- [- setCinematicVideoFixedFocusAtPoint:focusMode:](<setcinematicvideofixedfocus(at_focusmode_).md>) — Fix focus at a distance.
- [- setCinematicVideoTrackingFocusAtPoint:focusMode:](<setcinematicvideotrackingfocus(at_focusmode_).md>) — Focus on and start tracking an object if it can be detected at the region specified by the point.
- [CinematicVideoFocusMode](cinematicvideofocusmode.md) — Constants indicating the focus behavior when recording a Cinematic Video.
- [AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus.md) — An informative status about the scene observed by the device.
- [AVCaptureSceneMonitoringStatusNotEnoughLight](../avcapturescenemonitoringstatus/notenoughlight.md) — The light level of the current scene is insufficient for the current set of features to function optimally.
- [cinematicVideoCaptureSceneMonitoringStatuses](cinematicvideocapturescenemonitoringstatuses.md) — The current scene monitoring statuses related to Cinematic Video capture.
