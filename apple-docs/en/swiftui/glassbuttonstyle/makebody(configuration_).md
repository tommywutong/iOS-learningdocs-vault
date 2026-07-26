---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/glassbuttonstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/glassbuttonstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glassbuttonstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:fe5d79aa1d5f21dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GlassButtonStyle](../glassbuttonstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
nonisolated func makeBody(configuration: GlassButtonStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the button.

## Discussion

The system calls this method for each [Button](../button.md) instance in a view hierarchy where this style is the current button style.
