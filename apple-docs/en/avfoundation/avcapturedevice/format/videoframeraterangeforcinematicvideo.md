---
title: videoFrameRateRangeForCinematicVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcinematicvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcinematicvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcinematicvideo.json'
content_hash: 'sha256:fe9db4fc1713f4d0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFrameRateRangeForCinematicVideo

<sub>Instance Property</sub>

Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoFrameRateRangeForCinematicVideo: AVFrameRateRange? { get }
```

## Discussion

Devices may support a limited frame rate range when Cinematic Video capture is active. If this device format does not support Cinematic Video capture, this property returns `nil`.

## See Also

### Determining Cinematic video support

- [cinematicVideoCaptureSupported](iscinematicvideocapturesupported.md) — Indicates whether the format supports Cinematic Video capture.
- [defaultSimulatedAperture](defaultsimulatedaperture.md) — Default shallow depth of field simulated aperture.
- [minSimulatedAperture](minsimulatedaperture.md) — Minimum supported shallow depth of field simulated aperture.
- [maxSimulatedAperture](maxsimulatedaperture.md) — Maximum supported shallow depth of field simulated aperture.
- [videoMaxZoomFactorForCinematicVideo](videomaxzoomfactorforcinematicvideo.md) — Indicates the maximum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoMinZoomFactorForCinematicVideo](videominzoomfactorforcinematicvideo.md) — Indicates the minimum zoom factor available for the [videoZoomFactor](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
