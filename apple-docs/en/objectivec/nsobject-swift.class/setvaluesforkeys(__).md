---
title: 'setValuesForKeys(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvaluesforkeys(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvaluesforkeys(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvaluesforkeys%28_%3A%29.json'
content_hash: 'sha256:88b3f2b4ab0780d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValuesForKeys(_:)

<sub>Instance Method</sub>

Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValuesForKeys(_ keyedValues: [String : Any])
```

## Parameters

- `keyedValues` — A dictionary whose keys identify properties in the receiver. The values of the properties in the receiver are set to the corresponding values in the dictionary.

## Discussion

The default implementation invokes [- setValue:forKey:](<setvalue(__forkey_).md>) for each key-value pair, substituting `nil` for `NSNull` values in `keyedValues`.

## See Also

### Related Documentation

- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — Returns a dictionary containing the property values identified by each of the keys in a given array.

### Setting Values

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — Sets the value for the property identified by a given key path to a given value.
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the property of the receiver specified by a given key to a given value.
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it finds no property for a given key.
