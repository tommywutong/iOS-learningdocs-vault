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
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(_:systemimage:content:)-7rnqc'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:systemimage:content:)-7rnqc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28_%3Asystemimage%3Acontent%3A%29-7rnqc.json'
content_hash: 'sha256:31c6fa53d068913c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(_:systemImage:content:)

<sub>Initializer</sub>

Creates an `AccessoryWidgetGroup` that generates its label from a string and system image name.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleKey: some StringProtocol, systemImage: String, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleKey` — A string for the `AccessoryWidgetGroup`’s label.

- `systemImage` — The name of the image resource to lookup.

- `content` — A view builder for the content of the accessory group.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the label similar to `Text/init(_:)-9d1g4`. See `Text` for more information about localizing strings.
