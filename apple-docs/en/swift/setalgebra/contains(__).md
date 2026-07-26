---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/contains%28_%3A%29.json'
content_hash: 'sha256:163bf23b41a58133'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the given element exists in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ member: Self.Element) -> Bool
```

## Parameters

- `member` — An element to look for in the set.

## Return Value

`true` if `member` exists in the set; otherwise, `false`.

## Discussion

This example uses the `contains(_:)` method to test whether an integer is a member of a set of prime numbers.

```swift
let primes: Set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
let x = 5
if primes.contains(x) {
    print("\(x) is prime!")
} else {
    print("\(x). Not prime.")
}
// Prints "5 is prime!"
```

## Default Implementations

### SetAlgebra Implementations

- [contains(_:)](<contains(__)-xkyd.md>) — Returns a Boolean value that indicates whether a given element is a member of the option set.

## See Also

### Testing for Membership

- [Element](element.md) — A type for which the conforming type provides a containment test.
