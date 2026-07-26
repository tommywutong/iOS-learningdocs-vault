---
title: maxPhotoQualityPrioritization
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/maxphotoqualityprioritization
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/maxphotoqualityprioritization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/maxphotoqualityprioritization.json'
content_hash: 'sha256:4d4cd782e96b7c32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# maxPhotoQualityPrioritization

<sub>Instance Property</sub>

The highest quality the photo output should prepare to deliver on a capture-by-capture basis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var maxPhotoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization { get set }
```

## Discussion

[AVCapturePhotoOutput](../avcapturephotooutput.md) can apply a variety of techniques to improve photo quality, such as reducing noise, preserving detail in low light, freezing motion, and so on. Some techniques improve image quality at the expense of the shot-to-shot time. Before starting your session, you may set this property to indicate the highest quality prioritization you intend to request when calling the [- capturePhotoWithSettings:delegate:](<capturephoto(with_delegate_).md>) method.

When configuring an [AVCapturePhotoSettings](../avcapturephotosettings.md) object, you can’t exceed this quality prioritization level, but you may select a lower prioritization level that favors speed over quality.

When you attach the photo output to an [AVCaptureSession](../avcapturesession.md), the default value of this property is [AVCapturePhotoQualityPrioritizationBalanced](qualityprioritization/balanced.md). If you instead attach it to an [AVCaptureMultiCamSession](../avcapturemulticamsession.md), the default value is [AVCapturePhotoQualityPrioritizationSpeed](qualityprioritization/speed.md).

> [!important] Important
> Changing the value of this property while the session is running causes the session to be rebuilt. This can be an expensive operation that will interrupt video preview until complete.

## See Also

### Setting the capture prioritization

- [QualityPrioritization](qualityprioritization.md) — Constants that indicate how to prioritize photo quality relative to capture speed.
