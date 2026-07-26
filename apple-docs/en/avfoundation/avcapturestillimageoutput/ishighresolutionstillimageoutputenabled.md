---
title: isHighResolutionStillImageOutputEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）, macOS 10.14+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/ishighresolutionstillimageoutputenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/ishighresolutionstillimageoutputenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/ishighresolutionstillimageoutputenabled.json'
content_hash: 'sha256:f4e7dae3f39b23fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# isHighResolutionStillImageOutputEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var isHighResolutionStillImageOutputEnabled: Bool { get set }
```

## Discussion

By default, `AVCaptureStillImageOutput` emits images with the same dimensions as its source [AVCaptureDevice](../avcapturedevice.md) instance’s `activeFormat.formatDescription`.  However, if you set this property to [true](../../swift/true.md), the receiver emits still images at the capture device’s [highResolutionStillImageDimensions](../avcapturedevice/format/highresolutionstillimagedimensions.md) value.

> [!note] Note
> If you enable video stabilization by setting `preferredVideoStabilizationMode` to [true](../../swift/true.md) for any output, the high resolution still images emitted by `AVCaptureStillImageOutput` may be smaller by 10% or more.

## See Also

### Configuring image settings

- [availableImageDataCVPixelFormatTypes](availableimagedatacvpixelformattypes.md) — The supported image pixel formats that can be specified as output settings. _(deprecated)_
- [availableImageDataCodecTypes](availableimagedatacodectypes.md) — The supported image codec formats that can be specified as output settings. _(deprecated)_
- [outputSettings](outputsettings.md) — The compression settings for the output. _(deprecated)_
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
