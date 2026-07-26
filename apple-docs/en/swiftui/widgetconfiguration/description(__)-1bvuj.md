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
doc_path: '/documentation/swiftui/widgetconfiguration/description(_:)-1bvuj'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/description(_:)-1bvuj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/description%28_%3A%29-1bvuj.json'
content_hash: 'sha256:3650d00518fbe5ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# description(_:)

<sub>Instance Method</sub>

Sets the description shown for a widget when a user adds or edits it using the contents of a text view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func description(_ description: Text) -> some WidgetConfiguration

```

## Parameters

- `description` — A text view containing a localized string to display.

## Return Value

A widget configuration with a description of the widget.
