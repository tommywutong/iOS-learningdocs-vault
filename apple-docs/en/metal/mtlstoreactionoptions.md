---
title: MTLStoreActionOptions
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlstoreactionoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlstoreactionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoreactionoptions.json'
content_hash: 'sha256:b0c3311663e8a6e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStoreActionOptions

<sub>Structure</sub>

Options that modify a store action.

> [!warning] Deprecated
> Store action options have no effect on Apple Silicon

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLStoreActionOptions
```

## Overview

This property modifies the intended behavior of the store actions in the [MTLStoreAction](mtlstoreaction.md) enumeration.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Using programmable sample positions

- [MTLStoreActionOptionCustomSamplePositions](mtlstoreactionoptions/customsamplepositions.md) — An option that stores data in a sample-position–agnostic representation. _(deprecated)_

### Initializers

- [init(rawValue:)](<mtlstoreactionoptions/init(rawvalue_).md>) — Creates a store action option from a raw integer value. _(deprecated)_

## See Also

### Encoding a render pass in parallel

- [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) — An instance that splits up a single render pass so that it can be simultaneously encoded from multiple threads.
- [MTLLoadAction](mtlloadaction.md) — Types of actions performed for an attachment at the start of a rendering pass.
- [MTLStoreAction](mtlstoreaction.md) — Types of actions performed for an attachment at the end of a rendering pass.
