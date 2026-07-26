---
title: Configuration
framework: WidgetKit
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintentcontrolvalueprovider/configuration
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentcontrolvalueprovider/configuration.json'
content_hash: 'sha256:41fdc7f1722b08a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentControlValueProvider](../appintentcontrolvalueprovider.md)

# Configuration

<sub>Associated Type</sub>

The type of intent used to prepare the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
associatedtype Configuration : ControlConfigurationIntent
```

## Discussion

When you create a custom provider, Swift infers this type from your implementation of the required `ValueProvider/previewValue(configuration:)` and `ValueProvider/currentValue(configuration:)` methods.
