---
title: NSViewControllerRepresentableContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsviewcontrollerrepresentablecontext
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentablecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentablecontext.json'
content_hash: 'sha256:d7155f960a25ef4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSViewControllerRepresentableContext

<sub>Structure</sub>

Contextual information about the state of the system that you use to create and update your AppKit view controller.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency struct NSViewControllerRepresentableContext<ViewController> where ViewController : NSViewControllerRepresentable
```

## Overview

An [NSViewControllerRepresentableContext](nsviewcontrollerrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view controller, the system creates one of these structures and passes it to the appropriate method of your custom [NSViewControllerRepresentable](nsviewcontrollerrepresentable.md) instance. Use the information in this structure to configure your view controller. For example, use the provided environment values to configure the appearance of your view controller and views. Don’t create this structure yourself.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Coordinating view-related interactions

- [coordinator](nsviewcontrollerrepresentablecontext/coordinator.md) — An object you use to communicate your AppKit view controller’s behavior and state out to SwiftUI objects.
- [transaction](nsviewcontrollerrepresentablecontext/transaction.md) — The current transaction.

### Getting the current environment data

- [environment](nsviewcontrollerrepresentablecontext/environment.md) — Environment data that describes the current state of the system.

### Instance Methods

- [animate(changes:completion:)](<nsviewcontrollerrepresentablecontext/animate(changes_completion_).md>) — Animates changes using the animation in the current transaction.

## See Also

### Adding AppKit views to SwiftUI view hierarchies

- [NSViewRepresentable](nsviewrepresentable.md) — A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [NSViewRepresentableContext](nsviewrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your AppKit view.
- [NSViewControllerRepresentable](nsviewcontrollerrepresentable.md) — A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
