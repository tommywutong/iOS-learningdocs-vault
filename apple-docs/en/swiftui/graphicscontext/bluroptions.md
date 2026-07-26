---
title: GraphicsContext.BlurOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/bluroptions
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/bluroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/bluroptions.json'
content_hash: 'sha256:12ef04370e84293b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.BlurOptions

<sub>Structure</sub>

Options that configure the graphics context filter that creates blur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct BlurOptions
```

## Overview

You can use a set of these options when you call [blur(radius:options:)](<filter/blur(radius_options_).md>) to create a [Filter](filter.md) that adds blur to an object that you draw into a [GraphicsContext](../graphicscontext.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting blur options

- [dithersResult](bluroptions/dithersresult.md) — An option that causes the filter to dither the result, to reduce banding.
- [opaque](bluroptions/opaque.md) — An option that causes the filter to ensure the result is completely opaque.

## See Also

### Filtering

- [addFilter(_:options:)](<addfilter(__options_).md>) — Adds a filter that applies to subsequent drawing operations.
- [Filter](filter.md) — A type that applies image processing operations to rendered content.
- [FilterOptions](filteroptions.md) — Options that configure a filter that you add to a graphics context.
- [ShadowOptions](shadowoptions.md) — Options that configure the graphics context filter that creates shadows.
