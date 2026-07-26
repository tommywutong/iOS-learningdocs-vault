---
title: NSCalendar.Identifier
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/identifier
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/identifier.json'
content_hash: 'sha256:d373dad5c1e212f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# NSCalendar.Identifier

<sub>Structure</sub>

The supported calendar types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Identifier
```

## Discussion

Use these identifiers to specify the kind of calendar. The Gregorian calendar is the calendar typically used in Europe, the Western Hemisphere, and elsewhere.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<identifier/init(__).md>)
- [init(rawValue:)](<identifier/init(rawvalue_).md>)

### Calendar identifiers

- [NSCalendarIdentifierGregorian](identifier/gregorian.md) — Identifier for the Gregorian calendar.
- [NSCalendarIdentifierISO8601](identifier/iso8601.md) — Identifier for the ISO8601 calendar.
- [NSCalendarIdentifierBangla](identifier/bangla.md)
- [NSCalendarIdentifierBuddhist](identifier/buddhist.md) — Identifier for the Buddhist calendar.
- [NSCalendarIdentifierChinese](identifier/chinese.md) — Identifier for the Chinese calendar.
- [NSCalendarIdentifierCoptic](identifier/coptic.md) — Identifier for the Coptic calendar.
- [NSCalendarIdentifierDangi](identifier/dangi.md)
- [NSCalendarIdentifierEthiopicAmeteAlem](identifier/ethiopicametealem.md) — Identifier for the Ethiopic (Amete Alem) calendar.
- [NSCalendarIdentifierEthiopicAmeteMihret](identifier/ethiopicametemihret.md) — Identifier for the Ethiopic (Amete Mihret) calendar.
- [NSCalendarIdentifierGujarati](identifier/gujarati.md)
- [NSCalendarIdentifierHebrew](identifier/hebrew.md) — Identifier for the Hebrew calendar.
- [NSCalendarIdentifierIndian](identifier/indian.md) — Identifier for the Indian calendar.
- [NSCalendarIdentifierIslamic](identifier/islamic.md) — Identifier for the Islamic calendar.
- [NSCalendarIdentifierIslamicCivil](identifier/islamiccivil.md) — Identifier for the Islamic civil calendar.
- [NSCalendarIdentifierIslamicTabular](identifier/islamictabular.md) — Identifier for a tabular Islamic calendar.
- [NSCalendarIdentifierIslamicUmmAlQura](identifier/islamicummalqura.md) — Identifier for the Islamic Umm al-Qura calendar.
- [NSCalendarIdentifierJapanese](identifier/japanese.md) — Identifier for the Japanese calendar.
- [NSCalendarIdentifierKannada](identifier/kannada.md)
- [NSCalendarIdentifierMalayalam](identifier/malayalam.md)
- [NSCalendarIdentifierMarathi](identifier/marathi.md)
- [NSCalendarIdentifierOdia](identifier/odia.md)
- [NSCalendarIdentifierPersian](identifier/persian.md) — Identifier for the Persian calendar.
- [NSCalendarIdentifierRepublicOfChina](identifier/republicofchina.md) — Identifier for the Republic of China calendar.
- [NSCalendarIdentifierTamil](identifier/tamil.md)
- [NSCalendarIdentifierTelugu](identifier/telugu.md)
- [NSCalendarIdentifierVietnamese](identifier/vietnamese.md)
- [NSCalendarIdentifierVikram](identifier/vikram.md)

## See Also

### Creating and Initializing Calendars

- [+ calendarWithIdentifier:](<init(identifier_).md>) — Creates a new calendar specified by a given identifier.
- [- initWithCalendarIdentifier:](<init(calendaridentifier_).md>) — Initializes a calendar according to a given identifier.
