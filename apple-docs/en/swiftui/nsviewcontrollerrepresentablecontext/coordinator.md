---
title: coordinator
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsviewcontrollerrepresentablecontext/coordinator
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentablecontext/coordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentablecontext/coordinator.json'
content_hash: 'sha256:fad67d4e42c61239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentableContext](../nsviewcontrollerrepresentablecontext.md)

# coordinator

<sub>Instance Property</sub>

An object you use to communicate your AppKit view controller’s behavior and state out to SwiftUI objects.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency let coordinator: ViewController.Coordinator
```

## Discussion

The coordinator is a custom object you define. When updating your view controller, communicate changes to SwiftUI by updating the properties of your coordinator, or by calling relevant methods to make those changes. The implementation of those properties and methods are responsible for updating the appropriate SwiftUI values. For example, you might define a property in your coordinator that binds to a SwiftUI value, as shown in the following code example. Changing the property updates the value of the corresponding SwiftUI variable.

```swift
class Coordinator: NSObject {
   @Binding var rating: Int
   init(rating: Binding<Int>) {
      $rating = rating
   }
}
```

To create and configure your custom coordinator, implement the [makeCoordinator()](<../nsviewcontrollerrepresentable/makecoordinator().md>) method of your [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md) object.

## See Also

### Coordinating view-related interactions

- [transaction](transaction.md) — The current transaction.
