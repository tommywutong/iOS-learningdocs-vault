---
title: 'addFilter(_:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/addfilter(_:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/addfilter(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/addfilter%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:564e6037dec28f1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# addFilter(_:options:)

<sub>Instance Method</sub>

Adds a filter that applies to subsequent drawing operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addFilter(_ filter: GraphicsContext.Filter, options: GraphicsContext.FilterOptions = FilterOptions())
```

## Parameters

- `filter` — A graphics context filter that you create by calling one of the [Filter](filter.md) factory methods.

- `options` — A set of options from [FilterOptions](filteroptions.md) that you can use to configure filter operations.

## Discussion

To draw with filtering, SwiftUI:

- Rasterizes the drawing operation to an implicit transparency layer without blending, adjusting opacity, or applying any clipping.
- Applies the filter to the layer containing the rasterized image.
- Composites the layer onto the background, using the context’s current blend mode, opacity setting, and clip shapes.

When SwiftUI draws with a filter, the blend mode might apply to regions outside the drawing operation’s intrinsic shape, but inside its clip shape. That might result in unexpected behavior for certain blend modes like [copy](blendmode-swift.struct/copy.md), where the drawing operation completely overwrites the background even if the source alpha is zero.

## See Also

### Filtering

- [Filter](filter.md) — A type that applies image processing operations to rendered content.
- [FilterOptions](filteroptions.md) — Options that configure a filter that you add to a graphics context.
- [BlurOptions](bluroptions.md) — Options that configure the graphics context filter that creates blur.
- [ShadowOptions](shadowoptions.md) — Options that configure the graphics context filter that creates shadows.
