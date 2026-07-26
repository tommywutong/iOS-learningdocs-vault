---
title: MTLLoadAction
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlloadaction
source_url: 'https://developer.apple.com/documentation/metal/mtlloadaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlloadaction.json'
content_hash: 'sha256:b3cddd8705127a5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLoadAction

<sub>Enumeration</sub>

Types of actions performed for an attachment at the start of a rendering pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLLoadAction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Load actions

- [MTLLoadActionDontCare](mtlloadaction/dontcare.md) — The GPU has permission to discard the existing contents of the attachment at the start of the render pass, replacing them with arbitrary data.
- [MTLLoadActionLoad](mtlloadaction/load.md) — The GPU preserves the existing contents of the attachment at the start of the render pass.
- [MTLLoadActionClear](mtlloadaction/clear.md) — The GPU writes a value to every pixel in the attachment at the start of the render pass.

### Initializers

- [init(rawValue:)](<mtlloadaction/init(rawvalue_).md>)

## See Also

### Encoding a render pass in parallel

- [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) — An instance that splits up a single render pass so that it can be simultaneously encoded from multiple threads.
- [MTLStoreAction](mtlstoreaction.md) — Types of actions performed for an attachment at the end of a rendering pass.
- [MTLStoreActionOptions](mtlstoreactionoptions.md) — Options that modify a store action. _(deprecated)_
