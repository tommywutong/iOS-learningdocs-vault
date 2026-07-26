---
title: 'height(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/custompresentationdetent/height(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/custompresentationdetent/height(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/custompresentationdetent/height%28in%3A%29.json'
content_hash: 'sha256:7284096d3d0269be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomPresentationDetent](../custompresentationdetent.md)

# height(in:)

<sub>Type Method</sub>

Calculates and returns a height based on the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func height(in context: Self.Context) -> CGFloat?
```

## Parameters

- `context` — Information that can help to determine the height of the detent.

## Return Value

The height of the detent, or `nil` if the detent should be inactive based on the `contenxt` input.

## See Also

### Getting the height

- [Context](context.md) — Information that you can use to calculate the height of a custom detent.
