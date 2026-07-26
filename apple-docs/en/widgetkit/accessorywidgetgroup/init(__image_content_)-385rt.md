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
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(_:image:content:)-385rt'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:image:content:)-385rt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28_%3Aimage%3Acontent%3A%29-385rt.json'
content_hash: 'sha256:9ed11798300852a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(_:image:content:)

<sub>Initializer</sub>

Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and image resource.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleResource: LocalizedStringResource, image: ImageResource, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleResource` — Resource for the `AccessoryWidgetGroup`’s localized label.

- `image` — The image resource to lookup.

- `content` — A view builder for the content of the accessory group.

## Discussion

This initializer creates a `Label` view on your behalf. See `Text` for more information about localizing strings.
