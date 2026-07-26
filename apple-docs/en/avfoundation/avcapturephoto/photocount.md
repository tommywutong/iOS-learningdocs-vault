---
title: photoCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/photocount
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/photocount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/photocount.json'
content_hash: 'sha256:cbda173cabd722b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# photoCount

<sub>Instance Property</sub>

The 1-based index of this photo capture relative to other results from the same capture request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var photoCount: Int { get }
```

## Discussion

The [expectedPhotoCount](../avcaptureresolvedphotosettings/expectedphotocount.md) property of this capture result’s [resolvedSettings](resolvedsettings.md) object indicates the total number of images that will be returned for a given capture request. When your delegate’s [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method receives a photo whose [photoCount](photocount.md) value  matches the [expectedPhotoCount](../avcaptureresolvedphotosettings/expectedphotocount.md) value, you know you’ve received the last one for the given capture request.

## See Also

### Resolving photo capture requests

- [resolvedSettings](resolvedsettings.md) — The settings object that was used to request this photo capture.
- [timestamp](timestamp.md) — The time at which the image was captured.
