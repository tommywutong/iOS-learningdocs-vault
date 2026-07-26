---
title: UIViewRepresentableContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uiviewrepresentablecontext
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentablecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentablecontext.json'
content_hash: 'sha256:3f88c86cd444a78c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIViewRepresentableContext

<sub>Structure</sub>

Contextual information about the state of the system that you use to create and update your UIKit view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct UIViewRepresentableContext<Representable> where Representable : UIViewRepresentable
```

## Overview

A [UIViewRepresentableContext](uiviewrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view, the system creates one of these structures and passes it to the appropriate method of your custom [UIViewRepresentable](uiviewrepresentable.md) instance. Use the information in this structure to configure your view. For example, use the provided environment values to configure the appearance of your view. Don’t create this structure yourself.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Coordinating view-related interactions

- [coordinator](uiviewrepresentablecontext/coordinator.md) — The view’s associated coordinator.
- [transaction](uiviewrepresentablecontext/transaction.md) — The current transaction.

### Getting the current environment data

- [environment](uiviewrepresentablecontext/environment.md) — The current environment.

### Instance Methods

- [animate(changes:completion:)](<uiviewrepresentablecontext/animate(changes_completion_).md>) — Animates changes using the animation in the current transaction.

## See Also

### Adding UIKit views to SwiftUI view hierarchies

- [UIViewRepresentable](uiviewrepresentable.md) — A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md) — A view that represents a UIKit view controller.
- [UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your UIKit view controller.
