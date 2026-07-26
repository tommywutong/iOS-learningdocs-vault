---
title: 'init(key:ascending:comparator:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssortdescriptor/init(key:ascending:comparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/init(key:ascending:comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/init%28key%3Aascending%3Acomparator%3A%29.json'
content_hash: 'sha256:2585d4cc89259d3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# init(key:ascending:comparator:)

<sub>Initializer</sub>

Creates a sort descriptor with a specified string key path and ordering, and a comparator block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(key: String?, ascending: Bool, comparator cmptr: @escaping Comparator)
```

## Parameters

- `key` — The property key for performing a comparison. For information about key paths, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

- `ascending` — [true](../../swift/true.md) if the receiver specifies sorting in ascending order; otherwise, [false](../../swift/false.md).

- `cmptr` — A comparator block.

## Return Value

A sort descriptor that initializes with the specified key, ordering, and comparator.

## See Also

### Creating a Sort Descriptor

- [- initWithKey:ascending:](<init(key_ascending_).md>) — Creates a sort descriptor with a specified string key path and sort order.
- [- initWithKey:ascending:selector:](<init(key_ascending_selector_).md>) — Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [init(keyPath:ascending:)](<init(keypath_ascending_).md>) — Creates a sort descriptor with a specified key path and ordering.
- [init(keyPath:ascending:comparator:)](<init(keypath_ascending_comparator_).md>) — Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [- initWithCoder:](<init(coder_).md>) — Creates a sort descriptor by decoding from the coder you specify.
- [init(_:)](<init(__)-7qf91.md>) — Creates a sort descriptor using a sort descriptor you specify. _(deprecated)_
