---
title: PartialRangeUpTo
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/partialrangeupto
source_url: 'https://developer.apple.com/documentation/swift/partialrangeupto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/partialrangeupto.json'
content_hash: 'sha256:3f56b2d7be06770c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# PartialRangeUpTo

<sub>Structure</sub>

A partial half-open interval up to, but not including, an upper bound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct PartialRangeUpTo<Bound> where Bound : Comparable
```

## Overview

You create `PartialRangeUpTo` instances by using the prefix half-open range operator (prefix `..<`).

```swift
let upToFive = ..<5.0
```

You can use a `PartialRangeUpTo` instance to quickly check if a value is contained in a particular range of values. For example:

```swift
upToFive.contains(3.14)       // true
upToFive.contains(6.28)       // false
upToFive.contains(5.0)        // false
```

You can use a `PartialRangeUpTo` instance of a collection’s indices to represent the range from the start of the collection up to, but not including, the partial range’s upper bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[..<3])
// Prints "[10, 20, 30]"
```

## Relationships

- **Conforms To**: [BNNSGraph.Builder.SliceIndex](../accelerate/bnnsgraph/builder/sliceindex.md), [BitwiseCopyable](bitwisecopyable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomTestStringConvertible](../testing/customteststringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Escapable](escapable.md), [MLShapedArrayRangeExpression](../coreml/mlshapedarrayrangeexpression.md), [MLTensorRangeExpression](../coreml/mltensorrangeexpression.md), [NDArray.RangeExpression](../coreai/ndarray/rangeexpression.md), [RangeExpression](rangeexpression.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<partialrangeupto/init(__).md>)

### Instance Properties

- [upperBound](partialrangeupto/upperbound.md)

### Default Implementations

- [Decodable Implementations](partialrangeupto/decodable-implementations.md)
- [Encodable Implementations](partialrangeupto/encodable-implementations.md)
- [RangeExpression Implementations](partialrangeupto/rangeexpression-implementations.md)

## See Also

### Range Expressions

- [PartialRangeThrough](partialrangethrough.md) — A partial interval up to, and including, an upper bound.
- [PartialRangeFrom](partialrangefrom.md) — A partial interval extending upward from a lower bound.
- [RangeExpression](rangeexpression.md) — A type that can be used to slice a collection.
- [UnboundedRange_](unboundedrange_.md) — A range expression that represents the entire range of a collection.
