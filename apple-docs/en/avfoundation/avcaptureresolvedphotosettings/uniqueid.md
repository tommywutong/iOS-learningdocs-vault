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
doc_path: /documentation/avfoundation/avcaptureresolvedphotosettings/uniqueid
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/uniqueid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/uniqueid.json'
content_hash: 'sha256:50946c3aa8141788'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# uniqueID

<sub>Instance Property</sub>

The unique identifier for the photo capture this settings object corresponds to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var uniqueID: Int64 { get }
```

## Discussion

The value of this property matches the matches the [uniqueID](../avcapturephotosettings/uniqueid.md) value of the [AVCapturePhotoSettings](../avcapturephotosettings.md) object you passed when initiating a photo capture with the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. Use this value to determine which delegate method calls correspond to which capture requests.

## See Also

### Resolving photo capture requests

- [expectedPhotoCount](expectedphotocount.md) — The number of photo capture results in the capture request.
