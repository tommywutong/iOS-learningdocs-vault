---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/checkboxtogglestyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/checkboxtogglestyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/checkboxtogglestyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:b24b5c9ddd547d7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CheckboxToggleStyle](../checkboxtogglestyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a toggle checkbox.

<sub>macOS</sub>

```swift
nonisolated func makeBody(configuration: CheckboxToggleStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the toggle, including a label and a binding to the toggle’s state.

## Return Value

A view that represents a checkbox.

## Discussion

SwiftUI implements this required method of the [ToggleStyle](../togglestyle.md) protocol to define the behavior and appearance of the [checkbox](../togglestyle/checkbox.md) toggle style. Don’t call this method directly. Rather, the system calls this method for each [Toggle](../toggle.md) instance in a view hierarchy that’s styled as a checkbox.
