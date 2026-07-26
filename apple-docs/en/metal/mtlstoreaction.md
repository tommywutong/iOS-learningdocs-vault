---
title: MTLStoreAction
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstoreaction
source_url: 'https://developer.apple.com/documentation/metal/mtlstoreaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoreaction.json'
content_hash: 'sha256:d9e672407faa43d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStoreAction

<sub>Enumeration</sub>

Types of actions performed for an attachment at the end of a rendering pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLStoreAction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Store actions

- [MTLStoreActionDontCare](mtlstoreaction/dontcare.md) — The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreActionStore](mtlstoreaction/store.md) — The GPU stores the rendered contents to the texture.
- [MTLStoreActionMultisampleResolve](mtlstoreaction/multisampleresolve.md) — The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.
- [MTLStoreActionStoreAndMultisampleResolve](mtlstoreaction/storeandmultisampleresolve.md) — The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.
- [MTLStoreActionUnknown](mtlstoreaction/unknown.md) — The system selects a store action when it encodes the render pass.
- [MTLStoreActionCustomSampleDepthStore](mtlstoreaction/customsampledepthstore.md) — The GPU stores depth data in a sample-position–agnostic representation.

### Initializers

- [init(rawValue:)](<mtlstoreaction/init(rawvalue_).md>)

## See Also

### Encoding a render pass in parallel

- [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) — An instance that splits up a single render pass so that it can be simultaneously encoded from multiple threads.
- [MTLLoadAction](mtlloadaction.md) — Types of actions performed for an attachment at the start of a rendering pass.
- [MTLStoreActionOptions](mtlstoreactionoptions.md) — Options that modify a store action. _(deprecated)_
