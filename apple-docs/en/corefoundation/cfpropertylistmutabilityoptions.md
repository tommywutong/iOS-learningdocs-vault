---
title: CFPropertyListMutabilityOptions
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfpropertylistmutabilityoptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistmutabilityoptions.json'
content_hash: 'sha256:96cfee9b01a7c6ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListMutabilityOptions

<sub>Structure</sub>

Type for flags that determine the degree of mutability of newly created property lists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFPropertyListMutabilityOptions
```

## Overview

See [Property List Mutability Options](property_list_mutability_options.md) for possible values.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<cfpropertylistmutabilityoptions/init(rawvalue_).md>)

### Type Properties

- [kCFPropertyListMutableContainers](cfpropertylistmutabilityoptions/mutablecontainers.md) — Specifies that the property list should have mutable containers but immutable leaves.
- [kCFPropertyListMutableContainersAndLeaves](cfpropertylistmutabilityoptions/mutablecontainersandleaves.md) — Specifies that the property list should have mutable containers and mutable leaves.
