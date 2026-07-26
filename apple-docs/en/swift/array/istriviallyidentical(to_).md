---
title: 'isTriviallyIdentical(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/istriviallyidentical(to:)'
source_url: 'https://developer.apple.com/documentation/swift/array/istriviallyidentical(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/istriviallyidentical%28to%3A%29.json'
content_hash: 'sha256:8dc57779eed8e9f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# isTriviallyIdentical(to:)

<sub>Instance Method</sub>

Returns a boolean value indicating whether this array is identical to `other`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isTriviallyIdentical(to other: Array<Element>) -> Bool
```

## Discussion

Two array values are identical if there is no way to distinguish between them.

For any values `a`, `b`, and `c`:

- `a.isTriviallyIdentical(to: a)` is always `true`. (Reflexivity)
- `a.isTriviallyIdentical(to: b)` implies `b.isTriviallyIdentical(to: a)`. (Symmetry)
- If `a.isTriviallyIdentical(to: b)` and `b.isTriviallyIdentical(to: c)` are both `true`, then `a.isTriviallyIdentical(to: c)` is also `true`. (Transitivity)
- If `a` and `b` are `Equatable`, then `a.isTriviallyIdentical(b)` implies `a == b`. `a == b` does not imply `a.isTriviallyIdentical(b)`

Values produced by copying the same value, with no intervening mutations, compare as identical:

```swift
let d = c
print(c.isTriviallyIdentical(to: d))
// Prints true.
```

Comparing arrays this way includes comparing implementation details that are normally hidden, such as the memory location of any underlying array storage, These details aren’t considered when comparing for equality with the `==` operator. Therefore, identical arrays are guaranteed to compare equal, but not all equal arrays are identical.

> [!abstract] Complexity
> O(1)
