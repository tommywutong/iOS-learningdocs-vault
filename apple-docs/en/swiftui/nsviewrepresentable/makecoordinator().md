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
doc_path: /documentation/swiftui/nsviewrepresentable/makecoordinator()
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentable/makecoordinator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentable/makecoordinator%28%29.json'
content_hash: 'sha256:2374a22838bacd36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentable](../nsviewrepresentable.md)

# makeCoordinator()

<sub>Instance Method</sub>

Creates the custom instance that you use to communicate changes from your view to other parts of your SwiftUI interface.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator() -> Self.Coordinator
```

## Discussion

Implement this method if changes to your view might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your view doesn’t interact with other parts of your app, you don’t have to provide a coordinator.

SwiftUI calls this method before calling the [makeNSView(context:)](<makensview(context_).md>) method. The system provides your coordinator instance either directly or as part of a context structure when calling the other methods of your representable instance.

## Default Implementations

### NSViewRepresentable Implementations

- [makeCoordinator()](<makecoordinator()-6l2eg.md>) — Creates a `Coordinator` instance to coordinate with the `NSView`.

## See Also

### Providing a custom coordinator object

- [Coordinator](coordinator.md) — A type to coordinate with the view.
