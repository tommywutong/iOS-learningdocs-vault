---
title: isShutterSoundSuppressionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isshuttersoundsuppressionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isshuttersoundsuppressionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isshuttersoundsuppressionsupported.json'
content_hash: 'sha256:db482b9fbeac0c72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isShutterSoundSuppressionSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the photo output supports suppressing the system shutter sound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isShutterSoundSuppressionSupported: Bool { get }
```

## Discussion

In iOS, the value is [true](../../swift/true.md), except in jurisdictions where you can’t disable the shutter sound. On all other platforms, the value is always [false](../../swift/false.md).

If the output supports this feature, you can supress the shutter sound when capturing a photo using the [shutterSoundSuppressionEnabled](../avcapturephotosettings/isshuttersoundsuppressionenabled.md) property of [AVCapturePhotoSettings](../avcapturephotosettings.md).
