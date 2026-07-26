---
title: 'value(forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstorecachenode/value(forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/value(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstorecachenode/value%28forkey%3A%29.json'
content_hash: 'sha256:c32674abb07cf57a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStoreCacheNode](../nsatomicstorecachenode.md)

# value(forKey:)

<sub>Instance Method</sub>

Returns the value for a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forKey key: String) -> Any?
```

## Parameters

- `key` — The name of a property.

## Return Value

The value for the property named `key`. For an attribute, the return value is an instance of an attribute type supported by Core Data (see [NSAttributeDescription](../nsattributedescription.md)); for a to-one relationship, the return value must be another cache node instance; for a to-many relationship, the return value must be an collection of the related cache nodes.

## Discussion

The default implementation forwards the request to the [propertyCache](propertycache.md) dictionary if `key` matches a property name of the entity for the cache node. If `key` does not represent a property, the standard [value(forKey:)](<../../objectivec/nsobject-swift.class/value(forkey_).md>) implementation is used.

## See Also

### Managing Node Data

- [objectID](objectid.md) — The managed object ID of the node.
- [propertyCache](propertycache.md) — The property cache dictionary of the node.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the value for the given key.
