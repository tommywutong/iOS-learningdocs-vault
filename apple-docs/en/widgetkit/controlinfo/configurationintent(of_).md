---
title: 'configurationIntent(of:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlinfo/configurationintent(of:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlinfo/configurationintent(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlinfo/configurationintent%28of%3A%29.json'
content_hash: 'sha256:3569819575e4c8e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlInfo](../controlinfo.md)

# configurationIntent(of:)

<sub>Instance Method</sub>

Gets the associated App Intent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func configurationIntent<Intent>(of intentType: Intent.Type = Intent.self) -> Intent? where Intent : ControlConfigurationIntent
```

## Parameters

- `intentType` — The expected type for the App Intent.

## Return Value

An App Intent that contains the user-edited values or nil if there is no associated App Intent or the type does not match `intentType`.
