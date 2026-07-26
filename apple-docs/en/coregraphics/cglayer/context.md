---
title: context
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglayer/context
source_url: 'https://developer.apple.com/documentation/coregraphics/cglayer/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglayer/context.json'
content_hash: 'sha256:ed21e29fe6db3902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGLayer](../cglayer.md)

# context

<sub>Instance Property</sub>

Returns the graphics context associated with a layer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var context: CGContext? { get }
```

## Discussion

The context that’s returned is the context for the layer itself, not the context that you specified when you created the layer.

## See Also

### Examining a Layer

- [CGLayerGetSize](size.md) — Returns the width and height of a layer object.
