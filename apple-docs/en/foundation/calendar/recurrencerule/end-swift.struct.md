---
title: Calendar.RecurrenceRule.End
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/recurrencerule/end-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/end-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/end-swift.struct.json'
content_hash: 'sha256:1b2150c66052d031'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# Calendar.RecurrenceRule.End

<sub>Structure</sub>

When a recurring event stops recurring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct End
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [date](end-swift.struct/date.md) — The latest date when the event may occur This value is set when the struct was initialized with `.afterDate()`
- [occurrences](end-swift.struct/occurrences.md) — At most many times the event may occur This value is set when the struct was initialized with `.afterOccurrences()`

### Type Properties

- [never](end-swift.struct/never.md) — The event repeats indefinitely

### Type Methods

- [afterDate(_:)](<end-swift.struct/afterdate(__).md>) — The event stops repeating after a given date
- [afterOccurrences(_:)](<end-swift.struct/afteroccurrences(__).md>) — The event stops repeating after a given number of times
