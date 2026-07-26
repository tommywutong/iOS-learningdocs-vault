---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4renderpipelinecolorattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinecolorattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:86c69a6e8908f617'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineColorAttachmentDescriptorArray](../mtl4renderpipelinecolorattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses a color attachment at a specific index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTL4RenderPipelineColorAttachmentDescriptor! { get set }
```

## Parameters

- `attachmentIndex` — Index of the attachment to access.
