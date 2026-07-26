---
title: 'init(label:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(label:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(label:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28label%3Acontent%3A%29.json'
content_hash: 'sha256:52bf8015c77df77e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(label:content:)

<sub>Initializer</sub>

Creates an AccessoryWidgetGroup composed of a label and three circular or rounded square contents with equal spacing and vertical alignment.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(@ViewBuilder label: () -> Label, @ViewBuilder content: () -> Content)
```

## Parameters

- `label` — A label or a text to show up on the top corner of the widget view to describe the purpose of the group.

- `content` — A view builder for the content of the accessory group.
