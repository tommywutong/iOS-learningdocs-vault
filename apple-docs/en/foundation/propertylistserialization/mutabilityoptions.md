---
title: PropertyListSerialization.MutabilityOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/propertylistserialization/mutabilityoptions
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization/mutabilityoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization/mutabilityoptions.json'
content_hash: 'sha256:275498a5334ccb86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListSerialization](../propertylistserialization.md)

# PropertyListSerialization.MutabilityOptions

<sub>Structure</sub>

These constants specify mutability options in property lists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MutabilityOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSPropertyListMutableContainers](mutabilityoptions/mutablecontainers.md) — Causes the returned property list to have mutable containers but immutable leaves.
- [NSPropertyListMutableContainersAndLeaves](mutabilityoptions/mutablecontainersandleaves.md) — Causes the returned property list to have mutable containers and leaves.

### Initializers

- [init(rawValue:)](<mutabilityoptions/init(rawvalue_).md>)

## See Also

### Constants

- [PropertyListFormat](propertylistformat.md) — These constants are used to specify a property list serialization format.
- [ReadOptions](readoptions.md) — The only read options supported are described in [MutabilityOptions](mutabilityoptions.md).
