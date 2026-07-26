---
title: 'init(objects:forKeys:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(objects:forkeys:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(objects:forkeys:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28objects%3Aforkeys%3Acount%3A%29.json'
content_hash: 'sha256:10aa05b6ee4cfeb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(objects:forKeys:count:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(objects: UnsafePointer<AnyObject>?, forKeys keys: UnsafePointer<any NSCopying>?, count cnt: Int)
```

## Parameters

- `objects` — A C array of values for the new dictionary.

- `keys` — A C array of keys for the new dictionary. Each key is copied (using [- copyWithZone:](<../nscopying/copy(with_).md>); keys must conform to the `NSCopying` protocol), and the copy is added to the new dictionary.

- `cnt` — The number of elements to use from the `keys` and `objects` arrays. `count` must not exceed the number of elements in `objects` or `keys`.

## Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if a key or value object is `nil`.

This method is a designated initializer of `NSDictionary`.

## See Also

### Related Documentation

- [- init](<init().md>) — Initializes a newly allocated dictionary.

### Creating a Dictionary from Objects and Keys

- [- initWithObjects:forKeys:](<init(objects_forkeys_).md>) — Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [+ dictionaryWithObject:forKey:](<init(object_forkey_).md>) — Creates a dictionary containing a given key and value.
