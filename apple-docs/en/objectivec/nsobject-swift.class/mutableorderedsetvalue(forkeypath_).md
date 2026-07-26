---
title: 'mutableOrderedSetValue(forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue(forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue(forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue%28forkeypath%3A%29.json'
content_hash: 'sha256:e0f0415b773f751b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# mutableOrderedSetValue(forKeyPath:)

<sub>Instance Method</sub>

Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet
```

## Parameters

- `keyPath` — A key path, relative to the receiver, to a uniquing ordered to-many relationship represented by a set.

## Return Value

A mutable ordered set that provides read-write access to the uniquing to-many relationship specified by `keyPath`.

## Discussion

See [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) for additional details.

## See Also

### Getting Values

- [- valueForKey:](<value(forkey_).md>) — Returns the value for the property identified by a given key.
- [- valueForKeyPath:](<value(forkeypath_).md>) — Returns the value for the derived property identified by a given key path.
- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — Returns a dictionary containing the property values identified by each of the keys in a given array.
- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — Invoked by [- valueForKey:](<value(forkey_).md>) when it finds no property corresponding to a given key.
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.
- [- mutableArrayValueForKeyPath:](<mutablearrayvalue(forkeypath_).md>) — Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.
