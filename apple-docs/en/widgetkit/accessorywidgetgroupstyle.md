---
title: AccessoryWidgetGroupStyle
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/accessorywidgetgroupstyle
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroupstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroupstyle.json'
content_hash: 'sha256:dee5a81e35e33f66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# AccessoryWidgetGroupStyle

<sub>Structure</sub>

The style for an [AccessoryWidgetGroup](accessorywidgetgroup.md) view.

<sub>watchOS</sub>

```swift
struct AccessoryWidgetGroupStyle
```

## Overview

Use the `View/accessoryWidgetGroupStyle(_:)` modifier to set the desired style.

## Topics

### Type Properties

- [automatic](accessorywidgetgroupstyle/automatic.md) — The default style that is set to circular.
- [circular](accessorywidgetgroupstyle/circular.md) — Masks each content view with a circle.
- [roundedSquare](accessorywidgetgroupstyle/roundedsquare.md) — Masks each content view with a rounded square.

## See Also

### Accessory and watchOS widgets

- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md) — Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [AccessoryWidgetGroup](accessorywidgetgroup.md) — A view type that has a label at the top and three content views masked with a circle or rounded square.
- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md) — Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
