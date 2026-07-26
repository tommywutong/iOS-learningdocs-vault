---
title: NSPointerFunctions.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/options
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/options.json'
content_hash: 'sha256:ec9a5936cf705cd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# NSPointerFunctions.Options

<sub>Structure</sub>

Defines the memory and personality options for an `NSPointerFunctions` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Overview

When specifying a value, you can use only one of the options listed in Memory Options,  only one of the options listed in Personality Options, and any number of other options.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Memory Options

- [NSPointerFunctionsMachVirtualMemory](options/machvirtualmemory.md) — Use Mach memory.
- [NSPointerFunctionsMallocMemory](options/mallocmemory.md) — Use `free()` on removal, `calloc()` on copy in.
- [NSPointerFunctionsOpaqueMemory](options/opaquememory.md) — Take no action when pointers are deleted.
- [NSPointerFunctionsStrongMemory](options/strongmemory.md) — Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [NSPointerFunctionsWeakMemory](options/weakmemory.md) — Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [NSMapTableStrongMemory](../nsmaptablestrongmemory.md) — Equivalent to [NSPointerFunctionsStrongMemory](options/strongmemory.md).
- [NSMapTableWeakMemory](../nsmaptableweakmemory.md) — Equivalent to [NSPointerFunctionsWeakMemory](options/weakmemory.md).

### Personality Options

- [NSPointerFunctionsCStringPersonality](options/cstringpersonality.md) — Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [NSPointerFunctionsIntegerPersonality](options/integerpersonality.md) — Use unshifted value as hash and equality.
- [NSPointerFunctionsObjectPersonality](options/objectpersonality.md) — Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [NSPointerFunctionsObjectPointerPersonality](options/objectpointerpersonality.md) — Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [NSPointerFunctionsOpaquePersonality](options/opaquepersonality.md) — Use shifted pointer for the hash value and direct comparison to determine equality.
- [NSPointerFunctionsStructPersonality](options/structpersonality.md) — Use a memory hash and `memcmp` (using a size function that you must set—see [sizeFunction](sizefunction.md)).
- [NSMapTableObjectPointerPersonality](../nsmaptableobjectpointerpersonality.md) — Equivalent to [NSPointerFunctionsObjectPointerPersonality](options/objectpointerpersonality.md).

### Copy Option

- [NSPointerFunctionsCopyIn](options/copyin.md) — Use the memory acquire function to allocate and copy items on input (see [acquireFunction](acquirefunction.md)).
- [NSMapTableCopyIn](../nsmaptablecopyin.md) — Equivalent to [NSPointerFunctionsCopyIn](options/copyin.md).

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)
