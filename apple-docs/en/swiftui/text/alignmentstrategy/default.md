---
title: default
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/alignmentstrategy/default
source_url: 'https://developer.apple.com/documentation/swiftui/text/alignmentstrategy/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/alignmentstrategy/default.json'
content_hash: 'sha256:2729cc64b5418f99'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [AlignmentStrategy](../alignmentstrategy.md)

# default

<sub>Type Property</sub>

The default strategy based on the context it is used in.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: Text.AlignmentStrategy
```

## Discussion

The default strategy for [Text](../../text.md) is [layoutBased](layoutbased.md). UI components that accept user input, such as [TextEditor](../../texteditor.md) and [TextField](../../textfield.md), default to [writingDirectionBased](writingdirectionbased.md).
