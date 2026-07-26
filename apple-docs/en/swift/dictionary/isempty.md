---
title: isEmpty
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/isempty
source_url: 'https://developer.apple.com/documentation/swift/dictionary/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/isempty.json'
content_hash: 'sha256:1708ef6478ab0f5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value that indicates whether the dictionary is empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

Dictionaries are empty when created with an initializer or an empty dictionary literal.

```swift
var frequencies: [String: Int] = [:]
print(frequencies.isEmpty)
// Prints "true"
```

## See Also

### Inspecting a Dictionary

- [count](count.md) — The number of key-value pairs in the dictionary.
- [capacity](capacity.md) — The total number of key-value pairs that the dictionary can contain without allocating new storage.
