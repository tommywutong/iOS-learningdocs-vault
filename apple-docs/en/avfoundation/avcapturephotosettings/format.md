---
title: format
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/format
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/format.json'
content_hash: 'sha256:7f474b898c289325'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# format

<sub>Instance Property</sub>

A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var format: [String : Any]? { get }
```

## Discussion

This property is read-only—you specify a processed format when creating a settings object with the [photoSettings](photosettings.md), [+ photoSettingsWithFormat:](<init(format_).md>), or [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) initializer.

When capturing images in processed formats, the following requirements apply:

- This dictionary must contain a value for either the [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) (to request an uncompressed format) or [AVVideoCodecKey](../avvideocodeckey.md) (to request a compressed format such as JPEG) key, but not both.
- If this dictionary has the [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) key, the value for that key must be listed in the photo output’s [availablePhotoPixelFormatTypes](../avcapturephotooutput/availablephotopixelformattypes-6eyb.md) array.

If this dictionary has the [AVVideoCodecKey](../avvideocodeckey.md) key, the value for that key must be listed in the photo output’s [availablePhotoCodecTypes](../avcapturephotooutput/availablephotocodectypes.md) array.

- Your delegate method must implement the [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) method.

The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate do not meet these requirements, that method raises an exception.

## See Also

### Inspecting settings

- [uniqueID](uniqueid.md) — A unique identifier for this photo settings instance.
- [processedFileType](processedfiletype.md) — The container file format for eventual output of the processed image.
- [rawFileType](rawfiletype.md) — The container file format for eventual output of the RAW image.
- [rawPhotoPixelFormatType](rawphotopixelformattype.md) — An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.
