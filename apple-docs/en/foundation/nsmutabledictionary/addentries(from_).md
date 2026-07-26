---
title: 'addEntries(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/addentries(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/addentries(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/addentries%28from%3A%29.json'
content_hash: 'sha256:efdac71e064f5b65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# addEntries(from:)

<sub>Instance Method</sub>

Adds to the receiving dictionary the entries from another dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addEntries(from otherDictionary: [AnyHashable : Any])
```

## Parameters

- `otherDictionary` — The dictionary from which to add entries

## Discussion

Each value object from `otherDictionary` is sent a [retain](../../objectivec/nsobject-c.protocol/retain.md) message before being added to the receiving dictionary. In contrast, each key object is copied (using [- copyWithZone:](<../nscopying/copy(with_).md>)—keys must conform to the `NSCopying` protocol), and the copy is added to the receiving dictionary.

If both dictionaries contain the same key, the receiving dictionary’s previous value object for that key is sent a `release` message, and the new value object takes its place.

## See Also

### Adding Entries to a Mutable Dictionary

- [- setObject:forKey:](<setobject(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- setDictionary:](<setdictionary(__).md>) — Sets the contents of the receiving dictionary to entries in a given dictionary.
