---
title: 'setValue(_:forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstorecachenode/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstorecachenode/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:6d64830178cb1693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStoreCacheNode](../nsatomicstorecachenode.md)

# setValue(_:forKey:)

<sub>Instance Method</sub>

Sets the value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The value for the property identified by `key`.

- `key` — The name of a property.

## Discussion

The default implementation forwards the request to the [propertyCache](propertycache.md) dictionary if `key` matches a property name of the entity for this cache node. If `key` does not represent a property, the standard [setValue(_:forKey:)](<../../objectivec/nsobject-swift.class/setvalue(__forkey_).md>) implementation is used.

## See Also

### Managing Node Data

- [objectID](objectid.md) — The managed object ID of the node.
- [propertyCache](propertycache.md) — The property cache dictionary of the node.
- [- valueForKey:](<value(forkey_).md>) — Returns the value for a given key.
