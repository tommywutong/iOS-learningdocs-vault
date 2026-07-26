---
title: 'pushTokenDidChange(_:widgets:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetpushhandler/pushtokendidchange(_:widgets:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetpushhandler/pushtokendidchange(_:widgets:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetpushhandler/pushtokendidchange%28_%3Awidgets%3A%29.json'
content_hash: 'sha256:55de443f84641919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetPushHandler](../widgetpushhandler.md)

# pushTokenDidChange(_:widgets:)

<sub>Instance Method</sub>

Handle push tokens changing for widgets reloads and relevance refreshes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func pushTokenDidChange(_ pushInfo: WidgetPushInfo, widgets: [WidgetInfo])
```

## Parameters

- `pushInfo` — Provides information containing your push token to use.

- `widgets` — Information about widgets that support push updates.
