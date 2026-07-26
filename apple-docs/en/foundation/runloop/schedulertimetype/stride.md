---
title: RunLoop.SchedulerTimeType.Stride
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/schedulertimetype/stride
source_url: 'https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/stride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/schedulertimetype/stride.json'
content_hash: 'sha256:7689098213554d80'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RunLoop](../../runloop.md) · [SchedulerTimeType](../schedulertimetype.md)

# RunLoop.SchedulerTimeType.Stride

<sub>Structure</sub>

The interval by which run loop times advance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Stride
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](../../../swift/additivearithmetic.md), [Comparable](../../../swift/comparable.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [ExpressibleByFloatLiteral](../../../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../../../swift/expressiblebyintegerliteral.md), [Numeric](../../../swift/numeric.md), [SchedulerTimeIntervalConvertible](../../../combine/schedulertimeintervalconvertible.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md), [SignedNumeric](../../../swift/signednumeric.md)

## Topics

### Creating Scheduler Time Strides

- [init(_:)](<stride/init(__).md>) — Creates a run loop scheduler time interval from the given time interval.
- [init(exactly:)](<stride/init(exactly_).md>) — Creates a run loop scheduler time interval from a binary integer type.
- [init(floatLiteral:)](<stride/init(floatliteral_).md>) — Creates a run loop scheduler time interval from a floating-point seconds value.
- [init(integerLiteral:)](<stride/init(integerliteral_).md>) — Creates a run loop scheduler time interval from an integer seconds value.

### Converting to Seconds

- [microseconds(_:)](<stride/microseconds(__).md>) — Converts the specified number of microseconds into an instance of this scheduler time type.
- [milliseconds(_:)](<stride/milliseconds(__).md>) — Converts the specified number of milliseconds into an instance of this scheduler time type.
- [nanoseconds(_:)](<stride/nanoseconds(__).md>) — Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [seconds(_:)](<stride/seconds(__)-4kk8j.md>) — Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [seconds(_:)](<stride/seconds(__)-48wwk.md>) — Converts the specified number of seconds into an instance of this scheduler time type.

### Inspecting Stride Properties

- [magnitude](stride/magnitude.md) — The value of this time interval in seconds.
- [timeInterval](stride/timeinterval.md) — The value of this time interval in seconds.

### Operators

- [*(_:_:)](<stride/_(____).md>) — Returns the result of multiplying the values of the two arguments.
- [*=(_:_:)](<stride/_=(____).md>) — Multiplies the values of the two arguments, and assigns the result to the first argument.
- [+(_:_:)](<stride/+(____).md>) — Returns the result of adding the values of the two arguments.
- [+=(_:_:)](<stride/+=(____).md>) — Adds the values of the two arguments, and assigns the result to the first argument.
- [-(_:_:)](<stride/-(____).md>) — Returns the result of subtracting the second stride from the first.
- [-=(_:_:)](<stride/-=(____).md>) — Subtracts the second stride from the first and assigns the result to the first.
- [\<(_:_:)](<stride/_(____).md>) — Returns a Boolean value indicating whether the first stride is less than the second.

## See Also

### Working with Scheduler Time Intervals

- [advanced(by:)](<advanced(by_).md>) — Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
- [distance(to:)](<distance(to_).md>) — Returns the distance to another run loop scheduler time.
