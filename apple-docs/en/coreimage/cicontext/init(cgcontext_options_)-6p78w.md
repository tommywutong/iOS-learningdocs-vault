---
title: 'init(cgContext:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/init(cgcontext:options:)-6p78w'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init(cgcontext:options:)-6p78w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28cgcontext%3Aoptions%3A%29-6p78w.json'
content_hash: 'sha256:f88c570044ca2e37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init(cgContext:options:)

<sub>Initializer</sub>

Creates a Core Image context from a Quartz context, using the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(cgContext cgctx: CGContext, options: [CIContextOption : Any]? = nil)
```

## Parameters

- `cgctx` — A Quartz graphics context.

- `options` — A dictionary that contains color space information. You can pass any of the keys defined in [CIContextOption](../cicontextoption.md) along with the appropriate value.

## Discussion

After calling this method, Core Image draws content to the specified Quartz graphics context.

When you create a [CIContext](../cicontext.md) object using a Quartz graphics context, any transformations that are already set on the Quartz graphics context affect drawing to that context.

> [!note] Note
> To obtain a Core Image context for the current AppKit drawing context in macOS, use the [NSGraphicsContext](../../appkit/nsgraphicscontext.md) [ciContext](../../appkit/nsgraphicscontext/cicontext.md) property.
