---
title: 'init(score:duration:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/timelineentryrelevance/init(score:duration:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineentryrelevance/init(score:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineentryrelevance/init%28score%3Aduration%3A%29.json'
content_hash: 'sha256:cc09d515ca9837d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [TimelineEntryRelevance](../timelineentryrelevance.md)

# init(score:duration:)

<sub>Initializer</sub>

Creates an object that represents the importance of a widget and the length of time for WidgetKit to consider it for rotation to the top of the stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(score: Float, duration: TimeInterval = 0.0)
```

## Parameters

- `score` — A value on a scale of your choosing, indicating the importance of an entry compared to other entries in the same timeline.

- `duration` — The number of seconds following an entry’s date that WidgetKit may rotate the widget to the top of the stack.
