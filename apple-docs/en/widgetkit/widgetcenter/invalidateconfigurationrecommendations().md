---
title: invalidateConfigurationRecommendations()
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetcenter/invalidateconfigurationrecommendations()
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetcenter/invalidateconfigurationrecommendations()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetcenter/invalidateconfigurationrecommendations%28%29.json'
content_hash: 'sha256:c9ca8c867018618c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetCenter](../widgetcenter.md)

# invalidateConfigurationRecommendations()

<sub>Instance Method</sub>

Invalidates and refreshes the preconfigured intent configurations for user-customizable widgets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func invalidateConfigurationRecommendations()
```

## Discussion

In watchOS, call this function when your app receives new data for preconfigured widgets you’d like to appear in the list of available watch complications.

> [!note] Note
> On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `invalidateConfigurationRecommendations()` is inactive.
