---
title: reversed()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/values-swift.struct/reversed()
source_url: 'https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/reversed()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/values-swift.struct/reversed%28%29.json'
content_hash: 'sha256:a2165db11b48fdeb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Values](../values-swift.struct.md)

# reversed()

<sub>Instance Method</sub>

Returns an array containing the elements of this sequence in reverse order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reversed() -> [Self.Element]
```

## Return Value

An array containing the elements of this sequence in reverse order.

## Discussion

The sequence must be finite.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.
