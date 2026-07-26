---
title: TimelineReloadPolicy
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelinereloadpolicy
source_url: 'https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelinereloadpolicy.json'
content_hash: 'sha256:8a00f7e40f4518b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# TimelineReloadPolicy

<sub>Structure</sub>

A type that indicates the earliest date WidgetKit requests a new timeline from the widget’s provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct TimelineReloadPolicy
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Reload Policies

- [atEnd](timelinereloadpolicy/atend.md) — A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.
- [after(_:)](<timelinereloadpolicy/after(__).md>) — A policy that specifies a future date for WidgetKit to request a new timeline.
- [never](timelinereloadpolicy/never.md) — A policy that specifies that the app prompts WidgetKit when a new timeline is available.

## See Also

### Getting Timeline Properties

- [entries](timeline/entries.md) — An array of timeline entries.
- [policy](timeline/policy.md) — The policy that determines the earliest date and time WidgetKit requests a new timeline from a timeline provider.
