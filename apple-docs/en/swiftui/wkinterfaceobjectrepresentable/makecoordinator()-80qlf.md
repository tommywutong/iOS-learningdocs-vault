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
doc_path: /documentation/swiftui/wkinterfaceobjectrepresentable/makecoordinator()-80qlf
source_url: 'https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/makecoordinator()-80qlf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkinterfaceobjectrepresentable/makecoordinator%28%29-80qlf.json'
content_hash: 'sha256:ccbd2c6f6fc0cd28'
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
