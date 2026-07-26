---
title: PartialRangeThrough
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/partialrangethrough
source_url: 'https://developer.apple.com/documentation/swift/partialrangethrough'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/partialrangethrough.json'
content_hash: 'sha256:cac4d6c70163fecf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# PartialRangeThrough

<sub>Structure</sub>

A partial interval up to, and including, an upper bound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct PartialRangeThrough<Bound> where Bound : Comparable
```

## Overview

You create `PartialRangeThrough` instances by using the prefix closed range operator (prefix `...`).

```swift
let throughFive = ...5.0
```

You can use a `PartialRangeThrough` instance to quickly check if a value is contained in a particular range of values. For example:

```swift
throughFive.contains(4.0)     // true
throughFive.contains(5.0)     // true
throughFive.contains(6.0)     // false
```

You can use a `PartialRangeThrough` instance of a collection’s indices to represent the range from the start of the collection up to, and including, the partial range’s upper bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[...3])
// Prints "[10, 20, 30, 40]"
```

## Relationships

- **Conforms To**: [BNNSGraph.Builder.SliceIndex](../accelerate/bnnsgraph/builder/sliceindex.md), [BitwiseCopyable](bitwisecopyable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomTestStringConvertible](../testing/customteststringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Escapable](escapable.md), [MLShapedArrayRangeExpression](../coreml/mlshapedarrayrangeexpression.md), [MLTensorRangeExpression](../coreml/mltensorrangeexpression.md), [NDArray.RangeExpression](../coreai/ndarray/rangeexpression.md), [RangeExpression](rangeexpression.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<partialrangethrough/init(__).md>)

### Instance Properties

- [upperBound](partialrangethrough/upperbound.md)

### Default Implementations

- [Decodable Implementations](partialrangethrough/decodable-implementations.md)
- [Encodable Implementations](partialrangethrough/encodable-implementations.md)
- [RangeExpression Implementations](partialrangethrough/rangeexpression-implementations.md)

## See Also

### Range Expressions

- [PartialRangeUpTo](partialrangeupto.md) — A partial half-open interval up to, but not including, an upper bound.
- [PartialRangeFrom](partialrangefrom.md) — A partial interval extending upward from a lower bound.
- [RangeExpression](rangeexpression.md) — A type that can be used to slice a collection.
- [UnboundedRange_](unboundedrange_.md) — A range expression that represents the entire range of a collection.
