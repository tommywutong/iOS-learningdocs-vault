---
title: isCinematicVideoCaptureSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/iscinematicvideocapturesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscinematicvideocapturesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/iscinematicvideocapturesupported.json'
content_hash: 'sha256:723d683d8373529b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isCinematicVideoCaptureSupported

<sub>Instance Property</sub>

Indicates whether the format supports Cinematic Video capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isCinematicVideoCaptureSupported: Bool { get }
```

## Discussion

This property returns `true` if the format supports Cinematic Video that produces a controllable, simulated depth of field and adds beautiful focus transitions for a cinema-grade look.

## See Also

### Determining Cinematic video support

- [defaultSimulatedAperture](defaultsimulatedaperture.md) — Default shallow depth of field simulated aperture.
- [minSimulatedAperture](minsimulatedaperture.md) — Minimum supported shallow depth of field simulated aperture.
- [maxSimulatedAperture](maxsimulatedaperture.md) — Maximum supported shallow depth of field simulated aperture.
- [videoMaxZoomFactorForCinematicVideo](videomaxzoomfactorforcinematicvideo.md) — Indicates the maximum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoMinZoomFactorForCinematicVideo](videominzoomfactorforcinematicvideo.md) — Indicates the minimum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoFrameRateRangeForCinematicVideo](videoframeraterangeforcinematicvideo.md) — Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.
