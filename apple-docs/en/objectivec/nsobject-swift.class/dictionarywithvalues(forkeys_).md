---
title: 'dictionaryWithValues(forKeys:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/dictionarywithvalues(forkeys:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/dictionarywithvalues(forkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/dictionarywithvalues%28forkeys%3A%29.json'
content_hash: 'sha256:569eb9b99fe3f245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# dictionaryWithValues(forKeys:)

<sub>Instance Method</sub>

Returns a dictionary containing the property values identified by each of the keys in a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]
```

## Parameters

- `keys` — An array containing `NSString` objects that identify properties of the receiver.

## Return Value

A dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values.

## Discussion

The default implementation invokes [- valueForKey:](<value(forkey_).md>) for each key in `keys` and substitutes `NSNull` values in the dictionary for returned `nil` values.

## See Also

### Related Documentation

- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.

### Getting Values

- [- valueForKey:](<value(forkey_).md>) — Returns the value for the property identified by a given key.
- [- valueForKeyPath:](<value(forkeypath_).md>) — Returns the value for the derived property identified by a given key path.
- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — Invoked by [- valueForKey:](<value(forkey_).md>) when it finds no property corresponding to a given key.
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.
- [- mutableArrayValueForKeyPath:](<mutablearrayvalue(forkeypath_).md>) — Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.
