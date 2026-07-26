---
title: DateComponentsFormatter.UnitsStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum.json'
content_hash: 'sha256:9906c5e02cd6be5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# DateComponentsFormatter.UnitsStyle

<sub>Enumeration</sub>

Constants for specifying how to represent quantities of time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum UnitsStyle
```

## Overview

All date and time values are localized and formatted according to the current user’s language preferences.

The following table shows how the quantity of 9 hours, 41 minutes, and 30 seconds is displayed in the U.S. English locale for each style:

| Style | Displayed result |
|---|---|
| [NSDateComponentsFormatterUnitsStyleSpellOut](unitsstyle-swift.enum/spellout.md) | “nine hours, forty-one minutes, thirty seconds” |
| [NSDateComponentsFormatterUnitsStyleFull](unitsstyle-swift.enum/full.md) | “9 hours, 41 minutes, 30 seconds” |
| [NSDateComponentsFormatterUnitsStyleShort](unitsstyle-swift.enum/short.md) | “9 hr, 41 min, 30 sec” |
| [NSDateComponentsFormatterUnitsStyleBrief](unitsstyle-swift.enum/brief.md) | “9hr 41min 30sec” |
| [NSDateComponentsFormatterUnitsStyleAbbreviated](unitsstyle-swift.enum/abbreviated.md) | “9h 41m 30s” |
| [NSDateComponentsFormatterUnitsStylePositional](unitsstyle-swift.enum/positional.md) | “9:31:30” |

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Styles

- [NSDateComponentsFormatterUnitsStyleSpellOut](unitsstyle-swift.enum/spellout.md) — A style that spells out the units and quantities of time.
- [NSDateComponentsFormatterUnitsStyleFull](unitsstyle-swift.enum/full.md) — A style that spells out the units of time, but not the quantities.
- [NSDateComponentsFormatterUnitsStyleShort](unitsstyle-swift.enum/short.md) — A style that uses a shortened spelling for units.
- [NSDateComponentsFormatterUnitsStyleBrief](unitsstyle-swift.enum/brief.md) — A style that uses a shortened spelling for units of time that is shorter than [NSDateComponentsFormatterUnitsStyleShort](unitsstyle-swift.enum/short.md).
- [NSDateComponentsFormatterUnitsStyleAbbreviated](unitsstyle-swift.enum/abbreviated.md) — A style that uses the most abbreviated spelling for units of time.
- [NSDateComponentsFormatterUnitsStylePositional](unitsstyle-swift.enum/positional.md) — A style that uses the position of a unit of time to identify its value.

### Initializers

- [init(rawValue:)](<unitsstyle-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [ZeroFormattingBehavior](zeroformattingbehavior-swift.struct.md) — Formatting constants for when values contain zeroes.
