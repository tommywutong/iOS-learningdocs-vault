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
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(_:content:)-3ij0e'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:content:)-3ij0e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28_%3Acontent%3A%29-3ij0e.json'
content_hash: 'sha256:28ab2ad2cdaaaa44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(_:content:)

<sub>Initializer</sub>

Creates an `AccessoryWidgetGroup` that generates its label from a string.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ title: some StringProtocol, @ViewBuilder content: () -> Content)
```

## Parameters

- `title` — A string for the label of `AccessoryWidgetGroup`.

- `content` — A view builder for the content of the accessory group.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the label similar to `Text/init(_:)-9d1g4`. See `Text` for more information about localizing strings.
