---
title: GraphicsContext.FilterOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/filteroptions
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filteroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filteroptions.json'
content_hash: 'sha256:6f4cfe59f6a3c4a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.FilterOptions

<sub>Structure</sub>

Options that configure a filter that you add to a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct FilterOptions
```

## Overview

You can use filter options to configure a [Filter](filter.md) that you apply to a [GraphicsContext](../graphicscontext.md) with the [addFilter(_:options:)](<addfilter(__options_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting filter options

- [linearColor](filteroptions/linearcolor.md) — An option that causes the filter to perform calculations in a linear color space.

## See Also

### Filtering

- [addFilter(_:options:)](<addfilter(__options_).md>) — Adds a filter that applies to subsequent drawing operations.
- [Filter](filter.md) — A type that applies image processing operations to rendered content.
- [BlurOptions](bluroptions.md) — Options that configure the graphics context filter that creates blur.
- [ShadowOptions](shadowoptions.md) — Options that configure the graphics context filter that creates shadows.
