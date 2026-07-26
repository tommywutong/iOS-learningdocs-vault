---
title: uniqueID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/uniqueid
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/uniqueid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/uniqueid.json'
content_hash: 'sha256:373bf98042fbaacb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# uniqueID

<sub>Instance Property</sub>

A unique identifier for this photo settings instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var uniqueID: Int64 { get }
```

## Discussion

Creating a [AVCapturePhotoSettings](../avcapturephotosettings.md) instance automatically assigns a unique value to this property.

Use this property to track a photo capture request. After you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method, the photo capture output calls your delegate object to provide information about the progress and results of the capture. Each delegate method includes a [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md) whose [uniqueID](uniqueid.md) property matches the [uniqueID](uniqueid.md) value of the [AVCapturePhotoSettings](../avcapturephotosettings.md) object you used to request capture.

It is illegal to reuse a [AVCapturePhotoSettings](../avcapturephotosettings.md) instance for multiple captures. Calling the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method throws an exception ([invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)) if the `settings` object’s [uniqueID](uniqueid.md) value matches that of any previously used settings object.

## See Also

### Inspecting settings

- [format](format.md) — A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [processedFileType](processedfiletype.md) — The container file format for eventual output of the processed image.
- [rawFileType](rawfiletype.md) — The container file format for eventual output of the RAW image.
- [rawPhotoPixelFormatType](rawphotopixelformattype.md) — An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.
