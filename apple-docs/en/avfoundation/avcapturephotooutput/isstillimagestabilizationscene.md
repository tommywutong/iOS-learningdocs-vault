---
title: isStillImageStabilizationScene
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationscene
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationscene.json'
content_hash: 'sha256:1393b2b494f52a10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isStillImageStabilizationScene

<sub>Instance Property</sub>

A Boolean value indicating whether the scene currently being previewed by the camera warrants image stabilization.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isStillImageStabilizationScene: Bool { get }
```

## Discussion

This property’s value changes depending on the scene currently visible to the camera. For example, you might use this property to highlight  controls in your app’s camera UI related to image stabilization, indicating to the user that the scene is dark enough that enabling image stabilization might be desirable.

If the photo capture output’s [stillImageStabilizationSupported](isstillimagestabilizationsupported.md) value is [false](../../swift/false.md), this property’s value is always [false](../../swift/false.md).

This property supports key-value observing.
