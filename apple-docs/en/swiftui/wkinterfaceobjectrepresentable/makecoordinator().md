---
title: makeCoordinator()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkinterfaceobjectrepresentable/makecoordinator()
source_url: 'https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/makecoordinator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkinterfaceobjectrepresentable/makecoordinator%28%29.json'
content_hash: 'sha256:b4a834cb947e9179'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKInterfaceObjectRepresentable](../wkinterfaceobjectrepresentable.md)

# makeCoordinator()

<sub>Instance Method</sub>

Creates the custom instance that you use to communicate changes from your interface object to other parts of your SwiftUI interface.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator() -> Self.Coordinator
```

## Discussion

Implement this method if changes to your interface object might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your interface object doesn’t interact with other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the [makeWKInterfaceObject(context:)](<makewkinterfaceobject(context_).md>) method. The system provides your coordinator either directly or as part of a context structure when calling the other methods of your representable instance.

## Default Implementations

### WKInterfaceObjectRepresentable Implementations

- [makeCoordinator()](<makecoordinator()-80qlf.md>) — Creates the custom instance that you use to communicate changes from your interface object to other parts of your SwiftUI interface.

## See Also

### Providing a custom coordinator object

- [Coordinator](coordinator.md) — A type to coordinate with the WatchKit interface object.
- [WKInterfaceObjectType](wkinterfaceobjecttype.md) — The type of WatchKit interface object to be presented.
