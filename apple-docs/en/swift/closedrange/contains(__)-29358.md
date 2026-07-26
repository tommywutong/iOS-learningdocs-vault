---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/closedrange/contains(_:)-29358'
source_url: 'https://developer.apple.com/documentation/swift/closedrange/contains(_:)-29358'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/contains%28_%3A%29-29358.json'
content_hash: 'sha256:6ba2959dd4cee36e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given range is contained within this closed range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ other: Range<Bound>) -> Bool
```

## Parameters

- `other` — A range to check for containment within this closed range.

## Return Value

`true` if `other` is empty or wholly contained within this closed range; otherwise, `false`.

## Discussion

The given range is contained within this closed range if the elements of the range are all contained within this closed range.

```swift
let range = 0...10
range.contains(5..<7)     // true
range.contains(5..<10)    // true
range.contains(5..<12)    // false

// Note that `5..<11` contains 5, 6, 7, 8, 9, and 10.
range.contains(5..<11)    // true
```

Additionally, passing any empty range as `other` results in the value `true`, even if the empty range’s bounds are outside the bounds of this closed range.

```swift
range.contains(3..<3)     // true
range.contains(20..<20)   // true
```

> [!abstract] Complexity
> O(1)
