---
title: MTLStoreAction.multisampleResolve
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstoreaction/multisampleresolve
source_url: 'https://developer.apple.com/documentation/metal/mtlstoreaction/multisampleresolve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoreaction/multisampleresolve.json'
content_hash: 'sha256:994bef412fe08566'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStoreAction](../mtlstoreaction.md)

# MTLStoreAction.multisampleResolve

<sub>Case</sub>

The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case multisampleResolve
```

## Discussion

Use this option when you need to resolve the multisample attachment’s contents at the end of the render pass but don’t need the multisample data afterwards. Some GPUs may still store the multisample data back to the texture, but you can’t rely on that behavior. You need to assume that GPU discarded the multisample texture’s contents.

## See Also

### Store actions

- [MTLStoreActionDontCare](dontcare.md) — The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreActionStore](store.md) — The GPU stores the rendered contents to the texture.
- [MTLStoreActionStoreAndMultisampleResolve](storeandmultisampleresolve.md) — The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.
- [MTLStoreActionUnknown](unknown.md) — The system selects a store action when it encodes the render pass.
- [MTLStoreActionCustomSampleDepthStore](customsampledepthstore.md) — The GPU stores depth data in a sample-position–agnostic representation.
