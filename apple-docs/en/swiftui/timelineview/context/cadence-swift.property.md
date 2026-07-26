---
title: cadence
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineview/context/cadence-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/timelineview/context/cadence-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineview/context/cadence-swift.property.json'
content_hash: 'sha256:c91a4e71d9892370'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [TimelineView](../../timelineview.md) · [Context](../context.md)

# cadence

<sub>Instance Property</sub>

The rate at which the timeline updates the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let cadence: TimelineView<Schedule, Content>.Context.Cadence
```

## Discussion

Use this value to hide information that updates faster than the view’s current update rate. For example, you could hide the millisecond component of a digital timer when the cadence is anything slower than [TimelineView.Context.Cadence.live](cadence-swift.enum/live.md).

Because the [Cadence](cadence-swift.enum.md) enumeration conforms to the [Comparable](../../../swift/comparable.md) protocol, you can compare cadences with relational operators. Slower cadences have higher values, so you could perform the check described above with the following comparison:

```swift
let hideMilliseconds = cadence > .live
```

## See Also

### Getting the cadence

- [Cadence](cadence-swift.enum.md) — A rate at which timeline views can receive updates.
