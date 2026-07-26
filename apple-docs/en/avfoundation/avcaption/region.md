---
title: region
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaption/region
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/region.json'
content_hash: 'sha256:3d0c78115738f2e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# region

<sub>Instance Property</sub>

The region in which the caption exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var region: AVCaptionRegion? { get }
```

## Discussion

This property is `nil` when the underlying caption format doesn’t support or use regions.
