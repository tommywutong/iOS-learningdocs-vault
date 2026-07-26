---
title: layer
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldrawable/layer
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldrawable/layer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldrawable/layer.json'
content_hash: 'sha256:b898a4233e6c5915'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDrawable](../cametaldrawable.md)

# layer

<sub>Instance Property</sub>

The layer that owns this drawable object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layer: CAMetalLayer { get }
```

## Discussion

When you present the drawable object, it becomes the owning layer’s content.
