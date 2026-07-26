---
title: minSimulatedAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/minsimulatedaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/minsimulatedaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/minsimulatedaperture.json'
content_hash: 'sha256:9451071636b201bb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# minSimulatedAperture

<sub>Instance Property</sub>

Minimum supported shallow depth of field simulated aperture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var minSimulatedAperture: Float { get }
```

## Discussion

On devices that do not support changing the simulated aperture value, this returns a value of `0`.

## See Also

### Determining Cinematic video support

- [cinematicVideoCaptureSupported](iscinematicvideocapturesupported.md) — Indicates whether the format supports Cinematic Video capture.
- [defaultSimulatedAperture](defaultsimulatedaperture.md) — Default shallow depth of field simulated aperture.
- [maxSimulatedAperture](maxsimulatedaperture.md) — Maximum supported shallow depth of field simulated aperture.
- [videoMaxZoomFactorForCinematicVideo](videomaxzoomfactorforcinematicvideo.md) — Indicates the maximum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoMinZoomFactorForCinematicVideo](videominzoomfactorforcinematicvideo.md) — Indicates the minimum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoFrameRateRangeForCinematicVideo](videoframeraterangeforcinematicvideo.md) — Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.
