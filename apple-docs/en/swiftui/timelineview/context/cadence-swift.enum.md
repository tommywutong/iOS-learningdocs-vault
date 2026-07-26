---
title: TimelineView.Context.Cadence
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineview/context/cadence-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/timelineview/context/cadence-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineview/context/cadence-swift.enum.json'
content_hash: 'sha256:5c76a120979a35de'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [TimelineView](../../timelineview.md) · [Context](../context.md)

# TimelineView.Context.Cadence

<sub>Enumeration</sub>

A rate at which timeline views can receive updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Cadence
```

## Overview

Use the cadence presented to content in a [TimelineView](../../timelineview.md) to hide information that updates faster than the view’s current update rate. For example, you could hide the millisecond component of a digital timer when the cadence is [TimelineView.Context.Cadence.seconds](cadence-swift.enum/seconds.md) or [TimelineView.Context.Cadence.minutes](cadence-swift.enum/minutes.md).

Because this enumeration conforms to the [Comparable](../../../swift/comparable.md) protocol, you can compare cadences with relational operators. Slower cadences have higher values, so you could perform the check described above with the following comparison:

```swift
let hideMilliseconds = cadence > .live
```

## Relationships

- **Conforms To**: [Comparable](../../../swift/comparable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Getting cadences

- [TimelineView.Context.Cadence.live](cadence-swift.enum/live.md) — Updates the view continuously.
- [TimelineView.Context.Cadence.seconds](cadence-swift.enum/seconds.md) — Updates the view approximately once per second.
- [TimelineView.Context.Cadence.minutes](cadence-swift.enum/minutes.md) — Updates the view approximately once per minute.

## See Also

### Getting the cadence

- [cadence](cadence-swift.property.md) — The rate at which the timeline updates the view.
