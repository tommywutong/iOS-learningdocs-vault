---
title: photoSettings
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/photosettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/photosettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/photosettings.json'
content_hash: 'sha256:1a657cc4c928c5bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# photoSettings

<sub>Type Method</sub>

Creates a photo settings object with default settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) photoSettings;
```

## Return Value

A new photo settings object.

## Discussion

Capturing a photo with default settings delivers a single image in JPEG format.

Requesting capture in a processed format (such as JPEG) adds requirements for other photo settings: for details, see the [format](format.md) property. The capture output validates these requirement when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate don’t meet these requirement, that method raises an exception.

## See Also

### Creating photo settings

- [+ photoSettingsWithFormat:](<init(format_).md>) — Creates a photo settings object with the specified output format.
- [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) — Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) — Creates a photo settings object for capture in both RAW format and a processed format.
- [+ photoSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:](<init(rawpixelformattype_rawfiletype_processedformat_processedfiletype_).md>) — Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [+ photoSettingsFromPhotoSettings:](<init(from_).md>) — Creates a unique photo settings object, copying all settings values from the specified photo settings object.
