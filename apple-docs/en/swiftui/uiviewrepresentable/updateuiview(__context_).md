---
title: 'updateUIView(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewrepresentable/updateuiview(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentable/updateuiview(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentable/updateuiview%28_%3Acontext%3A%29.json'
content_hash: 'sha256:c69ec98aa15d2966'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewRepresentable](../uiviewrepresentable.md)

# updateUIView(_:context:)

<sub>Instance Method</sub>

Updates the state of the specified view with new information from SwiftUI.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func updateUIView(_ uiView: Self.UIViewType, context: Self.Context)
```

## Parameters

- `uiView` — Your custom view object.

- `context` — A context structure containing information about the current state of the system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding UIKit view. Use this method to update the configuration of your view to match the new state information provided in the `context` parameter.

## See Also

### Creating and updating the view

- [makeUIView(context:)](<makeuiview(context_).md>) — Creates the view object and configures its initial state.
- [Context](context.md)
- [UIViewType](uiviewtype.md) — The type of view to present.
