---
title: promptsForUserConfiguration()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlwidgetconfiguration/promptsforuserconfiguration()
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgetconfiguration/promptsforuserconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgetconfiguration/promptsforuserconfiguration%28%29.json'
content_hash: 'sha256:5a3fad1031ea4db9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidgetConfiguration](../controlwidgetconfiguration.md)

# promptsForUserConfiguration()

<sub>Instance Method</sub>

Specifies that a control’s configuration UI should be automatically presented after the widget is added.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency func promptsForUserConfiguration() -> some ControlWidgetConfiguration

```

## Return Value

A control configuration that knows whether the presentation of a configuration UI is preferred.
