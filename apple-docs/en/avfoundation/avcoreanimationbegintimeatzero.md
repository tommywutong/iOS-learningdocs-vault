---
title: AVCoreAnimationBeginTimeAtZero
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoreanimationbegintimeatzero
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoreanimationbegintimeatzero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoreanimationbegintimeatzero.json'
content_hash: 'sha256:9b852d6aad529f6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCoreAnimationBeginTimeAtZero

<sub>Global Variable</sub>

A value that sets an animation begin time to `0`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVCoreAnimationBeginTimeAtZero: CFTimeInterval
```

## Discussion

The constant is a small, non-zero, positive value which prevents CoreAnimation from replacing `0.0` with [CACurrentMediaTime()](<../quartzcore/cacurrentmediatime().md>).
