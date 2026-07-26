---
title: 'sizeThatFits(_:uiViewController:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewcontrollerrepresentable/sizethatfits(_:uiviewcontroller:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/sizethatfits(_:uiviewcontroller:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentable/sizethatfits%28_%3Auiviewcontroller%3Acontext%3A%29.json'
content_hash: 'sha256:521dcb9f704b1611'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewControllerRepresentable](../uiviewcontrollerrepresentable.md)

# sizeThatFits(_:uiViewController:context:)

<sub>Instance Method</sub>

Given a proposed size, returns the preferred size of the composite view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func sizeThatFits(_ proposal: ProposedViewSize, uiViewController: Self.UIViewControllerType, context: Self.Context) -> CGSize?
```

## Parameters

- `proposal` — The proposed size for the view controller.

- `uiViewController` — Your custom view controller object.

- `context` — A context structure containing information about the current state of the system.

## Return Value

The composite size of the represented view controller. Returning a value of `nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during the same layout pass. SwiftUI views choose their own size, so one of the values returned from this function will always be used as the actual size of the composite view.

## Default Implementations

### UIViewControllerRepresentable Implementations

- [sizeThatFits(_:uiViewController:context:)](<sizethatfits(__uiviewcontroller_context_)-7x9zd.md>) — Given a proposed size, returns the preferred size of the composite view.
