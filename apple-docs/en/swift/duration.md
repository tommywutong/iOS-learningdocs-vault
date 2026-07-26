---
title: Duration
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration
source_url: 'https://developer.apple.com/documentation/swift/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration.json'
content_hash: 'sha256:72c2c69bb4e5ddca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Duration

<sub>Structure</sub>

A representation of high precision time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Duration
```

## Overview

`Duration` represents an elapsed time value with high precision in an integral form. It may be used for measurements of varying clock sources. In those cases it represents the elapsed time measured by that clock. Calculations using `Duration` may span from a negative value to a positive value and have a suitable range to at least cover attosecond scale for both small elapsed durations like sub-second precision to durations that span centuries.

Typical construction of `Duration` values should be created via the static methods for specific time values.

```swift
 var d: Duration = .seconds(3)
 d += .milliseconds(33)
 print(d) // 3.033 seconds
```

`Duration` itself does not ferry any additional information other than the temporal measurement component; specifically leap seconds should be represented as an additional accessor since that is specific only to certain clock implementations.

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BitwiseCopyable](bitwisecopyable.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [DisplayRepresentable](../appintents/displayrepresentable.md), [DurationProtocol](durationprotocol.md), [ElectricityInsightMeasure](../energykit/electricityinsightmeasure.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [InstanceDisplayRepresentable](../appintents/instancedisplayrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [TypeDisplayRepresentable](../appintents/typedisplayrepresentable.md)

## Topics

### Creating a duration

- [init(secondsComponent:attosecondsComponent:)](<duration/init(secondscomponent_attosecondscomponent_).md>) — Construct a `Duration` by adding attoseconds to a seconds value.
- [seconds(_:)](<duration/seconds(__)-311cx.md>) — Construct a `Duration` given a number of seconds represented as a `BinaryInteger`.
- [seconds(_:)](<duration/seconds(__)-5ifzr.md>) — Construct a `Duration` given a number of seconds represented as a `Double` by converting the value into the closest attosecond scale value.
- [milliseconds(_:)](<duration/milliseconds(__)-1w328.md>) — Construct a `Duration` given a number of milliseconds represented as a `BinaryInteger`.
- [milliseconds(_:)](<duration/milliseconds(__)-7ledy.md>) — Construct a `Duration` given a number of seconds milliseconds as a `Double` by converting the value into the closest attosecond scale value.
- [microseconds(_:)](<duration/microseconds(__)-1zzcc.md>) — Construct a `Duration` given a number of seconds microseconds as a `Double` by converting the value into the closest attosecond scale value.
- [microseconds(_:)](<duration/microseconds(__)-2majo.md>) — Construct a `Duration` given a number of microseconds represented as a `BinaryInteger`.

### Accessing a duration’s components

- [components](duration/components.md) — The composite components of the `Duration`.

### Performing calculations on durations

- [*(_:_:)](<duration/_(____)-3d469.md>)
- [*=(_:_:)](<duration/_=(____).md>)
- [/(_:_:)](<duration/_(____)-7fkmh.md>)
- [/=(_:_:)](<duration/_=(____)-10rgx.md>)
- [/=(_:_:)](<duration/_=(____)-1qfv3.md>)

### Formatting a duration

- [formatted()](<duration/formatted().md>) — Formats the string using a localized hour-minute-second time pattern.
- [formatted(_:)](<duration/formatted(__).md>) — Formats the duration, using the provided format style.
- [TimeFormatStyle](duration/timeformatstyle.md) — A format style that shows durations in a compact, localized format with separators.
- [UnitsFormatStyle](duration/unitsformatstyle.md) — A format style that shows durations with localized labeled components

### Initializers

- [init(attoseconds:)](<duration/init(attoseconds_).md>) — Construct a `Duration` from the given number of attoseconds.

### Instance Properties

- [attoseconds](duration/attoseconds.md) — The number of attoseconds represented by this `Duration`.

### Type Aliases

- [Specification](duration/specification.md)
- [UnwrappedType](duration/unwrappedtype.md)
- [ValueType](duration/valuetype.md)

### Type Properties

- [defaultResolverSpecification](duration/defaultresolverspecification.md)

### Type Methods

- [nanoseconds(_:)](<duration/nanoseconds(__)-1cg32.md>) — Construct a `Duration` given a number of nanoseconds as a `Double` by converting the value into the closest attosecond scale value.
- [nanoseconds(_:)](<duration/nanoseconds(__)-8nsaz.md>) — Construct a `Duration` given a number of nanoseconds represented as a `BinaryInteger`.

### Default Implementations

- [AdditiveArithmetic Implementations](duration/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](duration/atomicrepresentable-implementations.md)
- [Comparable Implementations](duration/comparable-implementations.md)
- [CustomStringConvertible Implementations](duration/customstringconvertible-implementations.md)
- [Decodable Implementations](duration/decodable-implementations.md)
- [DurationProtocol Implementations](duration/durationprotocol-implementations.md)
- [Encodable Implementations](duration/encodable-implementations.md)
- [Equatable Implementations](duration/equatable-implementations.md)
- [Hashable Implementations](duration/hashable-implementations.md)

## See Also

### Durations

- [DurationProtocol](durationprotocol.md) — A type that defines a duration for a given `InstantProtocol` type.
