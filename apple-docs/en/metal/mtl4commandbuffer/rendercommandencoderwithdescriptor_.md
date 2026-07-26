---
title: 'renderCommandEncoderWithDescriptor:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/rendercommandencoderwithdescriptor:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/rendercommandencoderwithdescriptor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/rendercommandencoderwithdescriptor%3A.json'
content_hash: 'sha256:8e46e8be18352804'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# renderCommandEncoderWithDescriptor:

<sub>Instance Method</sub>

Creates a render command encoder from a render pass descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4RenderCommandEncoder>) renderCommandEncoderWithDescriptor:(MTL4RenderPassDescriptor *) descriptor;
```

## Parameters

- `descriptor` — Descriptor for the render pass.

## Return Value

The created [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md) instance, or `nil` if the function failed.
