---
title: 'relative(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeexpression/relative(to:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeexpression/relative(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeexpression/relative%28to%3A%29.json'
content_hash: 'sha256:74e4db8f2e97e57b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeExpression](../rangeexpression.md)

# relative(to:)

<sub>Instance Method</sub>

Returns the range of indices described by this range expression within the given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func relative<C>(to collection: C) -> Range<Self.Bound> where C : Collection, Self.Bound == C.Index
```

## Parameters

- `collection` — The collection to evaluate this range expression in relation to.

## Return Value

A range suitable for slicing `collection`. The returned range is _not_ guaranteed to be inside the bounds of `collection`. Callers should apply the same preconditions to the return value as they would to a range provided directly by the user.

## Discussion

You can use the `relative(to:)` method to convert a range expression, which could be missing one or both of its endpoints, into a concrete range that is bounded on both sides. The following example uses this method to convert a partial range up to `4` into a half-open range, using an array instance to add the range’s lower bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
let upToFour = ..<4

let r1 = upToFour.relative(to: numbers)
// r1 == 0..<4
```

The `r1` range is bounded on the lower end by `0` because that is the starting index of the `numbers` array. When the collection passed to `relative(to:)` starts with a different index, that index is used as the lower bound instead. The next example creates a slice of `numbers` starting at index `2`, and then uses the slice with `relative(to:)` to convert `upToFour` to a concrete range.

```swift
let numbersSuffix = numbers[2...]
// numbersSuffix == [30, 40, 50, 60, 70]

let r2 = upToFour.relative(to: numbersSuffix)
// r2 == 2..<4
```

Use this method only if you need the concrete range it produces. To access a slice of a collection using a range expression, use the collection’s generic subscript that uses a range expression as its parameter.

```swift
let numbersPrefix = numbers[upToFour]
// numbersPrefix == [10, 20, 30, 40]
```
