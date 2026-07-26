---
title: 'init(objects:forKeys:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(objects:forkeys:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(objects:forkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28objects%3Aforkeys%3A%29.json'
content_hash: 'sha256:9f3d196007120657'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(objects:forKeys:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(objects: [Any], forKeys keys: [any NSCopying])
```

## Parameters

- `objects` — An array containing the values for the new dictionary.

- `keys` — An array containing the keys for the new dictionary. Each key is copied (using [- copyWithZone:](<../nscopying/copy(with_).md>); keys must conform to the `NSCopying` protocol), and the copy is added to the new dictionary.

## Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if the objects and keys arrays do not have the same number of elements.

## See Also

### Creating a Dictionary from Objects and Keys

- [- initWithObjects:forKeys:count:](<init(objects_forkeys_count_).md>) — Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [+ dictionaryWithObject:forKey:](<init(object_forkey_).md>) — Creates a dictionary containing a given key and value.
