---
title: 'lexicographicallyPrecedes(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/lexicographicallyprecedes(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/lexicographicallyprecedes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/lexicographicallyprecedes%28_%3A%29.json'
content_hash: 'sha256:c7fecc6ffd665e46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# lexicographicallyPrecedes(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lexicographicallyPrecedes<OtherSequence>(_ other: OtherSequence) -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

## Parameters

- `other` — A sequence to compare to this sequence.

## Return Value

`true` if this sequence precedes `other` in a dictionary ordering; otherwise, `false`.

## Discussion

This example uses the `lexicographicallyPrecedes` method to test which array of integers comes first in a lexicographical ordering.

```swift
let a = [1, 2, 2, 2]
let b = [1, 2, 3, 4]

print(a.lexicographicallyPrecedes(b))
// Prints "true"
print(b.lexicographicallyPrecedes(b))
// Prints "false"
```

> [!note] Note
> This method implements the mathematical notion of lexicographical ordering, which has no connection to Unicode.  If you are sorting strings to present to the end user, use `String` APIs that perform localized comparison.

> [!abstract] Complexity
> O(_m_), where _m_ is the lesser of the length of the sequence and the length of `other`.
