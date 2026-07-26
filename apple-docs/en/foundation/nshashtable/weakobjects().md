---
title: weakObjects()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtable/weakobjects()
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/weakobjects()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/weakobjects%28%29.json'
content_hash: 'sha256:8905bd5e85bc92d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# weakObjects()

<sub>Type Method</sub>

Returns a new hash table for storing weak references to its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func weakObjects() -> NSHashTable<ObjectType>
```

## Return Value

A new hash table that uses the [NSPointerFunctionsWeakMemory](../nspointerfunctions/options/weakmemory.md) options and [NSPointerFunctionsObjectPersonality](../nspointerfunctions/options/objectpersonality.md) and has an initial capacity of `0`.

## See Also

### Convenience Constructors

- [+ hashTableWithOptions:](<init(options_).md>) — Returns a hash table with given pointer functions options.
