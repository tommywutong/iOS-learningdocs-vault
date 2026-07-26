---
title: AVCaptureVideoStabilizationMode.standard
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideostabilizationmode/standard
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideostabilizationmode/standard.json'
content_hash: 'sha256:1cb332fa81e8b5d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoStabilizationMode](../avcapturevideostabilizationmode.md)

# AVCaptureVideoStabilizationMode.standard

<sub>Case</sub>

A mode that uses the standard algorithm.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case standard
```

## Discussion

Standard video stabilization has a reduced field of view. Enabling video stabilization may introduce additional latency into the video capture pipeline.

## See Also

### Stabilization modes

- [AVCaptureVideoStabilizationModeOff](off.md) — A mode that doesn’t stabilize video capture.
- [AVCaptureVideoStabilizationModeCinematic](cinematic.md) — A mode that uses the cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeCinematicExtended](cinematicextended.md) — A mode that uses the extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModePreviewOptimized](previewoptimized.md) — A mode that uses the preview optimized stabilization algorithm.
- [AVCaptureVideoStabilizationModeCinematicExtendedEnhanced](cinematicextendedenhanced.md) — A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeAuto](auto.md) — A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.
- [AVCaptureVideoStabilizationModeLowLatency](lowlatency.md) — Indicates that video should be stabilized using the low latency stabilization algorithm. Low Latency stabilization has a reduced field of view. Enabling low latency stabilization introduces no additional latency into the video capture pipeline.
