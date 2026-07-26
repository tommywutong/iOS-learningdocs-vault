---
title: 'supportedRawPhotoPixelFormatTypesForFileType:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotooutput/supportedrawphotopixelformattypesforfiletype:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedrawphotopixelformattypesforfiletype:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/supportedrawphotopixelformattypesforfiletype%3A.json'
content_hash: 'sha256:89cb1c70198da51d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# supportedRawPhotoPixelFormatTypesForFileType:

<sub>Instance Method</sub>

Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSArray<NSNumber *> *) supportedRawPhotoPixelFormatTypesForFileType:(AVFileType) fileType;
```

## Parameters

- `fileType` — The file type for which to obtain format information.

## Return Value

An array of pixel format types supported for encoding in the specified file type.

## Discussion

When you issue a photo capture request, you can separately specify the format for capturing or encoding image data and the container format for producing output files containing that data. However, each file type supports only a specific set of image data types.

After choosing a file type from the [availableRawPhotoFileTypes](availablerawphotofiletypes.md) array, use this method to find a compatible image data format before creating a photo settings object.

## See Also

### Determining supported pixel formats

- [availablePhotoPixelFormatTypes](availablephotopixelformattypes-6eyb.md) — The pixel formats the capture output supports for photo capture.
- [availableRawPhotoPixelFormatTypes](availablerawphotopixelformattypes-5fatm.md) — The pixel formats the capture output supports for RAW photo capture.
- [supportedPhotoPixelFormatTypesForFileType:](supportedphotopixelformattypesforfiletype_.md) — Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [+ isAppleProRAWPixelFormat:](<isappleprorawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [+ isBayerRAWPixelFormat:](<isbayerrawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.
