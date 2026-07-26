---
title: NSCache
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscache
source_url: 'https://developer.apple.com/documentation/foundation/nscache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache.json'
content_hash: 'sha256:6353e08be34184b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCache

<sub>Class</sub>

A mutable collection you use to temporarily store transient key-value pairs that are subject to eviction when resources are low.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSCache<KeyType, ObjectType> where KeyType : AnyObject, ObjectType : AnyObject
```

## Overview

Cache objects differ from other mutable collections in a few ways:

- The [NSCache](nscache.md) class incorporates various auto-eviction policies, which ensure that a cache doesn’t use too much of the system’s memory. If memory is needed by other applications, these policies remove some items from the cache, minimizing its memory footprint.
- You can add, remove, and query items in the cache from different threads without having to lock the cache yourself.
- Unlike an [NSMutableDictionary](nsmutabledictionary.md) object, a cache does not copy the key objects that are put into it.

You typically use [NSCache](nscache.md) objects to temporarily store objects with transient data that are expensive to create. Reusing these objects can provide performance benefits, because their values do not have to be recalculated. However, the objects are not critical to the application and can be discarded if memory is tight. If discarded, their values will have to be recomputed again when needed.

Objects that have subcomponents that can be discarded when not being used can adopt the [NSDiscardableContent](nsdiscardablecontent.md) protocol to improve cache eviction behavior. By default, [NSDiscardableContent](nsdiscardablecontent.md) objects in a cache are automatically removed if their content is discarded, although this automatic removal policy can be changed. If an [NSDiscardableContent](nsdiscardablecontent.md) object is put into the cache, the cache calls [- discardContentIfPossible](<nsdiscardablecontent/discardcontentifpossible().md>) on it upon its removal.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing the Name

- [name](nscache/name.md) — The name of the cache.

### Managing Cache Size

- [countLimit](nscache/countlimit.md) — The maximum number of objects the cache should hold.
- [totalCostLimit](nscache/totalcostlimit.md) — The maximum total cost that the cache can hold before it starts evicting objects.

### Managing Discardable Content

- [evictsObjectsWithDiscardedContent](nscache/evictsobjectswithdiscardedcontent.md) — Whether the cache will automatically evict discardable-content objects whose content has been discarded.
- [NSDiscardableContent](nsdiscardablecontent.md) — You implement this protocol when a class’s objects have subcomponents that can be discarded when not being used, thereby giving an application a smaller memory footprint.

### Managing the Delegate

- [delegate](nscache/delegate.md) — The cache’s delegate.
- [NSCacheDelegate](nscachedelegate.md) — The delegate of an [NSCache](nscache.md) object implements this protocol to perform specialized actions when an object is about to be evicted or removed from the cache.

### Getting a Cached Value

- [- objectForKey:](<nscache/object(forkey_).md>) — Returns the value associated with a given key.

### Adding and Removing Cached Values

- [- setObject:forKey:](<nscache/setobject(__forkey_).md>) — Sets the value of the specified key in the cache.
- [- setObject:forKey:cost:](<nscache/setobject(__forkey_cost_).md>) — Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [- removeObjectForKey:](<nscache/removeobject(forkey_).md>) — Removes the value of the specified key in the cache.
- [- removeAllObjects](<nscache/removeallobjects().md>) — Empties the cache.

## See Also

### Purgeable Collections

- [NSPurgeableData](nspurgeabledata.md) — A mutable data object containing bytes that can be discarded when they’re no longer needed.
