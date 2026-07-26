---
title: 'init(_:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(_:content:)-nb0'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:content:)-nb0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28_%3Acontent%3A%29-nb0.json'
content_hash: 'sha256:85a4dc9bc026ecdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(_:content:)

<sub>Initializer</sub>

Creates an `AccessoryWidgetGroup` that generates its label from a localized string key.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleKey: LocalizedStringKey, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleKey` — The key for the `AccessoryWidgetGroup`’s localized label.

- `content` — A view builder for the content of the accessory group.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the localized key similar to `Text/init(_:tableName:bundle:comment:)`. See `Text` for more information about localizing strings.
