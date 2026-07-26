---
title: 'setVisibilityResultMode(_:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvisibilityresultmode(_:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvisibilityresultmode(_:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvisibilityresultmode%28_%3Aoffset%3A%29.json'
content_hash: 'sha256:fbdc47f8829cb58e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVisibilityResultMode(_:offset:)

<sub>Instance Method</sub>

Configures which visibility test the GPU runs and the destination for any results it generates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset: Int)
```

## Parameters

- `mode` — An [MTLVisibilityResultMode](../mtlvisibilityresultmode.md) that configures which visibility test results the render pass saves to a buffer, or disables visibility testing.

- `offset` — A location, in bytes, relative to the start of the render pass’s [visibilityResultBuffer](../mtlrenderpassdescriptor/visibilityresultbuffer.md). The GPU stores the result of a visibility test at `offset`, which needs to be a multiple of 8.

## Discussion

To create a render pass that can enable visibility testing, assign an [MTLBuffer](../mtlbuffer.md) instance to the [visibilityResultBuffer](../mtlrenderpassdescriptor/visibilityresultbuffer.md) property of an [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md).

You can monitor one or more drawing commands with a visibility test by calling this method before the drawing commands. The encoder uses the new visibility mode and offset for subsequent drawing commands until you change the configuration by calling the method again. For example, you can change the offset or entirely disable visibility tests for subsequent commands by passing [MTLVisibilityResultModeDisabled](../mtlvisibilityresultmode/disabled.md).

> [!note] Note
> You can set a specific `offset` value only once per render pass. This means you need to encode all drawing commands for an offset at one time.

The default mode for a render pass is [MTLVisibilityResultModeDisabled](../mtlvisibilityresultmode/disabled.md).
