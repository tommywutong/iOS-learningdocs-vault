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
doc_path: '/documentation/swiftui/widgetconfiguration/description(_:)-2bfr'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/description(_:)-2bfr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/description%28_%3A%29-2bfr.json'
content_hash: 'sha256:c8cd2bbe0eda2bcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# description(_:)

<sub>Instance Method</sub>

Sets the description shown for a widget when a user adds or edits it using the specified string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func description<S>(_ description: S) -> some WidgetConfiguration where S : StringProtocol

```

## Parameters

- `description` — A string describing the widget.

## Return Value

A widget configuration with a description of the widget.
