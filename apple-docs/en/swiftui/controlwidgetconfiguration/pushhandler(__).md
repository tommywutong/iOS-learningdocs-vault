---
title: 'pushHandler(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlwidgetconfiguration/pushhandler(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgetconfiguration/pushhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgetconfiguration/pushhandler%28_%3A%29.json'
content_hash: 'sha256:8398408b08b09fa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidgetConfiguration](../controlwidgetconfiguration.md)

# pushHandler(_:)

<sub>Instance Method</sub>

Register a type that can handle push tokens changing for controls of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency func pushHandler(_ pushHandlerType: any ControlPushHandler.Type) -> some ControlWidgetConfiguration

```

## Parameters

- `pushHandlerType` — The type of the object that can handle push tokens you use to update the control with push notifications.

## Overview

Use this to opt your control into using push notifications.

If you have multiple control types, you can choose to use the same push handler type for those control types.

When the push configuration of your controls changes, each handler type will be instantiated and [pushTokensDidChange(controls:)](<../../widgetkit/controlpushhandler/pushtokensdidchange(controls_).md>) will be called.
