---
title: MTLStoreAction.customSampleDepthStore
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstoreaction/customsampledepthstore
source_url: 'https://developer.apple.com/documentation/metal/mtlstoreaction/customsampledepthstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoreaction/customsampledepthstore.json'
content_hash: 'sha256:14add08574b1c3fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStoreAction](../mtlstoreaction.md)

# MTLStoreAction.customSampleDepthStore

<sub>Case</sub>

The GPU stores depth data in a sample-position–agnostic representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case customSampleDepthStore
```

## Discussion

You can only set this action on an [MTLRenderPassDepthAttachmentDescriptor](../mtlrenderpassdepthattachmentdescriptor.md) instance.

Set this action when you need to read the depth data in a subsequent render pass or blit operation that is unaware of the programmable sample positions used to generate the data.

If you specify this action, Metal may decompress the depth render target and store the resulting data in its decompressed form. If you don’t change programmable sample positions in a subsequent render pass, use [MTLStoreActionStore](store.md) instead to improve performance.

## See Also

### Store actions

- [MTLStoreActionDontCare](dontcare.md) — The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreActionStore](store.md) — The GPU stores the rendered contents to the texture.
- [MTLStoreActionMultisampleResolve](multisampleresolve.md) — The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.
- [MTLStoreActionStoreAndMultisampleResolve](storeandmultisampleresolve.md) — The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.
- [MTLStoreActionUnknown](unknown.md) — The system selects a store action when it encodes the render pass.
