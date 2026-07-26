---
title: Value
framework: WidgetKit
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintentcontrolvalueprovider/value
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentcontrolvalueprovider/value.json'
content_hash: 'sha256:ca136d6b858123b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentControlValueProvider](../appintentcontrolvalueprovider.md)

# Value

<sub>Associated Type</sub>

The type of value provided to the template.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
associatedtype Value
```

## Discussion

When you create a custom provider, Swift infers this type from your implementation of the required `ValueProvider/previewValue(configuration:)` and `ValueProvider/currentValue(configuration:)` methods.
