---
title: 'init(intent:description:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/intentrecommendation/init(intent:description:)-6o8yy'
source_url: 'https://developer.apple.com/documentation/widgetkit/intentrecommendation/init(intent:description:)-6o8yy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intentrecommendation/init%28intent%3Adescription%3A%29-6o8yy.json'
content_hash: 'sha256:3736fa4f2e0a62ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [IntentRecommendation](../intentrecommendation.md)

# init(intent:description:)

<sub>Initializer</sub>

Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(intent: T, description: LocalizedStringResource)
```

## Parameters

- `intent` — The intent that represents the recommended configuration.

- `description` — A localized string in your bundle that helps the user understand the value of the preconfigured configuration option. For example, if the configuration represents a location in a weather app, the description may be the name of one of the user’s favorite cities, such as `Cupertino`.

## Discussion

> [!note] Note
> On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `IntentRecommendation` is inactive.
