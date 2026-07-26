---
title: 'configurationDisplayName(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/configurationdisplayname(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/configurationdisplayname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/configurationdisplayname%28_%3A%29.json'
content_hash: 'sha256:b212d18b02af80d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# configurationDisplayName(_:)

<sub>Instance Method</sub>

Sets the localized name shown for a widget when a user adds or edits the widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func configurationDisplayName(_ displayName: LocalizedStringResource) -> some WidgetConfiguration

```

## Parameters

- `displayName` — Text resource for the localized name to display.

## Return Value

A widget configuration that includes a descriptive name for the widget.
