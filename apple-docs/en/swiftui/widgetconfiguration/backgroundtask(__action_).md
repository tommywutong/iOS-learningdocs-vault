---
title: 'backgroundTask(_:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/backgroundtask(_:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/backgroundtask(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/backgroundtask%28_%3Aaction%3A%29.json'
content_hash: 'sha256:0747b3d477d29c60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# backgroundTask(_:action:)

<sub>Instance Method</sub>

Runs the given action when the system provides a background task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func backgroundTask<D, R>(_ task: BackgroundTask<D, R>, action: @escaping @Sendable (D) async -> R) -> some WidgetConfiguration where D : Sendable, R : Sendable

```

## Parameters

- `task` — The type of task the action responds to.

- `action` — The closure that is called when the system provides a task matching the provided task.

## Discussion

When the system wakes your app or extension for one or more background tasks, it will call any actions associated with matching tasks. When your async actions return, the system will put your app back into a suspended state. In Widget Extensions, this modifier can be used to handle URL Session background tasks with [urlSession](../backgroundtask/urlsession.md).

## See Also

### Managing background tasks

- [onBackgroundURLSessionEvents(matching:_:)](<onbackgroundurlsessionevents(matching___).md>) — Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.
