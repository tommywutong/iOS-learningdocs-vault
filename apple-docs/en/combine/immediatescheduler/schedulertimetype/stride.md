---
title: ImmediateScheduler.SchedulerTimeType.Stride
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/immediatescheduler/schedulertimetype/stride
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler/schedulertimetype/stride.json'
content_hash: 'sha256:997f4e88cea7e80c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [ImmediateScheduler](../../immediatescheduler.md) · [SchedulerTimeType](../schedulertimetype.md)

# ImmediateScheduler.SchedulerTimeType.Stride

<sub>Structure</sub>

The increment by which the immediate scheduler counts time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Stride
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](../../../swift/additivearithmetic.md), [Comparable](../../../swift/comparable.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [ExpressibleByFloatLiteral](../../../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../../../swift/expressiblebyintegerliteral.md), [Numeric](../../../swift/numeric.md), [SchedulerTimeIntervalConvertible](../../schedulertimeintervalconvertible.md), [SignedNumeric](../../../swift/signednumeric.md)

## Topics

### Creating Scheduler Time Strides

- [init(_:)](<stride/init(__).md>) — Creates an immediate scheduler time interval from the given time interval.
- [init(exactly:)](<stride/init(exactly_).md>) — Creates an immediate scheduler time interval from a binary integer type.
- [init(floatLiteral:)](<stride/init(floatliteral_).md>) — Creates an immediate scheduler time interval from a floating-point seconds value.
- [init(integerLiteral:)](<stride/init(integerliteral_).md>) — Creates an immediate scheduler time interval from an integer seconds value.

### Creating Scheduler Time Strides from Seconds

- [microseconds(_:)](<stride/microseconds(__).md>) — Converts the specified number of microseconds into an instance of this scheduler time type.
- [milliseconds(_:)](<stride/milliseconds(__).md>) — Converts the specified number of milliseconds into an instance of this scheduler time type.
- [nanoseconds(_:)](<stride/nanoseconds(__).md>) — Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [seconds(_:)](<stride/seconds(__)-8lm65.md>) — Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [seconds(_:)](<stride/seconds(__)-9uwki.md>) — Converts the specified number of seconds into an instance of this scheduler time type.

### Declaring Timekeeping Types

- [FloatLiteralType](stride/floatliteraltype.md) — The type used when evaluating floating-point literals.
- [IntegerLiteralType](stride/integerliteraltype.md) — The type used when evaluating integer literals.
- [Magnitude](stride/magnitude-swift.typealias.md) — The type used for expressing the stride’s magnitude.

### Expressing Scheduler Time Strides as Seconds

- [magnitude](stride/magnitude-swift.property.md) — The value of this time interval in seconds.
