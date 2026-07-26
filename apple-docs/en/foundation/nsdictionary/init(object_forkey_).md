---
title: 'init(object:forKey:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(object:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(object:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28object%3Aforkey%3A%29.json'
content_hash: 'sha256:04e87052c75331ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(object:forKey:)

<sub>Initializer</sub>

Creates a dictionary containing a given key and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(object: Any, forKey key: any NSCopying)
```

## Parameters

- `object` — The value corresponding to `aKey`. If this value is `nil`, an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) is raised.

- `key` — The key for `anObject`. If this value is `nil`, an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) is raised.

## Return Value

A new dictionary containing a single object, `object`, for a single key, `aKey`.

## See Also

### Creating a Dictionary from Objects and Keys

- [- initWithObjects:forKeys:](<init(objects_forkeys_).md>) — Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [- initWithObjects:forKeys:count:](<init(objects_forkeys_count_).md>) — Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
