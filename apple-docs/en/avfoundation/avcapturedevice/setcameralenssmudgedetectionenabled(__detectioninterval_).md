---
title: 'setCameraLensSmudgeDetectionEnabled(_:detectionInterval:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setcameralenssmudgedetectionenabled%28_%3Adetectioninterval%3A%29.json'
content_hash: 'sha256:6729078bf68e231e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setCameraLensSmudgeDetectionEnabled(_:detectionInterval:)

<sub>Instance Method</sub>

Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setCameraLensSmudgeDetectionEnabled(_ cameraLensSmudgeDetectionEnabled: Bool, detectionInterval: CMTime)
```

## Parameters

- `cameraLensSmudgeDetectionEnabled` — Specify whether camera lens smudge detection should be enabled.

- `detectionInterval` — The detection running interval if detection is enabled.

## Discussion

Each run of detection processes frames over a short period, and produces one detection result. Use `detectionInterval` to specify the interval time between each run of detections. For example, when [cameraLensSmudgeDetectionEnabled](iscameralenssmudgedetectionenabled.md) is set to `true` and `detectionInterval` is set to 1 minute, detection runs once per minute, and updates [AVCaptureCameraLensSmudgeDetectionStatus](../avcapturecameralenssmudgedetectionstatus.md). If `detectionInterval` is set to `kCMTimeInvalid`, detection runs only once after the session starts. If `detectionInterval` is set to `kCMTimeZero`, detection runs continuously.

[AVCaptureDevice](../avcapturedevice.md) throws an `NSInvalidArgumentException` if the [cameraLensSmudgeDetectionSupported](format/iscameralenssmudgedetectionsupported.md) property on the current active format returns `false`. Enabling detection requires a lengthy reconfiguration of the capture render pipeline, so you should enable detection before calling [- startRunning](<../avcapturesession/startrunning().md>) or within [- beginConfiguration](<../avcapturesession/beginconfiguration().md>) and [- commitConfiguration](<../avcapturesession/commitconfiguration().md>) while running.

## See Also

### Configuring lens smudge detection

- [cameraLensSmudgeDetectionEnabled](iscameralenssmudgedetectionenabled.md) — Whether camera lens smudge detection is enabled.
- [cameraLensSmudgeDetectionInterval](cameralenssmudgedetectioninterval.md) — The camera lens smudge detection interval.
- [cameraLensSmudgeDetectionStatus](cameralenssmudgedetectionstatus.md) — A value specifying the status of camera lens smudge detection.
- [AVCaptureCameraLensSmudgeDetectionStatus](../avcapturecameralenssmudgedetectionstatus.md) — Constants indicating the current camera lens smudge detection status.
