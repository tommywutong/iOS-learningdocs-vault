---
title: 'setObject(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/setobject(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/setobject(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/setobject%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:930dccc9ce50fd7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# setObject(_:forKey:)

<sub>Instance Method</sub>

Adds a given key-value pair to the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setObject(_ anObject: Any, forKey aKey: any NSCopying)
```

## Parameters

- `anObject` — The value for `aKey`. A strong reference to the object is maintained by the dictionary. > [!important] Important > Raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if `anObject` is `nil`. If you need to represent a `nil` value in the dictionary, use [NSNull](../nsnull.md).

- `aKey` — The key for `value`. The key is copied (using [- copyWithZone:](<../nscopying/copy(with_).md>); keys must conform to the `NSCopying` protocol). If `aKey` already exists in the dictionary, `anObject` takes its place. > [!important] Important > Raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if `aKey` is `nil`.

## See Also

### Related Documentation

- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes a given key and its associated value from the dictionary.

### Adding Entries to a Mutable Dictionary

- [- setValue:forKey:](<setvalue(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- addEntriesFromDictionary:](<addentries(from_).md>) — Adds to the receiving dictionary the entries from another dictionary.
- [- setDictionary:](<setdictionary(__).md>) — Sets the contents of the receiving dictionary to entries in a given dictionary.
