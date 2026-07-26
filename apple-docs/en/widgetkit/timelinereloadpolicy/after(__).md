---
title: 'after(_:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/timelinereloadpolicy/after(_:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy/after(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelinereloadpolicy/after%28_%3A%29.json'
content_hash: 'sha256:190b0be93c616f5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [TimelineReloadPolicy](../timelinereloadpolicy.md)

# after(_:)

<sub>Type Method</sub>

A policy that specifies a future date for WidgetKit to request a new timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static func after(_ date: Date) -> TimelineReloadPolicy
```

## See Also

### Reload Policies

- [atEnd](atend.md) — A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.
- [never](never.md) — A policy that specifies that the app prompts WidgetKit when a new timeline is available.
