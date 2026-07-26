---
title: 'init(role:action:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(role:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(role:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28role%3Aaction%3A%29.json'
content_hash: 'sha256:95f923929da469b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(role:action:)

<sub>Initializer</sub>

Creates a button that displays a default label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency nonisolated init(role: ButtonRole, action: @escaping @MainActor () -> Void)
```

## Parameters

- `role` — A semantic role describing the button.

- `action` — The action to perform when the user triggers the button.

## Discussion

For example, the following view would display a button with a ‘x’ symbol in the toolbar.

```swift
struct NewContactSheet: View {
    var body: some View {
        NavigationStack {
            NewContactEditor()
                .toolbar {
                    Button(role: .cancel) {
                        dismissView()
                    }
                }
        }
    }
}
```
