---
title: videoMaxZoomFactorForCenterStage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcenterstage
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcenterstage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcenterstage.json'
content_hash: 'sha256:f63eee915062bbfd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoMaxZoomFactorForCenterStage

<sub>Instance Property</sub>

The maximum zoom factor available when Center Stage is active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoMaxZoomFactorForCenterStage: CGFloat { get }
```

## Discussion

Devices support a limited zoom range when Center Stage is active. If the device doesn’t support Center Stage, the value is [videoMaxZoomFactor](videomaxzoomfactor.md).

## See Also

### Determining Center Stage support

- [centerStageSupported](iscenterstagesupported.md) — A Boolean value that indicates whether the format supports Center Stage.
- [videoFrameRateRangeForCenterStage](videoframeraterangeforcenterstage.md) — The range of frame rates available when Center Stage is active.
- [videoMinZoomFactorForCenterStage](videominzoomfactorforcenterstage.md) — The minimum zoom factor available when Center Stage is active.
