---
title: preservesDepth
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/careplicatorlayer/preservesdepth
source_url: 'https://developer.apple.com/documentation/quartzcore/careplicatorlayer/preservesdepth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/careplicatorlayer/preservesdepth.json'
content_hash: 'sha256:c28f63bd6c42455b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAReplicatorLayer](../careplicatorlayer.md)

# preservesDepth

<sub>Instance Property</sub>

Defines whether this layer flattens its sublayers into its plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preservesDepth: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the layer acts similarly to the `CATransformLayer` and has the same restrictions.

Default is [false](../../swift/false.md).
