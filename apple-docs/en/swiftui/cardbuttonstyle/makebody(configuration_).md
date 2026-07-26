---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/cardbuttonstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/cardbuttonstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/cardbuttonstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:3b56b09882699b7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CardButtonStyle](../cardbuttonstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a button.

<sub>tvOS</sub>

```swift
nonisolated func makeBody(configuration: CardButtonStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the button.

## Discussion

The system calls this method for each [Button](../button.md) instance in a view hierarchy in which [CardButtonStyle](../cardbuttonstyle.md) is the current button style.
