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
doc_path: '/documentation/swift/closedrange/clamped(to:)'
source_url: 'https://developer.apple.com/documentation/swift/closedrange/clamped(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/clamped%28to%3A%29.json'
content_hash: 'sha256:ffb91f6233fbd117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# clamped(to:)

<sub>Instance Method</sub>

Returns a copy of this range clamped to the given limiting range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func clamped(to limits: ClosedRange<Bound>) -> ClosedRange<Bound>
```

## Parameters

- `limits` — The range to clamp the bounds of this range.

## Return Value

A new range clamped to the bounds of `limits`.

## Discussion

The bounds of the result are always limited to the bounds of `limits`. For example:

```swift
let x: ClosedRange = 0...20
print(x.clamped(to: 10...1000))
// Prints "10...20"
```

If the two ranges do not overlap, the result is a single-element range at the upper or lower bound of `limits`.

```swift
let y: ClosedRange = 0...5
print(y.clamped(to: 10...1000))
// Prints "10...10"
```
