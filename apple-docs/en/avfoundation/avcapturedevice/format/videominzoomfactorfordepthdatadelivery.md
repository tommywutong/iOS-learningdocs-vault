---
title: videoMinZoomFactorForDepthDataDelivery
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（16.0 起废弃）, iPadOS 11.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/format/videominzoomfactorfordepthdatadelivery
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videominzoomfactorfordepthdatadelivery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videominzoomfactorfordepthdatadelivery.json'
content_hash: 'sha256:34da17558d4a313d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoMinZoomFactorForDepthDataDelivery

<sub>Instance Property</sub>

A minimum zoom factor the device supports when configured for depth data delivery.

> [!warning] Deprecated
> Use [supportedVideoZoomFactorsForDepthDataDelivery](../../avcapturedeviceformat/supportedvideozoomfactorsfordepthdatadelivery.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var videoMinZoomFactorForDepthDataDelivery: CGFloat { get }
```

## Discussion

Depth data capture requires coordinating the zoom factors of the two cameras on a dual-camera device. Therefore, when you enable depth data delivery for a capture format using the [AVCaptureDepthDataOutput](../../avcapturedepthdataoutput.md) class, the range of available values for the device’s [videoZoomFactor](../videozoomfactor.md) property is reduced.

If this format doesn’t support depth capture, this property’s value is `1.0`.

## See Also

### Determining zoom capabilities

- [supportedVideoZoomFactorsForDepthDataDelivery](supportedvideozoomfactorsfordepthdatadelivery.md) — The zoom factors that a format supports for depth data delivery. _(deprecated)_
- [videoMaxZoomFactorForDepthDataDelivery](videomaxzoomfactorfordepthdatadelivery.md) — A maximum zoom factor the device supports when configured for depth data delivery. _(deprecated)_
