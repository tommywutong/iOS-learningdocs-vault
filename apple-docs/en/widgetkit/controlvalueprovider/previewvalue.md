---
title: previewValue
framework: WidgetKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controlvalueprovider/previewvalue
source_url: 'https://developer.apple.com/documentation/widgetkit/controlvalueprovider/previewvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlvalueprovider/previewvalue.json'
content_hash: 'sha256:a580681a2daf634b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlValueProvider](../controlvalueprovider.md)

# previewValue

<sub>Instance Property</sub>

A value to be shown while previewing the control in the add sheet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
var previewValue: Self.Value { get }
```

## Discussion

This value should be generated quickly and cheaply. Calculate more expensive and accurate values in [currentValue()](<currentvalue().md>).
