---
title: AVCaptureVideoStabilizationMode.previewOptimized
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideostabilizationmode/previewoptimized
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/previewoptimized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideostabilizationmode/previewoptimized.json'
content_hash: 'sha256:d7d738bb2907fe11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoStabilizationMode](../avcapturevideostabilizationmode.md)

# AVCaptureVideoStabilizationMode.previewOptimized

<sub>Case</sub>

A mode that uses the preview optimized stabilization algorithm.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case previewOptimized
```

## Discussion

Preview stabilization is a low-latency and low-power algorithm which the system supports only on connections that have either an associated preview layer or a preview-sized [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md).

## See Also

### Stabilization modes

- [AVCaptureVideoStabilizationModeOff](off.md) — A mode that doesn’t stabilize video capture.
- [AVCaptureVideoStabilizationModeStandard](standard.md) — A mode that uses the standard algorithm.
- [AVCaptureVideoStabilizationModeCinematic](cinematic.md) — A mode that uses the cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeCinematicExtended](cinematicextended.md) — A mode that uses the extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeCinematicExtendedEnhanced](cinematicextendedenhanced.md) — A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationModeAuto](auto.md) — A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.
- [AVCaptureVideoStabilizationModeLowLatency](lowlatency.md) — Indicates that video should be stabilized using the low latency stabilization algorithm. Low Latency stabilization has a reduced field of view. Enabling low latency stabilization introduces no additional latency into the video capture pipeline.
