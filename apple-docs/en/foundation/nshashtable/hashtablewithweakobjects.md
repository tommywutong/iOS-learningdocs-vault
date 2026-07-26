---
title: hashTableWithWeakObjects
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nshashtable/hashtablewithweakobjects
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/hashtablewithweakobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/hashtablewithweakobjects.json'
content_hash: 'sha256:bafe7b85b435cf4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# hashTableWithWeakObjects

<sub>Type Method</sub>

Returns a new hash table for storing weak references to its contents.

> [!warning] Deprecated
> Use [+ weakObjectsHashTable](<weakobjects().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) hashTableWithWeakObjects;
```

## Return Value

A new has table that uses the options [NSHashTableZeroingWeakMemory](../nshashtablezeroingweakmemory.md) and [NSPointerFunctionsObjectPersonality](../nspointerfunctions/options/objectpersonality.md) and has an initial capacity of `0`.

## Discussion

This method is not supported under Automatic Reference Counting (ARC).

## See Also

### Deprecated

- [Legacy Hash Table Implementation](../legacy-hash-table-implementation.md)
