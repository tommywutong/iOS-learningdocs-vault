---
title: 'afterDate(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/recurrencerule/end-swift.struct/afterdate(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/end-swift.struct/afterdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/end-swift.struct/afterdate%28_%3A%29.json'
content_hash: 'sha256:c1b77f54e1e60348'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Calendar](../../../calendar.md) · [RecurrenceRule](../../recurrencerule.md) · [End](../end-swift.struct.md)

# afterDate(_:)

<sub>Type Method</sub>

The event stops repeating after a given date

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func afterDate(_ date: Date) -> Calendar.RecurrenceRule.End
```

## Parameters

- `date` — The date on which the event may last occur. No further occurrences will be found after that
