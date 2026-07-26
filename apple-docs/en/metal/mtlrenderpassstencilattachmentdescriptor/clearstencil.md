---
title: clearStencil
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassstencilattachmentdescriptor/clearstencil
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassstencilattachmentdescriptor/clearstencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassstencilattachmentdescriptor/clearstencil.json'
content_hash: 'sha256:b5cfd463749d053a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassStencilAttachmentDescriptor](../mtlrenderpassstencilattachmentdescriptor.md)

# clearStencil

<sub>Instance Property</sub>

The value to use when clearing the stencil attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var clearStencil: UInt32 { get set }
```

## Discussion

If the [loadAction](../mtlrenderpassattachmentdescriptor/loadaction.md) property of the attachment is set to [MTLLoadActionClear](../mtlloadaction/clear.md), then at the start of a render pass, the GPU fills the contents of the attachment with the value stored in the [clearStencil](clearstencil.md) property. Otherwise, the GPU ignores [clearStencil](clearstencil.md).

The default value is `0`.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
