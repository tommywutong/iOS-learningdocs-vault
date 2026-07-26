---
title: 'supportedPhotoCodecTypes(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotooutput/supportedphotocodectypes(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedphotocodectypes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/supportedphotocodectypes%28for%3A%29.json'
content_hash: 'sha256:50c6334c124f5408'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# supportedPhotoCodecTypes(for:)

<sub>Instance Method</sub>

Returns the list of photo codecs (such as JPEG or HEVC) supported for photo data in the specified file type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func supportedPhotoCodecTypes(for fileType: AVFileType) -> [AVVideoCodecType]
```

## Parameters

- `fileType` — The file type (such as JFIF or HEIF) for which to obtain codec information.

## Return Value

An array of video codec types supported for encoding in the specified file type.

## Discussion

When you issue a photo capture request, you can separately specify the format for capturing or encoding image data and the container format for producing output files containing that data. However, each file type supports only a specific set of image data types.

After choosing a file type from the [availablePhotoFileTypes](availablephotofiletypes.md) array, use this method to find a compatible image data codec before creating a photo settings object.

## See Also

### Determining supported codec types

- [availablePhotoCodecTypes](availablephotocodectypes.md) — The compression codecs this capture output currently supports for photo capture.
