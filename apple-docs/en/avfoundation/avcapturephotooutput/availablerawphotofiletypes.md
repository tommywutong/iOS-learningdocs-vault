---
title: availableRawPhotoFileTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/availablerawphotofiletypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablerawphotofiletypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/availablerawphotofiletypes.json'
content_hash: 'sha256:77407f3d786f2738'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# availableRawPhotoFileTypes

<sub>Instance Property</sub>

The list of file types currently supported for RAW format capture and output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var availableRawPhotoFileTypes: [AVFileType] { get }
```

## Discussion

When you issue a photo capture request, you can separately specify the format for capturing or encoding image data and the container format for producing output files containing that data. However, each file type supports only a specific set of image data types.

After choosing an output file type, use the [supportedRawPhotoPixelFormatTypesForFileType:](supportedrawphotopixelformattypesforfiletype_.md) method to choose an appropriate data format before creating a photo settings object.

## See Also

### Determining supported file types

- [availablePhotoFileTypes](availablephotofiletypes.md) — The list of file types currently supported for photo capture and output.
