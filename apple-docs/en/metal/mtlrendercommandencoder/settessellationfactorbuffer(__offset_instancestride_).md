---
title: 'setTessellationFactorBuffer(_:offset:instanceStride:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settessellationfactorbuffer(_:offset:instancestride:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settessellationfactorbuffer(_:offset:instancestride:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settessellationfactorbuffer%28_%3Aoffset%3Ainstancestride%3A%29.json'
content_hash: 'sha256:8a51b879ac1f1dbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTessellationFactorBuffer(_:offset:instanceStride:)

<sub>Instance Method</sub>

Configures the per-patch tessellation factors for any subsequent patch-drawing commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTessellationFactorBuffer(_ buffer: (any MTLBuffer)?, offset: Int, instanceStride: Int)
```

## Parameters

- `buffer` — An [MTLBuffer](../mtlbuffer.md) instance that stores the per-patch tessellation factors, which can’t be empty or `nil`.

- `offset` — The distance, in bytes, between the start of the data and the start of the buffer, which needs to be a multiple of `4`.

- `instanceStride` — The number of bytes between two instances of data in `buffer`, which needs to be a multiple of `4`.

## Discussion

Call this method before encoding patch-drawing commands.

## See Also

### Configuring tessellation factors

- [- setTessellationFactorScale:](<settessellationfactorscale(__).md>) — Configures the scale factor for per-patch tessellation factors.
