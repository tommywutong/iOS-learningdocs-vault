---
title: 'setValue(_:forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:7bbd6f39dff261a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValue(_:forKey:)

<sub>Instance Method</sub>

Sets the property of the receiver specified by a given key to a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The value for the property identified by `key`.

- `key` — The name of one of the receiver’s properties.

## Discussion

If `key` identifies a to-one relationship, relate the object specified by `value` to the receiver, unrelating the previously related object if there was one. Given a collection object and a `key` that identifies a to-many relationship, relate the objects contained in the collection to the receiver, unrelating previously related objects if there were any.

The search pattern that `setValue:forKey:` uses is described in [Accessor Search Patterns](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) in [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

In a reference-counted environment, if the instance variable is accessed directly, `value` is retained.

## See Also

### Setting Values

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — Sets the value for the property identified by a given key path to a given value.
- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it finds no property for a given key.
