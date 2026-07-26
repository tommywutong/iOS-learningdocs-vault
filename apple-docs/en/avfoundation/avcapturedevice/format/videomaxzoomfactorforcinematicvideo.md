---
title: videoMaxZoomFactorForCinematicVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcinematicvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcinematicvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcinematicvideo.json'
content_hash: 'sha256:0bb13c129b4945ee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoMaxZoomFactorForCinematicVideo

<sub>Instance Property</sub>

Indicates the maximum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoMaxZoomFactorForCinematicVideo: CGFloat { get }
```

## Discussion

Devices support a limited zoom range when Cinematic Video capture is active. If this device format does not support Cinematic Video capture, this property returns `1.0`.

## See Also

### Determining Cinematic video support

- [cinematicVideoCaptureSupported](iscinematicvideocapturesupported.md) — Indicates whether the format supports Cinematic Video capture.
- [defaultSimulatedAperture](defaultsimulatedaperture.md) — Default shallow depth of field simulated aperture.
- [minSimulatedAperture](minsimulatedaperture.md) — Minimum supported shallow depth of field simulated aperture.
- [maxSimulatedAperture](maxsimulatedaperture.md) — Maximum supported shallow depth of field simulated aperture.
- [videoMinZoomFactorForCinematicVideo](videominzoomfactorforcinematicvideo.md) — Indicates the minimum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoFrameRateRangeForCinematicVideo](videoframeraterangeforcinematicvideo.md) — Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.
