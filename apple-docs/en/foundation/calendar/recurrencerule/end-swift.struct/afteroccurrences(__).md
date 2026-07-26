---
title: 'afterOccurrences(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/recurrencerule/end-swift.struct/afteroccurrences(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/end-swift.struct/afteroccurrences(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/end-swift.struct/afteroccurrences%28_%3A%29.json'
content_hash: 'sha256:2e645f53a0230b6b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Calendar](../../../calendar.md) · [RecurrenceRule](../../recurrencerule.md) · [End](../end-swift.struct.md)

# afterOccurrences(_:)

<sub>Type Method</sub>

The event stops repeating after a given number of times

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func afterOccurrences(_ count: Int) -> Calendar.RecurrenceRule.End
```

## Parameters

- `count` — How many times to repeat the event, including the first occurrence. `count` must be greater than `0`
