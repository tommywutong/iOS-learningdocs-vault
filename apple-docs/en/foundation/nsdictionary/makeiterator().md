---
title: makeIterator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/makeiterator()
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/makeiterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/makeiterator%28%29.json'
content_hash: 'sha256:b00d83d08f9725ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# makeIterator()

<sub>Instance Method</sub>

Returns an iterator over the elements of this sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeIterator() -> NSDictionary.Iterator
```

## Discussion

Complexity: O(1).

## See Also

### Enumerating Dictionaries

- [- keyEnumerator](<keyenumerator().md>) — Provides an enumerator to access the keys in the dictionary.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each value in the dictionary.
- [- enumerateKeysAndObjectsUsingBlock:](<enumeratekeysandobjects(__).md>) — Applies a given block object to the entries of the dictionary.
- [- enumerateKeysAndObjectsWithOptions:usingBlock:](<enumeratekeysandobjects(options_using_).md>) — Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
