---
title: 'init(for:content:dynamicIsland:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/activityconfiguration/init(for:content:dynamicisland:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/activityconfiguration/init(for:content:dynamicisland:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/activityconfiguration/init%28for%3Acontent%3Adynamicisland%3A%29.json'
content_hash: 'sha256:6a3836d366c001b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ActivityConfiguration](../activityconfiguration.md)

# init(for:content:dynamicIsland:)

<sub>Initializer</sub>

Creates a configuration object for a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency init<Content>(for attributesType: Attributes.Type, @ViewBuilder content: @escaping (ActivityViewContext<Attributes>) -> Content, dynamicIsland: @escaping (ActivityViewContext<Attributes>) -> DynamicIsland) where Content : View
```

## Parameters

- `attributesType` — The type that describes the content of the Live Activity.

- `content` — A closure that creates the view for the Live Activity that appears on the Lock Screen. This view also appears as a banner on the Home Screen of devices that don’t support the Dynamic Island when you alert a person about updated Live Activity content.

- `dynamicIsland` — A closure that builds the Live Activity that appears in the Dynamic Island.

## See Also

### Creating a Live Activity configuration

- [ActivityViewContext](../activityviewcontext.md) — A structure that describes the view context for creating the views of a Live Activity.
