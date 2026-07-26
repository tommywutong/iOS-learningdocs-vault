---
title: 'setNilValueForKey(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setnilvalueforkey(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setnilvalueforkey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setnilvalueforkey%28_%3A%29.json'
content_hash: 'sha256:3f40a434bded5a40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setNilValueForKey(_:)

<sub>Instance Method</sub>

Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setNilValueForKey(_ key: String)
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Discussion

Subclasses can override this method to handle the request in some other way, such as by substituting `0` or a sentinel value for `nil` and invoking [- setValue:forKey:](<setvalue(__forkey_).md>) again or setting the variable directly. The default implementation raises an `NSInvalidArgumentException`.

## See Also

### Setting Values

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — Sets the value for the property identified by a given key path to a given value.
- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the property of the receiver specified by a given key to a given value.
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it finds no property for a given key.
