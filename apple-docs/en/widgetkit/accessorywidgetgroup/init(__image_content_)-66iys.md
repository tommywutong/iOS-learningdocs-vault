---
title: 'init(_:image:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(_:image:content:)-66iys'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:image:content:)-66iys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28_%3Aimage%3Acontent%3A%29-66iys.json'
content_hash: 'sha256:ff77cd9a0516cb32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(_:image:content:)

<sub>Initializer</sub>

Creates an `AccessoryWidgetGroup` that generates its label from a string and image resource.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ title: some StringProtocol, image: ImageResource, @ViewBuilder content: () -> Content)
```

## Parameters

- `title` — A string for the label of `AccessoryWidgetGroup`.

- `image` — The image resource to lookup.

- `content` — A view builder for the content of the accessory group.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the label similar to `Text/init(_:)-9d1g4`. See `Text` for more information about localizing strings.
