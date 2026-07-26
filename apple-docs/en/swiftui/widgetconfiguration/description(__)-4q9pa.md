---
title: 'description(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/description(_:)-4q9pa'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/description(_:)-4q9pa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/description%28_%3A%29-4q9pa.json'
content_hash: 'sha256:26e1e5b7994e2a31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# description(_:)

<sub>Instance Method</sub>

Sets the localized description shown for a widget when a user adds or edits the widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func description(_ descriptionKey: LocalizedStringKey) -> some WidgetConfiguration

```

## Parameters

- `descriptionKey` — The key for the localized description to display.

## Return Value

A widget configuration with a description of the widget.
