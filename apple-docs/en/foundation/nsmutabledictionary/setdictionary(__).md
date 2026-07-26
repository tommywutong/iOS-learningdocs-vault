---
title: 'setDictionary(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/setdictionary(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/setdictionary(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/setdictionary%28_%3A%29.json'
content_hash: 'sha256:ca93d5ad0686c8f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# setDictionary(_:)

<sub>Instance Method</sub>

Sets the contents of the receiving dictionary to entries in a given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDictionary(_ otherDictionary: [AnyHashable : Any])
```

## Parameters

- `otherDictionary` — A dictionary containing the new entries.

## Discussion

All entries are removed from the receiving dictionary (with [- removeAllObjects](<removeallobjects().md>)), then each entry from `otherDictionary` added into the receiving dictionary.

## See Also

### Adding Entries to a Mutable Dictionary

- [- setObject:forKey:](<setobject(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- addEntriesFromDictionary:](<addentries(from_).md>) — Adds to the receiving dictionary the entries from another dictionary.
