---
title: detectsCustomRoutes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avroutedetector/detectscustomroutes
source_url: 'https://developer.apple.com/documentation/avfoundation/avroutedetector/detectscustomroutes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avroutedetector/detectscustomroutes.json'
content_hash: 'sha256:c26ee96c70a913b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVRouteDetector](../avroutedetector.md)

# detectsCustomRoutes

<sub>Instance Property</sub>

A Boolean value that indicates whether route detection includes custom routes.

> [!warning] Deprecated
> To detect custom routes, adopt the [AVSystemRouting](../../avsystemrouting.md) framework instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var detectsCustomRoutes: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Only set it to [true](../../swift/true.md) if your app uses an instance of [AVCustomRoutingController](../../avrouting/avcustomroutingcontroller.md).
