---
title: PeriodicTimelineSchedule.Entries
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/periodictimelineschedule/entries
source_url: 'https://developer.apple.com/documentation/swiftui/periodictimelineschedule/entries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/periodictimelineschedule/entries.json'
content_hash: 'sha256:fc8ffda9fdba4872'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PeriodicTimelineSchedule](../periodictimelineschedule.md)

# PeriodicTimelineSchedule.Entries

<sub>Structure</sub>

The sequence of dates in periodic schedule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Entries
```

## Overview

The [entries(from:mode:)](<entries(from_mode_).md>) method returns a value of this type, which is a [Sequence](../../swift/sequence.md) of periodic dates in ascending order. A [TimelineView](../timelineview.md) that you create updates its content at the moments in time corresponding to the dates included in the sequence.

## Relationships

- **Conforms To**: [IteratorProtocol](../../swift/iteratorprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## See Also

### Getting the sequence of dates

- [entries(from:mode:)](<entries(from_mode_).md>) — Provides a sequence of periodic dates starting from around a given date.
