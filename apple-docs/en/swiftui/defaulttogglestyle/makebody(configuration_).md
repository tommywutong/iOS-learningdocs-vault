---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/defaulttogglestyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/defaulttogglestyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaulttogglestyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:a9f6fdc85e47df85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DefaultToggleStyle](../defaulttogglestyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a toggle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func makeBody(configuration: DefaultToggleStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the toggle, including a label and a binding to the toggle’s state.

## Return Value

A view that acts as a toggle.

## Discussion

SwiftUI implements this required method of the [ToggleStyle](../togglestyle.md) protocol to define the behavior and appearance of the [automatic](../togglestyle/automatic.md) toggle style. Don’t call this method directly. Rather, the system calls this method for each [Toggle](../toggle.md) instance in a view hierarchy that needs the default style.
