---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/buttontogglestyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/buttontogglestyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttontogglestyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:fda167980f54a506'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ButtonToggleStyle](../buttontogglestyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a toggle button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func makeBody(configuration: ButtonToggleStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the toggle, including a label and a binding to the toggle’s state.

## Return Value

A view that acts as a button that controls a Boolean state.

## Discussion

SwiftUI implements this required method of the [ToggleStyle](../togglestyle.md) protocol to define the behavior and appearance of the [button](../togglestyle/button.md) toggle style. Don’t call this method directly; the system calls this method for each [Toggle](../toggle.md) instance in a view hierarchy that’s styled as a button.
