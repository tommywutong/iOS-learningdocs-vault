---
title: Locale.Components
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components
source_url: 'https://developer.apple.com/documentation/foundation/locale/components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components.json'
content_hash: 'sha256:a71aad962760ff56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Components

<sub>Structure</sub>

A type that represents the components of a locale, for use when creating a locale with specific overrides.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Components
```

## Overview

Use [Components](components.md) with the [init(components:)](<init(components_).md>) initializer to create a custom [Locale](../locale.md) that overrides specific traits of a default locale. When you create a locale with components, the locale uses any overridden values instead of defaults preferred by the region or language. Leave a property `nil` to accept the default value.

The properties in this type correspond with those in [Locale](../locale.md), which declares them as read-only rather than read-write. You use this type to customize components when creating a custom locale, and use [Locale](../locale.md) to examine the components of an existing locale.

The following example creates a [Components](components.md) instance for US English, but then customizes its components. It sets the first day of the week to Monday and the hour cycle to zero-to-23. These components override the `en-US` defaults of Sunday and one-to-12, respectively. It then uses [init(components:)](<init(components_).md>) to create a custom [Locale](../locale.md).

```swift
var components = Locale.Components(languageCode: "en", languageRegion: "US")
components.firstDayOfWeek = Locale.Weekday.monday
components.hourCycle = Locale.HourCycle.zeroToTwentyThree
let locale = Locale(components: components)
```

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a locale components instance

- [init(identifier:)](<components/init(identifier_).md>) — Creates a locale components instance with the specified identifier.
- [init(languageCode:script:languageRegion:)](<components/init(languagecode_script_languageregion_).md>) — Creates a locale components instance with the specified language code, script, and region identifier.
- [init(locale:)](<components/init(locale_).md>) — Creates a language components instance from an existing locale.

### Specifying language components

- [languageComponents](components/languagecomponents.md) — The Unicode language identifier part of a locale.
- [Components](language-swift.struct/components.md) — A type that identifies a language by its various components.

### Specifying date and time components

- [calendar](components/calendar.md) — The calendar used by the locale.
- [Identifier](../calendar/identifier-swift.enum.md) — An enumeration for the available calendars.
- [firstDayOfWeek](components/firstdayofweek.md) — The first day of the week as represented by this locale.
- [Weekday](weekday.md) — A type that represents weekdays, used for indicating a locale’s first day of the week.
- [hourCycle](components/hourcycle.md) — The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [HourCycle](hourcycle-swift.enum.md) — A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [timeZone](components/timezone.md) — The time zone used by the locale.

### Specifiying measurement and counting components

- [currency](components/currency.md) — The currency used by the locale.
- [Currency](currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [measurementSystem](components/measurementsystem.md) — The measurement system used by the locale, like metric or the US system.
- [MeasurementSystem](measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [numberingSystem](components/numberingsystem.md) — The numbering system used by the locale.
- [NumberingSystem](numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.

### Specifying region components

- [region](components/region.md) — The region used by the locale.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [subdivision](components/subdivision.md) — The optional subdivision of the region used by this locale.
- [Subdivision](subdivision-swift.struct.md) — A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [variant](components/variant.md) — An optional variant used by the locale.
- [Variant](variant-swift.struct.md) — A type that represents a locale’s language variant.

### Specifying ordering components

- [collation](components/collation.md) — The string sort order of the locale.
- [Collation](collation-swift.struct.md) — A type that represents the string sort order used by the locale.

## See Also

### Creating a locale by components

- [init(components:)](<init(components_).md>) — Creates a locale from the given components.
- [init(languageCode:script:languageRegion:)](<init(languagecode_script_languageregion_).md>) — Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents:)](<init(languagecomponents_).md>) — Creates a locale from the given language components.
- [Components](language-swift.struct/components.md) — A type that identifies a language by its various components.
