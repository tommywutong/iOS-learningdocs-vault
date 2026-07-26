---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/endindex
source_url: 'https://developer.apple.com/documentation/swift/dictionary/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/endindex.json'
content_hash: 'sha256:a8fd8c28510c00e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# endIndex

<sub>Instance Property</sub>

The dictionary’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: Dictionary<Key, Value>.Index { get }
```

## Discussion

If the collection is empty, `endIndex` is equal to `startIndex`.

> [!abstract] Complexity
> Amortized O(1) if the dictionary does not wrap a bridged `NSDictionary`; otherwise, the performance is unspecified.
