---
title: Entries
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineschedule/entries
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedule/entries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedule/entries.json'
content_hash: 'sha256:5699f5146cd735b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineSchedule](../timelineschedule.md)

# Entries

<sub>Associated Type</sub>

The sequence of dates within a schedule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Entries : Sequence where Self.Entries.Element == Date
```

## Discussion

The [entries(from:mode:)](<entries(from_mode_).md>) method returns a value of this type, which is a [Sequence](../../swift/sequence.md) of dates in ascending order. A [TimelineView](../timelineview.md) that you create with a schedule updates its content at the moments in time corresponding to the dates included in the sequence.

## See Also

### Getting a sequence of dates

- [entries(from:mode:)](<entries(from_mode_).md>) — Provides a sequence of dates starting around a given date.
