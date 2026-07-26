---
title: UIViewControllerRepresentable
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uiviewcontrollerrepresentable
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentable.json'
content_hash: 'sha256:73517f2c1e3af9d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIViewControllerRepresentable

<sub>Protocol</sub>

A view that represents a UIKit view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol UIViewControllerRepresentable : View where Self.Body == Never
```

## Overview

Use a [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md) instance to create and manage a [UIViewController](../uikit/uiviewcontroller.md) object in your SwiftUI interface. Adopt this protocol in one of your app’s custom instances, and use its methods to create, update, and tear down your view controller. The creation and update processes parallel the behavior of SwiftUI views, and you use them to configure your view controller with your app’s current state information. Use the teardown process to remove your view controller cleanly from your SwiftUI. For example, you might use the teardown process to notify other objects that the view controller is disappearing.

To add your view controller into your SwiftUI interface, create your [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md) instance and add it to your SwiftUI interface. The system calls the methods of your custom instance at appropriate times.

The system doesn’t automatically communicate changes occurring within your view controller to other parts of your SwiftUI interface. When you want your view controller to coordinate with other SwiftUI views, you must provide a [Coordinator](nsviewcontrollerrepresentable/coordinator.md) instance to facilitate those interactions. For example, you use a coordinator to forward target-action and delegate messages from your view controller to any SwiftUI views.

> [!warning] Warning
> SwiftUI fully controls the layout of the UIKit view controller’s view using the view’s [center](../uikit/uiview/center.md), [bounds](../uikit/uiview/bounds.md), [frame](../uikit/uiview/frame.md), and [transform](../uikit/uiview/transform.md) properties. Don’t directly set these layout-related properties on the view managed by a `UIViewControllerRepresentable` instance from your own code because that conflicts with SwiftUI and results in undefined behavior.

## Relationships

- **Inherits From**: [View](view.md)

## Topics

### Creating and updating the view controller

- [makeUIViewController(context:)](<uiviewcontrollerrepresentable/makeuiviewcontroller(context_).md>) — Creates the view controller object and configures its initial state.
- [updateUIViewController(_:context:)](<uiviewcontrollerrepresentable/updateuiviewcontroller(__context_).md>) — Updates the state of the specified view controller with new information from SwiftUI.
- [Context](uiviewcontrollerrepresentable/context.md)
- [UIViewControllerType](uiviewcontrollerrepresentable/uiviewcontrollertype.md) — The type of view controller to present.

### Specifying a size

- [sizeThatFits(_:uiViewController:context:)](<uiviewcontrollerrepresentable/sizethatfits(__uiviewcontroller_context_).md>) — Given a proposed size, returns the preferred size of the composite view.

### Cleaning up the view controller

- [dismantleUIViewController(_:coordinator:)](<uiviewcontrollerrepresentable/dismantleuiviewcontroller(__coordinator_).md>) — Cleans up the presented view controller (and coordinator) in anticipation of their removal.

### Providing a custom coordinator object

- [makeCoordinator()](<uiviewcontrollerrepresentable/makecoordinator().md>) — Creates the custom instance that you use to communicate changes from your view controller to other parts of your SwiftUI interface.
- [Coordinator](uiviewcontrollerrepresentable/coordinator.md) — A type to coordinate with the view controller.

### Performing layout

- [LayoutOptions](uiviewcontrollerrepresentable/layoutoptions.md)

## See Also

### Adding UIKit views to SwiftUI view hierarchies

- [UIViewRepresentable](uiviewrepresentable.md) — A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [UIViewRepresentableContext](uiviewrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your UIKit view.
- [UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your UIKit view controller.
