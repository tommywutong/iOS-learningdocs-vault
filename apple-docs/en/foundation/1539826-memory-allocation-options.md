---
title: Memory Allocation Options
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/1539826-memory-allocation-options
source_url: 'https://developer.apple.com/documentation/foundation/1539826-memory-allocation-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1539826-memory-allocation-options.json'
content_hash: 'sha256:7a1b692ce5f90c26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Object Runtime](object-runtime.md) · [Objective-C Garbage Collection](objective-c-garbage-collection.md)

# Memory Allocation Options

<sub>API Collection</sub>

Constants used to control behavior when allocating or reallocating collectible memory.

## Overview

These constants are used as components in a bitfield to specify the behavior of [NSAllocateCollectable](nsallocatecollectable.md) and [NSReallocateCollectable](nsreallocatecollectable.md).

## Topics

### Constants

- [NSScannedOption](nsscannedoption.md) — Specifies allocation of scanned memory.
- [NSCollectorDisabledOption](nscollectordisabledoption.md) — Specifies that the block is retained, and therefore ineligible for collection. Specifying this option is equivalent to invoking [disableCollectorForPointer:](nsgarbagecollector/disablecollectorforpointer_.md) with the returned block as the argument.

## See Also

### Legacy
