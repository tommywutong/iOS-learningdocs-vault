---
title: 'enumerateKeysAndObjects(options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/enumeratekeysandobjects(options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/enumeratekeysandobjects(options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/enumeratekeysandobjects%28options%3Ausing%3A%29.json'
content_hash: 'sha256:0cc1e2b8eb2ba679'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# enumerateKeysAndObjects(options:using:)

<sub>Instance Method</sub>

Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateKeysAndObjects(options opts: NSEnumerationOptions = [], using block: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `opts` — Enumeration options.

- `block` — A block object to operate on entries in the dictionary.

## Discussion

If the block sets `*stop` to [true](../../swift/true.md), the enumeration stops.

## See Also

### Enumerating Dictionaries

- [- keyEnumerator](<keyenumerator().md>) — Provides an enumerator to access the keys in the dictionary.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each value in the dictionary.
- [- enumerateKeysAndObjectsUsingBlock:](<enumeratekeysandobjects(__).md>) — Applies a given block object to the entries of the dictionary.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of this sequence.
