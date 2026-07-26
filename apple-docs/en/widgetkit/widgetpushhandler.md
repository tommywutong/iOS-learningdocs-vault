---
title: WidgetPushHandler
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetpushhandler
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetpushhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetpushhandler.json'
content_hash: 'sha256:5a27a810624d54a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetPushHandler

<sub>Protocol</sub>

A type that can receive push information about widget refreshes and relevance refreshes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
protocol WidgetPushHandler
```

## Overview

Register a type conforming to this protocol to receive push information using the [pushHandler(_:)](<../swiftui/widgetconfiguration/pushhandler(__).md>) modifier on your widgets’ configurations.

## Topics

### Initializers

- [init()](<widgetpushhandler/init().md>) — Creates a push handler.

### Instance Methods

- [pushTokenDidChange(_:widgets:)](<widgetpushhandler/pushtokendidchange(__widgets_).md>) — Handle push tokens changing for widgets reloads and relevance refreshes.

## See Also

### Push notification updates

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md) — Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- [WidgetPushInfo](widgetpushinfo.md) — A structure that contains information about the push token for updating widgets and widget relevances.
