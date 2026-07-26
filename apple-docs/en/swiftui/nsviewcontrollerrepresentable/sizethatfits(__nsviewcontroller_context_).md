---
title: 'sizeThatFits(_:nsViewController:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewcontrollerrepresentable/sizethatfits(_:nsviewcontroller:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/sizethatfits(_:nsviewcontroller:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentable/sizethatfits%28_%3Ansviewcontroller%3Acontext%3A%29.json'
content_hash: 'sha256:a7cd52239fa86e40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md)

# sizeThatFits(_:nsViewController:context:)

<sub>Instance Method</sub>

Given a proposed size, returns the preferred size of the composite view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func sizeThatFits(_ proposal: ProposedViewSize, nsViewController: Self.NSViewControllerType, context: Self.Context) -> CGSize?
```

## Parameters

- `proposal` — The proposed size for the view controller.

- `nsViewController` — Your custom view controller object.

- `context` — A context structure containing information about the current state of the system.

## Return Value

The composite size of the represented view controller. Returning a value of `nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during the same layout pass. SwiftUI views choose their own size, so one of the values returned from this function will always be used as the actual size of the composite view.

## Default Implementations

### NSViewControllerRepresentable Implementations

- [sizeThatFits(_:nsViewController:context:)](<sizethatfits(__nsviewcontroller_context_)-52cs0.md>) — Given a proposed size, returns the preferred size of the composite view.
