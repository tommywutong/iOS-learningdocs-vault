---
title: 'pushHandler(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/pushhandler(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/pushhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/pushhandler%28_%3A%29.json'
content_hash: 'sha256:524b8004140e5cf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# pushHandler(_:)

<sub>Instance Method</sub>

Register a type that can handle push tokens changing for widgets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func pushHandler(_ pushHandlerType: any WidgetPushHandler.Type) -> some WidgetConfiguration

```

## Parameters

- `pushHandlerType` — The type of the object that can handle push tokens you use to update the widget with push notifications.

## Overview

Use this to opt this widget into supporting updates via push notifications.

If you have multiple widget configurations, you can choose to use the same push handler type for those widget configurations.

When the push configuration of your widgets changes, each unique handler type will be instantiated and [pushTokenDidChange(_:widgets:)](<../../widgetkit/widgetpushhandler/pushtokendidchange(__widgets_).md>) will be called.
