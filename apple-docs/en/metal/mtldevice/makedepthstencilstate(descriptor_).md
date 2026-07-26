---
title: 'makeDepthStencilState(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makedepthstencilstate(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makedepthstencilstate(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makedepthstencilstate%28descriptor%3A%29.json'
content_hash: 'sha256:2b503a2ee761d939'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeDepthStencilState(descriptor:)

<sub>Instance Method</sub>

Creates a depth-stencil state instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeDepthStencilState(descriptor: MTLDepthStencilDescriptor) -> (any MTLDepthStencilState)?
```

## Parameters

- `descriptor` — An [MTLDepthStencilDescriptor](../mtldepthstencildescriptor.md) instance.

## Return Value

A new [MTLDepthStencilState](../mtldepthstencilstate.md) instance if the method completed successfully; otherwise `nil`.
