---
title: CFNumberFormatterRoundingMode
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnumberformatterroundingmode
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformatterroundingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformatterroundingmode.json'
content_hash: 'sha256:1339953ca320c2b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterRoundingMode

<sub>Enumeration</sub>

These constants are used to specify how numbers should be rounded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFNumberFormatterRoundingMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFNumberFormatterRoundCeiling](cfnumberformatterroundingmode/roundceiling.md) — Round towards positive infinity.
- [kCFNumberFormatterRoundFloor](cfnumberformatterroundingmode/roundfloor.md) — Round towards negative infinity.
- [kCFNumberFormatterRoundDown](cfnumberformatterroundingmode/rounddown.md) — Round towards zero.
- [kCFNumberFormatterRoundUp](cfnumberformatterroundingmode/roundup.md) — Round away from zero.
- [kCFNumberFormatterRoundHalfEven](cfnumberformatterroundingmode/roundhalfeven.md) — Round towards the nearest integer, or towards an even number if equidistant.
- [kCFNumberFormatterRoundHalfDown](cfnumberformatterroundingmode/roundhalfdown.md) — Round towards the nearest integer, or towards zero if equidistant.
- [kCFNumberFormatterRoundHalfUp](cfnumberformatterroundingmode/roundhalfup.md) — Round towards the nearest integer, or away from zero if equidistant.

### Initializers

- [init(rawValue:)](<cfnumberformatterroundingmode/init(rawvalue_).md>)

## See Also

### Constants

- [Number Formatter Styles](number-formatter-styles.md) — Predefined number format styles.
- [Number Formatter Property Keys](number-formatter-property-keys.md) — The keys used in key-value pairs to specify the value of number formatter properties.
- [Number Format Options](number_format_options.md) — These constants are used to specify how numbers should be parsed.
- [Padding Positions](padding-positions.md) — These constants are used to specify how numbers should be padded.
