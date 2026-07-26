---
title: Decodable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/decodable
source_url: 'https://developer.apple.com/documentation/swift/decodable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodable.json'
content_hash: 'sha256:79cb822c848d18ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Decodable

<sub>Protocol</sub>

A type that can decode itself from an external representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Decodable
```

## Relationships

- **Inherited By**: [SIMD](simd.md)

- **Conforming Types**: [Array](array.md), [Bool](bool.md), [ClosedRange](closedrange.md), [CollectionDifference](collectiondifference.md), [Change](collectiondifference/change.md), [ContiguousArray](contiguousarray.md), [Instant](continuousclock/instant.md), [Dictionary](dictionary.md), [Double](double.md), [Duration](duration.md), [TimeFormatStyle](duration/timeformatstyle.md), [Attributed](duration/timeformatstyle/attributed-swift.struct.md), [Pattern](duration/timeformatstyle/pattern-swift.struct.md), [UnitsFormatStyle](duration/unitsformatstyle.md), [Attributed](duration/unitsformatstyle/attributed-swift.struct.md), [FractionalPartDisplayStrategy](duration/unitsformatstyle/fractionalpartdisplaystrategy.md), [Unit](duration/unitsformatstyle/unit.md), [UnitWidth](duration/unitsformatstyle/unitwidth-swift.struct.md), [ZeroValueUnitsDisplayStrategy](duration/unitsformatstyle/zerovalueunitsdisplaystrategy.md), [Float](float.md), [Float16](float16.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [LocalTestingActorID](../distributed/localtestingactorid.md), [Never](never.md), [ObservationRegistrar](../observation/observationregistrar.md), [Optional](optional.md), [PartialRangeFrom](partialrangefrom.md), [PartialRangeThrough](partialrangethrough.md), [PartialRangeUpTo](partialrangeupto.md), [Range](range.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [SIMDMask](simdmask.md), [Set](set.md), [String](string.md), [Comparator](string/comparator.md), [LocalizationValue](string/localizationvalue.md), [Placeholder](string/localizationvalue/placeholder.md), [StandardComparator](string/standardcomparator.md), [Instant](suspendingclock/instant.md), [TaskPriority](taskpriority.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md)

## Topics

### Initializers

- [init(from:)](<decodable/init(from_).md>) — Creates a new instance by decoding from the given decoder.

## See Also

### Custom Encoding and Decoding

- [Encoding and Decoding Custom Types](../foundation/encoding-and-decoding-custom-types.md) — Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [Codable](codable.md) — A type that can convert itself into and out of an external representation.
- [Encodable](encodable.md) — A type that can encode itself to an external representation.
- [CodingKey](codingkey.md) — A type that can be used as a key for encoding and decoding.
- [CodingKeyRepresentable](codingkeyrepresentable.md) — A type that can be converted to and from a coding key.
- [CodingUserInfoKey](codinguserinfokey.md) — A user-defined key for providing context during encoding and decoding.
