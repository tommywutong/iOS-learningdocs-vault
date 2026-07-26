---
title: availablePhotoCodecTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/availablephotocodectypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablephotocodectypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/availablephotocodectypes.json'
content_hash: 'sha256:d39af57bf9aed664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# availablePhotoCodecTypes

<sub>Instance Property</sub>

The compression codecs this capture output currently supports for photo capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var availablePhotoCodecTypes: [AVVideoCodecType] { get }
```

## Discussion

To capture a photo in a compressed format, such as JPEG, use the [+ photoSettingsWithFormat:](<../avcapturephotosettings/init(format_).md>) initializer to create your photo settings object. In that initializer’s `format` dictionary, pass the key [AVVideoCodecKey](../avvideocodeckey.md), whose value must be one of the codec identifiers listed in this array.

> [!note] Note
> Read this property only after adding the photo capture output to an [AVCaptureSession](../avcapturesession.md) object containing a video source. If the photo capture output isn’t connected to a session with a video source, this array is empty.

This property supports key-value observing.

## See Also

### Determining supported codec types

- [- supportedPhotoCodecTypesForFileType:](<supportedphotocodectypes(for_).md>) — Returns the list of photo codecs (such as JPEG or HEVC) supported for photo data in the specified file type.
