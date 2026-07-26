---
title: 'applying(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/applying(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/applying(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/applying%28_%3A%29.json'
content_hash: 'sha256:3fa6af00c9467cff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# applying(_:)

<sub>Instance Method</sub>

Applies the given difference to this collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applying(_ difference: CollectionDifference<Self.Element>) -> Self?
```

## Parameters

- `difference` — The difference to be applied.

## Return Value

An instance representing the state of the receiver with the difference applied, or `nil` if the difference is incompatible with the receiver’s state.

## Discussion

> [!abstract] Complexity
> O(_n_ + _c_), where _n_ is `self.count` and _c_ is the number of changes contained by the parameter.

## See Also

### Creating and Applying Differences

- [difference(from:)](<difference(from_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](<difference(from_by_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
