---
title: customSamplePositions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlstoreactionoptions/customsamplepositions
source_url: 'https://developer.apple.com/documentation/metal/mtlstoreactionoptions/customsamplepositions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoreactionoptions/customsamplepositions.json'
content_hash: 'sha256:318a5ef93d93985f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStoreActionOptions](../mtlstoreactionoptions.md)

# customSamplePositions

<sub>Type Property</sub>

An option that stores data in a sample-position–agnostic representation.

> [!warning] Deprecated
> Store action options have no effect on Apple Silicon

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var customSamplePositions: MTLStoreActionOptions { get }
```

## Discussion

Set this option only on an [MTLRenderPassColorAttachmentDescriptor](../mtlrenderpasscolorattachmentdescriptor.md) or [MTLRenderPassDepthAttachmentDescriptor](../mtlrenderpassdepthattachmentdescriptor.md) instance. Setting this option on an [MTLRenderPassStencilAttachmentDescriptor](../mtlrenderpassstencilattachmentdescriptor.md) instance or combining it with a nonstore [storeAction](../mtlrenderpassattachmentdescriptor/storeaction.md) value results in a runtime error.

Set this action when you need to read the data in a subsequent render pass or blit operation that is unaware of the programmable sample positions used to generate the data. You should set this option when, for example, reading per-sample data within a fragment function that uses different programmable sample positions.

If you specify this action, Metal may decompress the depth render target and store the resulting data in its decompressed form. If you don’t change programmable sample positions in a subsequent render pass, use [MTLStoreActionStore](../mtlstoreaction/store.md) instead to improve performance.
