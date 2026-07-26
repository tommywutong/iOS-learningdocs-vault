---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:b8dba310a91e2c97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineColorAttachmentDescriptorArray](../mtlrenderpipelinecolorattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the render pipeline state for the specified color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor! { get set }
```

## Parameters

- `attachmentIndex` — An index in the color attachment array.

## Return Value

An [MTLRenderPipelineColorAttachmentDescriptor](../mtlrenderpipelinecolorattachmentdescriptor.md) instance that describes the render pipeline information for a color attachment.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
