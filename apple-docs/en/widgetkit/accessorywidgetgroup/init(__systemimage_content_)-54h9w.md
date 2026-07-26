---
title: 'init(_:systemImage:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(_:systemimage:content:)-54h9w'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:systemimage:content:)-54h9w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28_%3Asystemimage%3Acontent%3A%29-54h9w.json'
content_hash: 'sha256:86208ec560b56b32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(_:systemImage:content:)

<sub>Initializer</sub>

Creates an `AccessoryWidgetGroup` that generates its label from a localized string key and a system image name.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleKey: LocalizedStringKey, systemImage: String, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleKey` — The key for the `AccessoryWidgetGroup`’s localized label.

- `systemImage` — The name of the image resource to lookup.

- `content` — A view builder for the content of the accessory group.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the localized key similar to `Text/init(_:tableName:bundle:comment:)`. See `Text` for more information about localizing strings.
