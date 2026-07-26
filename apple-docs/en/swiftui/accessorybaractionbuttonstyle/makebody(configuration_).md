---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessorybaractionbuttonstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessorybaractionbuttonstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessorybaractionbuttonstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:e2c688a56439ae3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessoryBarActionButtonStyle](../accessorybaractionbuttonstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a button.

<sub>macOS</sub>

```swift
nonisolated func makeBody(configuration: AccessoryBarActionButtonStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the button.

## Discussion

The system calls this method for each [Button](../button.md) instance in a view hierarchy where this style is the current button style.
