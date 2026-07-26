---
title: 'removeObjects(forKeys:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/removeobjects(forkeys:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/removeobjects(forkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/removeobjects%28forkeys%3A%29.json'
content_hash: 'sha256:545ab3b955fb29ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# removeObjects(forKeys:)

<sub>Instance Method</sub>

Removes from the dictionary entries specified by elements in a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObjects(forKeys keyArray: [Any])
```

## Parameters

- `keyArray` — An array of objects specifying the keys to remove.

## Discussion

If a key in `keyArray` does not exist, the entry is ignored.

## See Also

### Removing Entries From a Mutable Dictionary

- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes a given key and its associated value from the dictionary.
- [- removeAllObjects](<removeallobjects().md>) — Empties the dictionary of its entries.
