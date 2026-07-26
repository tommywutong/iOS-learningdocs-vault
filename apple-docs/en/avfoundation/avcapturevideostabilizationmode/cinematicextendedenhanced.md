---
title: AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideostabilizationmode/cinematicextendedenhanced
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/cinematicextendedenhanced'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideostabilizationmode/cinematicextendedenhanced.json'
content_hash: 'sha256:b5af4e6650536f60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoStabilizationMode](../avcapturevideostabilizationmode.md)

# AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced

<sub>Case</sub>

A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case cinematicExtendedEnhanced
```

## Discussion

Enhanced extended cinematic has a reduced field of view compared to extended cinematic, without any noticeable increase in latency, and it yields improved stability.

> [!note] Note
> It’s recommended to use identical or similar minimum and maximum frame durations in conjunction with this mode.

## See Also

### Stabilization modes

- [AVCaptureVideoStabilizationModeOff](off.md) — A mode that doesn’t stabilize video capture.
- [AVCaptureVideoStabilizationModeStandard](standard.md) — A mode that uses the standard algorithm.
- [AVCaptureVideoStabilizationModeCinematic](cinematic.md) — A mode that uses the cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeCinematicExtended](cinematicextended.md) — A mode that uses the extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModePreviewOptimized](previewoptimized.md) — A mode that uses the preview optimized stabilization algorithm.
- [AVCaptureVideoStabilizationModeAuto](auto.md) — A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.
- [AVCaptureVideoStabilizationModeLowLatency](lowlatency.md) — Indicates that video should be stabilized using the low latency stabilization algorithm. Low Latency stabilization has a reduced field of view. Enabling low latency stabilization introduces no additional latency into the video capture pipeline.
