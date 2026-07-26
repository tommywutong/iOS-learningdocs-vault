---
title: zone
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector/zone
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/zone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/zone.json'
content_hash: 'sha256:21e8ec304813360c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# zone

<sub>Instance Method</sub>

Returns a zone of unscanned memory.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSZone *) zone;
```

## Return Value

A memory zone of memory that is not scanned.

## Discussion

The collector provides a [NSZoneMalloc](../nszonemalloc.md)-style allocation interface, primarily for compatibility with existing code that maintains zone affinity. Such memory is unscanned and you must free it using [NSZoneFree](../nszonefree.md).  This is exactly equivalent to calling [NSAllocateCollectable](../nsallocatecollectable.md) with the option [NSCollectorDisabledOption](../nscollectordisabledoption.md).

You should typically allocate garbage-collected memory using [NSAllocateCollectable](../nsallocatecollectable.md).
