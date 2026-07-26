---
title: 'previewValue(configuration:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/appintentcontrolvalueprovider/previewvalue(configuration:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider/previewvalue(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentcontrolvalueprovider/previewvalue%28configuration%3A%29.json'
content_hash: 'sha256:ed952a33b8891ec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentControlValueProvider](../appintentcontrolvalueprovider.md)

# previewValue(configuration:)

<sub>Instance Method</sub>

A value to be shown while previewing the control in the add sheet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func previewValue(configuration: Self.Configuration) -> Self.Value
```

## Parameters

- `configuration` — The intent containing user-editable parameters.

## Discussion

This value should be generated quickly and cheaply. Calculate more expensive and accurate values in [currentValue(configuration:)](<currentvalue(configuration_).md>).
