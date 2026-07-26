---
title: 'setValue(_:forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvalue(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvalue%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:7bdacc7d392f0109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValue(_:forKeyPath:)

<sub>Instance Method</sub>

Sets the value for the property identified by a given key path to a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKeyPath keyPath: String)
```

## Parameters

- `value` — The value for the property identified by `keyPath`.

- `keyPath` — A key path of the form relationship.property (with one or more relationships): for example “department.name” or “department.manager.lastName.”

## Discussion

The default implementation of this method gets the destination object for each relationship using [- valueForKey:](<value(forkey_).md>), and sends the final object a [- setValue:forKey:](<setvalue(__forkey_).md>) message.

### Special Considerations

When using this method, and the destination object does not implement an accessor for the value, the default behavior is for that object to retain `value` rather than copy or assign `value`.

## See Also

### Related Documentation

- [- valueForKeyPath:](<value(forkeypath_).md>) — Returns the value for the derived property identified by a given key path.

### Setting Values

- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the property of the receiver specified by a given key to a given value.
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — Invoked by [- setValue:forKey:](<setvalue(__forkey_).md>) when it finds no property for a given key.
