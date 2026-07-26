---
title: 'overlaps(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/closedrange/overlaps(_:)-947dt'
source_url: 'https://developer.apple.com/documentation/swift/closedrange/overlaps(_:)-947dt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/overlaps%28_%3A%29-947dt.json'
content_hash: 'sha256:7df4e44936f409e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# overlaps(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this range and the given range contain an element in common.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func overlaps(_ other: Range<Bound>) -> Bool
```

## Parameters

- `other` — A range to check for elements in common.

## Return Value

`true` if this range and `other` have at least one element in common; otherwise, `false`.

## Discussion

This example shows two overlapping ranges:

```swift
let x: Range = 0...20
print(x.overlaps(10..<1000))
// Prints "true"
```

Because a closed range includes its upper bound, the ranges in the following example overlap:

```swift
let y = 20..<30
print(x.overlaps(y))
// Prints "true"
```

## See Also

### Comparing Ranges

- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two ranges are equal.
- [!=(_:_:)](<!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [overlaps(_:)](<overlaps(__)-7dfep.md>) — Returns a Boolean value indicating whether this range and the given closed range contain an element in common.
