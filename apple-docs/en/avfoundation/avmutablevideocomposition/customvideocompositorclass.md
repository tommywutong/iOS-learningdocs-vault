---
title: customVideoCompositorClass
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（26.0 起废弃）, iPadOS 7.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocomposition/customvideocompositorclass
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/customvideocompositorclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/customvideocompositorclass.json'
content_hash: 'sha256:2e397d91daa19834'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# customVideoCompositorClass

<sub>Instance Property</sub>

The custom compositor class to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var customVideoCompositorClass: (any AVVideoCompositing.Type)? { get set }
```

## Discussion

The default value is `nil`, indicating that the internal video compositor is used
