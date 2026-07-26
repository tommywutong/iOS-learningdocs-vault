---
title: AVCaptureDevice.AspectRatio
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/aspectratio
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/aspectratio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/aspectratio.json'
content_hash: 'sha256:aba857d5ef2875df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.AspectRatio

<sub>Structure</sub>

String constants describing the different video aspect ratios you can configure for a particular device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct AspectRatio
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Aspect ratios

- [AVCaptureAspectRatio16x9](aspectratio/ratio16x9.md) — An aspect ratio of 16x9.
- [AVCaptureAspectRatio1x1](aspectratio/ratio1x1.md) — An aspect ratio of 1x1.
- [AVCaptureAspectRatio3x4](aspectratio/ratio3x4.md) — An aspect ratio of 3x4.
- [AVCaptureAspectRatio4x3](aspectratio/ratio4x3.md) — An aspect ratio of 4x3.
- [AVCaptureAspectRatio9x16](aspectratio/ratio9x16.md) — An aspect ratio of 9x16.

### Initializers

- [init(rawValue:)](<aspectratio/init(rawvalue_).md>)

## See Also

### Configuring dynamic aspect ratio

- [- setDynamicAspectRatio:completionHandler:](<setdynamicaspectratio(__completionhandler_).md>) — Updates the dynamic aspect ratio of the device.
- [dynamicAspectRatio](dynamicaspectratio.md) — A key-value observable property indicating the current aspect ratio for a device.
- [dynamicDimensions](dynamicdimensions.md) — A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.
