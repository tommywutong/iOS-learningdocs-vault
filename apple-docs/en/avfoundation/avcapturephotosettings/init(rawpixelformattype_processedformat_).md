---
title: 'init(rawPixelFormatType:processedFormat:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:processedformat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:processedformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/init%28rawpixelformattype%3Aprocessedformat%3A%29.json'
content_hash: 'sha256:0a5d1b71f91f319d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# init(rawPixelFormatType:processedFormat:)

<sub>Initializer</sub>

Creates a photo settings object for capture in both RAW format and a processed format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)
```

## Parameters

- `rawPixelFormatType` — The Bayer RAW pixel format type to use for capture. This value must be one of the format identifiers listed in the [availableRawPhotoPixelFormatTypes](../avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) array of your photo capture output.

- `processedFormat` — A dictionary of Core Video pixel buffer attributes or AVFoundation video settings constants (see `Video Settings`). To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, set the key [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) in the `format` dictionary. The corresponding value must be one of the pixel format identifiers listed in the [availablePhotoPixelFormatTypes](../avcapturephotooutput/availablephotopixelformattypes-6eyb.md) array of your photo capture output. To capture a photo in a compressed format, such as JPEG, set the key [AVVideoCodecKey](../avvideocodeckey.md) in the `format` dictionary. The corresponding value must be one of the codec identifiers listed in the [availablePhotoCodecTypes](../avcapturephotooutput/availablephotocodectypes.md) array of your photo capture output. For a compressed format, you can also specify a compression level with the key [AVVideoQualityKey](../avvideoqualitykey.md).

## Return Value

A new photo settings object.

## Discussion

Use this initializer to capture an image in both RAW format and a processed format (such as JPEG). For RAW-only capture, use the [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) initializer instead.

Requesting both formats adds requirements for other photo settings: see the [format](format.md) property for processed format requirements and the [rawPhotoPixelFormatType](rawphotopixelformattype.md) property for RAW format requirements. The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## See Also

### Creating photo settings

- [+ photoSettingsWithFormat:](<init(format_).md>) — Creates a photo settings object with the specified output format.
- [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) — Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [+ photoSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:](<init(rawpixelformattype_rawfiletype_processedformat_processedfiletype_).md>) — Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [+ photoSettingsFromPhotoSettings:](<init(from_).md>) — Creates a unique photo settings object, copying all settings values from the specified photo settings object.
