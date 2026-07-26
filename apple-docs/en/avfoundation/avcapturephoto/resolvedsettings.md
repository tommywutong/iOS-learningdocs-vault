---
title: resolvedSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/resolvedsettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/resolvedsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/resolvedsettings.json'
content_hash: 'sha256:6e2f8050b556961c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# resolvedSettings

<sub>Instance Property</sub>

The settings object that was used to request this photo capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var resolvedSettings: AVCaptureResolvedPhotoSettings { get }
```

## Discussion

To determine which [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) call produced this photo capture result, match this [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md) object’s [uniqueID](../avcaptureresolvedphotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you requested capture with. You can also use this object to find out which values the photo output has chosen for automatic settings.

## See Also

### Resolving photo capture requests

- [photoCount](photocount.md) — The 1-based index of this photo capture relative to other results from the same capture request.
- [timestamp](timestamp.md) — The time at which the image was captured.
