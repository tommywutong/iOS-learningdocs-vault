---
title: makeCoordinator()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uiviewrepresentable/makecoordinator()-9405l
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentable/makecoordinator()-9405l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentable/makecoordinator%28%29-9405l.json'
content_hash: 'sha256:bcde166f4f60f185'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewRepresentable](../uiviewrepresentable.md)

# makeCoordinator()

<sub>Instance Method</sub>

Creates the custom instance that you use to communicate changes from your view to other parts of your SwiftUI interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator() -> Self.Coordinator
```

## Discussion

Implement this method if changes to your view might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your view doesn’t interact with other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the [makeUIView(context:)](<makeuiview(context_).md>) method. The system provides your coordinator either directly or as part of a context structure when calling the other methods of your representable instance.
