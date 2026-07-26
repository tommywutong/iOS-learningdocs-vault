---
title: 'starts(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawbufferpointer/starts(with:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/starts(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/starts%28with%3A%29.json'
content_hash: 'sha256:34fc8211812a54e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# starts(with:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func starts<PossiblePrefix>(with possiblePrefix: PossiblePrefix) -> Bool where PossiblePrefix : Sequence, Self.Element == PossiblePrefix.Element
```

## Parameters

- `possiblePrefix` — A sequence to compare to this sequence.

## Return Value

`true` if the initial elements of the sequence are the same as the elements of `possiblePrefix`; otherwise, `false`. If `possiblePrefix` has no elements, the return value is `true`.

## Discussion

This example tests whether one countable range begins with the elements of another countable range.

```swift
let a = 1...3
let b = 1...10

print(b.starts(with: a))
// Prints "true"
```

Passing a sequence with no elements or an empty collection as `possiblePrefix` always results in `true`.

```swift
print(b.starts(with: []))
// Prints "true"
```

> [!abstract] Complexity
> O(_m_), where _m_ is the lesser of the length of the sequence and the length of `possiblePrefix`.
