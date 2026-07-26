---
title: 'init(objectID:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstorecachenode/init(objectid:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/init(objectid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstorecachenode/init%28objectid%3A%29.json'
content_hash: 'sha256:156134a643c0b8c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStoreCacheNode](../nsatomicstorecachenode.md)

# init(objectID:)

<sub>Initializer</sub>

Returns a cache node for the given managed object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(objectID moid: NSManagedObjectID)
```

## Parameters

- `moid` — A managed object ID.

## Return Value

A cache node for the given managed object ID, or `nil` if the node could not be initialized.

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
