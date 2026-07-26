---
title: MKDistanceFormatter.DistanceUnitStyle
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdistanceformatter/distanceunitstyle
source_url: 'https://developer.apple.com/documentation/mapkit/mkdistanceformatter/distanceunitstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdistanceformatter/distanceunitstyle.json'
content_hash: 'sha256:97eae01a8b4a5752'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDistanceFormatter](../mkdistanceformatter.md)

# MKDistanceFormatter.DistanceUnitStyle

<sub>Enumeration</sub>

Constants that indicate the format style to use for strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DistanceUnitStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [MKDistanceFormatterUnitStyleDefault](distanceunitstyle/default.md) — Bases the determination to abbreviate on the current locale and user language settings.
- [MKDistanceFormatterUnitStyleAbbreviated](distanceunitstyle/abbreviated.md) — Abbreviates units.
- [MKDistanceFormatterUnitStyleFull](distanceunitstyle/full.md) — Spells out units in full.
- [MKDistanceFormatterUnitStyleDefault](distanceunitstyle/default.md) — Bases the determination to abbreviate on the current locale and user language settings.
- [MKDistanceFormatterUnitStyleAbbreviated](distanceunitstyle/abbreviated.md) — Abbreviates units.
- [MKDistanceFormatterUnitStyleFull](distanceunitstyle/full.md) — Spells out units in full.

### Initializers

- [init(rawValue:)](<distanceunitstyle/init(rawvalue_).md>)

## See Also

### Specifying the format

- [locale](locale.md) — The locale to use when formatting strings.
- [units](units-swift.property.md) — The measuring system — imperial or metric — to use for units.
- [Units](units-swift.enum.md) — Constants that reflect the type of units to use in the string.
- [unitStyle](unitstyle.md) — The preferred style for units.
