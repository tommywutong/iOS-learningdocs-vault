---
title: 'init(options:capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshashtable/init(options:capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/init(options:capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/init%28options%3Acapacity%3A%29.json'
content_hash: 'sha256:746868bf4254eb32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# init(options:capacity:)

<sub>Initializer</sub>

Returns a hash table initialized with the given attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(options: NSPointerFunctions.Options = [], capacity initialCapacity: Int)
```

## Parameters

- `options` — A bit field that specifies the options for the elements in the hash table. For possible values, see [NSHashTableOptions](../nshashtableoptions.md).

- `initialCapacity` — The initial number of elements the hash table can hold.

## Return Value

A hash table initialized with options specified by `options` and initial capacity of `capacity`.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)

### Initialization

- [- initWithPointerFunctions:capacity:](<init(pointerfunctions_capacity_).md>) — Returns a hash table initialized with the given functions and capacity.
