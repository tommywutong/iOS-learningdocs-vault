---
title: signum()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/signum()
source_url: 'https://developer.apple.com/documentation/swift/int/signum()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/signum%28%29.json'
content_hash: 'sha256:937821c98621b796'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# signum()

<sub>Instance Method</sub>

Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signum() -> Int
```

## Return Value

The sign of this number, expressed as an integer of the same type.

## See Also

### Finding the Sign and Magnitude

- [magnitude](magnitude-swift.property.md) — The magnitude of this value.
- [Magnitude](magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of this type.
- [abs(_:)](<../abs(__).md>) — Returns the absolute value of the given number.
