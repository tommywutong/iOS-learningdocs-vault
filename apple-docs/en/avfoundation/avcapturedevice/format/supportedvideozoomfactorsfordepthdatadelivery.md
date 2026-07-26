---
title: supportedVideoZoomFactorsForDepthDataDelivery
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+（17.2 起废弃）, iPadOS 16.0+（17.2 起废弃）, Mac Catalyst 16.0+（17.2 起废弃）, tvOS 17.0+（17.2 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/format/supportedvideozoomfactorsfordepthdatadelivery
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supportedvideozoomfactorsfordepthdatadelivery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/supportedvideozoomfactorsfordepthdatadelivery.json'
content_hash: 'sha256:0cadf35369cba5c8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# supportedVideoZoomFactorsForDepthDataDelivery

<sub>Instance Property</sub>

The zoom factors that a format supports for depth data delivery.

> [!warning] Deprecated
> Use AVCaptureDevice.Format.supportedVideoZoomRangesForDepthDataDelivery instead

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@nonobjc var supportedVideoZoomFactorsForDepthDataDelivery: [CGFloat] { get }
```

## See Also

### Determining depth capture support

- [supportedDepthDataFormats](supporteddepthdataformats.md) — The list of data formats compatible with this video format.
