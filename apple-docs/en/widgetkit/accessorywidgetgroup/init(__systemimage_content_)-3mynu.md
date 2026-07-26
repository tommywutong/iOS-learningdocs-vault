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
doc_path: '/documentation/widgetkit/accessorywidgetgroup/init(_:systemimage:content:)-3mynu'
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:systemimage:content:)-3mynu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup/init%28_%3Asystemimage%3Acontent%3A%29-3mynu.json'
content_hash: 'sha256:6e8919e66f0f9cd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AccessoryWidgetGroup](../accessorywidgetgroup.md)

# init(_:systemImage:content:)

<sub>Initializer</sub>

Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and a system image name.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleResource: LocalizedStringResource, systemImage: String, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleResource` — Resource for the `AccessoryWidgetGroup`’s localized label.

- `systemImage` — The name of the image resource to lookup.

- `content` — A view builder for the content of the accessory group.

## Discussion

This initializer creates a `Label` view on your behalf. See `Text` for more information about localizing strings.
