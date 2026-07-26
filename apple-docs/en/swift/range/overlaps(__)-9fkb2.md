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
doc_path: '/documentation/swift/range/overlaps(_:)-9fkb2'
source_url: 'https://developer.apple.com/documentation/swift/range/overlaps(_:)-9fkb2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/overlaps%28_%3A%29-9fkb2.json'
content_hash: 'sha256:398390e82ea741fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# overlaps(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this range and the given closed range contain an element in common.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func overlaps(_ other: ClosedRange<Bound>) -> Bool
```

## Parameters

- `other` — A closed range to check for elements in common.

## Return Value

`true` if this range and `other` have at least one element in common; otherwise, `false`.

## Discussion

This example shows two overlapping ranges:

```swift
let x: Range = 0..<20
print(x.overlaps(10...1000))
// Prints "true"
```

Because a half-open range does not include its upper bound, the ranges in the following example do not overlap:

```swift
let y = 20...30
print(x.overlaps(y))
// Prints "false"
```

## See Also

### Comparing Ranges

- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two ranges are equal.
- [!=(_:_:)](<!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [overlaps(_:)](<overlaps(__)-7osha.md>) — Returns a Boolean value indicating whether this range and the given range contain an element in common.
