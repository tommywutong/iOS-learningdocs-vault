---
title: 'init(rawPixelFormatType:rawFileType:processedFormat:processedFileType:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/init%28rawpixelformattype%3Arawfiletype%3Aprocessedformat%3Aprocessedfiletype%3A%29.json'
content_hash: 'sha256:eb7ec8df5f337167'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# init(rawPixelFormatType:rawFileType:processedFormat:processedFileType:)

<sub>Initializer</sub>

Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)
```

## Parameters

- `rawPixelFormatType` — The Bayer RAW pixel format type to use for capture. This value must be one of the format identifiers listed in the [availableRawPhotoPixelFormatTypes](../avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) array of your photo capture output.

- `rawFileType` — The container file format for eventual output of the RAW image. If you have no preferred file format, pass `nil` and the photo output will automatically choose a default file format appropriate to the `rawPixelFormatType` parameter.

- `processedFormat` — A dictionary of Core Video pixel buffer attributes or AVFoundation video settings constants (see `Video Settings`). To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, set the key [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) in the `format` dictionary. The corresponding value must be one of the pixel format identifiers listed in the [availablePhotoPixelFormatTypes](../avcapturephotooutput/availablephotopixelformattypes-6eyb.md) array of your photo capture output. To capture a photo in a compressed format, such as JPEG, set the key [AVVideoCodecKey](../avvideocodeckey.md) in the `format` dictionary. The corresponding value must be one of the codec identifiers listed in the [availablePhotoCodecTypes](../avcapturephotooutput/availablephotocodectypes.md) array of your photo capture output. For a compressed format, you can also specify a compression level with the key [AVVideoQualityKey](../avvideoqualitykey.md).

- `processedFileType` — The container file format for eventual output of the processed image. If you have no preferred file format, pass `nil` and the photo output will automatically choose a default file format appropriate to the `processedFormat` parameter.

## Return Value

A new photo settings object.

## Discussion

Use this initializer to capture an image in both RAW format and a processed format (such as JPEG). For RAW-only capture, use the [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) initializer instead.

Requesting both formats adds requirements for other photo settings: see the [format](format.md) property for processed format requirements and the [rawPhotoPixelFormatType](rawphotopixelformattype.md) property for RAW format requirements. The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate do not meet these requirements, that method raises an exception.

## See Also

### Creating photo settings

- [+ photoSettingsWithFormat:](<init(format_).md>) — Creates a photo settings object with the specified output format.
- [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) — Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) — Creates a photo settings object for capture in both RAW format and a processed format.
- [+ photoSettingsFromPhotoSettings:](<init(from_).md>) — Creates a unique photo settings object, copying all settings values from the specified photo settings object.
