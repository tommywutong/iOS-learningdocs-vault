---
title: isCameraLensSmudgeDetectionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/iscameralenssmudgedetectionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscameralenssmudgedetectionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/iscameralenssmudgedetectionenabled.json'
content_hash: 'sha256:808e86ff87f736e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isCameraLensSmudgeDetectionEnabled

<sub>Instance Property</sub>

Whether camera lens smudge detection is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isCameraLensSmudgeDetectionEnabled: Bool { get }
```

## Discussion

You enable lens smudge detection by calling [- setCameraLensSmudgeDetectionEnabled:detectionInterval:](<setcameralenssmudgedetectionenabled(__detectioninterval_).md>). By default, this property is returns `false`.

## See Also

### Configuring lens smudge detection

- [- setCameraLensSmudgeDetectionEnabled:detectionInterval:](<setcameralenssmudgedetectionenabled(__detectioninterval_).md>) — Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [cameraLensSmudgeDetectionInterval](cameralenssmudgedetectioninterval.md) — The camera lens smudge detection interval.
- [cameraLensSmudgeDetectionStatus](cameralenssmudgedetectionstatus.md) — A value specifying the status of camera lens smudge detection.
- [AVCaptureCameraLensSmudgeDetectionStatus](../avcapturecameralenssmudgedetectionstatus.md) — Constants indicating the current camera lens smudge detection status.
