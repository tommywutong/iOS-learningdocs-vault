---
title: 'configurationDisplayName(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/configurationdisplayname(_:)-3sbn4'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/configurationdisplayname(_:)-3sbn4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/configurationdisplayname%28_%3A%29-3sbn4.json'
content_hash: 'sha256:c75430f36bcc8497'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# configurationDisplayName(_:)

<sub>Instance Method</sub>

Sets the name shown for a widget when a user adds or edits it using the contents of a text view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func configurationDisplayName(_ displayName: Text) -> some WidgetConfiguration

```

## Parameters

- `displayName` — A text view containing a localized string to display.

## Return Value

A widget configuration with a descriptive name for the widget.
