---
title: defaultSimulatedAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/defaultsimulatedaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/defaultsimulatedaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/defaultsimulatedaperture.json'
content_hash: 'sha256:8a38e7002f8447a9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# defaultSimulatedAperture

<sub>Instance Property</sub>

Default shallow depth of field simulated aperture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var defaultSimulatedAperture: Float { get }
```

## Discussion

This property return a non-zero value on devices that support the shallow depth of field effect.

## See Also

### Determining Cinematic video support

- [cinematicVideoCaptureSupported](iscinematicvideocapturesupported.md) — Indicates whether the format supports Cinematic Video capture.
- [minSimulatedAperture](minsimulatedaperture.md) — Minimum supported shallow depth of field simulated aperture.
- [maxSimulatedAperture](maxsimulatedaperture.md) — Maximum supported shallow depth of field simulated aperture.
- [videoMaxZoomFactorForCinematicVideo](videomaxzoomfactorforcinematicvideo.md) — Indicates the maximum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoMinZoomFactorForCinematicVideo](videominzoomfactorforcinematicvideo.md) — Indicates the minimum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoFrameRateRangeForCinematicVideo](videoframeraterangeforcinematicvideo.md) — Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.
