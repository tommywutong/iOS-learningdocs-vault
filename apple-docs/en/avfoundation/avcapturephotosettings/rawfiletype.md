---
title: rawFileType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/rawfiletype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/rawfiletype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/rawfiletype.json'
content_hash: 'sha256:b5972b46b714f531'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# rawFileType

<sub>Instance Property</sub>

The container file format for eventual output of the RAW image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var rawFileType: AVFileType? { get }
```

## Discussion

You specify a file format when creating capture settings with the [+ photoSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:](<init(rawpixelformattype_rawfiletype_processedformat_processedfiletype_).md>) initializer. If you didn’t specify a file format, this value is `nil`, and the photo output automatically choosea a default file format appropriate to the [rawPhotoPixelFormatType](rawphotopixelformattype.md) property.

## See Also

### Inspecting settings

- [uniqueID](uniqueid.md) — A unique identifier for this photo settings instance.
- [format](format.md) — A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [processedFileType](processedfiletype.md) — The container file format for eventual output of the processed image.
- [rawPhotoPixelFormatType](rawphotopixelformattype.md) — An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.
