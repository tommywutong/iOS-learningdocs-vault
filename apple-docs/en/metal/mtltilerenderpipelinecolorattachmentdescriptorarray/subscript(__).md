---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:3d08f6f262dcef7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineColorAttachmentDescriptorArray](../mtltilerenderpipelinecolorattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the render pipeline state for the specified color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTLTileRenderPipelineColorAttachmentDescriptor { get set }
```

## Parameters

- `attachmentIndex` — An index in the color attachment array.

## Return Value

An [MTLTileRenderPipelineColorAttachmentDescriptor](../mtltilerenderpipelinecolorattachmentdescriptor.md) that describes the render pipeline information for a color attachment.
