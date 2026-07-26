---
title: layoutQueue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/layoutqueue
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/layoutqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/layoutqueue.json'
content_hash: 'sha256:26b08733e2e08cc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# layoutQueue

<sub>Instance Property</sub>

The queue on which the framework dispatches layout operations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var layoutQueue: OperationQueue? { get set }
```

## Discussion

If non-`nil`, the queue the framework uses for layout operations.
