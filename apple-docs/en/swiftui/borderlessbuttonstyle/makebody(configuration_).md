---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/borderlessbuttonstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/borderlessbuttonstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/borderlessbuttonstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:3e1dada767f359f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BorderlessButtonStyle](../borderlessbuttonstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func makeBody(configuration: BorderlessButtonStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the button.

## Discussion

The system calls this method for each [Button](../button.md) instance in a view hierarchy where this style is the current button style.
