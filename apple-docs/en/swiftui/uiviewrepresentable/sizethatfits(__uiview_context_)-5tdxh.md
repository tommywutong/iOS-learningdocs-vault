---
title: 'sizeThatFits(_:uiView:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewrepresentable/sizethatfits(_:uiview:context:)-5tdxh'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentable/sizethatfits(_:uiview:context:)-5tdxh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentable/sizethatfits%28_%3Auiview%3Acontext%3A%29-5tdxh.json'
content_hash: 'sha256:2fa56d123da8d602'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewRepresentable](../uiviewrepresentable.md)

# sizeThatFits(_:uiView:context:)

<sub>Instance Method</sub>

Given a proposed size, returns the preferred size of the composite view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func sizeThatFits(_ proposal: ProposedViewSize, uiView: Self.UIViewType, context: Self.Context) -> CGSize?
```

## Parameters

- `proposal` — The proposed size for the view.

- `uiView` — Your custom view object.

- `context` — A context structure containing information about the current state of the system.

## Return Value

The composite size of the represented view controller. Returning a value of `nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during the same layout pass. SwiftUI views choose their own size, so one of the values returned from this function will always be used as the actual size of the composite view.
