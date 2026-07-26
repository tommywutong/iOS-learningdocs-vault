---
title: removeAllObjects()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutabledictionary/removeallobjects()
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/removeallobjects()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/removeallobjects%28%29.json'
content_hash: 'sha256:14548dfc9a6e765f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# removeAllObjects()

<sub>Instance Method</sub>

Empties the dictionary of its entries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeAllObjects()
```

## Discussion

Each key and corresponding value object is sent a [release](../../objectivec/nsobject-c.protocol/release.md) message.

## See Also

### Removing Entries From a Mutable Dictionary

- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes a given key and its associated value from the dictionary.
- [- removeObjectsForKeys:](<removeobjects(forkeys_).md>) — Removes from the dictionary entries specified by elements in a given array.
