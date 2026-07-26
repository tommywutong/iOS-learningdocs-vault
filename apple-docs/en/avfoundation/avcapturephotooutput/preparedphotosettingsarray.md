---
title: preparedPhotoSettingsArray
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/preparedphotosettingsarray
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/preparedphotosettingsarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/preparedphotosettingsarray.json'
content_hash: 'sha256:678cc85afb582576'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# preparedPhotoSettingsArray

<sub>Instance Property</sub>

An array of photo settings for which the photo output has prepared capture resources.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var preparedPhotoSettingsArray: [AVCapturePhotoSettings] { get }
```

## Discussion

Some types of photo capture, such as bracketed captures and RAW captures, require the photo output to allocate additional buffers or prepare other resources. To prevent photo capture requests from executing slowly due to lazy resource allocation, you may call the [- setPreparedPhotoSettingsArray:completionHandler:](<setpreparedphotosettingsarray(__completionhandler_).md>) method with an array of settings objects representative of the types of capture you will be performing (such as settings for a bracketed capture, RAW capture, or capture with still image stabilization).

By default, the photo output prepares sufficient resources to capture photos with default settings (as defined by the [AVCapturePhotoSettings](../avcapturephotosettings.md) default initializer).

## See Also

### Preparing for resource-intensive captures

- [- setPreparedPhotoSettingsArray:completionHandler:](<setpreparedphotosettingsarray(__completionhandler_).md>) — Tells the photo capture output to prepare resources for future capture requests with the specified settings.
