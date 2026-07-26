---
title: DateComponentsFormatter.UnitsStyle.positional
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum/positional
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum/positional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum/positional.json'
content_hash: 'sha256:37a975b660aedb80'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DateComponentsFormatter](../../datecomponentsformatter.md) · [UnitsStyle](../unitsstyle-swift.enum.md)

# DateComponentsFormatter.UnitsStyle.positional

<sub>Case</sub>

A style that uses the position of a unit of time to identify its value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case positional
```

## Discussion

This style is most commonly used for time values where the hour, minute, and second values are separated by colons. You can use the zero formatting behaviors ([ZeroFormattingBehavior](../zeroformattingbehavior-swift.struct.md)) to further modify the formatting of this value.

For example, one hour and ten minutes is displayed in the U.S. English locale as “1:10:00”.

> [!note] Note
> This style may fall back to the behavior of [NSDateComponentsFormatterUnitsStyleAbbreviated](abbreviated.md) when attempting to display large time quantities.

## See Also

### Styles

- [NSDateComponentsFormatterUnitsStyleSpellOut](spellout.md) — A style that spells out the units and quantities of time.
- [NSDateComponentsFormatterUnitsStyleFull](full.md) — A style that spells out the units of time, but not the quantities.
- [NSDateComponentsFormatterUnitsStyleShort](short.md) — A style that uses a shortened spelling for units.
- [NSDateComponentsFormatterUnitsStyleBrief](brief.md) — A style that uses a shortened spelling for units of time that is shorter than [NSDateComponentsFormatterUnitsStyleShort](short.md).
- [NSDateComponentsFormatterUnitsStyleAbbreviated](abbreviated.md) — A style that uses the most abbreviated spelling for units of time.
