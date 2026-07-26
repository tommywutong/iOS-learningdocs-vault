---
title: 'init(rawPixelFormatType:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/init%28rawpixelformattype%3A%29.json'
content_hash: 'sha256:6594b254739dfa45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# init(rawPixelFormatType:)

<sub>Initializer</sub>

Creates a photo settings object for RAW-format-only capture with the specified pixel format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
convenience init(rawPixelFormatType: OSType)
```

## Parameters

- `rawPixelFormatType` — The Bayer RAW pixel format type to use for capture. This value must be one of the format identifiers listed in the [availableRawPhotoPixelFormatTypes](../avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) array of your photo capture output.

## Return Value

A new photo settings object.

## Discussion

Use this initializer for RAW-only capture. To capture an image in both RAW format and a processed format (such as JPEG), use the [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) initializer instead.

Requesting RAW format capture adds requirements for other photo settings: for details, see the [rawPhotoPixelFormatType](rawphotopixelformattype.md) property. The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## See Also

### Creating photo settings

- [+ photoSettingsWithFormat:](<init(format_).md>) — Creates a photo settings object with the specified output format.
- [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) — Creates a photo settings object for capture in both RAW format and a processed format.
- [+ photoSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:](<init(rawpixelformattype_rawfiletype_processedformat_processedfiletype_).md>) — Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [+ photoSettingsFromPhotoSettings:](<init(from_).md>) — Creates a unique photo settings object, copying all settings values from the specified photo settings object.
