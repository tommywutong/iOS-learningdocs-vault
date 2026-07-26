---
title: 'toolbarRole(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarrole(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarrole(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarrole%28_%3A%29.json'
content_hash: 'sha256:55f72d4a538a4ce3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarRole(_:)

<sub>Instance Method</sub>

Configures the semantic role for the content populating the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarRole(_ role: ToolbarRole) -> some View

```

## Parameters

- `role` — The role of the toolbar.

## Discussion

Use this modifier to configure the semantic role for content populating your app’s toolbar. SwiftUI uses this role when rendering the content of your app’s toolbar.

```swift
ContentView()
    .navigationTitle("Browser")
    .toolbarRole(.browser)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            AddButton()
        }
     }
```

## See Also

### Specifying the role of toolbar content

- [ToolbarRole](../toolbarrole.md) — The purpose of content that populates the toolbar.
