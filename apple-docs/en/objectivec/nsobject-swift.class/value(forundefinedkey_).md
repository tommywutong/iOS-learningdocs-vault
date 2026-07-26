---
title: 'value(forUndefinedKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(forundefinedkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forundefinedkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28forundefinedkey%3A%29.json'
content_hash: 'sha256:7231abe968f2362b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(forUndefinedKey:)

<sub>Instance Method</sub>

Invoked by [- valueForKey:](<value(forkey_).md>) when it finds no property corresponding to a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forUndefinedKey key: String) -> Any?
```

## Parameters

- `key` — A string that is not equal to the name of any of the receiver’s properties.

## Discussion

Subclasses can override this method to return an alternate value for undefined keys. The default implementation raises an `NSUndefinedKeyException`.

## See Also

### Related Documentation

- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it finds no property for a given key.

### Getting Values

- [- valueForKey:](<value(forkey_).md>) — Returns the value for the property identified by a given key.
- [- valueForKeyPath:](<value(forkeypath_).md>) — Returns the value for the derived property identified by a given key path.
- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — Returns a dictionary containing the property values identified by each of the keys in a given array.
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.
- [- mutableArrayValueForKeyPath:](<mutablearrayvalue(forkeypath_).md>) — Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.
