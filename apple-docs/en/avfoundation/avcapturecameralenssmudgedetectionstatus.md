---
title: AVCaptureCameraLensSmudgeDetectionStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturecameralenssmudgedetectionstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturecameralenssmudgedetectionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturecameralenssmudgedetectionstatus.json'
content_hash: 'sha256:d2852c262d79ce22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureCameraLensSmudgeDetectionStatus

<sub>Enumeration</sub>

Constants indicating the current camera lens smudge detection status.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum AVCaptureCameraLensSmudgeDetectionStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVCaptureCameraLensSmudgeDetectionStatusDisabled](avcapturecameralenssmudgedetectionstatus/disabled.md) — Indicates that the detection is not enabled.
- [AVCaptureCameraLensSmudgeDetectionStatusSmudgeNotDetected](avcapturecameralenssmudgedetectionstatus/smudgenotdetected.md) — Indicates that the most recent detection found no smudge on the camera lens.
- [AVCaptureCameraLensSmudgeDetectionStatusSmudged](avcapturecameralenssmudgedetectionstatus/smudged.md) — Indicates that the most recent detection found the camera lens to be smudged.
- [AVCaptureCameraLensSmudgeDetectionStatusUnknown](avcapturecameralenssmudgedetectionstatus/unknown.md) — Indicates that the detection result has not settled, commonly caused by excessive camera movement or the content of the scene.

### Initializers

- [init(rawValue:)](<avcapturecameralenssmudgedetectionstatus/init(rawvalue_).md>)

## See Also

### Configuring lens smudge detection

- [cameraLensSmudgeDetectionEnabled](avcapturedevice/iscameralenssmudgedetectionenabled.md) — Whether camera lens smudge detection is enabled.
- [- setCameraLensSmudgeDetectionEnabled:detectionInterval:](<avcapturedevice/setcameralenssmudgedetectionenabled(__detectioninterval_).md>) — Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [cameraLensSmudgeDetectionInterval](avcapturedevice/cameralenssmudgedetectioninterval.md) — The camera lens smudge detection interval.
- [cameraLensSmudgeDetectionStatus](avcapturedevice/cameralenssmudgedetectionstatus.md) — A value specifying the status of camera lens smudge detection.
