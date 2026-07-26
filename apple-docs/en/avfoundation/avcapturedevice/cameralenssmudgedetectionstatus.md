---
title: cameraLensSmudgeDetectionStatus
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/cameralenssmudgedetectionstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectionstatus.json'
content_hash: 'sha256:31f775150979e890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# cameraLensSmudgeDetectionStatus

<sub>Instance Property</sub>

A value specifying the status of camera lens smudge detection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus { get }
```

## Discussion

During initial detection execution, [cameraLensSmudgeDetectionStatus](cameralenssmudgedetectionstatus.md) returns `AVCaptureCameraLensSmudgeDetectionStatusUnknown` until the detection result settles. Once a detection result is produced, [cameraLensSmudgeDetectionStatus](cameralenssmudgedetectionstatus.md) returns the most recent detection result. This property can be key-value observed.

## See Also

### Configuring lens smudge detection

- [cameraLensSmudgeDetectionEnabled](iscameralenssmudgedetectionenabled.md) — Whether camera lens smudge detection is enabled.
- [- setCameraLensSmudgeDetectionEnabled:detectionInterval:](<setcameralenssmudgedetectionenabled(__detectioninterval_).md>) — Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [cameraLensSmudgeDetectionInterval](cameralenssmudgedetectioninterval.md) — The camera lens smudge detection interval.
- [AVCaptureCameraLensSmudgeDetectionStatus](../avcapturecameralenssmudgedetectionstatus.md) — Constants indicating the current camera lens smudge detection status.
