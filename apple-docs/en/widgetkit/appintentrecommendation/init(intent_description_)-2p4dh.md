---
title: 'init(intent:description:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/appintentrecommendation/init(intent:description:)-2p4dh'
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentrecommendation/init(intent:description:)-2p4dh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentrecommendation/init%28intent%3Adescription%3A%29-2p4dh.json'
content_hash: 'sha256:ee68eabf2a3433c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentRecommendation](../appintentrecommendation.md)

# init(intent:description:)

<sub>Initializer</sub>

Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(intent: Intent, description: LocalizedStringKey)
```

## Parameters

- `intent` — The intent that represents the recommended configuration.

- `description` — A key for a localized string in your bundle that helps the user understand the value of the preconfigured configuration option. For example, if the configuration represents a location in a weather app, the description may be the name of one of the user’s favorite cities, such as `Cupertino`.

## Discussion

> [!note] Note
> On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `AppIntentRecommendation` is inactive.

## See Also

### Creating a recommended widget configuration

- [init(intent:description:)](<init(intent_description_)-65igj.md>) — Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.
- [init(intent:description:)](<init(intent_description_)-7zn32.md>) — Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.
