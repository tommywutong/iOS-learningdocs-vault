---
title: 'init(pointerFunctions:capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshashtable/init(pointerfunctions:capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/init(pointerfunctions:capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/init%28pointerfunctions%3Acapacity%3A%29.json'
content_hash: 'sha256:d8e8c3847d995945'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# init(pointerFunctions:capacity:)

<sub>Initializer</sub>

Returns a hash table initialized with the given functions and capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pointerFunctions functions: NSPointerFunctions, capacity initialCapacity: Int)
```

## Parameters

- `functions` — The pointer functions for the new hash table.

- `initialCapacity` — The initial capacity of the hash table.

## Return Value

A hash table initialized with the given functions and capacity.

## Discussion

Hash tables allocate additional memory as needed, so `initialCapacity` simply establishes the object’s initial capacity.

## See Also

### Initialization

- [- initWithOptions:capacity:](<init(options_capacity_).md>) — Returns a hash table initialized with the given attributes.
