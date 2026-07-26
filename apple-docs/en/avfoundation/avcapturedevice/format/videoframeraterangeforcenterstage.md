---
title: videoFrameRateRangeForCenterStage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcenterstage
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcenterstage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcenterstage.json'
content_hash: 'sha256:bcaa3c0a5783398a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFrameRateRangeForCenterStage

<sub>Instance Property</sub>

The range of frame rates available when Center Stage is active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoFrameRateRangeForCenterStage: AVFrameRateRange? { get }
```

## Discussion

Devices may support a limited frame rate range when Center Stage is active. The value is `nil` if the device doesn’t support Center Stage.

## See Also

### Determining Center Stage support

- [centerStageSupported](iscenterstagesupported.md) — A Boolean value that indicates whether the format supports Center Stage.
- [videoMinZoomFactorForCenterStage](videominzoomfactorforcenterstage.md) — The minimum zoom factor available when Center Stage is active.
- [videoMaxZoomFactorForCenterStage](videomaxzoomfactorforcenterstage.md) — The maximum zoom factor available when Center Stage is active.
