---
title: outputSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/outputsettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/outputsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/outputsettings.json'
content_hash: 'sha256:62e8908ecd805ab1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# outputSettings

<sub>Instance Property</sub>

The compression settings for the output.

> [!warning] Deprecated
> Use AVCapturePhotoOutput instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var outputSettings: [String : Any] { get set }
```

## Discussion

Use [availableImageDataCVPixelFormatTypes](availableimagedatacvpixelformattypes.md) and [availableImageDataCodecTypes](availableimagedatacodectypes.md) to determine what codec keys and pixel formats are supported.

In iOS, the only currently supported keys are [AVVideoCodecKey](../avvideocodeckey.md) and [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md). These keys are mutually exclusive—only one may be present. The recommended values are [kCMVideoCodecType_JPEG](../../coremedia/kcmvideocodectype_jpeg.md) for [AVVideoCodecKey](../avvideocodeckey.md) and [kCVPixelFormatType_420YpCbCr8BiPlanarFullRange](../../corevideo/kcvpixelformattype_420ypcbcr8biplanarfullrange.md) and [kCVPixelFormatType_32BGRA](../../corevideo/kcvpixelformattype_32bgra.md) for [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md).

In iOS 6.0 and later, the [AVVideoQualityKey](../avvideoqualitykey.md) is supported, and may only be used when [AVVideoCodecKey](../avvideocodeckey.md) is set to [AVVideoCodecJPEG](../avvideocodecjpeg.md).

## See Also

### Configuring image settings

- [highResolutionStillImageOutputEnabled](ishighresolutionstillimageoutputenabled.md) — A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property. _(deprecated)_
- [availableImageDataCVPixelFormatTypes](availableimagedatacvpixelformattypes.md) — The supported image pixel formats that can be specified as output settings. _(deprecated)_
- [availableImageDataCodecTypes](availableimagedatacodectypes.md) — The supported image codec formats that can be specified as output settings. _(deprecated)_
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
