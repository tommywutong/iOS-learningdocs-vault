---
title: 'init(from:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotosettings/init(from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/init%28from%3A%29.json'
content_hash: 'sha256:eba5244cf2c592ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# init(from:)

<sub>Initializer</sub>

Creates a unique photo settings object, copying all settings values from the specified photo settings object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
convenience init(from photoSettings: AVCapturePhotoSettings)
```

## Parameters

- `photoSettings` — The photo settings object from which to copy settings.

## Return Value

A new photo settings object.

## Discussion

It is illegal to reuse a [AVCapturePhotoSettings](../avcapturephotosettings.md) instance for multiple captures. Calling the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method throws an exception if the [uniqueID](uniqueid.md) value of the `settings` parameter matches that of any previously used settings object.

To reuse a specific combination of settings, use this initializer to create a new [AVCapturePhotoSettings](../avcapturephotosettings.md) instance from an existing photo settings object. The newly created instance has a new, unique value for its [uniqueID](uniqueid.md) property, but copies the values for all other properties from the `photoSettings` parameter.

## See Also

### Creating photo settings

- [+ photoSettingsWithFormat:](<init(format_).md>) — Creates a photo settings object with the specified output format.
- [+ photoSettingsWithRawPixelFormatType:](<init(rawpixelformattype_).md>) — Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [+ photoSettingsWithRawPixelFormatType:processedFormat:](<init(rawpixelformattype_processedformat_).md>) — Creates a photo settings object for capture in both RAW format and a processed format.
- [+ photoSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:](<init(rawpixelformattype_rawfiletype_processedformat_processedfiletype_).md>) — Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
