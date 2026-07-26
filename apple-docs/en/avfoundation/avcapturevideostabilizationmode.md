---
title: AVCaptureVideoStabilizationMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideostabilizationmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideostabilizationmode.json'
content_hash: 'sha256:08d4cb9d73ca9f13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureVideoStabilizationMode

<sub>Enumeration</sub>

An enumeration of video stabilization modes that capture devices and formats support.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum AVCaptureVideoStabilizationMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Stabilization modes

- [AVCaptureVideoStabilizationModeOff](avcapturevideostabilizationmode/off.md) — A mode that doesn’t stabilize video capture.
- [AVCaptureVideoStabilizationModeStandard](avcapturevideostabilizationmode/standard.md) — A mode that uses the standard algorithm.
- [AVCaptureVideoStabilizationModeCinematic](avcapturevideostabilizationmode/cinematic.md) — A mode that uses the cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeCinematicExtended](avcapturevideostabilizationmode/cinematicextended.md) — A mode that uses the extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModePreviewOptimized](avcapturevideostabilizationmode/previewoptimized.md) — A mode that uses the preview optimized stabilization algorithm.
- [AVCaptureVideoStabilizationModeCinematicExtendedEnhanced](avcapturevideostabilizationmode/cinematicextendedenhanced.md) — A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeAuto](avcapturevideostabilizationmode/auto.md) — A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.
- [AVCaptureVideoStabilizationModeLowLatency](avcapturevideostabilizationmode/lowlatency.md) — Indicates that video should be stabilized using the low latency stabilization algorithm. Low Latency stabilization has a reduced field of view. Enabling low latency stabilization introduces no additional latency into the video capture pipeline.

### Initializers

- [init(rawValue:)](<avcapturevideostabilizationmode/init(rawvalue_).md>)

## See Also

### Determining video stabilization support

- [- isVideoStabilizationModeSupported:](<avcapturedevice/format/isvideostabilizationmodesupported(__).md>) — A Boolean value that indicates whether the format supports a given video stabilization mode.
