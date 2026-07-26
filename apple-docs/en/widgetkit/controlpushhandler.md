---
title: ControlPushHandler
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controlpushhandler
source_url: 'https://developer.apple.com/documentation/widgetkit/controlpushhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlpushhandler.json'
content_hash: 'sha256:5efb9bd13c685a01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ControlPushHandler

<sub>Protocol</sub>

A type that can receive push information about user-configured controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
protocol ControlPushHandler
```

## Overview

Register a type conforming to this protocol to receive push information using the [pushHandler(_:)](<../swiftui/controlwidgetconfiguration/pushhandler(__).md>) modifier on your controls’ configurations.

## Topics

### Initializers

- [init()](<controlpushhandler/init().md>) — Creates a push handler.

### Instance Methods

- [pushTokensDidChange(controls:)](<controlpushhandler/pushtokensdidchange(controls_).md>) — Handle push tokens changing for configured controls.

## See Also

### Updates

- [Updating controls locally and remotely](updating-controls-locally-and-remotely.md) — Update and reload controls from your app or using push notifications.
- [ControlPushInfo](controlpushinfo.md) — A structure that contains information about the push token of a user-configured control.
