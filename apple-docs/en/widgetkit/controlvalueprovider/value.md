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
doc_path: /documentation/widgetkit/controlvalueprovider/value
source_url: 'https://developer.apple.com/documentation/widgetkit/controlvalueprovider/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlvalueprovider/value.json'
content_hash: 'sha256:757144f6913a4f15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlValueProvider](../controlvalueprovider.md)

# Value

<sub>Associated Type</sub>

The type of value provided to the template.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
associatedtype Value
```

## Discussion

When you create a custom provider, Swift infers this type from your implementation of the required [previewValue](previewvalue.md) property and [currentValue()](<currentvalue().md>) method.
