---
title: 'setValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:3fcb8b950e241b2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# setValue(_:forKey:)

<sub>Instance Method</sub>

Adds a given key-value pair to the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The value for `key`.

- `key` — The key for `value`. Note that when using key-value coding, the key must be a string (see [Accessing Object Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170)).

## Discussion

This method adds `value` and `key` to the dictionary using [- setObject:forKey:](<setobject(__forkey_).md>), unless `value` is `nil` in which case the method instead attempts to remove `key` using [- removeObjectForKey:](<removeobject(forkey_).md>).

## See Also

### Related Documentation

- [- valueForKey:](<../nsdictionary/value(forkey_).md>) — Returns the value associated with a given key.

### Adding Entries to a Mutable Dictionary

- [- setObject:forKey:](<setobject(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- addEntriesFromDictionary:](<addentries(from_).md>) — Adds to the receiving dictionary the entries from another dictionary.
- [- setDictionary:](<setdictionary(__).md>) — Sets the contents of the receiving dictionary to entries in a given dictionary.
