---
title: 'disableCollectorForPointer:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsgarbagecollector/disablecollectorforpointer:'
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector/disablecollectorforpointer:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector/disablecollectorforpointer%3A.json'
content_hash: 'sha256:4dfc4a8ac4c12d4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSGarbageCollector](../nsgarbagecollector.md)

# disableCollectorForPointer:

<sub>Instance Method</sub>

Specifies that a given pointer will not be collected.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) disableCollectorForPointer:(const void *) ptr;
```

## Parameters

- `ptr` — A pointer to the memory that should not be collected.

## Discussion

You use this method to ensure that memory at a given address will not be collected. You can use this, for example, to create new root objects:

```objc
NSMutableDictionary *globalDictionary;
globalDictionary = [NSMutableDictionary dictionary];
[[NSGarbageCollector defaultCollector]
    disableCollectorForPointer:globalDictionary];
```

The new dictionary will not be collectable and will persist for the lifetime of the application unless it is subsequently passed as the argument to [enableCollectorForPointer:](enablecollectorforpointer_.md). For more about root objects and scanned memory, see Garbage Collection Programming Guide.

## See Also

### Manipulating External References

- [enableCollectorForPointer:](enablecollectorforpointer_.md) — Specifies that a given pointer may be collected. _(deprecated)_
