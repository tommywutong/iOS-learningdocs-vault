---
title: 'setVertexAmplificationCount(_:viewMappings:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexamplificationcount(_:viewmappings:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexamplificationcount(_:viewmappings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexamplificationcount%28_%3Aviewmappings%3A%29.json'
content_hash: 'sha256:7758131e16468f85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexAmplificationCount(_:viewMappings:)

<sub>Instance Method</sub>

Configures the number of output vertices the render pipeline produces for each input vertex, optionally with render target and viewport offsets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexAmplificationCount(_ count: Int, viewMappings: UnsafePointer<MTLVertexAmplificationViewMapping>?)
```

## Parameters

- `count` — The number of outputs to create.

- `viewMappings` — An optional pointer to a C array that has at least `count` [MTLVertexAmplificationViewMapping](../mtlvertexamplificationviewmapping.md) elements. Each element in the array provides per-output offsets to a specific render target and viewport.

## Discussion

With _vertex amplification_, you can encode drawing commands that process the same vertex multiple times, one per render target. You can configure the render pipeline’s vertex amplification multiplier by calling this method with a `count` argument that’s greater than `1`.

> [!note] Note
> Render pipelines don’t apply vertex amplification by default.

For more information about vertex amplification and how to use the `viewMappings` parameter, see [Improving rendering performance with vertex amplification](../improving-rendering-performance-with-vertex-amplification.md).
