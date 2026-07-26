---
title: MTLStoreAction.storeAndMultisampleResolve
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstoreaction/storeandmultisampleresolve
source_url: 'https://developer.apple.com/documentation/metal/mtlstoreaction/storeandmultisampleresolve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoreaction/storeandmultisampleresolve.json'
content_hash: 'sha256:580f0afb91792a5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStoreAction](../mtlstoreaction.md)

# MTLStoreAction.storeAndMultisampleResolve

<sub>Case</sub>

The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case storeAndMultisampleResolve
```

## See Also

### Store actions

- [MTLStoreActionDontCare](dontcare.md) — The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreActionStore](store.md) — The GPU stores the rendered contents to the texture.
- [MTLStoreActionMultisampleResolve](multisampleresolve.md) — The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.
- [MTLStoreActionUnknown](unknown.md) — The system selects a store action when it encodes the render pass.
- [MTLStoreActionCustomSampleDepthStore](customsampledepthstore.md) — The GPU stores depth data in a sample-position–agnostic representation.
