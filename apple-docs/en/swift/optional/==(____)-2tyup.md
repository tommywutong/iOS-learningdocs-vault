---
title: '==(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/==(_:_:)-2tyup'
source_url: 'https://developer.apple.com/documentation/swift/optional/==(_:_:)-2tyup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/%3D%3D%28_%3A_%3A%29-2tyup.json'
content_hash: 'sha256:bb0b5a2dc6f7a78b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the left-hand-side argument is `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == (lhs: borrowing Wrapped?, rhs: _OptionalNilComparisonType) -> Bool
```

## Parameters

- `lhs` — A value to compare to `nil`.

- `rhs` — A `nil` literal.

## Discussion

You can use this equal-to operator (`==`) to test whether an optional instance is `nil` even when the wrapped value’s type does not conform to the `Equatable` protocol.

The following example declares the `stream` variable as an optional instance of a hypothetical `DataStream` type. Although `DataStream` is not an `Equatable` type, this operator allows checking whether `stream` is `nil`.

```swift
var stream: DataStream? = nil
if stream == nil {
    print("No data stream is configured.")
}
// Prints "No data stream is configured."
```
