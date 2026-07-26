---
title: availableImageDataCVPixelFormatTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/availableimagedatacvpixelformattypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/availableimagedatacvpixelformattypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/availableimagedatacvpixelformattypes.json'
content_hash: 'sha256:d4b094c9323b0fe3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# availableImageDataCVPixelFormatTypes

<sub>Instance Property</sub>

The supported image pixel formats that can be specified as output settings.

> [!warning] Deprecated
> Use AVCapturePhotoOutput instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var availableImageDataCVPixelFormatTypes: [NSNumber] { get }
```

## Discussion

The value of this property is an array of `NSNumber` objects that you can use as values for the [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) in the [outputSettings](outputsettings.md) property.

## See Also

### Configuring image settings

- [highResolutionStillImageOutputEnabled](ishighresolutionstillimageoutputenabled.md) — A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property. _(deprecated)_
- [availableImageDataCodecTypes](availableimagedatacodectypes.md) — The supported image codec formats that can be specified as output settings. _(deprecated)_
- [outputSettings](outputsettings.md) — The compression settings for the output. _(deprecated)_
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
