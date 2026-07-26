---
title: 'sizeThatFits(_:nsView:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewrepresentable/sizethatfits(_:nsview:context:)-fuqx'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentable/sizethatfits(_:nsview:context:)-fuqx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentable/sizethatfits%28_%3Ansview%3Acontext%3A%29-fuqx.json'
content_hash: 'sha256:2e035b6e04f758ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentable](../nsviewrepresentable.md)

# sizeThatFits(_:nsView:context:)

<sub>Instance Method</sub>

Given a proposed size, returns the preferred size of the composite view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func sizeThatFits(_ proposal: ProposedViewSize, nsView: Self.NSViewType, context: Self.Context) -> CGSize?
```

## Parameters

- `proposal` — The proposed size for the view.

- `nsView` — Your custom view object.

- `context` — A context structure containing information about the current state of the system.

## Return Value

The composite size of the represented view controller. Returning a value of `nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during the same layout pass. SwiftUI views choose their own size, so one of the values returned from this function will always be used as the actual size of the composite view.
