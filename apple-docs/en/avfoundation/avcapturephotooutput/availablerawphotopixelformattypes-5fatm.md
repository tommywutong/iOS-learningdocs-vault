---
title: availableRawPhotoPixelFormatTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/availablerawphotopixelformattypes-5fatm
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablerawphotopixelformattypes-5fatm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/availablerawphotopixelformattypes-5fatm.json'
content_hash: 'sha256:872d72648e15a5a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# availableRawPhotoPixelFormatTypes

<sub>Instance Property</sub>

The pixel formats the capture output supports for RAW photo capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * availableRawPhotoPixelFormatTypes;
```

## Discussion

To capture a photo in RAW format, use the [+ photoSettingsWithRawPixelFormatType:](<../avcapturephotosettings/init(rawpixelformattype_).md>) or [+ photoSettingsWithRawPixelFormatType:processedFormat:](<../avcapturephotosettings/init(rawpixelformattype_processedformat_).md>) initializer to create your photo settings object. The value for that initializer’s `rawPixelFormatType` parameter must be one of the Bayer RAW format identifiers listed in this array.

> [!note] Note
> Read this property only after adding the photo capture output to an [AVCaptureSession](../avcapturesession.md) object containing a video source. If the photo capture output isn’t connected to a session with a video source, this array is empty.
>
> Not all devices support RAW image capture. If the current device doesn’t support RAW capture, this array is empty.

This property supports key-value observing.

## See Also

### Determining supported pixel formats

- [availablePhotoPixelFormatTypes](availablephotopixelformattypes-6eyb.md) — The pixel formats the capture output supports for photo capture.
- [supportedPhotoPixelFormatTypesForFileType:](supportedphotopixelformattypesforfiletype_.md) — Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [supportedRawPhotoPixelFormatTypesForFileType:](supportedrawphotopixelformattypesforfiletype_.md) — Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [+ isAppleProRAWPixelFormat:](<isappleprorawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [+ isBayerRAWPixelFormat:](<isbayerrawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.
