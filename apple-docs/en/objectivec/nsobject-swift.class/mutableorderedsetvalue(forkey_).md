---
title: 'mutableOrderedSetValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue%28forkey%3A%29.json'
content_hash: 'sha256:21bf030831be4908'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# mutableOrderedSetValue(forKey:)

<sub>Instance Method</sub>

Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet
```

## Parameters

- `key` — The name of a uniquing ordered to-many relationship.

## Return Value

A mutable ordered set that provides read-write access to the uniquing to-many relationship specified by `key`.

## Discussion

Objects added to the mutable set proxy become related to the receiver, and objects removed from the mutable set become unrelated. The default implementation recognizes the same simple accessor methods and set accessor methods as [- valueForKey:](<value(forkey_).md>), and follows the same direct instance variable access policies, but always returns a mutable collection proxy object instead of the immutable collection that [- valueForKey:](<value(forkey_).md>) would return.

The search pattern that `mutableOrderedSetValueForKey:` uses is described in [Accessor Search Patterns](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) in [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

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
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.
