---
title: supportedDepthDataFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/supporteddepthdataformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supporteddepthdataformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/supporteddepthdataformats.json'
content_hash: 'sha256:67606d9e9cb0dd27'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# supportedDepthDataFormats

<sub>Instance Property</sub>

The list of data formats compatible with this video format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var supportedDepthDataFormats: [AVCaptureDevice.Format] { get }
```

## Discussion

Depth data capture requires a compatible pairing of video format and depth data format. After you set a capture device’s [activeFormat](../activeformat.md) property to this format, you can set the device’s [activeDepthDataFormat](../activedepthdataformat.md) property to one of the formats in this array.

Supported depth data formats always match the aspect ratio of their corresponding video format.

## See Also

### Determining depth capture support

- [supportedVideoZoomFactorsForDepthDataDelivery](supportedvideozoomfactorsfordepthdatadelivery.md) — The zoom factors that a format supports for depth data delivery. _(deprecated)_
