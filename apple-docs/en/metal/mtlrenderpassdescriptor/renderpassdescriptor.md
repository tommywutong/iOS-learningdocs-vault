---
title: renderPassDescriptor
framework: Metal
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/renderpassdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/renderpassdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/renderpassdescriptor.json'
content_hash: 'sha256:179fdacd280cafbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# renderPassDescriptor

<sub>Type Method</sub>

Creates a default render pass descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (MTLRenderPassDescriptor *) renderPassDescriptor;
```

## Return Value

A new render pass descriptor with no attachments at all.

## Discussion

Set the desired color attachments with the [setObject:atIndexedSubscript:](../mtlrenderpasscolorattachmentdescriptorarray/setobject_atindexedsubscript_.md) method of the [colorAttachments](colorattachments.md) property. Set the desired depth and stencil attachments with the [depthAttachment](depthattachment.md) and [stencilAttachment](stencilattachment.md) properties, respectively.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
