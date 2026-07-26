---
title: hasProtectedContent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/hasprotectedcontent
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/hasprotectedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/hasprotectedcontent.json'
content_hash: 'sha256:f53056fc4c19e9df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# hasProtectedContent

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset contains protected content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hasProtectedContent: Bool { get }
```

## Discussion

Assets that contain protected content may not be playable without successful authorization, even if the value of its [playable](../avasset/isplayable.md) property is [true](../../swift/true.md).
