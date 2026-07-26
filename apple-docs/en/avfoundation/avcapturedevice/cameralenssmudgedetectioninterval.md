---
title: cameraLensSmudgeDetectionInterval
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/cameralenssmudgedetectioninterval
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectioninterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectioninterval.json'
content_hash: 'sha256:d3ff84a83697ad3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# cameraLensSmudgeDetectionInterval

<sub>Instance Property</sub>

The camera lens smudge detection interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var cameraLensSmudgeDetectionInterval: CMTime { get }
```

## Discussion

[cameraLensSmudgeDetectionInterval](cameralenssmudgedetectioninterval.md) is set by calling [- setCameraLensSmudgeDetectionEnabled:detectionInterval:](<setcameralenssmudgedetectionenabled(__detectioninterval_).md>). By default, this property returns `kCMTimeInvalid`.

## See Also

### Configuring lens smudge detection

- [cameraLensSmudgeDetectionEnabled](iscameralenssmudgedetectionenabled.md) — Whether camera lens smudge detection is enabled.
- [- setCameraLensSmudgeDetectionEnabled:detectionInterval:](<setcameralenssmudgedetectionenabled(__detectioninterval_).md>) — Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [cameraLensSmudgeDetectionStatus](cameralenssmudgedetectionstatus.md) — A value specifying the status of camera lens smudge detection.
- [AVCaptureCameraLensSmudgeDetectionStatus](../avcapturecameralenssmudgedetectionstatus.md) — Constants indicating the current camera lens smudge detection status.
