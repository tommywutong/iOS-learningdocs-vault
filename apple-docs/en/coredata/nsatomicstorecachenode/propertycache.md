---
title: propertyCache
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsatomicstorecachenode/propertycache
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/propertycache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstorecachenode/propertycache.json'
content_hash: 'sha256:5097e03f5ca6fceb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStoreCacheNode](../nsatomicstorecachenode.md)

# propertyCache

<sub>Instance Property</sub>

The property cache dictionary of the node.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var propertyCache: NSMutableDictionary? { get set }
```

## Discussion

This dictionary is used by [- valueForKey:](<value(forkey_).md>) and [- setValue:forKey:](<setvalue(__forkey_).md>) for property values. This property is `nil` unless it has been explicitly set or non-`nil` values have been set for keys using [- setValue:forKey:](<setvalue(__forkey_).md>).

## See Also

### Managing Node Data

- [objectID](objectid.md) — The managed object ID of the node.
- [- valueForKey:](<value(forkey_).md>) — Returns the value for a given key.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the value for the given key.
