---
title: Date.FormatStyle.TimeStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/timestyle
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/timestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/timestyle.json'
content_hash: 'sha256:eeb7b5d14d1e4d94'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# Date.FormatStyle.TimeStyle

<sub>Structure</sub>

Type that defines time styles varied in length or components included.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TimeStyle
```

## Overview

The exact format depends on the locale. Possible time styles include [omitted](timestyle/omitted.md), [shortened](timestyle/shortened.md), [standard](timestyle/standard.md), and [complete](timestyle/complete.md).

The following code sample shows a variety of time style format results using the `en_US` locale.

```swift
let meetingDate = Date()
meetingDate.formatted(date: .numeric, time: .omitted)
// 10/17/2020
 
meetingDate.formatted(date: .numeric, time: .shortened)
// 10/17/2020, 9:54 PM
 
meetingDate.formatted(date: .numeric, time: .standard)
// 10/17/2020, 9:54:29 PM
 
meetingDate.formatted(date: .numeric, time: .complete)
// 10/17/2020, 9:54:29 PM CDT

meetingDate.formatted()
// 10/17/2020, 9:54 PM

```

The default time style is [shortened](timestyle/shortened.md).

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Modifying a Time Style

- [complete](timestyle/complete.md) — A time style with all components represented.
- [omitted](timestyle/omitted.md) — A time style with no time-related components represented.
- [shortened](timestyle/shortened.md) — A shortened time style with only the hour, minute, and day period components represented.
- [standard](timestyle/standard.md) — A time style with all components except the time zone represented.

### Comparing Time Styles

- [==(_:_:)](<../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

## See Also

### Specifying the Time Format

- [hour(_:)](<hour(__).md>) — Modifies the date format style to use the specified hour format style.
- [minute(_:)](<minute(__).md>) — Modifies the date format style to use the specified minute format style.
- [second(_:)](<second(__).md>) — Modifies the date format style to use the specified second format style.
- [secondFraction(_:)](<secondfraction(__).md>) — Modifies the date format style to use the specified second fraction format style.
- [timeZone(_:)](<timezone(__).md>) — Modifies the date format style to use the specified time zone format style.
