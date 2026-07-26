---
title: removesDuplicateFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturescreeninput/removesduplicateframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/removesduplicateframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/removesduplicateframes.json'
content_hash: 'sha256:b76fad3de1c5f28b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# removesDuplicateFrames

<sub>Instance Property</sub>

A Boolean value that specifies whether the capture input skips duplicate frames.

> [!warning] Deprecated
> The capture system ignores this property in macOS 10.10 and later: the capture input never removes duplicate frames. You can re-create this functionality by using [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) and comparing successive frames.

<sub>macOS</sub>

```swift
var removesDuplicateFrames: Bool { get set }
```
