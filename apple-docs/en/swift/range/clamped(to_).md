---
title: 'clamped(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/clamped(to:)'
source_url: 'https://developer.apple.com/documentation/swift/range/clamped(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/clamped%28to%3A%29.json'
content_hash: 'sha256:941edb9d7a9cf33b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# clamped(to:)

<sub>Instance Method</sub>

Returns a copy of this range clamped to the given limiting range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func clamped(to limits: Range<Bound>) -> Range<Bound>
```

## Parameters

- `limits` — The range to clamp the bounds of this range.

## Return Value

A new range clamped to the bounds of `limits`.

## Discussion

The bounds of the result are always limited to the bounds of `limits`. For example:

```swift
let x: Range = 0..<20
print(x.clamped(to: 10..<1000))
// Prints "10..<20"
```

If the two ranges do not overlap, the result is an empty range within the bounds of `limits`.

```swift
let y: Range = 0..<5
print(y.clamped(to: 10..<1000))
// Prints "10..<10"
```
