---
title: 'makeUIView(context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewrepresentable/makeuiview(context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentable/makeuiview(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentable/makeuiview%28context%3A%29.json'
content_hash: 'sha256:1f3d99d7ebdb8bbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewRepresentable](../uiviewrepresentable.md)

# makeUIView(context:)

<sub>Instance Method</sub>

Creates the view object and configures its initial state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func makeUIView(context: Self.Context) -> Self.UIViewType
```

## Parameters

- `context` — A context structure containing information about the current state of the system.

## Return Value

Your UIKit view configured with the provided information.

## Discussion

You must implement this method and use it to create your view object. Configure the view using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view for the first time. For all subsequent updates, the system calls the [updateUIView(_:context:)](<updateuiview(__context_).md>) method.

## See Also

### Creating and updating the view

- [updateUIView(_:context:)](<updateuiview(__context_).md>) — Updates the state of the specified view with new information from SwiftUI.
- [Context](context.md)
- [UIViewType](uiviewtype.md) — The type of view to present.
