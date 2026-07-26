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
doc_path: /documentation/swiftui/uiviewcontrollerrepresentable/makecoordinator()
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/makecoordinator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentable/makecoordinator%28%29.json'
content_hash: 'sha256:7770963a65c95c7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewControllerRepresentable](../uiviewcontrollerrepresentable.md)

# makeCoordinator()

<sub>Instance Method</sub>

Creates the custom instance that you use to communicate changes from your view controller to other parts of your SwiftUI interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator() -> Self.Coordinator
```

## Discussion

Implement this method if changes to your view controller might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your view controller doesn’t interact with other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the [makeUIViewController(context:)](<makeuiviewcontroller(context_).md>) method. The system provides your coordinator either directly or as part of a context structure when calling the other methods of your representable instance.

## Default Implementations

### UIViewControllerRepresentable Implementations

- [makeCoordinator()](<makecoordinator()-9vwm8.md>) — Creates the custom instance that you use to communicate changes from your view controller to other parts of your SwiftUI interface.

## See Also

### Providing a custom coordinator object

- [Coordinator](coordinator.md) — A type to coordinate with the view controller.
