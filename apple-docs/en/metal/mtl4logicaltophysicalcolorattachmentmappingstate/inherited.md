---
title: MTL4LogicalToPhysicalColorAttachmentMappingState.inherited
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate/inherited
source_url: 'https://developer.apple.com/documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate/inherited'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate/inherited.json'
content_hash: 'sha256:dbd38610cb292d12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4LogicalToPhysicalColorAttachmentMappingState](../mtl4logicaltophysicalcolorattachmentmappingstate.md)

# MTL4LogicalToPhysicalColorAttachmentMappingState.inherited

<sub>Case</sub>

Deduces the color attachment mapping by inheriting it from the color attachment map of the current encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case inherited
```

## Discussion

Use this setting to indicate Metal should inherit the mapping from the `colorAttachmentMap` property of the current [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md) or [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) in use at draw time.
