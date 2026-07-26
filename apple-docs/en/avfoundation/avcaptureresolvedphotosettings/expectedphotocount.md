---
title: expectedPhotoCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureresolvedphotosettings/expectedphotocount
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/expectedphotocount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/expectedphotocount.json'
content_hash: 'sha256:db496c1d7e4bd8be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# expectedPhotoCount

<sub>Instance Property</sub>

The number of photo capture results in the capture request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var expectedPhotoCount: Int { get }
```

## Discussion

When you request a photo capture, the photo output calls your delegate’s [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method many times based on the settings you choose. For example, if you request a bracket of three exposures with image delivery in both JPEG and RAW formats, the expected photo count is `6`.

The [photoCount](../avcapturephoto/photocount.md) property of each [AVCapturePhoto](../avcapturephoto.md) object delivered to your delegate indicates where that capture result relates to this sequence. When your delegate receives a photo whose [photoCount](../avcapturephoto/photocount.md) value matches the [expectedPhotoCount](expectedphotocount.md), you know you’ve received the last one for the given capture request.

## See Also

### Resolving photo capture requests

- [uniqueID](uniqueid.md) — The unique identifier for the photo capture this settings object corresponds to.
