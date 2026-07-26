---
title: 'init(format:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotosettings/init(format:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/init%28format%3A%29.json'
content_hash: 'sha256:0bb916b69430dd7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# init(format:)

<sub>Initializer</sub>

Creates a photo settings object with the specified output format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
convenience init(format: [String : Any]?)
```

## Parameters

- `format` — A dictionary of Core Video pixel buffer attributes or AVFoundation video settings constants (see Video Settings). To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, set the key [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) in the `format` dictionary. The corresponding value must be one of the pixel format identifiers listed in the [availablePhotoPixelFormatTypes](../avcapturephotooutput/availablephotopixelformattypes-6eyb.md) array of your photo capture output. To capture a photo in a compressed format, such as JPEG, set the key [AVVideoCodecKey](../avvideocodeckey.md) in the `format` dictionary. The corresponding value must be one of the codec identifiers listed in the [availablePhotoCodecTypes](../avcapturephotooutput/availablephotocodectypes.md) array of your photo capture output. For a compressed format, you can also specify a compression level with the key [AVVideoQualityKey](../avvideoqualitykey.md).

## Return Value

A new photo settings object.

## Discussion

Requesting capture in a processed format adds requirements for other photo settings: for details, see the [format](format.md) property. The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## See Also

### Creating photo settings

- [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) — Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) — Creates a photo settings object for capture in both RAW format and a processed format.
- [+ photoSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:](<init(rawpixelformattype_rawfiletype_processedformat_processedfiletype_).md>) — Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [+ photoSettingsFromPhotoSettings:](<init(from_).md>) — Creates a unique photo settings object, copying all settings values from the specified photo settings object.
