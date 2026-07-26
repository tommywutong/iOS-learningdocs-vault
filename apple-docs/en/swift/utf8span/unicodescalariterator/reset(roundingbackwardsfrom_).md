---
title: 'reset(roundingBackwardsFrom:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/unicodescalariterator/reset(roundingbackwardsfrom:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/reset(roundingbackwardsfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/reset%28roundingbackwardsfrom%3A%29.json'
content_hash: 'sha256:45dd792a40c2ae0b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# reset(roundingBackwardsFrom:)

<sub>Instance Method</sub>

Reset to the nearest scalar-aligned code unit offset `<= i`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reset(roundingBackwardsFrom i: Int)
```

## Discussion

```swift
func printScalarAfterReset(_ string: borrowing String) {
    var iterator = string.utf8Span.makeUnicodeScalarIterator()
    iterator.reset(roundingBackwardsFrom: 8)  // Position 8 is mid-emoji, rounds back to 6
    if let scalar = iterator.next() {
        print(scalar)  // Prints "🌍" (emoji starts at byte 6)
    }
}
let string = "Hello 🌍"
printScalarAfterReset(string)
```

> [!abstract] Complexity
> O(1)
