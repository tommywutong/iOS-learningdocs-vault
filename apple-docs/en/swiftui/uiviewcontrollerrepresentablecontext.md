---
title: UIViewControllerRepresentableContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uiviewcontrollerrepresentablecontext
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentablecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentablecontext.json'
content_hash: 'sha256:bebf26cc97d97663'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIViewControllerRepresentableContext

<sub>Structure</sub>

Contextual information about the state of the system that you use to create and update your UIKit view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct UIViewControllerRepresentableContext<Representable> where Representable : UIViewControllerRepresentable
```

## Overview

A [UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view controller, the system creates one of these structures and passes it to the appropriate method of your custom [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md) instance. Use the information in this structure to configure your view controller. For example, use the provided environment values to configure the appearance of your view controller and views. Don’t create this structure yourself.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Coordinating view controller interactions

- [coordinator](uiviewcontrollerrepresentablecontext/coordinator.md) — The view’s associated coordinator.
- [transaction](uiviewcontrollerrepresentablecontext/transaction.md) — The current transaction.

### Getting the environment data

- [environment](uiviewcontrollerrepresentablecontext/environment.md) — Environment values that describe the current state of the system.

### Instance Methods

- [animate(changes:completion:)](<uiviewcontrollerrepresentablecontext/animate(changes_completion_).md>) — Animates changes using the animation in the current transaction.

## See Also

### Adding UIKit views to SwiftUI view hierarchies

- [UIViewRepresentable](uiviewrepresentable.md) — A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [UIViewRepresentableContext](uiviewrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your UIKit view.
- [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md) — A view that represents a UIKit view controller.
