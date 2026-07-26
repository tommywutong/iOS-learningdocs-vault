---
title: 'widgetConfigurationIntent(of:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetinfo/widgetconfigurationintent(of:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetinfo/widgetconfigurationintent(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetinfo/widgetconfigurationintent%28of%3A%29.json'
content_hash: 'sha256:63757ecf91a9b5b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetInfo](../widgetinfo.md)

# widgetConfigurationIntent(of:)

<sub>Instance Method</sub>

Gets the associated App Intent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func widgetConfigurationIntent<Intent>(of intentType: Intent.Type = Intent.self) -> Intent? where Intent : WidgetConfigurationIntent
```

## Parameters

- `intentType` — The expected type for the App Intent.

## Return Value

An App Intent that contains the user-edited values or nil if there is no associated App Intent or the type does not match `intentType`.
