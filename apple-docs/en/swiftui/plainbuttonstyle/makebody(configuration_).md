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
doc_path: '/documentation/swiftui/plainbuttonstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/plainbuttonstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/plainbuttonstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:286144c6dc3975c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PlainButtonStyle](../plainbuttonstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func makeBody(configuration: PlainButtonStyle.Configuration) -> some View

```

## Parameters

- `configuration` — The properties of the button.

## Discussion

The system calls this method for each [Button](../button.md) instance in a view hierarchy where this style is the current button style.
