---
title: 'setVisibilityResultMode(_:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setvisibilityresultmode(_:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setvisibilityresultmode(_:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setvisibilityresultmode%28_%3Aoffset%3A%29.json'
content_hash: 'sha256:c2b95f7575ef1ebe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setVisibilityResultMode(_:offset:)

<sub>Instance Method</sub>

Configures a visibility test for Metal to run, and the destination for any results it generates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset: Int)
```

## Parameters

- `mode` — A [MTLVisibilityResultMode](../mtlvisibilityresultmode.md) that configures which visibility test results the render pass saves to a buffer, or disables visibility testing.

- `offset` — A location, in bytes, relative to the start of [visibilityResultBuffer](../mtl4renderpassdescriptor/visibilityresultbuffer.md) The GPU stores the result of a visibility test at `offset`, which needs to be a multiple of `8`.

## Discussion

You use the `mode` parameter to enable or disable the visibility test, and determine if it produces a boolean response for passing fragments, or if it counts the number of fragments.
