---
title: never
framework: WidgetKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelinereloadpolicy/never
source_url: 'https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy/never'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelinereloadpolicy/never.json'
content_hash: 'sha256:bf8ade65bfe61473'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [TimelineReloadPolicy](../timelinereloadpolicy.md)

# never

<sub>Type Property</sub>

A policy that specifies that the app prompts WidgetKit when a new timeline is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let never: TimelineReloadPolicy
```

## See Also

### Reload Policies

- [atEnd](atend.md) — A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.
- [after(_:)](<after(__).md>) — A policy that specifies a future date for WidgetKit to request a new timeline.
