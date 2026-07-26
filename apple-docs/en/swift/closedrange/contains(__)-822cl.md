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
doc_path: '/documentation/swift/closedrange/contains(_:)-822cl'
source_url: 'https://developer.apple.com/documentation/swift/closedrange/contains(_:)-822cl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/contains%28_%3A%29-822cl.json'
content_hash: 'sha256:d85f5898432cc91e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given closed range is contained within this closed range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ other: ClosedRange<Bound>) -> Bool
```

## Parameters

- `other` — A closed range to check for containment within this closed range.

## Return Value

`true` if `other` is wholly contained within this closed range; otherwise, `false`.

## Discussion

The given closed range is contained within this range if its bounds are contained within this closed range.

```swift
let range = 0...10
range.contains(2...5)        // true
range.contains(2...10)       // true
range.contains(2...12)       // false
```

> [!abstract] Complexity
> O(1)
