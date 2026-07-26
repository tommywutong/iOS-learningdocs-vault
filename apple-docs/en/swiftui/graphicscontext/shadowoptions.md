---
title: GraphicsContext.ShadowOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/shadowoptions
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shadowoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shadowoptions.json'
content_hash: 'sha256:62d9054137eee1be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.ShadowOptions

<sub>Structure</sub>

Options that configure the graphics context filter that creates shadows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ShadowOptions
```

## Overview

You can use a set of these options when you call [shadow(color:radius:x:y:blendMode:options:)](<filter/shadow(color_radius_x_y_blendmode_options_).md>) to create a [Filter](filter.md) that adds a drop shadow to an object that you draw into a [GraphicsContext](../graphicscontext.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting shadow options

- [disablesGroup](shadowoptions/disablesgroup.md) — An option that causes the filter to composite the object and its shadow separately in the current layer.
- [invertsAlpha](shadowoptions/invertsalpha.md) — An option that causes the filter to invert the alpha of the shadow.
- [shadowAbove](shadowoptions/shadowabove.md) — An option that causes the filter to draw the shadow above the object, rather than below it.
- [shadowOnly](shadowoptions/shadowonly.md) — An option that causes the filter to draw only the shadow, and omit the source object.

## See Also

### Filtering

- [addFilter(_:options:)](<addfilter(__options_).md>) — Adds a filter that applies to subsequent drawing operations.
- [Filter](filter.md) — A type that applies image processing operations to rendered content.
- [FilterOptions](filteroptions.md) — Options that configure a filter that you add to a graphics context.
- [BlurOptions](bluroptions.md) — Options that configure the graphics context filter that creates blur.
