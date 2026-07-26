---
title: rawPhotoPixelFormatType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/rawphotopixelformattype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/rawphotopixelformattype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/rawphotopixelformattype.json'
content_hash: 'sha256:15b6cfaa42e6fa7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# rawPhotoPixelFormatType

<sub>Instance Property</sub>

An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var rawPhotoPixelFormatType: OSType { get }
```

## Discussion

This property is read-only—you specify a RAW pixel format when creating a settings object with the [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>), [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) initializer.

When capturing RAW images, the following requirements apply:

- The [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) setting must be [false](../../swift/false.md).
- Your delegate object must implement the [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) method.
- The [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) setting may be [true](../../swift/true.md) or [false](../../swift/false.md), but that setting applies only to the separate processed image.

(You request separate processed images with the [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) initializer. This restriction does not apply when you request RAW-only capture with the [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) initializer).

The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate do not meet these requirements, that method raises an exception.

## See Also

### Inspecting settings

- [uniqueID](uniqueid.md) — A unique identifier for this photo settings instance.
- [format](format.md) — A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [processedFileType](processedfiletype.md) — The container file format for eventual output of the processed image.
- [rawFileType](rawfiletype.md) — The container file format for eventual output of the RAW image.
