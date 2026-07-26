---
title: availablePhotoFileTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/availablephotofiletypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablephotofiletypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/availablephotofiletypes.json'
content_hash: 'sha256:9eb9d0cef323ba3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# availablePhotoFileTypes

<sub>Instance Property</sub>

The list of file types currently supported for photo capture and output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var availablePhotoFileTypes: [AVFileType] { get }
```

## Discussion

When you issue a photo capture request, you can separately specify the format for capturing or encoding image data and the container format for producing output files containing that data. However, each file type supports only a specific set of image data types.

After choosing an output file type, use the [- supportedPhotoCodecTypesForFileType:](<supportedphotocodectypes(for_).md>) (for capture in compressed formats such as HEVC and JPEG) or [supportedPhotoPixelFormatTypesForFileType:](supportedphotopixelformattypesforfiletype_.md) (for capture in uncompressed formats such as TIFF) method to choose an appropriate data format before creating a photo settings object.

## See Also

### Determining supported file types

- [availableRawPhotoFileTypes](availablerawphotofiletypes.md) — The list of file types currently supported for RAW format capture and output.
