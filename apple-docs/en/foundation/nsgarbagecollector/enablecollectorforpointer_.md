---
title: 'enableCollectorForPointer:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsgarbagecollector/enablecollectorforpointer:'
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/enablecollectorforpointer:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/enablecollectorforpointer%3A.json'
content_hash: 'sha256:44b0e5099834c443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# enableCollectorForPointer:

<sub>Instance Method</sub>

Specifies that a given pointer may be collected.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) enableCollectorForPointer:(const void *) ptr;
```

## Parameters

- `ptr` — A pointer to the memory that may be collected.

## Discussion

You use this method to make memory that was previously marked as uncollectable. For example, given the address of the global dictionary created in [disableCollectorForPointer:](disablecollectorforpointer_.md), you could make the dictionary collectable as follows:

```objc
[[NSGarbageCollector defaultCollector]
    enableCollectorForPointer:globalDictionary];
```

For more about root objects and scanned memory, see Garbage Collection Programming Guide.

## See Also

### Manipulating External References

- [disableCollectorForPointer:](disablecollectorforpointer_.md) — Specifies that a given pointer will not be collected. _(deprecated)_
