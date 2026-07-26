---
title: RangeExpression
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rangeexpression
source_url: 'https://developer.apple.com/documentation/swift/rangeexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeexpression.json'
content_hash: 'sha256:64975ea40df0c8f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RangeExpression

<sub>Protocol</sub>

A type that can be used to slice a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol RangeExpression<Bound>
```

## Overview

A type that conforms to `RangeExpression` can convert itself to a `Range<Bound>` of indices within a given collection.

## Relationships

- **Conforming Types**: [ClosedRange](closedrange.md), [PartialRangeFrom](partialrangefrom.md), [PartialRangeThrough](partialrangethrough.md), [PartialRangeUpTo](partialrangeupto.md), [Range](range.md)

## Topics

### Operators

- [~=(_:_:)](<rangeexpression/~=(____).md>) — Returns a Boolean value indicating whether a value is included in a range.

### Associated Types

- [Bound](rangeexpression/bound.md) — The type for which the expression describes a range.

### Instance Methods

- [contains(_:)](<rangeexpression/contains(__).md>) — Returns a Boolean value indicating whether the given element is contained within the range expression.
- [relative(to:)](<rangeexpression/relative(to_).md>) — Returns the range of indices described by this range expression within the given collection.

## See Also

### Range Expressions

- [PartialRangeUpTo](partialrangeupto.md) — A partial half-open interval up to, but not including, an upper bound.
- [PartialRangeThrough](partialrangethrough.md) — A partial interval up to, and including, an upper bound.
- [PartialRangeFrom](partialrangefrom.md) — A partial interval extending upward from a lower bound.
- [UnboundedRange_](unboundedrange_.md) — A range expression that represents the entire range of a collection.
