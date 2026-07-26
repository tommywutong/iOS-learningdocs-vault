---
title: Date.FormatStyle.DateStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/datestyle
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/datestyle.json'
content_hash: 'sha256:481fc6706c46891a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# Date.FormatStyle.DateStyle

<sub>Structure</sub>

Type that defines date styles varied in length or components included.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DateStyle
```

## Overview

The exact format depends on the locale. Possible values of date style include [omitted](datestyle/omitted.md), [numeric](datestyle/numeric.md), [abbreviated](datestyle/abbreviated.md), [long](datestyle/long.md), and [complete](datestyle/complete.md).

The following code sample shows a variety of date style format results using the `en_US` locale.

```swift
let meetingDate = Date()
meetingDate.formatted(date: .omitted, time: .standard) 
// 9:42:14 AM

meetingDate.formatted(date: .numeric, time: .omitted) 
// 10/17/2020

meetingDate.formatted(date: .abbreviated, time: .omitted)
// Oct 17, 2020

meetingDate.formatted(date: .long, time: .omitted) 
// October 17, 2020

meetingDate.formatted(date: .complete, time: .omitted) 
// Saturday, October 17, 2020

meetingDate.formatted()
// 10/17/2020, 9:42 AM
```

The default date style is `numeric`.

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Modifying a Date Style

- [abbreviated](datestyle/abbreviated.md) — A date style with some components abbreviated for space-constrained applications.
- [complete](datestyle/complete.md) — A date style with all components represented.
- [long](datestyle/long.md) — A lengthened date style with the full month, day of month, and year components represented.
- [numeric](datestyle/numeric.md) — A date style with the month, day of month, and year components represented as numeric values.
- [omitted](datestyle/omitted.md) — A date style with no date-related components represented.

### Comparing Date Styles

- [==(_:_:)](<../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

## See Also

### Specifying the Date Format

- [day(_:)](<day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<era(__).md>) — Modifies the date format style to use the specified era format style.
- [month(_:)](<month(__).md>) — Modifies the date format style to use the specified month format style.
- [quarter(_:)](<quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [week(_:)](<week(__).md>) — Modifies the date format style to use the specified week format style.
- [weekday(_:)](<weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [year(_:)](<year(__).md>) — Modifies the date format style to use the specified year format style.
