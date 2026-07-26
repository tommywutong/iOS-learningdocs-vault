---
title: availableImageDataCodecTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/availableimagedatacodectypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/availableimagedatacodectypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/availableimagedatacodectypes.json'
content_hash: 'sha256:9c5aa1af7c3dff04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# availableImageDataCodecTypes

<sub>Instance Property</sub>

The supported image codec formats that can be specified as output settings.

> [!warning] Deprecated
> Use AVCapturePhotoOutput instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var availableImageDataCodecTypes: [AVVideoCodecType] { get }
```

## Discussion

The value of this property is an array of `NSString` objects that you can use as values for the [AVVideoCodecKey](../avvideocodeckey.md) in the [outputSettings](outputsettings.md) property.

## See Also

### Configuring image settings

- [highResolutionStillImageOutputEnabled](ishighresolutionstillimageoutputenabled.md) — A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property. _(deprecated)_
- [availableImageDataCVPixelFormatTypes](availableimagedatacvpixelformattypes.md) — The supported image pixel formats that can be specified as output settings. _(deprecated)_
- [outputSettings](outputsettings.md) — The compression settings for the output. _(deprecated)_
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
