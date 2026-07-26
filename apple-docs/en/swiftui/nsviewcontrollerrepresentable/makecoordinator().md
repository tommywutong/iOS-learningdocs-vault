---
title: makeCoordinator()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsviewcontrollerrepresentable/makecoordinator()
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/makecoordinator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentable/makecoordinator%28%29.json'
content_hash: 'sha256:5dfdd0393797a85a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md)

# makeCoordinator()

<sub>Instance Method</sub>

Creates the custom object that you use to communicate changes from your view controller to other parts of your SwiftUI interface.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator() -> Self.Coordinator
```

## Discussion

Implement this method if changes to your view controller might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your view controller doesn’t interact with other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the [makeNSViewController(context:)](<makensviewcontroller(context_).md>) method. The system provides your coordinator instance either directly or as part of a context structure when calling the other methods of your representable instance.

## Default Implementations

### NSViewControllerRepresentable Implementations

- [makeCoordinator()](<makecoordinator()-72re2.md>) — Creates an object to coordinate with the AppKit view controller.

## See Also

### Providing a custom coordinator object

- [Coordinator](coordinator.md) — A type to coordinate with the view controller.
