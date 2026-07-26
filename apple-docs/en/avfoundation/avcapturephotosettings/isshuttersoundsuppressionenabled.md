---
title: isShutterSoundSuppressionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isshuttersoundsuppressionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isshuttersoundsuppressionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isshuttersoundsuppressionenabled.json'
content_hash: 'sha256:1752e4e8335bee8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isShutterSoundSuppressionEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to suppress the built-in shutter sound when capturing a photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isShutterSoundSuppressionEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Set the value to [true](../../swift/true.md) to suppress the photo output’s built-in shutter sound for this request. The photo output throws an invalid argument exception when calling [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) if its [shutterSoundSuppressionSupported](../avcapturephotooutput/isshuttersoundsuppressionsupported.md) property returns [false](../../swift/false.md).
