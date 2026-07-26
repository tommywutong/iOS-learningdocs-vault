---
title: hasProtectedContent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/hasprotectedcontent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/hasprotectedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/hasprotectedcontent.json'
content_hash: 'sha256:e5079c9accee869e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# hasProtectedContent

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset contains protected content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var hasProtectedContent: Bool { get }
```

## Discussion

Assets that contain protected content may not be playable without successful authorization, even if the value of its [playable](../avasset/isplayable.md) property is [true](../../swift/true.md).
