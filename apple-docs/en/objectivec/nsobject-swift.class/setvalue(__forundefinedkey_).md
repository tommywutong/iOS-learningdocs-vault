---
title: 'setValue(_:forUndefinedKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvalue(_:forundefinedkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forundefinedkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvalue%28_%3Aforundefinedkey%3A%29.json'
content_hash: 'sha256:5ce401c0c34f0c57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValue(_:forUndefinedKey:)

<sub>Instance Method</sub>

Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it finds no property for a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forUndefinedKey key: String)
```

## Parameters

- `value` — The value for the key identified by `key`.

- `key` — A string that is not equal to the name of any of the receiver’s properties.

## Discussion

Subclasses can override this method to handle the request in some other way. The default implementation raises an `NSUndefinedKeyException`.

## See Also

### Related Documentation

- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — Invoked by [- valueForKey:](<value(forkey_).md>) when it finds no property corresponding to a given key.

### Setting Values

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — Sets the value for the property identified by a given key path to a given value.
- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the property of the receiver specified by a given key to a given value.
