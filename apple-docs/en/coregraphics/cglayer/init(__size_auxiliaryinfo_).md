---
title: 'init(_:size:auxiliaryInfo:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cglayer/init(_:size:auxiliaryinfo:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cglayer/init(_:size:auxiliaryinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglayer/init%28_%3Asize%3Aauxiliaryinfo%3A%29.json'
content_hash: 'sha256:072e100ac87fc3d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGLayer](../cglayer.md)

# init(_:size:auxiliaryInfo:)

<sub>Initializer</sub>

Creates a layer object that is associated with a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ context: CGContext, size: CGSize, auxiliaryInfo: CFDictionary?)
```

## Parameters

- `context` — The graphics context you want to create the layer relative to. The layer uses this graphics context as a reference for initialization.

- `size` — The size, in default user space units, of the layer relative to the graphics context.

- `auxiliaryInfo` — Reserved for future use. Pass `NULL`.

## Return Value

A CGLayer object. In Objective-C, you’re responsible for releasing this object using the function [CGLayerRelease](../cglayerrelease.md) when you no longer need the layer.

## Discussion

After you create a [CGLayer](../cglayer.md) object, you should reuse it whenever you can to facilitate the Core Graphics caching strategy. Core Graphics caches any objects that are reused, including [CGLayer](../cglayer.md) objects. Objects that are reused frequently remain in the cache. In contrast, objects that are used once in a while may be moved in and out of the cache according to their frequency of use. If you don’t reuse [CGLayer](../cglayer.md) objects, Core Graphics won’t cache them. This means that you lose an opportunity to improve the performance of your application.
