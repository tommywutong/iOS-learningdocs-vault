---
title: OperationQueue.SchedulerTimeType.Stride
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/schedulertimetype/stride
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/stride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/schedulertimetype/stride.json'
content_hash: 'sha256:3732e70be0f60c7e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [OperationQueue](../../operationqueue.md) · [SchedulerTimeType](../schedulertimetype.md)

# OperationQueue.SchedulerTimeType.Stride

<sub>Structure</sub>

The interval by which operation queue times advance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Stride
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](../../../swift/additivearithmetic.md), [Comparable](../../../swift/comparable.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [ExpressibleByFloatLiteral](../../../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../../../swift/expressiblebyintegerliteral.md), [Numeric](../../../swift/numeric.md), [SchedulerTimeIntervalConvertible](../../../combine/schedulertimeintervalconvertible.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md), [SignedNumeric](../../../swift/signednumeric.md)

## Topics

### Managing Stride Properties

- [timeInterval](stride/timeinterval.md) — The value of this time interval, in seconds.
- [magnitude](stride/magnitude.md) — The value of this time interval, in seconds.

### Creating Scheduler Time Strides

- [init(_:)](<stride/init(__).md>) — Creates a stride using the specified time interval.
- [init(exactly:)](<stride/init(exactly_).md>) — Creates a stride using the specified integer, if it can be represented exactly.
- [init(floatLiteral:)](<stride/init(floatliteral_).md>) — Creates a stride using the specified floating-point value.
- [init(integerLiteral:)](<stride/init(integerliteral_).md>) — Creates a stride using the specified integer value.

## See Also

### Managing Scheduler Time Type Properties

- [date](date.md) — The date this type represents.
- [advanced(by:)](<advanced(by_).md>) — Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [distance(to:)](<distance(to_).md>) — The distance to another operation queue scheduler time.
